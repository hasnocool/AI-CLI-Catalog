#!/usr/bin/env python3
# scripts/validate_catalog.py
"""Validate catalog.json invariants using only the Python 3.12 standard library."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.json"

REQUIRED_FIELDS = {
    "name",
    "slug",
    "category",
    "provider",
    "installer",
    "installer_type",
    "binary",
    "url",
    "open_source",
    "local_models",
    "openai_compatible",
    "mcp",
    "acp",
    "subscription_auth",
    "api_key",
    "daemon_server",
    "last_verified",
    "official_source",
}
TRI_STATE_FIELDS = {
    "open_source",
    "local_models",
    "openai_compatible",
    "mcp",
    "acp",
    "subscription_auth",
    "api_key",
    "daemon_server",
}
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    errors = 0

    if data.get("schema_version") != 2:
        fail("schema_version must be 2")
        errors += 1

    entries = data.get("entries")
    if not isinstance(entries, list):
        fail("entries must be a list")
        return 1

    seen_slugs: set[str] = set()
    for index, entry in enumerate(entries):
        prefix = f"entries[{index}]"
        if not isinstance(entry, dict):
            fail(f"{prefix} must be an object")
            errors += 1
            continue

        missing = REQUIRED_FIELDS - entry.keys()
        if missing:
            fail(f"{prefix} missing fields: {', '.join(sorted(missing))}")
            errors += 1

        slug = entry.get("slug")
        if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
            fail(f"{prefix}.slug is invalid: {slug!r}")
            errors += 1
        elif slug in seen_slugs:
            fail(f"duplicate slug: {slug}")
            errors += 1
        else:
            seen_slugs.add(slug)

        for field in TRI_STATE_FIELDS:
            value = entry.get(field)
            if value not in (True, False, None):
                fail(f"{prefix}.{field} must be true, false, or null")
                errors += 1

        for field in ("last_verified",):
            value = entry.get(field)
            try:
                date.fromisoformat(value)
            except (TypeError, ValueError):
                fail(f"{prefix}.{field} must be YYYY-MM-DD")
                errors += 1

        url = entry.get("url")
        if isinstance(url, str):
            parsed = urlparse(url)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                fail(f"{prefix}.url must be an HTTP(S) URL: {url!r}")
                errors += 1

        installer = entry.get("installer")
        if not isinstance(installer, str) or not installer.strip():
            fail(f"{prefix}.installer must be a non-empty string")
            errors += 1

        official_source = entry.get("official_source")
        if not isinstance(official_source, bool):
            fail(f"{prefix}.official_source must be a boolean")
            errors += 1

    if errors:
        print(f"Catalog validation failed with {errors} error(s).", file=sys.stderr)
        return 1

    print(f"Catalog validation passed: {len(entries)} entries, {len(seen_slugs)} unique slugs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
