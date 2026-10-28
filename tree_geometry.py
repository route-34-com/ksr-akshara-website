"""Geometry for the Akshara tree: the school emblem's own tree, redrawn cleanly.

The leaf and trunk outlines in assets/data/akshara-tree.json were traced from the
logo, so they carry its exact layout but also the wobble of a trace. Here each
outline is resampled evenly, smoothed, and rebuilt as a clean closed curve.
Imported by build.py; run directly to write .tree-preview.svg.
"""
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = json.loads((ROOT / "assets/data/akshara-tree.json").read_text(encoding="utf-8"))
SCALE = 2                                   # work at 2x the trace for rounder numbers
W, H = SRC["w"] * SCALE, SRC["h"] * SCALE
OX, OY = (v * SCALE for v in SRC["origin"])  # where the canopy meets the trunk
BASE_Y = H

DECO = {"top", "topright", "dropL"}        # small drops in the logo, not clickable
# the symbol each leaf carries in the logo, as a Phosphor icon
GLYPH = {"dancer": "person-simple-tai-chi", "pencil": "pencil-simple", "molecules": "atom", "football": "soccer-ball",
         "lab": "flask", "compass": "compass-tool", "math": "math-operations", "laptop": "laptop", "veena": "guitar",
         "sun": "sun", "gymnast": "person-simple-throw", "children": "users-three", "music": "music-notes", "inner1": "book-open"}


# ---------------------------------------------------------------- path helpers
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


def sample(segs, n=24):
    pts = []
    for p0, p1, p2, p3 in segs:
        for k in range(n):
            t = k / n; u = 1 - t
            pts.append((u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
                        u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1]))
    return pts


def resample(pts, n):
    """Evenly spaced points around a closed polyline."""
    ring = pts + [pts[0]]
    seg = [math.dist(a, b) for a, b in zip(ring, ring[1:])]
    total = sum(seg)
    out, acc, j = [], 0.0, 0
    for k in range(n):
        target = total * k / n
        while j < len(seg) - 1 and acc + seg[j] < target:
            acc += seg[j]; j += 1
        f = (target - acc) / seg[j] if seg[j] else 0
        a, b = ring[j], ring[j + 1]
        out.append((a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f))
    return out, total


def smooth(pts, sigma):
    """Circular Gaussian blur of a closed point ring (sigma in samples)."""
    n, r = len(pts), int(sigma * 3)
    w = [math.exp(-(k * k) / (2 * sigma * sigma)) for k in range(-r, r + 1)]
    s = sum(w)
    return [(sum(w[k + r] * pts[(i + k) % n][0] for k in range(-r, r + 1)) / s,
             sum(w[k + r] * pts[(i + k) % n][1] for k in range(-r, r + 1)) / s) for i in range(n)]


def to_path(pts):
    """Closed Catmull-Rom spline through the points, as cubic Beziers."""
    n = len(pts)
    d = [f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"]
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f"C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}")
    return "".join(d) + "Z"


def clean(d, detail=48, sigma=4.5):
    """Traced outline -> smooth outline, same shape. `detail` = points on the final curve."""
    pts = [(x * SCALE, y * SCALE) for x, y in sample(parse(d))]
    dense, _ = resample(pts, 360)
    soft = smooth(dense, sigma)
    fine, _ = resample(soft, detail)
    return to_path(fine), fine


def inner_radius(cx, cy, ring):
    return min(math.dist((cx, cy), p) for p in ring)


def inside(x, y, ring):
    c = False
    for (x1, y1), (x2, y2) in zip(ring, ring[1:] + ring[:1]):
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            c = not c
    return c


# ---------------------------------------------------------------- the tree
BAKED = ROOT / "assets/data/akshara-tree-clean.json"

# leaves whose traced outline got squeezed by neighbours: drawn as a clean teardrop instead
# (base point near the trunk, rounded end, full width); the leaf sits on top of its neighbours
DRAWN = {"inner1": {"base": (214, 330), "end": (170, 160), "width": 104}}


