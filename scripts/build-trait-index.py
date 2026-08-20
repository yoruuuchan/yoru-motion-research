#!/usr/bin/env python3
"""Build the two index tables that themes/README.md joins on.

  data/shot-traits.tsv   bucket, category, shot, traits
  data/layout-keeps.tsv  layout, kept skins

Both are derived. Edit this script, never the .tsv files.

`shot-traits` is grepped out of the copied Video Shotcraft implementations, so
every trait is a fact about the code, not an impression of the clip. The traits
are split into two kinds, and the split is the whole point of the table:

  structural  spring, 3d, blur, blend
              baked into what the shot *is*. A design system that forbids one
              of these disqualifies the shot -- honouring the rule would mean
              rewriting the motion, i.e. a different shot.

  surface     radius, gradient, glow, hue
              one value each. A system that forbids one of these just means
              "remember to change it", not "can't use this".

Treating all eight as disqualifying collapses KUNLUN to 10 shots out of 109 and
core to 6, which is a wrong answer dressed as a strict one.

`layout-keeps` reads the generated layouts/README.md rather than the curation
snapshot: the README is itself generated from that snapshot, and parsing it
keeps this script free of the bz2/JSON schema.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Ordered so the output column reads the same way every run.
TRAITS = [
    ("spring", r"spring|outBack|elastic"),
    ("blur", r"blur\("),
    ("glow", r"boxShadow: *.0 0 [0-9]|drop-shadow\(0 0|textShadow: *.0 0 [0-9]"),
    ("3d", r"perspective|rotateX|rotateY|translateZ|preserve-3d"),
    ("hue", r"hue|hsl\("),
    ("blend", r"mix-blend|mixBlendMode"),
    ("gradient", r"gradient"),
    ("radius", r"borderRadius"),
]

STRUCTURAL = {"spring", "blur", "3d", "blend"}


def build_shot_traits():
    """One row per shot directory, unioning traits across its .tsx files."""
    patterns = [(name, re.compile(rx)) for name, rx in TRAITS]
    rows = []
    codeless = []

    for bucket in ("keep", "maybe"):
        for shot_dir in sorted((ROOT / "shots" / bucket).glob("*/*")):
            if not shot_dir.is_dir():
                continue
            sources = sorted(shot_dir.glob("*.tsx"))
            if not sources:
                # Upstream wrote a spec and a preview for these but never an
                # implementation -- see themes/README.md.
                codeless.append(f"{bucket}/{shot_dir.parent.name}/{shot_dir.name}")
                continue
            blob = "\n".join(f.read_text(encoding="utf-8") for f in sources)
            found = [name for name, rx in patterns if rx.search(blob)]
            rows.append((bucket, shot_dir.parent.name, shot_dir.name, " ".join(found)))

    out = ROOT / "data" / "shot-traits.tsv"
    out.write_text("".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
    return rows, codeless


def build_layout_keeps():
    """Per layout, the skins Yoru kept -- her own texture vote, already cast."""
    text = (ROOT / "layouts" / "README.md").read_text(encoding="utf-8")
    rows = []
    layout = None

    for line in text.splitlines():
        if line.startswith("### "):
            layout = line[4:].strip()
        elif line.startswith("- **留下**") and layout:
            body = re.sub(r"\[[^\]]*\]\([^)]*\)", "", line)
            body = body.split("**", 2)[-1].replace("`", "")
            skins = [s.strip() for s in body.split(",") if s.strip()]
            rows.append((layout, ",".join(skins)))

    out = ROOT / "data" / "layout-keeps.tsv"
    out.write_text("".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
    return rows


def main():
    shots, codeless = build_shot_traits()
    layouts = build_layout_keeps()

    keep = [r for r in shots if r[0] == "keep"]
    counts = {}
    for row in keep:
        for t in row[3].split():
            counts[t] = counts.get(t, 0) + 1

    print(f"shots  {len(shots)} rows ({len(keep)} keep), {len(codeless)} dirs with no code")
    for name, _ in TRAITS:
        kind = "structural" if name in STRUCTURAL else "surface"
        print(f"  {name:<9} {counts.get(name, 0):>3}/{len(keep)}  {kind}")
    print(f"layouts {len(layouts)} rows")

    if not shots or not layouts:
        print("refusing to ship an empty table -- check the paths", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
