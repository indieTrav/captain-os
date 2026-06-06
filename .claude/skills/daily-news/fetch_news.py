#!/usr/bin/env python3
"""Fetch top news from NewsAPI.org for configured topics.

Reads NEWS_API_KEY from the nearest .env (walking up from this file).
Falls back to NEWS_API_ENDPOINT if NEWS_API_KEY is unset, since the
project .env originally used that name for the key value.

Usage:
    python fetch_news.py "Technology" "AI & Machine Learning" "Science"

Output: JSON to stdout. Each topic returns up to 3 recent popular
English-language articles.
"""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def load_env() -> None:
    here = Path(__file__).resolve().parent
    for directory in [here, *here.parents]:
        env_path = directory / ".env"
        if not env_path.exists():
            continue
        for raw in env_path.read_text().splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
        return


def fetch_topic(topic: str, api_key: str, page_size: int = 3) -> dict:
    params = {
        "q": topic,
        "searchIn": "title",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": str(page_size),
        "apiKey": api_key,
    }
    url = "https://newsapi.org/v2/everything?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "daily-news-skill/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {"topic": topic, "error": f"HTTP {exc.code}: {body}", "articles": []}
    except Exception as exc:
        return {"topic": topic, "error": str(exc), "articles": []}

    if data.get("status") != "ok":
        return {
            "topic": topic,
            "error": data.get("message", "unknown error"),
            "articles": [],
        }

    articles = []
    for article in data.get("articles", [])[:page_size]:
        articles.append(
            {
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "source": (article.get("source") or {}).get("name"),
                "published_at": article.get("publishedAt"),
            }
        )
    return {"topic": topic, "articles": articles}


def main() -> int:
    load_env()
    api_key = os.environ.get("NEWS_API_KEY") or os.environ.get("NEWS_API_ENDPOINT")
    if not api_key:
        print(
            json.dumps({"error": "NEWS_API_KEY not set in .env"}),
            file=sys.stderr,
        )
        return 1

    topics = sys.argv[1:]
    if not topics:
        print(json.dumps({"error": "no topics provided"}), file=sys.stderr)
        return 1

    results = [fetch_topic(t, api_key) for t in topics]
    print(json.dumps({"topics": results}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