def teardrop(base, end, width, n=36):
    """A leaf from a pointed base to a rounded end, as a ring of points."""
    bx, by = base; ex, ey = end
    L = math.dist(base, end); ux, uy = (ex - bx) / L, (ey - by) / L; nx, ny = -uy, ux
    m = .6  # widest point, as a share of the length
    def half(t):
        if t <= m:
            return width / 2 * math.sin(math.pi / 2 * t / m) ** 1.15
        return width / 2 * math.sqrt(max(0, 1 - ((t - m) / (1 - m)) ** 2))
    ts = [(1 - math.cos(math.pi * k / (n // 2))) / 2 for k in range(n // 2 + 1)]
    side1 = [(bx + ux * L * t + nx * half(t), by + uy * L * t + ny * half(t)) for t in ts]
    side2 = [(bx + ux * L * t - nx * half(t), by + uy * L * t - ny * half(t)) for t in ts[::-1]][1:-1]
    return side1 + side2


def leaves():
    out = []
    baked = json.loads(BAKED.read_text(encoding="utf-8")) if BAKED.exists() else {}
    # paint order: the field-trip leaf tucks its base under the sun leaf
    order = [l for l in SRC["leaves"] if l["key"] != "inner1"]
    order.insert(next(i for i, l in enumerate(order) if l["key"] == "sun"), next(l for l in SRC["leaves"] if l["key"] == "inner1"))
    for l in order:
        if l["key"] in DRAWN:
            ring = teardrop(**DRAWN[l["key"]])
            d = to_path(ring)
        elif l["key"] in baked:
            ring = [tuple(p) for p in baked[l["key"]]]
            d = to_path(ring)
        else:
            d, ring = clean(l["d"], detail=40, sigma=10 if l["key"] in DECO else 7.5)
        cx = sum(p[0] for p in ring) / len(ring); cy = sum(p[1] for p in ring) / len(ring)
        # place the icon at the roomiest point of the leaf (largest inscribed circle, coarse search)
        best = (0, cx, cy)
        for dx in range(-60, 61, 4):
            for dy in range(-60, 61, 4):
                x, y = cx + dx, cy + dy
                if inside(x, y, ring):
                    r = inner_radius(x, y, ring)
                    if r > best[0]:
                        best = (r, x, y)
        r, ix, iy = best
        vx, vy = ix - OX, iy - OY
        n = max(math.hypot(vx, vy), 1)
        px, py = min(ring, key=lambda p: math.dist(p, (OX, OY)))  # the base: where wind bends it
        reach = math.dist((ix, iy), (px, py))
        out.append({"key": l["key"], "d": d, "fill": l["fill"], "deco": l["key"] in DECO, "px": px, "py": py, "reach": reach,
                    "icx": ix, "icy": iy, "icon": min(r * 1.2, 56), "dx": vx / n, "dy": vy / n})
    return out


def trunk():
    """Drawn by hand to the emblem's outline (the trace was too blocky to smooth):
    the top hides under the canopy, the right side swells toward the lowest leaf,
    and the foot flares out around the child."""
    return ("M118 446C160 440 196 470 204 520C210 574 200 648 164 718L342 718"
            "C318 700 306 666 306 630C306 590 322 560 352 536C368 524 372 500 352 468"
            "C300 430 180 422 118 446Z")


SCHOLAR = (253, 640, 96)  # the child with raised arms at the foot of the trunk: x, y, size


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


def bake(radius=8, grow=3, spacing=58):
    """Polish every leaf and store the outlines. Run once with shapely available:
        python tree_geometry.py --bake [radius grow spacing]
    1. round tips and notches to at least `radius` (opening + closing),
    2. grow each leaf by `grow` so neighbours overlap a little; the edge of the leaf
       in front then draws every gap, so gaps come out even,
    3. describe the outline with only a few evenly spaced points (one per `spacing`
       units); the spline through them has no room for hand-drawn wobble."""
    from shapely.geometry import Polygon
    out = {}
    for l in SRC["leaves"]:
        deco = l["key"] in DECO
        pts = [(x * SCALE, y * SCALE) for x, y in sample(parse(l["d"]))]
        dense, _ = resample(pts, 360)
        soft = smooth(dense, 10 if deco else 6)
        poly = Polygon(soft).buffer(0)
        r = radius * (1.5 if deco else 1)
        poly = poly.buffer(-r, join_style="round").buffer(r, join_style="round")
        poly = poly.buffer(r * .7, join_style="round").buffer(-r * .7, join_style="round")
        poly = poly.buffer(grow, join_style="round")
        if poly.geom_type == "MultiPolygon":
            poly = max(poly.geoms, key=lambda g: g.area)
        ring = list(poly.exterior.coords)[:-1]
        if Polygon(ring).exterior.is_ccw != Polygon(soft).exterior.is_ccw:
            ring = ring[::-1]
        ring, perim = resample(smooth(resample(ring, 360)[0], 4), 360)
        n = max(9, round(perim / spacing))
        coarse, _ = resample(ring, n)
        out[l["key"]] = [[round(x, 1), round(y, 1)] for x, y in coarse]
    BAKED.write_text(json.dumps(out), encoding="utf-8")
    print("baked", len(out), "outlines ->", BAKED.relative_to(ROOT))


if __name__ == "__main__":
    import sys
    if "--bake" in sys.argv:
        nums = [int(a) for a in sys.argv[2:]]  # optional: radius grow harmonics
        bake(*nums)
        raise SystemExit
    icons = json.loads((ROOT / "assets/data/tree-icons.json").read_text(encoding="utf-8"))
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20 -20 {W + 40} {H + 40}" width="600" style="background:#f5f8fb">',
             f'<path d="{trunk()}" fill="#07406a"/>']
    for l in leaves():
        parts.append(f'<path d="{l["d"]}" fill="{l["fill"]}" stroke="#f5f8fb" stroke-width="4" stroke-linejoin="round"/>')
        if not l["deco"]:
            parts.append(icon(icons[GLYPH[l["key"]]], l["icx"], l["icy"], l["icon"]).replace('class="drawing"', 'fill="#fff"'))
    parts.append(icon(icons["person-arms-spread"], *SCHOLAR).replace('class="drawing"', 'fill="#fff"'))
    parts.append("</svg>")
    (ROOT / ".tree-preview.svg").write_text("".join(parts), encoding="utf-8")
    print("wrote .tree-preview.svg")
