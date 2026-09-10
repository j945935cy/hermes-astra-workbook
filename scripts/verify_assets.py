"""Verify public asset hashes, Python syntax and local Markdown links (stdlib)."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import ast
import hashlib
import json
import re
import sys

def verify(root):
    manifest = json.loads((root / "extraction-manifest.json").read_text(encoding="utf-8"))
    if manifest["chapters"] != list(range(1, 19)):
        raise ValueError("chapter index must cover 01–18")
    paths = [entry["path"] for entry in manifest["assets"]]
    if len(paths) != len(set(paths)):
        raise ValueError("duplicate manifest path")
    for entry in manifest["assets"]:
        relative = Path(entry["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("unsafe manifest path")
        path = root / relative
        if not path.is_file() or path.is_symlink():
            raise ValueError("missing or symlink asset: " + entry["path"])
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError("asset differs: " + entry["path"])
    python_count = 0
    link_count = 0
    for path in root.rglob("*"):
        if ".git" in path.parts or "__pycache__" in path.parts or not path.is_file():
            continue
        if path.suffix == ".py":
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            python_count += 1
        if path.suffix == ".md":
            text = path.read_text(encoding="utf-8")
            text = re.sub(r"```.*?```", "", text, flags=re.S)
            for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", text):
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                resolved = path.parent / unquote(parsed.path)
                if not resolved.exists():
                    raise ValueError(f"broken link: {path.relative_to(root)} -> {target}")
                link_count += 1
    print(f"PASS: {len(paths)} assets; {python_count} Python syntax checks; {link_count} local links")
    for gap in manifest.get("known_gaps", []):
        print("KNOWN GAP:", gap)
    print("Only listed assets are checksummed; no model, UI or external-service validation.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        verify(args.root)
    except (OSError, ValueError, SyntaxError) as error:
        print("FAIL:", error, file=sys.stderr)
        sys.exit(1)
