#!/usr/bin/env python3
"""One-time helper: split wilds-of-osse.json into fragments under src/.

Monsters are grouped by their "group" field, everything else by content type.
After the split, src/ is the source of truth and tools/build.py reassembles
the combined file. Entries can be moved freely between fragments afterwards;
the build only concatenates them.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
COMBINED = ROOT / "wilds-of-osse.json"

TYPE_FILES = {
    "item": "items",
    "trap": "hazards",
    "object": "objects",
    "spell": "spells",
    "table": "tables",
}


def slug(text):
    text = re.sub(r"^the ", "", text.strip(), flags=re.I)
    text = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return text.strip("-") or "misc"


def write(path, doc):
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(doc, f, indent="\t", ensure_ascii=False)
        f.write("\n")
    print(f"wrote {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")


def main():
    if not COMBINED.exists():
        print(f"error: {COMBINED.name} not found", file=sys.stderr)
        sys.exit(1)
    if SRC.exists() and any(SRC.glob("*.json")):
        print("error: src/ already has fragments. Refusing to overwrite.", file=sys.stderr)
        sys.exit(1)

    data = json.loads(COMBINED.read_text(encoding="utf-8"))
    SRC.mkdir(exist_ok=True)

    write(SRC / "_meta.json", {"_meta": data.get("_meta", {})})

    fragments = {}
    for key, entries in data.items():
        if key == "_meta":
            continue
        for entry in entries:
            if key == "monster":
                groups = entry.get("group") or ["misc"]
                name = slug(groups[0])
            else:
                name = TYPE_FILES.get(key, f"{key}s")
            fragments.setdefault(name, {}).setdefault(key, []).append(entry)

    for name, doc in sorted(fragments.items()):
        write(SRC / f"{name}.json", doc)


if __name__ == "__main__":
    main()
