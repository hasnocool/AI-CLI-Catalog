#!/usr/bin/env python3
# scripts/catalog.py
"""Query AI-CLI-Catalog and optionally execute a selected upstream installer."""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.json"
UNSET = object()

TRI_FIELDS = (
    "open_source",
    "local_models",
    "openai_compatible",
    "mcp",
    "acp",
    "subscription_auth",
    "api_key",
    "daemon_server",
)


def load_entries() -> list[dict[str, Any]]:
    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    return data["entries"]


def parse_bool(value: str) -> bool | None:
    normalized = value.lower()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    if normalized in {"null", "unknown"}:
        return None
    raise argparse.ArgumentTypeError("expected true, false, or null")


def matches(entry: dict[str, Any], args: argparse.Namespace) -> bool:
    if args.category and entry["category"] != args.category:
        return False
    if args.installer_type and entry["installer_type"] != args.installer_type:
        return False
    for field in TRI_FIELDS:
        wanted = getattr(args, field, UNSET)
        if wanted is not UNSET and entry[field] is not wanted:
            return False
    if args.text:
        needle = args.text.casefold()
        haystack = " ".join(
            str(entry.get(key, ""))
            for key in ("name", "slug", "category", "provider", "binary", "url")
        ).casefold()
        if needle not in haystack:
            return False
    return True


def print_table(entries: list[dict[str, Any]]) -> None:
    if not entries:
        print("No matching entries.")
        return
    widths = {
        "slug": max(len("SLUG"), *(len(e["slug"]) for e in entries)),
        "category": max(len("CATEGORY"), *(len(e["category"]) for e in entries)),
        "binary": max(len("BINARY"), *(len(e["binary"]) for e in entries)),
    }
    print(f"{'SLUG':<{widths['slug']}}  {'CATEGORY':<{widths['category']}}  {'BINARY':<{widths['binary']}}  NAME")
    for entry in entries:
        print(
            f"{entry['slug']:<{widths['slug']}}  "
            f"{entry['category']:<{widths['category']}}  "
            f"{entry['binary']:<{widths['binary']}}  "
            f"{entry['name']}"
        )


def add_filters(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--text", help="case-insensitive text search")
    parser.add_argument("--category")
    parser.add_argument("--installer-type")
    for field in TRI_FIELDS:
        parser.add_argument(
            f"--{field.replace('_', '-')}",
            dest=field,
            type=parse_bool,
            default=UNSET,
            metavar="true|false|null",
        )


def cmd_list(args: argparse.Namespace) -> int:
    entries = [entry for entry in load_entries() if matches(entry, args)]
    entries.sort(key=lambda entry: (entry["category"], entry["name"].casefold()))
    if args.json:
        print(json.dumps(entries, indent=2))
    else:
        print_table(entries)
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    entry = next((e for e in load_entries() if e["slug"] == args.slug), None)
    if entry is None:
        raise SystemExit(f"Unknown slug: {args.slug}")
    print(json.dumps(entry, indent=2))
    return 0


def cmd_install(args: argparse.Namespace) -> int:
    entry = next((e for e in load_entries() if e["slug"] == args.slug), None)
    if entry is None:
        raise SystemExit(f"Unknown slug: {args.slug}")

    command = entry["installer"]
    print(f"Tool:      {entry['name']}")
    print(f"Source:    {entry['url']}")
    print(f"Verified:  {entry['last_verified']}")
    print(f"Installer: {command}")

    if not args.execute:
        print("Dry run only. Re-run with --execute to run this installer.")
        return 0

    if not entry["official_source"] and not args.allow_unofficial:
        raise SystemExit("Refusing to execute a non-official-source entry without --allow-unofficial.")

    if not args.yes:
        answer = input("Execute this upstream installer? [y/N] ").strip().lower()
        if answer not in {"y", "yes"}:
            print("Cancelled.")
            return 0

    # The catalog intentionally stores complete shell commands because many
    # upstream one-line installers contain pipes and chained package-manager
    # commands. Execution is opt-in and never occurs during lookup/listing.
    return subprocess.run(command, shell=True, check=False).returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="list/filter catalog entries")
    add_filters(list_parser)
    list_parser.add_argument("--json", action="store_true")
    list_parser.set_defaults(func=cmd_list)

    show_parser = subparsers.add_parser("show", help="show one catalog entry")
    show_parser.add_argument("slug")
    show_parser.set_defaults(func=cmd_show)

    install_parser = subparsers.add_parser("install", help="show or execute one installer")
    install_parser.add_argument("slug")
    install_parser.add_argument("--execute", action="store_true", help="actually run the installer")
    install_parser.add_argument("--yes", action="store_true", help="skip interactive confirmation")
    install_parser.add_argument("--allow-unofficial", action="store_true")
    install_parser.set_defaults(func=cmd_install)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
