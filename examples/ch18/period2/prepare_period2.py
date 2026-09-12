"""Copy period-2 starter only. No model, no references, no settings."""
from pathlib import Path
import sys


def prepare(target):
    if not target.is_absolute():
        raise ValueError("use an absolute destination")
    if ".." in target.parts:
        raise ValueError("parent traversal is not allowed")
    if target.exists() or target.is_symlink():
        raise ValueError("destination already exists")
    if not target.parent.is_dir() or any(p.is_symlink() for p in target.parents):
        raise ValueError("parent must exist without symlink ancestors")
    starter = Path(__file__).resolve().parent / "starter"
    required = ('approved-baseline.md', 'task-spec.md', 'verify.py',
                'input/tasks.csv', 'input/notes.md')
    checked = []
    for relative in required:
        source = starter / relative
        if not source.is_file() or source.is_symlink() or any(p.is_symlink() for p in source.parents):
            raise ValueError(f"required source missing or linked: {relative}")
        checked.append((relative, source.read_bytes()))
    target.mkdir()  # Existing or competing destinations must fail, never merge.
    for relative, data in checked:
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open('xb') as stream:
            stream.write(data)
    print(f"READY: {target}")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("supply one new absolute destination")
        prepare(Path(sys.argv[1]))
    except (OSError, ValueError) as error:
        print(f"STOP: {error}; do not continue", file=sys.stderr)
        sys.exit(1)
