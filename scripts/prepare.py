"""Copy approved starter files into a NEW directory; never run exercises."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import sys

ROOT = Path(__file__).resolve().parents[1]

def prepare(chapter, destination):
    manifest = json.loads((ROOT / "extraction-manifest.json").read_text(encoding="utf-8"))
    items = [e for e in manifest["assets"] if e["chapter"] == chapter and e["role"] == "starter"]
    if not items:
        raise ValueError("此章只有範本或起始素材尚不完整；請讀章節 README／索引")
    destination = Path(os.path.abspath(destination))
    if os.path.lexists(destination):
        raise FileExistsError("目的地已存在（含符號連結），停止：" + str(destination))
    if not destination.parent.is_dir() or any(p.is_symlink() for p in destination.parents):
        raise ValueError("父目錄必須存在且不是符號連結")
    checked = []
    for entry in items:
        source = ROOT / entry["path"]
        target = Path(entry["target"])
        if target.is_absolute() or ".." in target.parts:
            raise ValueError("不安全的目標路徑")
        if source.is_symlink():
            raise ValueError("素材不可是符號連結")
        data = source.read_bytes()
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise ValueError("素材與提取清單不同：" + entry["path"])
        checked.append((target, data))
    destination.mkdir()  # No exist_ok: competing initializations must fail.
    for relative, data in checked:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(data)
    if chapter in (3, 18):
        (destination / "output").mkdir()
    print("READY:", destination)
    print("僅複製起始素材；未呼叫模型、未產生答案。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter", type=int)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    try:
        prepare(args.chapter, args.destination)
    except (OSError, ValueError) as error:
        print("STOP:", error, file=sys.stderr)
        sys.exit(1)
