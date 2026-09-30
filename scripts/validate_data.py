#!/usr/bin/env python3
"""CI validation: data/cli.json parses, has required fields, and README counts match."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "cli.json"
README_FILE = ROOT / "README.md"

REQUIRED_FIELDS = {
    "name", "repo_url", "homepage", "description", "license", "category",
    "platforms", "stars", "last_commit_verified", "oss_verified",
    "source_url", "status",
}
VALID_STATUSES = {"active", "maintenance", "archived"}
VALID_CATEGORIES = {
    "shells-prompts", "terminal-multiplexers", "file-navigation",
    "search-find", "git-vcs", "editors", "system-monitoring",
    "networking", "data", "text-processing", "media", "productivity",
}
VALID_PLATFORMS = {"linux", "macos", "windows"}


def load_data():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    assert isinstance(data, list) and data, "cli.json must be a non-empty list"
    for i, entry in enumerate(data):
        missing = REQUIRED_FIELDS - entry.keys()
        assert not missing, f"entry {i} ({entry.get('name')}) missing {sorted(missing)}"
        assert entry["category"] in VALID_CATEGORIES, f"entry {i} bad category {entry['category']}"
        assert entry["status"] in VALID_STATUSES, f"entry {i} bad status {entry['status']}"
        assert isinstance(entry["oss_verified"], bool)
        assert isinstance(entry["last_commit_verified"], bool)
        assert isinstance(entry["platforms"], list)
        assert set(entry["platforms"]) <= VALID_PLATFORMS, f"entry {i} bad platforms"
        assert isinstance(entry["stars"], int) and entry["stars"] >= 0
        assert entry["repo_url"].startswith("https://github.com/"), f"entry {i} repo_url must be https://github.com/..."
        if entry["homepage"]:
            assert entry["homepage"].startswith("https://"), f"entry {i} homepage must be https"
        if entry["oss_verified"]:
            assert entry["source_url"].startswith("https://"), f"entry {i} verified entry needs https source_url"
            assert entry["license"] != "unverified", f"entry {i} verified entry must name a license"
    urls = [e["repo_url"] for e in data]
    assert len(urls) == len(set(urls)), "duplicate repo_url"
    names = [e["name"].lower() for e in data]
    assert len(names) == len(set(names)), "duplicate names"
    return data


def validate_readme(data):
    text = README_FILE.read_text(encoding="utf-8")
    m = re.search(r"A curated list of \*\*(\d+)\s+open-source command-line tools\*\*", text)
    assert m, "README summary line is missing the total entry count"
    assert int(m.group(1)) == len(data), "README total does not match data file"
    counts = {}
    for e in data:
        counts[e["category"]] = counts.get(e["category"], 0) + 1
    for cat, n in counts.items():
        assert re.search(rf"\({n}\)", text), f"README missing ({n}) count for {cat}"
    print(f"OK: {len(data)} entries, README in sync")


if __name__ == "__main__":
    validate_readme(load_data())
