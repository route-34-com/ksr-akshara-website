"""The Akshara tree: interactive emblem page and homepage hero."""
import re
from ..components import cta_band
from ..layout import href

LEAVES = {
    "dancer": ("ph-person-simple-tai-chi", "Performing arts", "Dance",
               "Dance is woven into the curriculum as per the NEP. Every year the Fine Arts Department stages a multidisciplinary show, with students leading the choreography.",
               "Arts.jpg", "Students performing a classical dance", "life-akshara#arts", "Visual and performing arts"),
    "pencil": ("ph-pencil-simple", "Pre-KG to Grade II", "The foundation years",
               "Young learners grow through play and discovery across eight domains of development, from sensory and fine motor skills to language and cognition.",
               "KSR-children-2.jpg", "Young children building with blocks", "methodology#foundation", "The foundation stage"),
    "molecules": ("ph-mask-happy", "Performing arts", "Drama",
                  "Drama is part of the curriculum as per the NEP, and students lead the set design for the Fine Arts Department's yearly multidisciplinary show.",
                  None, "", "life-akshara#arts", "Visual and performing arts"),
    "football": ("ph-soccer-ball", "After school", "Sport for every child",
                 "A floodlit, international-standard football turf, plus cricket, athletics, basketball, volleyball, handball, skating and chess.",
                 "sgfleet.jpg", "Students running on the athletics track", "sports", "Explore sports"),
    "lab": ("ph-flask", "Grades VI to XII", "Science and the IIT and NEET track",
            "An integrated programme builds strong concepts, problem-solving and mock-test practice for the IITs, NITs and medical colleges.",
            "KSR-higher.jpg", "Senior students in the chemistry lab", "life-akshara#iit", "IIT and NEET programme"),
    "compass": ("ph-palette", "Kindergarten to Grade 8", "STEAM and robotics",
                "Science, Technology, Engineering, Arts and Maths through hands-on activities, with robotics bringing every subject together.",
                "Robotics.jpg", "A robotics kit being assembled", "life-akshara#steam", "STEAM at Akshara"),
    "math": ("ph-function", "CBSE, shaped by the NEP", "A curriculum in four stages",
             "Foundation, Preparatory, Middle and Secondary. Each stage has its own way of teaching, from play-based learning to career guidance.",
             "career-banner.jpg", "A teacher guiding young students", "methodology", "See the curriculum"),
    "laptop": ("ph-globe-hemisphere-east", "British Council and TED-Ed", "Global classrooms",
               "Three consecutive International School Awards, a TED-Ed Club and projects with partner schools abroad bring the world into the classroom.",
               "ted.jpg", "A student giving a TED-Ed talk", "life-akshara#isa", "International School Award"),
    "veena": ("ph-users-three", "Nine to choose from", "Clubs",
              "Art, Cookery, Photography, Nature, Quiz, Reading, MUN, TED-Ed and Math. Every student joins at least one.",
              "Cooks-act.jpg", "Young students at the cookery club", "life-akshara#clubs", "Clubs and activities"),
    "sun": ("ph-book-open-text", "Values first", "Reading and values",
            "Kindness, respect and responsibility sit alongside academics, so Aksharites grow into compassionate members of society.",
            "why-akshara.jpg", "Students reading together on the lawn", "about-us", "Our story"),
    "gymnast": ("ph-person-simple-run", "Discipline and fitness", "NCC, Scouts and Guides",
                "Drill, first aid, map reading and camp training build discipline, fitness, teamwork and decision-making.",
                "ncc.jpg", "NCC cadets marching", "life-akshara#ncc", "NCC at Akshara"),
    "children": ("ph-flag-banner", "Four houses", "The house system",
                 "Anthuriums, Bluebells, Daffodils and Tulips. Inter-house competitions build leadership, creativity and collaboration.",
                 "House-system.jpg", "The house investiture ceremony", "life-akshara#houses", "About the houses"),
    "music": ("ph-music-notes", "Fine arts", "Music",
              "Vocal and instrumental music are part of the curriculum as per the NEP, and a highlight of the school's annual performances.",
              None, "", "life-akshara#arts", "Visual and performing arts"),
    "inner1": ("ph-map-trifold", "Beyond the classroom", "Field trips",
               "National and international trips take Aksharites out of the classroom to see new places, try new things and learn life lessons.",
               "Fieldstrip.jpg", "Students on a field trip", "life-akshara#trips", "Field trips"),
    "trunk": ("ph-plant", "At the root", "The Aksharite",
              "At the base of the tree is the child. Everything above grows from our vision: lifelong learners with values and leadership, contributing to the global society.",
              "KSR-children.jpg", "Four smiling Akshara students", "about-us/why-akshara", "Why Akshara?"),
}


