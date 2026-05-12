#!/usr/bin/env python3
"""release.py — bump python-for-android + ava-common recipe version, commit and tag."""

from __future__ import annotations

import argparse
import difflib
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def die(msg: str) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(1)


def apply_transform(file: Path, transform, tag: str, *, dry_run: bool) -> None:
    print(f"    {file.relative_to(REPO)}")
    if not file.exists():
        die(f"{file} not found")
    original = file.read_text()
    new = transform(original, tag)
    if original == new:
        print("        (no change)")
        return
    if dry_run:
        for line in difflib.unified_diff(
            original.splitlines(keepends=True),
            new.splitlines(keepends=True),
            fromfile=str(file),
            tofile=str(file),
        ):
            print("        " + line, end="")
    else:
        file.write_text(new)


def git_run(*args: str, dry_run: bool) -> None:
    cmd = ["git", "-C", str(REPO), *args]
    if dry_run:
        print(f"    [dry-run] {' '.join(cmd)}")
    else:
        subprocess.check_call(cmd)


def t_version(content: str, tag: str) -> str:
    return re.sub(r'(__version__\s*=\s*)["\'][^"\']+["\']', rf'\1"{tag}"', content)


def t_p4a_recipe_version(content: str, tag: str) -> str:
    return re.sub(
        r"(^\s*version\s*=\s*)[\"'][^\"']+[\"']",
        rf"\g<1>'{tag}'",
        content,
        flags=re.MULTILINE,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--tag", required=True, metavar="yy.mm.dd")
    parser.add_argument("--dry-run", "-n", action="store_true")
    args = parser.parse_args()

    recipe = REPO / "pythonforandroid" / "recipes" / "ava-common" / "__init__.py"
    p4a_init = REPO / "pythonforandroid" / "__init__.py"
    apply_transform(recipe, t_p4a_recipe_version, args.tag, dry_run=args.dry_run)
    apply_transform(p4a_init, t_version, args.tag, dry_run=args.dry_run)
    git_run("add", str(recipe), str(p4a_init), dry_run=args.dry_run)
    git_run(
        "commit", "-m",
        f"chore: bump ava-common recipe to {args.tag}, bump version to {args.tag}",
        dry_run=args.dry_run,
    )
    git_run("tag", args.tag, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
