---
name: domain-availability-checker
description: Check whether domains are available for registration — single or batch. Three-layer cascade: whois CLI → RDAP (free, IANA registry data) → RapidAPI (domainr) fallback for domains RDAP can't resolve. Use when the user asks to check a domain name, see if a domain is taken, batch-check domain ideas, or brainstorm domain availability for a brand or product.
version: 2.2.0
requires_secrets:
  - key: RAPID_API_KEY
    service: RapidAPI — Domainr
    url: https://rapidapi.com/domainr/api/domainr
    description: Optional — used only as a fallback when RDAP can't reach a verdict (no RDAP server for the TLD, rate-limited, or network error)
    instructions: |
      1. Go to rapidapi.com and sign up (free)
      2. Search for "Domainr" and subscribe to the free tier
      3. Go to the Domainr API page → Endpoints → copy your X-RapidAPI-Key
      4. Add RAPID_API_KEY=<your_key> to your .env file
    required: false
---

# Domain Availability Checker

Before any network calls, a cache check skips work for previously-resolved domains. Then a three-layer cascade verifies anything not served from cache:

| # | Layer | Cost | When it runs |
|---|-------|------|--------------|
| 0 | `domain-cache.json` | free, local | every domain — cached **taken** within TTL skips all layers |
| 1 | whois CLI | free | every domain not skipped by cache |
| 2 | RDAP (IANA) | free | every whois-available domain |
| 3 | RapidAPI / domainr | quota (10/day free tier) | every RDAP-unresolved domain, **only if** `RAPID_API_KEY` is set |

**Cache rules:**
- Cached as **taken** within TTL → skip the cascade, emit the cached verdict.
- Cached as **available** within TTL → re-run the full cascade. Availability is action-worthy; a stale "available" could send you to register a domain that's since been taken.
- Stale (older than TTL) or missing → run the full cascade.

Default TTL: 365 days. Override with `--cache-ttl-days N`. Bypass entirely with `--no-cache`.

Phase 3 is purely a fallback: if RDAP gives a clear answer (✅ available or ❌ taken), RapidAPI is not called. The `.io`, `.ai`, and some other ccTLDs have no IANA RDAP server, so they will always hit the Phase 3 fallback.

Every run writes to two files:

| File | Format | Purpose |
|------|--------|---------|
| `.claude/skills/domain-availability-checker/domain-cache.json` | JSON, keyed by domain | Fast O(1) lookup — the source of truth for cache skips |
| `.claude/skills/domain-availability-checker/domain-checks.log` | Timestamped session log (append-only) | Chronological record of every check run |

Results are also printed to the terminal at the end of every run. There is no separate research markdown file — `domain-cache.json` is the durable record of what's been checked.

Two internal caches, both safe to delete:
- `.rdap-bootstrap.json` — IANA's TLD→RDAP-server map, refreshed every 7 days.
- `domain-cache.json` — per-domain verdicts. Delete to force a full re-check on the next run.

## Script

```
.claude/skills/domain-availability-checker/scripts/check_domains.py
```

## Workflow

### Run the check

```bash
python3 .claude/skills/domain-availability-checker/scripts/check_domains.py example.com other.io
```

Or from a file (one domain per line, `#` lines ignored):

```bash
python3 .claude/skills/domain-availability-checker/scripts/check_domains.py --file domains.txt
```

All layers chain automatically. No user-confirmation prompt is needed between layers because Layer 2 (RDAP) is free and Layer 3 (RapidAPI) only fires when RDAP genuinely couldn't answer.

### Present results

After the script finishes, show the user the "Domains you can register" list. Each entry is tagged with the layer that confirmed it: `[rdap]`, `[rapidapi/domainr]`, `[whois]` (if RDAP was skipped), or `[cache:<original-source>]` (if the verdict came from the cache).

**If no available domains were found:** Tell the user, then generate a list of alternative domain ideas (do not check them automatically). Present alternatives as a plain list, then ask:

> "All X domains were taken. Here are some alternatives — would you like me to check any of these?"

Wait for the user to confirm before running another check.

## Options

| Flag | Default | Purpose |
|------|---------|---------|
| `--file FILE` | — | Read domains from file |
| `--rapidapi` | off | Force RapidAPI on every RDAP-available domain (third opinion, not just fallback) |
| `--no-rdap` | off | Skip the RDAP layer entirely |
| `--no-cache` | off | Bypass `domain-cache.json` — re-check every domain |
| `--cache-ttl-days N` | 365 | Treat cache entries older than N days as stale (re-check them) |
| `--cache FILE` | skill dir cache | Override cache path |
| `--rate-limit SECS` | 0.3 | Pause between requests |
| `--output FILE` | — | Save full JSON results |
| `--log FILE` | skill dir log | Override log path |

## Generating domain ideas

Before generating new domain ideas, read `.claude/skills/domain-availability-checker/domain-cache.json` to avoid suggesting names that are already in the cache as taken (or were recently confirmed available — those might be worth revisiting).

When the user gives a brand name or concept instead of a domain list, generate variations before checking:

- Core TLDs: `.com`, `.io`, `.co`, `.app`, `.dev`
- Patterns: `get{name}.com`, `try{name}.com`, `{name}hq.com`, `use{name}.com`
- Match TLDs to context (`.io`/`.dev` for SaaS, `.co` for startups, `.com` first for anything consumer)

## RDAP details

RDAP (RFC 7480–7484) is the modern, JSON-based replacement for whois. The script queries each TLD's registry directly using IANA's bootstrap registry (`https://data.iana.org/rdap/dns.json`), cached locally. The status-code contract:

| HTTP | Meaning |
|------|---------|
| 404 | Domain not registered (available) |
| 200 | Domain registered (taken) |
| 429 | Rate-limited — triggers Phase 3 fallback |
| other / missing TLD | Treated as unresolved — triggers Phase 3 fallback |

## RapidAPI fallback setup

See `references/premium-apis.md` for full setup guide and troubleshooting. Without a key, the script still works — domains RDAP couldn't resolve are simply reported as unknown.