def tree_parts(r):
    """The emblem tree SVG plus the data its script needs (used by the tree page and the homepage)."""
    import json
    import tree_geometry as tg
    leaves = tg.leaves()
    defs = [
        '<filter id="lift-hover" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="8" stdDeviation="7" flood-color="#021a30" flood-opacity=".32"/></filter>',
        '<filter id="lift-sel" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="6" stdDeviation="9" flood-color="#4aa3e8" flood-opacity=".85"/></filter>',
        '<radialGradient id="ground"><stop offset="0" stop-color="#07406a" stop-opacity=".38"/><stop offset="1" stop-color="#07406a" stop-opacity="0"/></radialGradient>',
        # soft light from the top left, laid over every leaf's own blue
        # the selected leaf lights up: white to sky blue
        '<linearGradient id="g-sel" x1="0" y1="0" x2=".8" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#bfe0fa"/></linearGradient>',
        '<linearGradient id="sheen" x1="0" y1="0" x2=".7" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".30"/>'
        '<stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#021a30" stop-opacity=".24"/></linearGradient>',
        # soft shade behind the crown and a firmer ground shadow: static gradients, no blur filters
        '<radialGradient id="crown-shade"><stop offset="0" stop-color="#07406a" stop-opacity=".30"/><stop offset=".62" stop-color="#07406a" stop-opacity=".12"/><stop offset="1" stop-color="#07406a" stop-opacity="0"/></radialGradient>',
        f'<linearGradient id="g-trunk" gradientUnits="userSpaceOnUse" x1="0" y1="440" x2="0" y2="{tg.BASE_Y}">'
        '<stop offset="0" stop-color="#0a4f86"/><stop offset="1" stop-color="#05304f"/></linearGradient>',
    ]
    live = [l for l in leaves if not l["deco"]]
    # chip and grow order: nearest the trunk first
    keys = [l["key"] for l in sorted(live, key=lambda l: (l["icx"] - tg.OX) ** 2 + (l["icy"] - tg.OY) ** 2)]
    rank = {k: i + 1 for i, k in enumerate(keys)}

    def leaf_svg(l):
        k, ix, iy = l["key"], l["icx"], l["icy"]
        wind = f'class="wind" data-px="{l["px"]:.1f}" data-py="{l["py"]:.1f}" data-reach="{l["reach"]:.0f}"'
        if l["deco"]:
            return (f'<g class="deco-leaf" aria-hidden="true"><g {wind}><path d="{l["d"]}" fill="{l["fill"]}"/>'
                    f'<path d="{l["d"]}" fill="url(#sheen)"/><path class="leaf-edge" d="{l["d"]}"/></g></g>')
        style = (f'--dx:{l["dx"] * 7:.1f}px;--dy:{l["dy"] * 7:.1f}px;--i:{rank[k]};--base:{l["fill"]};'
                 f'transform-origin:{ix:.1f}px {iy:.1f}px')
        return (f'<g class="leaf" data-key="{k}" style="{style}" tabindex="0" role="button" aria-label="{LEAVES[k][2]}">'
                f'<g {wind}><g class="leaf-in" id="lv-{k}" style="transform-origin:{ix:.1f}px {iy:.1f}px">'
                f'<path class="leaf-shape" d="{l["d"]}"/><path d="{l["d"]}" fill="url(#sheen)" pointer-events="none"/>'
                f'<path class="leaf-edge" d="{l["d"]}"/>'
                f'{tg.picture(l)}</g></g></g>')

    canopy_svg = "".join(leaf_svg(l) for l in leaves)
    sx, sy, ss = tg.SCHOLAR
    trunk_svg = (f'<g class="leaf" data-key="trunk" style="--dx:0px;--dy:-6px;--i:0;--base:url(#g-trunk);transform-origin:{sx}px 600px" tabindex="0" role="button" aria-label="{LEAVES["trunk"][2]}">'
                 f'<g class="trunk-in"><g class="trunk-wind"><g id="lv-trunk">'
                 f'<path class="leaf-shape" d="{tg.trunk()}"/><path d="{tg.trunk()}" fill="url(#sheen)" pointer-events="none"/>'
                 f'<path class="leaf-edge" d="{tg.trunk()}"/>{tg.figure(sx, sy, ss)}</g></g></g></g>')
    xs = [float(v) for l in leaves for v in re.findall(r"-?\d+\.?\d*", l["d"])[0::2]]
    ys = [float(v) for l in leaves for v in re.findall(r"-?\d+\.?\d*", l["d"])[1::2]]
    pad = 14
    vx, vy = min(xs) - pad, min(ys) - pad
    vw, vh = max(xs) - min(xs) + pad * 2, tg.BASE_Y + 18 - vy
    ratio = f"{vw:.0f} / {vh:.0f}"
    svg = (f'<svg class="tree-svg" viewBox="{vx:.0f} {vy:.0f} {vw:.0f} {vh:.0f}" role="group" aria-label="The Akshara tree. Choose a leaf to explore.">'
           f'<defs>{"".join(defs)}</defs>'
           f'<ellipse cx="{sx}" cy="{tg.BASE_Y + 6}" rx="190" ry="18" fill="url(#ground)"/>'
           f'<ellipse cx="{tg.W / 2 + 2}" cy="282" rx="318" ry="286" fill="url(#crown-shade)"/>'
           f'{trunk_svg}<g class="lift-under" aria-hidden="true"><g class="lift-wind"><use class="lift lift-trunk" href=""/></g></g>'
           f'<g class="canopy">{canopy_svg}</g>'
           # hover layer: a copy of the hovered leaf, drawn above its neighbours so it can lift freely
           f'<g class="lift-layer" aria-hidden="true"><g class="lift-wind"><use class="lift lift-sel" href=""/></g><g class="lift-wind"><use class="lift lift-hover" href=""/></g></g></svg>')
    js = {k: {"icon": v[0], "kicker": v[1], "title": v[2], "text": v[3],
              "img": f"{r}assets/img/{v[4]}" if v[4] else None, "alt": v[5], "href": href(r, v[6].split("#")[0]) + ("#" + v[6].split("#")[1] if "#" in v[6] else ""), "cta": v[7]}
          for k, v in LEAVES.items()}
    chip_keys = ["trunk"] + keys
    chips = "".join(f'<button type="button" class="chip" data-key="{k}" aria-pressed="false"><i class="ph {LEAVES[k][0]}"></i>{LEAVES[k][2]}</button>' for k in chip_keys)
    return {"svg": svg, "sx": sx, "ratio": ratio, "chips": chips, "count": len(chip_keys),
            "data": f'<script type="application/json" id="tree-data">{json.dumps(js)}</script>'}


