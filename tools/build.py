#!/usr/bin/env python3
"""Merge the fragments in src/ into the single wilds-of-osse.json brew file.

Each fragment is a JSON object whose keys are 5eTools content arrays
("monster", "item", "trap", ...). src/_meta.json holds the "_meta" block.
Fragments are merged in alphabetical order of filename.

Before the one-time split has been run there is no src/ directory. That is a
valid state, not an error: the combined file is still the source of truth, so
this script reports the skip and exits cleanly.
"""
import json
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "wilds-of-osse.json"


def fail(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def skip(msg):
    print(f"nothing to build: {msg}")
    sys.exit(0)


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"{path.name} is not valid JSON: {e}")


def main():
    if not SRC.is_dir():
        skip("src/ does not exist yet. Run the 'Split brew into src' workflow "
             "to start building from fragments. Until then wilds-of-osse.json "
             "is maintained directly and is left untouched.")

    fragments = sorted(p for p in SRC.glob("*.json") if p.name != "_meta.json")
    if not fragments:
        skip("src/ contains no fragments. wilds-of-osse.json left untouched.")

    meta_path = SRC / "_meta.json"
    if not meta_path.exists():
        fail("src/_meta.json is missing, but src/ has fragments. "
             "The split is incomplete; restore _meta.json before building.")

    meta_doc = load(meta_path)
    meta = meta_doc.get("_meta", meta_doc)

    now = int(time.time())
    meta["dateLastModified"] = now
    for source in meta.get("sources", []):
        source["dateLastModified"] = now

    out = {"_meta": meta}
    seen = {}
    counts = {}

    for path in fragments:
        doc = load(path)
        if not isinstance(doc, dict):
            fail(f"{path.name} must contain a JSON object at the top level.")
        for key, entries in doc.items():
            if key == "_meta":
                fail(f"{path.name} must not contain a _meta block. That lives in _meta.json.")
            if not isinstance(entries, list):
                fail(f"{path.name}: '{key}' must be an array.")
            for entry in entries:
                name = entry.get("name")
                ident = (key, name, entry.get("source"))
                if ident in seen:
                    fail(f"duplicate {key} '{name}' in {path.name} and {seen[ident]}")
                seen[ident] = path.name
            out.setdefault(key, []).extend(entries)
            counts[key] = counts.get(key, 0) + len(entries)

    with OUT.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent="\t", ensure_ascii=False)
        f.write("\n")

    summary = ", ".join(f"{n} {k}" for k, n in sorted(counts.items()))
    print(f"built {OUT.name} from {len(fragments)} fragments: {summary}")
    print(f"{OUT.stat().st_size} bytes")


if __name__ == "__main__":
    main()
