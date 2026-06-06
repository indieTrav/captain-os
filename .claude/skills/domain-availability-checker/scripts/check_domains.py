#!/usr/bin/env python3
"""
Domain availability checker.
  Phase 1: whois CLI — fast, free, no key needed.
  Phase 2: RapidAPI (domainr) — verified second-pass on available domains only.

Usage:
  python check_domains.py example.com [other.org ...]
  python check_domains.py --file domains.txt
  python check_domains.py --file domains.txt --rapidapi          # also run RapidAPI on available
  python check_domains.py --file domains.txt --rapidapi --only-available  # skip whois-taken
"""

import sys
import time
import json
import os
import subprocess
import argparse
from datetime import datetime, timezone
from pathlib import Path
import urllib.request
import urllib.error

DEFAULT_RATE_LIMIT = 0.3
LOG_FILE = Path(__file__).resolve().parent.parent / "domain-checks.log"

RAPIDAPI_HOST = "domainr.p.rapidapi.com"
RAPIDAPI_URL = "https://domainr.p.rapidapi.com/v2/status"

RDAP_BOOTSTRAP_URL = "https://data.iana.org/rdap/dns.json"
RDAP_CACHE = Path(__file__).resolve().parent.parent / ".rdap-bootstrap.json"
RDAP_CACHE_TTL_DAYS = 7

DOMAIN_CACHE = Path(__file__).resolve().parent.parent / "domain-cache.json"
DOMAIN_CACHE_TTL_DAYS = 365


# ── env loader ────────────────────────────────────────────────────────────────

def load_env():
    current = Path(__file__).resolve()
    for _ in range(10):
        current = current.parent
        env_path = current / ".env"
        if env_path.exists():
            try:
                with open(env_path) as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#") and "=" in line:
                            key, value = line.split("=", 1)
                            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))
                return True
            except Exception:
                continue
    return False


# ── whois ─────────────────────────────────────────────────────────────────────

NOT_FOUND_PATTERNS = [
    "no match for",
    "no match",
    "not found",
    "no entries found",
    "no data found",
    "object does not exist",
    "status: free",
    "domain not found",
    "no object found",
    "is available",
    "no whois server is known",
    "domain status: no object found",
    "% no entries found",
    "available for registration",
    "this domain name has not been registered",
]

REGISTERED_PATTERNS = [
    "domain name:",
    "registrar:",
    "creation date:",
    "created on:",
    "registry domain id:",
    "domain_name:",
    "registrant:",
    "name server:",
]