def akshara_tree(r):
    import tree_geometry as tg
    t = tree_parts(r)
    svg, sx, ratio, chips, chip_keys = t["svg"], t["sx"], t["ratio"], t["chips"], range(t["count"])
    crumbs = f'<nav aria-label="Breadcrumb"><ol class="crumbs"><li><a href="{href(r, "")}">Home</a></li><li><a href="{href(r, "about-us")}">About</a></li><li aria-current="page">The Akshara tree</li></ol></nav>'
    return f"""
<section class="tree-hero" data-tree="full" data-sway-x="{sx}" data-sway-y="{tg.BASE_Y}">
  <div class="tree-rays" aria-hidden="true"></div>
  <div class="tree-spot" aria-hidden="true"></div>
  <canvas class="wind-canvas" aria-hidden="true"></canvas>
  <header class="tree-intro">{crumbs}
    <span class="eyebrow">The Akshara emblem</span>
    <h1>Every leaf is a part of Akshara.</h1>
    <p class="lede">A tree of learning. Tap any leaf to see what it stands for.</p>
    <p class="more">From the child at its roots to the dancer at its crown, it maps out life at Akshara: academics, sport, the arts, values and the wider world.</p>
    <div class="tree-meta">
      <button class="icon-btn wind-toggle" type="button" aria-pressed="true" aria-label="Pause the wind"><i class="ph ph-wind"></i></button>
      <span class="wind-label" aria-hidden="true">Wind</span>
    </div>
    <div class="leaf-chips" aria-label="All leaves">{chips}</div>
  </header>
  <div class="tree-stage" style="aspect-ratio:{ratio}">{svg}<div class="tree-tip" aria-hidden="true"></div></div>
  <article class="tree-card" aria-live="polite" hidden>
    <button class="icon-btn tree-close" type="button" aria-label="Close"><i class="ph ph-x"></i></button>
    <div class="tree-card-in"></div>
  </article>
</section>
{t["data"]}""" + cta_band(r)
