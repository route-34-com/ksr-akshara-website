"""Geometry for the Akshara tree: the school emblem's own tree, redrawn precisely.

assets/data/akshara-tree-logo.json holds every leaf outline traced from the emblem
(split along the logo's white gaps, lightly smoothed, tips kept sharp), each leaf's
own blue sampled from the logo, and what each leaf carries: four keep the logo's own
drawing (the dancer and the gymnast traced, the music staff and the chalkboard's writing
redrawn), stored in the logo's units and scaled by `pic_scale`; the rest carry a
Phosphor icon of the same subject.
Imported by build.py; run directly to write .tree-preview.svg.
"""
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = json.loads((ROOT / "assets/data/akshara-tree-logo.json").read_text(encoding="utf-8"))
W = SRC["w"]
BASE_Y = H = SRC["base_y"]
OX, OY = SRC["origin"]                      # where the canopy meets the trunk
ICONS = json.loads((ROOT / "assets/data/tree-icons.json").read_text(encoding="utf-8"))

# the symbol each leaf carries in the logo, as a Phosphor icon (leaves with their own "pic" skip it)
GLYPH = {"pencil": "pencil-simple", "molecules": "mask-happy", "football": "soccer-ball", "lab": "flask", "compass": "palette",
         "laptop": "laptop", "veena": "guitar", "sun": "sun", "children": "users-three", "inner1": "book-open"}


def parse(d):
    """Absolute M/C/Z path -> list of cubic segments ((x0,y0),(x1,y1),(x2,y2),(x3,y3))."""
    toks = re.findall(r"[MCZ]|-?\d*\.?\d+(?:e-?\d+)?", d)
    segs, i, cur, start, cmd = [], 0, None, None, None
    while i < len(toks):
        t = toks[i]
        if t in "MCZ":
            cmd = t; i += 1
            if t == "Z":
                if cur != start:
                    segs.append((cur, cur, start, start))
                cur = start
            continue
        if cmd == "M":
            cur = start = (float(toks[i]), float(toks[i + 1])); i += 2; cmd = "C"
        else:
            p = [(float(toks[i + k]), float(toks[i + k + 1])) for k in (0, 2, 4)]
            segs.append((cur, *p)); cur = p[2]; i += 6
    return segs


def sample(segs, n=8):
    pts = []
    for p0, p1, p2, p3 in segs:
        for k in range(n):
            t = k / n; u = 1 - t
            pts.append((u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
                        u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1]))
    return pts


def leaves():
    out = []
    for l in SRC["leaves"]:
        ring = sample(parse(l["d"]))
        ix, iy = l["icx"], l["icy"]
        vx, vy = ix - OX, iy - OY
        n = max(math.hypot(vx, vy), 1)
        px, py = min(ring, key=lambda p: math.dist(p, (OX, OY)))  # the base: where wind bends it
        out.append({**l, "px": px, "py": py, "reach": math.dist((ix, iy), (px, py)), "dx": vx / n, "dy": vy / n})
    return out


def trunk():
    """Rises from under the leaf bases, narrows to a waist and flares out around the child."""
    return SRC["trunk"]["d"]


SCHOLAR = tuple(SRC["scholar"])  # the child with raised arms at the foot of the trunk: x, y, size


# the Aksharite at the foot of the trunk: a young graduate, arms raised to hold up the tree
# (drawn in a 100 x 100 box; strokes and fills both use the icon colour)
FIGURE = ('<path d="M50 6L67 12.5L50 19L33 12.5Z" stroke-width="2"/>'
          '<path d="M42 16V21.5Q50 25.5 58 21.5V16L50 19Z" stroke-width="1.5"/>'
          '<path d="M64 13.8V23" fill="none" stroke-width="1.8"/><circle cx="64" cy="25" r="2.1" stroke="none"/>'
          '<circle cx="50" cy="31.5" r="8" stroke="none"/>'
          '<path d="M41.5 47Q31 38 21 15" fill="none" stroke-width="7"/><path d="M58.5 47Q69 38 79 15" fill="none" stroke-width="7"/>'
          '<path d="M41 45Q50 41 59 45L64.5 85Q50 89.5 35.5 85Z" stroke-width="3"/>'
          '<path d="M45 86V95.5M55 86V95.5" fill="none" stroke-width="6.5"/>')


def figure(x, y, size):
    s = size / 100
    return (f'<g class="drawing figure" style="transform-origin:{x:.1f}px {y:.1f}px">'
            f'<g transform="translate({x - size / 2:.2f} {y - size / 2:.2f}) scale({s:.4f})">{FIGURE}</g></g>')


def icon(paths, x, y, size, cls="drawing"):
    s = size / 256
    body = "".join(f'<path d="{d}"/>' for d in paths)
    return (f'<g class="{cls}" style="transform-origin:{x:.1f}px {y:.1f}px">'
            f'<g transform="translate({x - size / 2:.2f} {y - size / 2:.2f}) scale({s:.4f})">{body}</g></g>')


def picture(l):
    """What the leaf carries: the logo's own drawing, else its icon (both take the icon colour)."""
    if "pic" in l:
        return (f'<g class="drawing pic" style="transform-origin:{l["icx"]:.1f}px {l["icy"]:.1f}px">'
                f'<g transform="scale({SRC["pic_scale"]})">{l["pic"]}</g></g>')
    if l["key"] in GLYPH:
        return icon(ICONS[GLYPH[l["key"]]], l["icx"], l["icy"], l["icon"])
    return ""


if __name__ == "__main__":
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20 -20 {W + 40} {H + 40}" width="600" style="background:#f5f8fb">',
             f'<path d="{trunk()}" fill="{SRC["trunk"]["fill"]}"/>']
    for l in leaves():
        parts.append(f'<path d="{l["d"]}" fill="{l["fill"]}" stroke="#f5f8fb" stroke-width="5" stroke-linejoin="round"/>')
        parts.append(picture(l).replace('class="drawing pic"', 'fill="#fff" stroke="#fff" stroke-linecap="round" stroke-linejoin="round"').replace('class="drawing"', 'fill="#fff"'))
    parts.append(figure(*SCHOLAR).replace('class="drawing figure"', 'fill="#fff" stroke="#fff"'))
    parts.append("</svg>")
    (ROOT / ".tree-preview.svg").write_text("".join(parts), encoding="utf-8")
    print("wrote .tree-preview.svg")