def check_whois(domain: str) -> dict:
    try:
        proc = subprocess.run(
            ["whois", domain],
            capture_output=True, text=True, timeout=30
        )
    except subprocess.TimeoutExpired:
        return {"domain": domain, "available": None, "source": "whois", "error": "timeout"}
    except FileNotFoundError:
        print("ERROR: 'whois' CLI not found. Install it: brew install whois", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        return {"domain": domain, "available": None, "source": "whois", "error": str(e)}

    output = proc.stdout.lower()

    for pattern in NOT_FOUND_PATTERNS:
        if pattern in output:
            return {"domain": domain, "available": True, "source": "whois"}

    for pattern in REGISTERED_PATTERNS:
        if pattern in output:
            return {"domain": domain, "available": False, "source": "whois"}

    return {"domain": domain, "available": None, "source": "whois", "error": "ambiguous whois output"}


# ── rdap (IANA) ───────────────────────────────────────────────────────────────

def load_rdap_bootstrap(cache_path: Path = RDAP_CACHE) -> dict:
    """Returns TLD -> base RDAP URL. Cached locally; refreshes every RDAP_CACHE_TTL_DAYS."""
    if cache_path.exists():
        age_days = (time.time() - cache_path.stat().st_mtime) / 86400
        if age_days < RDAP_CACHE_TTL_DAYS:
            try:
                with open(cache_path) as f:
                    return json.load(f)
            except Exception:
                pass

    try:
        req = urllib.request.Request(RDAP_BOOTSTRAP_URL, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
    except Exception:
        if cache_path.exists():
            with open(cache_path) as f:
                return json.load(f)
        return {}

    tld_to_url: dict[str, str] = {}
    for service in data.get("services", []):
        if len(service) >= 2 and service[1]:
            tlds, urls = service[0], service[1]
            base = urls[0].rstrip("/") + "/"
            for tld in tlds:
                tld_to_url[tld.lower()] = base

    try:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        with open(cache_path, "w") as f:
            json.dump(tld_to_url, f)
    except Exception:
        pass
    return tld_to_url


def check_rdap(domain: str, rdap_servers: dict) -> dict:
    if "." not in domain:
        return {"domain": domain, "available": None, "source": "rdap", "error": "no TLD"}
    tld = domain.rsplit(".", 1)[1].lower()
    base = rdap_servers.get(tld)
    if not base:
        return {"domain": domain, "available": None, "source": "rdap", "error": f"no RDAP server for .{tld}"}

    url = f"{base}domain/{domain}"
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/rdap+json"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            resp.read()
            return {"domain": domain, "available": False, "source": "rdap"}
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"domain": domain, "available": True, "source": "rdap"}
        if e.code == 429:
            return {"domain": domain, "available": None, "source": "rdap", "error": "rate_limited", "rate_limited": True}
        return {"domain": domain, "available": None, "source": "rdap", "error": f"HTTP {e.code}"}
    except Exception as e:
        return {"domain": domain, "available": None, "source": "rdap", "error": str(e)}


# ── rapidapi / domainr ────────────────────────────────────────────────────────

def check_rapidapi(domain: str, api_key: str) -> dict:
    url = f"{RAPIDAPI_URL}?domain={domain}"
    req = urllib.request.Request(
        url,
        headers={
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": RAPIDAPI_HOST,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
            statuses = data.get("status", [])
            if statuses:
                summary = statuses[0].get("summary", "").lower()
                status_str = statuses[0].get("status", "").lower()
                available = "inactive" in summary or "inactive" in status_str
                return {
                    "domain": domain,
                    "available": available,
                    "source": "rapidapi/domainr",
                    "status": statuses[0].get("status", ""),
                }
            return {"domain": domain, "available": None, "source": "rapidapi/domainr", "error": "empty response"}
    except urllib.error.HTTPError as e:
        if e.code == 403:
            return {"domain": domain, "available": None, "source": "rapidapi/domainr", "error": "invalid API key (403)"}
        return {"domain": domain, "available": None, "source": "rapidapi/domainr", "error": f"HTTP {e.code}"}
    except Exception as e:
        return {"domain": domain, "available": None, "source": "rapidapi/domainr", "error": str(e)}


# ── output helpers ────────────────────────────────────────────────────────────

def result_line(r: dict) -> str:
    if r["available"] is True:
        icon, label = "✅", "Available"
    elif r["available"] is False:
        icon, label = "❌", "Taken"
    else:
        icon, label = "⚠️ ", f"Unknown — {r.get('error', '?')}"
    source = f"[{r.get('source', '?')}]"
    return f"  {icon}  {r['domain']:<40} {label:<12} {source}"


def print_results(results: list[dict], heading: str = "") -> None:
    if heading:
        print(f"\n{heading}")
        print("─" * 65)
    for r in results:
        print(result_line(r))


def reconcile(
    whois_results: list[dict],
    rdap_results: list[dict] | None,
    api_results: list[dict] | None,
    cached_results: list[dict] | None = None,
) -> dict[str, dict]:
    """Latest-layer-wins per domain. Cached entries are pre-resolved and never
    have a competing whois/rdap/rapidapi entry for the same domain, so order
    among the live layers is what matters. Returns domain -> final result dict.
    """
    final: dict[str, dict] = {}
    for r in cached_results or []:
        final[r["domain"]] = r
    for r in whois_results:
        final[r["domain"]] = r
    for r in rdap_results or []:
        if r["available"] is not None:
            final[r["domain"]] = r
    for r in api_results or []:
        if r["available"] is not None:
            final[r["domain"]] = r
    return final


def print_summary(
    whois_results: list[dict],
    rdap_results: list[dict] | None = None,
    api_results: list[dict] | None = None,
    cached_results: list[dict] | None = None,
) -> None:
    available = [r for r in whois_results if r["available"] is True]
    taken     = [r for r in whois_results if r["available"] is False]
    unknown   = [r for r in whois_results if r["available"] is None]

    print(f"\n{'═' * 65}")
    if cached_results:
        print(f"  CACHE")
        print(f"{'─' * 65}")
        print(f"  Served from cache : {len(cached_results)}")
        print()
    print(f"  WHOIS SUMMARY")
    print(f"{'─' * 65}")
    print(f"  Checked   : {len(whois_results)}")
    print(f"  Available : {len(available)}")
    print(f"  Taken     : {len(taken)}")
    if unknown:
        print(f"  Unknown   : {len(unknown)}")

    if rdap_results:
        rdap_avail  = [r for r in rdap_results if r["available"] is True]
        rdap_taken  = [r for r in rdap_results if r["available"] is False]
        rdap_errors = [r for r in rdap_results if r["available"] is None]
        print(f"\n  RDAP VERIFICATION ({len(rdap_results)} domains re-checked)")
        print(f"  Confirmed available : {len(rdap_avail)}")
        print(f"  Actually taken      : {len(rdap_taken)}")
        if rdap_errors:
            print(f"  Errors / unknown    : {len(rdap_errors)}")

    if api_results:
        api_avail  = [r for r in api_results if r["available"] is True]
        api_taken  = [r for r in api_results if r["available"] is False]
        api_errors = [r for r in api_results if r["available"] is None]
        print(f"\n  RAPIDAPI FALLBACK ({len(api_results)} domains re-checked)")
        print(f"  Confirmed available : {len(api_avail)}")
        print(f"  Actually taken      : {len(api_taken)}")
        if api_errors:
            print(f"  Errors              : {len(api_errors)}")

    print(f"{'═' * 65}")

    final = reconcile(whois_results, rdap_results, api_results, cached_results)
    final_available = [r for r in final.values() if r["available"] is True]
    if final_available:
        print(f"\n  Domains you can register:")
        for r in sorted(final_available, key=lambda x: x["domain"]):
            print(f"    • {r['domain']}  [{r.get('source', '?')}]")
    print()


# ── logging ───────────────────────────────────────────────────────────────────

def append_log(
    whois_results: list[dict],
    rdap_results: list[dict] | None,
    api_results: list[dict] | None,
    log_path: Path,
    cached_results: list[dict] | None = None,
) -> None:
    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%d %H:%M UTC")

    all_results = reconcile(whois_results, rdap_results, api_results, cached_results)

    lines = [f"\n── {ts} {'─' * 30}"]

    for domain, r in all_results.items():
        src = r.get("source", "?")
        if r["available"] is True:
            status = "available"
        elif r["available"] is False:
            status = "taken"
        else:
            status = "unknown"
        lines.append(f"  {domain:<40} {status:<10} [{src}]")

    with open(log_path, "a") as f:
        f.write("\n".join(lines) + "\n")


# ── domain cache ──────────────────────────────────────────────────────────────

def load_cache(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        with open(path) as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_cache(cache: dict, path: Path) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(cache, f, indent=2, sort_keys=True)
    except Exception as e:
        print(f"⚠️  Could not save domain cache: {e}", file=sys.stderr)


def cache_lookup(cache: dict, domain: str, ttl_days: int) -> dict | None:
    """Return the cached entry if it exists and is fresher than ttl_days, else None."""
    entry = cache.get(domain)
    if not entry or "checked_at" not in entry or "available" not in entry:
        return None
    try:
        checked = datetime.fromisoformat(entry["checked_at"].replace("Z", "+00:00"))
    except Exception:
        return None
    age_days = (datetime.now(timezone.utc) - checked).days
    if age_days > ttl_days:
        return None
    return entry


def cache_update(cache: dict, results: dict[str, dict]) -> None:
    """Persist definitive verdicts (available is True/False) into the cache."""
    now_iso = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    for domain, r in results.items():
        if r.get("available") is None:
            continue
        if r.get("from_cache"):
            continue  # don't re-stamp entries we just served from cache
        source = r.get("source", "?")
        # Strip any "cache:" prefix if somehow present
        if source.startswith("cache:"):
            source = source.split(":", 1)[1]
        cache[domain] = {
            "available": r["available"],
            "source": source,
            "checked_at": now_iso,
        }


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    load_env()

    parser = argparse.ArgumentParser(description="Check domain availability via whois + optional RapidAPI")
    parser.add_argument("domains", nargs="*", help="Domains to check")
    parser.add_argument("--file", "-f", metavar="FILE", help="File with one domain per line (# = comment)")
    parser.add_argument("--rapidapi", action="store_true", help="Force RapidAPI on all RDAP-available domains (otherwise it only runs as fallback when RDAP is rate-limited)")
    parser.add_argument("--no-rdap", action="store_true", help="Skip RDAP layer entirely")
    parser.add_argument("--no-cache", action="store_true", help="Bypass the domain-cache.json lookup (re-check everything)")
    parser.add_argument("--cache-ttl-days", type=int, default=DOMAIN_CACHE_TTL_DAYS, help=f"Cache entries older than this are ignored (default: {DOMAIN_CACHE_TTL_DAYS})")
    parser.add_argument("--cache", default=DOMAIN_CACHE, metavar="FILE", help=f"Cache file path (default: {DOMAIN_CACHE})")
    parser.add_argument("--rate-limit", type=float, default=DEFAULT_RATE_LIMIT, metavar="SECS")
    parser.add_argument("--log", default=LOG_FILE, metavar="FILE", help=f"Log file path (default: {LOG_FILE})")
    parser.add_argument("--output", "-o", metavar="FILE", help="Save full JSON results")
    args = parser.parse_args()

    domains = list(args.domains)
    if args.file:
        p = Path(args.file)
        if not p.exists():
            print(f"Error: file not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        with open(p) as f:
            domains.extend(ln.strip() for ln in f if ln.strip() and not ln.startswith("#"))

    if not domains:
        parser.print_help()
        sys.exit(1)

    domains = [d.strip().lower().removeprefix("http://").removeprefix("https://").rstrip("/") for d in domains]

    # ── Phase 0: cache lookup ─────────────────────────────────────────────────
    # Taken-within-TTL → skip the cascade entirely.
    # Available-within-TTL → re-run the cascade (availability needs fresh confirmation).
    # Stale or missing → run the cascade.
    cache_path = Path(args.cache)
    cache = {} if args.no_cache else load_cache(cache_path)
    cached_results: list[dict] = []
    domains_to_check: list[str] = []

    for d in domains:
        hit = cache_lookup(cache, d, args.cache_ttl_days) if not args.no_cache else None
        if hit and hit["available"] is False:
            original_source = hit.get("source", "?").split(":", 1)[-1]
            cached_results.append({
                "domain": d,
                "available": False,
                "source": f"cache:{original_source}",
                "checked_at": hit["checked_at"],
                "from_cache": True,
            })
        else:
            domains_to_check.append(d)

    if cached_results:
        print(f"\nCache — {len(cached_results)} previously-taken domain(s) skipped\n")
        for r in cached_results:
            print(result_line(r))

    whois_results: list[dict] = []
    needs_rdap: list[dict] = []  # whois said available OR couldn't decide

    if not domains_to_check:
        print(f"\nAll {len(domains)} domain(s) served from cache. Use --no-cache to force re-check.")
    else:
        # ── Phase 1: whois ────────────────────────────────────────────────────
        print(f"\nPhase 1 — whois check ({len(domains_to_check)} domain(s))\n")
        for i, domain in enumerate(domains_to_check):
            if i > 0:
                time.sleep(args.rate_limit)
            result = check_whois(domain)
            whois_results.append(result)
            print(result_line(result))

        # Send to RDAP if whois said available OR if whois was ambiguous —
        # never if whois confirmed taken (registrar info is reliable).
        needs_rdap = [r for r in whois_results if r["available"] is not False]

    # ── Phase 2: RDAP (free, automatic) ───────────────────────────────────────
    rdap_results = None
    rdap_unresolved: list[str] = []  # domains RDAP couldn't reach a verdict on
    if needs_rdap and not args.no_rdap:
        print(f"\nPhase 2 — RDAP verification ({len(needs_rdap)} domain(s))\n")
        rdap_servers = load_rdap_bootstrap()
        if not rdap_servers:
            print("  ⚠️  Could not load IANA RDAP bootstrap — skipping RDAP layer.")
        else:
            rdap_results = []
            for i, r in enumerate(needs_rdap):
                if i > 0:
                    time.sleep(args.rate_limit)
                rdap_result = check_rdap(r["domain"], rdap_servers)
                rdap_results.append(rdap_result)
                print(result_line(rdap_result))
                if rdap_result["available"] is None:
                    rdap_unresolved.append(r["domain"])

    # ── Phase 3: RapidAPI fallback ────────────────────────────────────────────
    # Fires automatically on RDAP-unresolved domains when a key is present
    # (rate-limited, no RDAP server for that TLD, network errors, etc.).
    # Also fires on every RDAP-available domain if --rapidapi was passed.
    api_results = None
    api_key = os.environ.get("RAPID_API_KEY")

    if args.rapidapi:
        targets = [r["domain"] for r in (rdap_results or []) if r["available"] is True]
        if not targets:
            targets = [r["domain"] for r in needs_rdap]
    else:
        targets = rdap_unresolved

    if targets:
        if not api_key:
            if rdap_unresolved:
                print(f"\n⚠️  RDAP could not verify {len(rdap_unresolved)} domain(s) (rate limit, missing TLD server, or error).")
                print("   Add RAPID_API_KEY=<your_key> to .env to enable the RapidAPI fallback.")
                print("   Get a free key at: rapidapi.com → search 'Domainr'")
            elif args.rapidapi:
                print("\n⚠️  RAPID_API_KEY not found in .env — cannot run requested RapidAPI check.")
        else:
            label = "fallback" if not args.rapidapi else "verification"
            print(f"\nPhase 3 — RapidAPI {label} ({len(targets)} domain(s))\n")
            api_results = []
            for i, domain in enumerate(targets):
                if i > 0:
                    time.sleep(args.rate_limit)
                api_result = check_rapidapi(domain, api_key)
                api_results.append(api_result)
                print(result_line(api_result))

    # ── Persist cache ────────────────────────────────────────────────────────
    final = reconcile(whois_results, rdap_results, api_results, cached_results)
    if not args.no_cache:
        cache_update(cache, final)
        save_cache(cache, cache_path)

    # ── Summary + outputs ─────────────────────────────────────────────────────
    print_summary(whois_results, rdap_results, api_results, cached_results)

    log_path = Path(args.log)
    append_log(whois_results, rdap_results, api_results, log_path, cached_results)
    print(f"  Log appended  → {log_path.resolve()}")
    if not args.no_cache:
        print(f"  Cache updated → {cache_path.resolve()}\n")
    else:
        print()

    if args.output:
        payload = {"whois": whois_results}
        if rdap_results:
            payload["rdap"] = rdap_results
        if api_results:
            payload["rapidapi"] = api_results
        if cached_results:
            payload["cached"] = cached_results
        with open(args.output, "w") as f:
            json.dump(payload, f, indent=2)
        print(f"  JSON saved → {args.output}\n")


if __name__ == "__main__":
    main()
