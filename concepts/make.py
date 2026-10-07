#!/usr/bin/env python3
"""Four homepage concepts, one per current design trend, from the same real content.

Run:  python3 concepts/make.py   then open /concepts/ on the preview server.
Output: concepts/<name>/index.html and a chooser at concepts/index.html.
Only the homepage is built for each concept; links go to the existing inner pages.
"""
import html
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
import build  # noqa: E402  (real news, phone numbers, brand logos)

R = "../../"
def img(n): return f"{R}assets/img/{n}"
def page(slug): return f"{R}{slug + '/' if slug else ''}index.html"
E = html.escape

# ------------------------------------------------------------------ real content (from ksrakshara.org via build.py)
H1A, H1B = "Nurturing young minds and hearts of", "tomorrow's leaders."
LEDE = "From Pre-KG to Grade XII, Aksharites learn through inquiry, sport, the arts and strong values."
NOTICE = ("Admissions 2027-28", "Open from Vijayadasami for all classes")
NAV = [("About", "about-us"), ("Academics", "methodology"), ("Student life", "life-akshara"), ("Campus", "facilities-hostel"),
       ("News", "events"), ("Contact", "contact-us")]
FACTS = [("1984", None, "", "KSR Educational and Charitable Trust founded"),
         ("16", 16, "", "KSR institutions, from Pre-KG to Ph.D."),
         ("4,500+", 4500, "+", "students across the three KSR schools"),
         ("3x", 3, "x", "British Council International School Award"),
         ("25 km", 25, " km", "GPS-tracked bus network around Tiruchengode")]
STAGES = [
    ("foundation", "Foundation", "Pre-KG to Grade II", "KSR-children-2.jpg", "ph-plant",
     "Play-based learning across eight domains of development",
     "A holistic, discovery-based early years programme following NEP ECCE guidance. Children build cognitive, social, emotional, creative and physical skills."),
    ("preparatory", "Preparatory", "Grades III to V", "career-banner.jpg", "ph-pencil-simple",
     "Structured learning with room to explore",
     "An interdisciplinary, technology-rich curriculum with active learning. Skill development is planned into every term."),
    ("middle", "Middle", "Grades VI to VIII", "ATL-school.jpg", "ph-flask",
     "Projects that connect to the real world",
     "Project-based, hands-on learning, seminars, quizzes and e-research, starting in the Atal Tinkering Lab with the IIT and NEET foundation from Grade VI."),
    ("secondary", "Secondary", "Grades IX to XII", "KSR-higher.jpg", "ph-graduation-cap",
     "Ready for India's best colleges, and abroad",
     "A choice of subject combinations, career guidance and an integrated NEET and JEE programme with mock tests."),
]
LIFE = [
    ("isa", "Fieldstrip.jpg", "International School Award, three times in a row", "British Council, 2022 to 2025"),
    ("atl", "Robotics.jpg", "Atal Tinkering Lab", "Grades VI to XII"),
    ("ted", "ted.jpg", "TED-Ed Club", "Student talks, global sessions"),
    ("ncc", "ncc.jpg", "NCC, Scouts and Guides", "Drill, first aid, map reading and camp training"),
    ("arts", "Arts.jpg", "Art, music and dance", "Performing and visual arts every week"),
    ("steam", "ATL-school.jpg", "STEAM and Robotics", "From Kindergarten to Grade 8"),
]
CLUBS = ["Art", "Cookery", "Photography", "Nature", "Quiz", "Reading", "MUN", "TED-Ed", "Math"]
QUOTES = [
    ("I very much hope to see many chemists coming from this school.", "professor.jpg", "Prof. Dr. Robert Huber", "Nobel Laureate in Chemistry, 1988"),
    ("My son Nithin Rohit completed Grade XII here and went on to study Electrical Engineering at IIT Jodhpur. The JEE programme was truly amazing.",
     "Kumar-120x120.jpg", "K. Kumar", "Parent of Nithin Rohit"),
    ("The NEET coaching gave my twins the knowledge and the confidence to pursue medicine. Both are now in medical college.",
     "Vanitha-srinivasan.jpg", "Vanitha Srinivasan", "Parent of Kanimozhi and Kayalvizhi"),
]
SPORTS = [("cricket.jpg", "Cricket"), ("basketball.jpg", "Basketball"), ("sgfleet.jpg", "Athletics"), ("Skatings_sports.jpg", "Skating"),
          ("vollyball.jpg", "Volleyball"), ("handball.jpg", "Handball"), ("ches.jpg", "Chess")]
AGES = [("Pre-KG", "2 years 5 months by June"), ("Junior KG", "3 years 2 months"), ("Senior KG", "4 years 2 months"), ("Grade I", "5 years 2 months")]
STEPS = [("Enquire", "By phone or in person. Meet the Principal or Vice Principals."),
         ("Collect the application", "Available at the school office on payment."),
         ("Entrance assessment", "From Senior KG onwards. Submit the form on the day.")]
ADMIT_H = "Admissions open from Vijayadasami to March."
ADMIT_P = "Seats are offered first come, first served. Late applications in April depend on availability."
NEWS = build.NEWS[:3]


def head(title, css, extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | KSR Akshara Academy concept</title>
<meta name="robots" content="noindex">
<link rel="icon" href="{R}assets/img/favicon.ico">
<link rel="stylesheet" href="{R}assets/css/vendor.css">
<style>{css}</style>{extra}
</head>
"""


def socials():
    return "".join(f'<a class="soc" href="{u}" aria-label="{n}">{build.BRAND_SVG[k]}</a>' for k, n, u in [
        ("facebook", "Facebook", "https://www.facebook.com/ksrakshara"), ("instagram", "Instagram", "https://www.instagram.com/ksrakshara2010/"),
        ("youtube", "YouTube", "https://www.youtube.com/@ksrakshara"), ("whatsapp", "WhatsApp", "https://wa.me/919894932323")])


def brand(cls="brand"):
    return (f'<a class="{cls}" href="{page("")}"><img src="{img("logo-emblem.jpg")}" alt="" width="44" height="44">'
            f'<span><strong>KSR Akshara Academy</strong><small>Tiruchengode, since 2010</small></span></a>')


def navlinks():
    return "".join(f'<a href="{page(s)}">{t}</a>' for t, s in NAV)


COMMON_JS = """
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
// reveal on view
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .12 });
document.querySelectorAll('.rv').forEach(el => reduce ? el.classList.add('in') : io.observe(el));
// numbers count up once
const cio = new IntersectionObserver(es => es.forEach(e => { if (!e.isIntersecting) return; cio.unobserve(e.target);
  const el = e.target, end = +el.dataset.count, suf = el.dataset.suffix || '', t0 = performance.now();
  const step = t => { const k = Math.min(1, (t - t0) / 1500), v = Math.round(end * (1 - Math.pow(1 - k, 4)));
    el.textContent = v.toLocaleString('en-IN') + suf; if (k < 1) requestAnimationFrame(step); }; requestAnimationFrame(step); }), { threshold: .6 });
if (!reduce) document.querySelectorAll('[data-count]').forEach(el => cio.observe(el));
"""


def fact_num(shown, n, suf):
    return f'<strong data-count="{n}" data-suffix="{suf}">{shown}</strong>' if n else f"<strong>{shown}</strong>"


# ================================================================== 1. LIQUID GLASS
def glass():
    css = """
:root{--ink:#0b1b2e;--muted:#4f6378;--brand:#0b5d95;--deep:#07406a;--red:#d8392b;--r:28px;--ease:cubic-bezier(.2,.9,.25,1);
  --glass:rgb(255 255 255 / .2);--glass-edge:rgb(255 255 255 / .55);}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font:400 17px/1.6 Figtree,system-ui,sans-serif;color:var(--ink);background:#e9f1f9;overflow-x:hidden}
img{display:block;max-width:100%}a{color:inherit;text-decoration:none}
h1,h2,h3{font-family:Outfit,sans-serif;font-weight:600;letter-spacing:-.025em;line-height:1.08;margin:0;text-wrap:balance}
p{margin:0}
.wrap{max-width:1240px;margin:0 auto;padding:0 clamp(16px,4vw,40px)}
/* colour behind the glass: soft orbs in the school blues, plus one warm one */
.orbs{position:fixed;inset:0;z-index:-1;pointer-events:none;background:
 radial-gradient(38% 30% at 12% 30%,rgb(99 170 235/.55),transparent 70%),
 radial-gradient(34% 30% at 88% 55%,rgb(11 93 149/.35),transparent 70%),
 radial-gradient(30% 26% at 60% 92%,rgb(255 160 140/.35),transparent 70%),#eaf2fa}
/* liquid glass (web approximation of Apple's material): blur + saturation, a bright rim and a specular sheen */
.lg{position:relative;background:var(--glass);-webkit-backdrop-filter:blur(22px) saturate(185%);backdrop-filter:blur(22px) saturate(185%);
 border:1px solid var(--glass-edge);box-shadow:inset 0 1px 0 rgb(255 255 255/.75),inset 0 -1px 0 rgb(255 255 255/.18),0 12px 40px -12px rgb(10 40 80/.35);isolation:isolate}
.lg::before{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;z-index:-1;
 background:linear-gradient(135deg,rgb(255 255 255/.55),rgb(255 255 255/0) 38%,rgb(255 255 255/0) 70%,rgb(255 255 255/.18))}
.lg.dark{--glass:rgb(10 25 45/.28);--glass-edge:rgb(255 255 255/.32);color:#fff}
/* nav: a floating glass capsule */
.nav{position:fixed;top:16px;left:50%;transform:translateX(-50%);z-index:20;display:flex;align-items:center;gap:6px;padding:7px 7px 7px 10px;border-radius:999px;width:min(1180px,calc(100% - 24px))}
.brand{display:flex;align-items:center;gap:10px;margin-right:auto}.brand img{width:40px;height:40px;border-radius:12px;background:#fff;padding:2px}
.brand strong{display:block;font:700 1rem/1.1 Outfit}.brand small{font-size:.72rem;opacity:.8}
.links{display:flex;gap:2px}.links a{padding:.55rem .9rem;border-radius:999px;font-weight:500;font-size:.95rem;transition:background .3s}
.links a:hover{background:rgb(255 255 255/.28)}
.btn{display:inline-flex;align-items:center;gap:.5rem;padding:.85rem 1.35rem;border-radius:999px;font-weight:600;white-space:nowrap;transition:transform .35s var(--ease),box-shadow .35s}
.btn:active{transform:scale(.97)}
.btn-red{background:linear-gradient(180deg,#ec5143,#c92e21);color:#fff;box-shadow:inset 0 1px 0 rgb(255 255 255/.45),0 10px 24px -8px rgb(201 46 33/.7)}
.btn-red:hover{transform:translateY(-2px)}
.btn.lg:hover{transform:translateY(-2px)}
/* hero: full-bleed photo, content on glass */
.hero{position:relative;min-height:100dvh;display:grid;align-items:end;padding:120px 0 150px;color:#fff;overflow:hidden}
.hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 40%;transform:scale(1.04);animation:drift 22s ease-in-out infinite alternate}
@keyframes drift{to{transform:scale(1.12) translate(-1.5%,-1%)}}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgb(4 20 40/.62),rgb(4 20 40/.15) 62%,transparent),linear-gradient(180deg,rgb(4 20 40/.3),transparent 30%,rgb(4 20 40/.55))}
.hero .wrap{position:relative;z-index:1;width:100%}
.pill{display:inline-flex;align-items:center;gap:.6rem;padding:.4rem .9rem .4rem .4rem;border-radius:999px;font-size:.92rem}
.pill b{background:#fff;color:var(--deep);padding:.3rem .7rem;border-radius:999px;font-size:.8rem}
.hero h1{font-size:clamp(2.4rem,4.8vw,4.4rem);margin-top:1.2rem;max-width:16ch;text-shadow:0 4px 40px rgb(0 0 0/.25)}
.hero p{font-size:1.2rem;max-width:44ch;margin-top:1.1rem;opacity:.92}
.ctas{display:flex;flex-wrap:wrap;gap:.7rem;margin-top:1.8rem}
/* facts: one glass shelf overlapping the hero edge */
.facts{position:relative;z-index:2;margin-top:-92px}
.facts ul{list-style:none;margin:0;padding:10px;display:grid;grid-template-columns:repeat(5,1fr);border-radius:32px}
.facts li{padding:18px 20px;border-radius:22px;transition:background .3s}.facts li:hover{background:rgb(255 255 255/.3)}
.facts strong{display:block;font:600 clamp(1.7rem,2.6vw,2.3rem)/1 Outfit;letter-spacing:-.03em;color:var(--deep)}
.facts span{display:block;margin-top:.45rem;font-size:.86rem;color:var(--muted);line-height:1.35}
.sec{padding:clamp(70px,9vw,120px) 0}
.sec h2{font-size:clamp(2rem,4vw,3.3rem);max-width:20ch}
.sub{color:var(--muted);font-size:1.12rem;margin-top:.9rem;max-width:56ch}
/* stages: glass segmented control with a sliding thumb */
.seg{position:relative;display:inline-grid;grid-template-columns:repeat(4,1fr);padding:6px;border-radius:999px;margin-top:2rem}
.seg button{position:relative;z-index:1;border:0;background:none;font:600 .98rem Figtree;padding:.75rem 1.4rem;border-radius:999px;cursor:pointer;color:var(--ink)}
.thumb{position:absolute;top:6px;bottom:6px;left:6px;width:calc((100% - 12px)/4);border-radius:999px;background:rgb(255 255 255/.75);
 box-shadow:inset 0 1px 0 #fff,0 6px 18px -6px rgb(10 40 80/.35);transition:transform .55s var(--ease)}
.stage{display:grid;grid-template-columns:1.2fr 1fr;margin-top:1.8rem;position:relative}
.stage img{width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:var(--r)}
.stage .card{margin:auto 0 auto -90px;padding:clamp(22px,3vw,36px);border-radius:var(--r);align-self:center}
.stage .card small{font-weight:600;color:var(--brand)}
.stage h3{font-size:clamp(1.4rem,2.2vw,1.9rem);margin:.4rem 0 .8rem}
.stage p{color:var(--muted)}
.stage.swap{animation:fade .6s var(--ease)}@keyframes fade{from{opacity:0;transform:translateY(10px)}}
/* life: photos with glass caption plates */
.life{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:260px;gap:16px;margin-top:2.2rem}
.life a{position:relative;border-radius:var(--r);overflow:hidden}
.life a:first-child{grid-row:span 2}
.life img{width:100%;height:100%;object-fit:cover;transition:transform 1s var(--ease)}.life a:hover img{transform:scale(1.06)}
.life .lg{position:absolute;left:12px;right:12px;bottom:12px;padding:14px 16px;border-radius:20px}
.life h3{font-size:1.1rem}.life span{font-size:.86rem;opacity:.85}
/* voices over a photo */
.voices{position:relative;color:#fff;overflow:hidden}
.voices>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.voices::before{content:"";position:absolute;inset:0;background:rgb(5 25 50/.5)}
.voices .lg.dark{--glass:rgb(8 22 42/.5)}
.voices .wrap{position:relative}
.qs{display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:16px;margin-top:2.2rem}
.q{padding:28px;border-radius:var(--r);display:flex;flex-direction:column;gap:22px}
.q blockquote{margin:0;font:500 1.12rem/1.5 Outfit}.q:first-child blockquote{font-size:1.5rem;line-height:1.3}
.q figcaption{display:flex;gap:12px;align-items:center;margin-top:auto}.q figcaption img{width:46px;height:46px;border-radius:50%;object-fit:cover}
.q small{display:block;opacity:.8;font-size:.84rem}
/* sports: horizontal glass-captioned strip */
.strip{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;padding:6px 2px 16px;margin-top:2rem;scrollbar-width:none}
.strip figure{flex:0 0 230px;margin:0;position:relative;scroll-snap-align:start;border-radius:24px;overflow:hidden}
.strip img{width:100%;aspect-ratio:3/4;object-fit:cover}
.strip figcaption{position:absolute;left:10px;bottom:10px;padding:.45rem .9rem;border-radius:999px;font-weight:600;font-size:.9rem}
/* admissions on glass */
.admit{display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:clamp(24px,4vw,48px);border-radius:36px}
.ages{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-top:1.4rem}
.ages div{padding:14px 16px;border-radius:18px;background:rgb(255 255 255/.45);box-shadow:inset 0 1px 0 #fff}
.ages b{display:block;font-family:Outfit;color:var(--deep)}.ages span{font-size:.88rem;color:var(--muted)}
.steps{list-style:none;padding:0;margin:0;display:grid;gap:14px;counter-reset:s;align-content:start}
.steps li{display:grid;grid-template-columns:44px 1fr;gap:14px;padding:16px;border-radius:20px;background:rgb(255 255 255/.4)}
.steps li::before{counter-increment:s;content:counter(s);width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:var(--deep);color:#fff;font:600 1.05rem Outfit}
.steps b{font-family:Outfit}.steps p{color:var(--muted);font-size:.95rem}
footer{padding:40px 0 30px}.foot{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;padding:22px 26px;border-radius:28px;font-size:.92rem;color:var(--muted)}
.soc{display:inline-block;width:36px;height:36px;margin-left:8px}.soc svg{width:100%;height:100%}
.rv{opacity:0;transform:translateY(24px);transition:opacity 1s var(--ease),transform 1s var(--ease)}.rv.in{opacity:1;transform:none}
@media (max-width:1000px){.links{display:none}.facts ul{grid-template-columns:repeat(2,1fr)}.facts li:last-child{grid-column:span 2}
 .stage{grid-template-columns:1fr}.stage .card{margin:-60px 14px 0}.life{grid-template-columns:1fr 1fr}.qs,.admit{grid-template-columns:1fr}
 .seg{display:flex;overflow-x:auto;max-width:100%}.seg button{flex:0 0 auto;padding:.7rem 1rem}.thumb{display:none}.seg button[aria-selected=true]{background:rgb(255 255 255/.75)}}
@media (max-width:560px){.nav .btn{display:none}.life{grid-template-columns:1fr;grid-auto-rows:240px}.life a:first-child{grid-row:auto}}
@media (prefers-reduced-motion:reduce){.hero>img{animation:none}.rv{opacity:1;transform:none}}
@supports not ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){.lg{background:rgb(255 255 255/.85)}.lg.dark{background:rgb(10 25 45/.8)}}
"""
    s0 = STAGES[0]
    seg = "".join(f'<button role="tab" aria-selected="{str(i == 0).lower()}" data-i="{i}">{n}</button>' for i, (k, n, *_r) in enumerate(STAGES))
    facts = "".join(f'<li>{fact_num(a, n, s)}<span>{d}</span></li>' for a, n, s, d in FACTS)
    life = "".join(f'<a class="rv" href="{page("life-akshara")}#{k}"><img src="{img(i)}" alt="{E(t)}" loading="lazy"><div class="lg dark"><h3>{E(t)}</h3><span>{E(d)}</span></div></a>' for k, i, t, d in LIFE[:5])
    qs = "".join(f'<figure class="q lg dark rv"><blockquote>&ldquo;{E(q)}&rdquo;</blockquote><figcaption><img src="{img(p)}" alt="" loading="lazy"><div><b>{E(n)}</b><small>{E(r)}</small></div></figcaption></figure>' for q, p, n, r in QUOTES)
    strip = "".join(f'<figure><img src="{img(i)}" alt="{t} at Akshara" loading="lazy"><figcaption class="lg dark">{t}</figcaption></figure>' for i, t in SPORTS)
    ages = "".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in AGES)
    steps = "".join(f'<li><div><b>{a}</b><p>{b}</p></div></li>' for a, b in STEPS)
    import json
    stages_js = json.dumps([{"n": n, "g": g, "img": img(im), "h": h, "p": p} for k, n, g, im, ic, h, p in STAGES])
    return head("Liquid Glass", css) + f"""<body>
<div class="orbs" aria-hidden="true"></div>
<nav class="nav lg" aria-label="Main">{brand()}<div class="links">{navlinks()}</div><a class="btn btn-red" href="{page("admission")}">Admissions enquiry</a></nav>
<header class="hero"><img src="{img("KSR-children.jpg")}" alt="Four smiling Akshara students in uniform">
 <div class="wrap"><a class="pill lg dark" href="{page("admission")}"><b>{NOTICE[0]}</b>{NOTICE[1]} <i class="ph ph-arrow-right"></i></a>
 <h1>{H1A} {H1B}</h1><p>{LEDE}</p>
 <div class="ctas"><a class="btn btn-red" href="{page("admission")}">Admissions enquiry <i class="ph ph-arrow-right"></i></a>
 <a class="btn lg dark" href="{page("contact-us")}#visit"><i class="ph ph-map-pin"></i>Book a campus visit</a></div></div></header>
<section class="facts wrap" aria-label="Akshara at a glance"><ul class="lg">{facts}</ul></section>
<section class="sec"><div class="wrap"><h2 class="rv">One curriculum, four stages, shaped by the NEP.</h2>
 <p class="sub rv">Akshara follows CBSE expectations and builds skills for an international context.</p>
 <div class="seg lg" role="tablist" aria-label="Stages">{seg}<span class="thumb"></span></div>
 <div class="stage" id="stage"><img src="{img(s0[3])}" alt=""><div class="card lg"><small>{s0[2]}</small><h3>{s0[5]}</h3><p>{s0[6]}</p></div></div>
</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><h2 class="rv">More than a classroom, every single day.</h2><div class="life">{life}</div></div></section>
<section class="sec voices"><img src="{img("why-akshara.jpg")}" alt="" loading="lazy"><div class="wrap"><h2 class="rv">What visitors and parents say.</h2><div class="qs">{qs}</div></div></section>
<section class="sec"><div class="wrap"><h2 class="rv">A floodlit football turf, and a sport for every child.</h2><div class="strip">{strip}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="admit lg rv">
 <div><h2>{ADMIT_H}</h2><p class="sub">{ADMIT_P}</p><div class="ages">{ages}</div>
 <div class="ctas"><a class="btn btn-red" href="{page("admission")}">Admissions enquiry</a><a class="btn lg" href="tel:{build.TEL_1}"><i class="ph ph-phone"></i>Call {build.PHONE_1}</a></div></div>
 <ol class="steps">{steps}</ol></div></div></section>
<footer><div class="wrap"><div class="foot lg"><span>KSR Kalvi Nagar, Tiruchengode 637 215. CBSE Affiliation No. 1930318</span><span>{socials()}</span></div></div></footer>
<script>{COMMON_JS}
const S = {stages_js}, st = document.getElementById('stage'), th = document.querySelector('.thumb');
document.querySelectorAll('.seg button').forEach(b => b.addEventListener('click', () => {{
  const i = +b.dataset.i, s = S[i];
  document.querySelectorAll('.seg button').forEach(x => x.setAttribute('aria-selected', x === b));
  th.style.transform = `translateX(${{i * 100}}%)`;
  st.classList.remove('swap'); void st.offsetWidth; st.classList.add('swap');
  st.querySelector('img').src = s.img; st.querySelector('small').textContent = s.g; st.querySelector('h3').textContent = s.h; st.querySelector('p').textContent = s.p;
}}));
</script></body></html>"""


# ================================================================== 2. SCROLL STORYTELLING
def story():
    css = """
:root{--ink:#0a1220;--muted:#5d6b7c;--line:#e3e8ee;--brand:#0b5d95;--deep:#07406a;--red:#d8392b;--ease:cubic-bezier(.2,.9,.25,1)}
*{box-sizing:border-box}body{margin:0;font:400 18px/1.6 Figtree,system-ui,sans-serif;color:var(--ink);background:#fbfcfd;overflow-x:clip}
img{display:block;max-width:100%}a{color:inherit;text-decoration:none}p{margin:0}
h1,h2,h3{font-family:Outfit,sans-serif;font-weight:600;letter-spacing:-.04em;line-height:1;margin:0;text-wrap:balance}
.wrap{max-width:1280px;margin:0 auto;padding:0 clamp(16px,4vw,48px)}
.nav{position:sticky;top:0;z-index:20;background:rgb(251 252 253/.82);-webkit-backdrop-filter:blur(16px) saturate(180%);backdrop-filter:blur(16px) saturate(180%);border-bottom:1px solid rgb(0 0 0/.05)}
.nav .wrap{display:flex;align-items:center;gap:28px;height:64px}
.brand{display:flex;align-items:center;gap:10px;margin-right:auto}.brand img{width:34px;height:34px;object-fit:contain}
.brand strong{font:700 1rem Outfit;letter-spacing:-.01em}.brand small{display:none}
.links{display:flex;gap:24px;font-size:.92rem;color:var(--muted)}.links a:hover{color:var(--ink)}
.btn{display:inline-flex;align-items:center;gap:.5rem;padding:.8rem 1.3rem;border-radius:999px;font-weight:600;white-space:nowrap;transition:transform .3s var(--ease),background .3s}
.btn:active{transform:scale(.97)}.btn-red{background:var(--red);color:#fff}.btn-red:hover{background:#bf2c1f}
.btn-line{box-shadow:inset 0 0 0 1.5px var(--ink)}.btn-line:hover{background:var(--ink);color:#fff}
.nav .btn{padding:.55rem 1rem;font-size:.9rem}
/* opening: huge type, one line at a time */
.open{padding:clamp(56px,8vw,110px) 0 40px}
.kick{display:inline-flex;gap:.6rem;align-items:center;font-weight:600;color:var(--red);font-size:1rem}
.open h1{font-size:clamp(2.8rem,7.4vw,7.6rem);letter-spacing:-.055em;line-height:.92;margin-top:1.4rem}
.open h1 span{display:block;overflow:hidden;padding-bottom:.06em}
.open h1 span i{display:block;font-style:normal;animation:up 1.1s var(--ease) both}
.open h1 span:nth-child(2) i{animation-delay:.14s;color:var(--brand)}
@keyframes up{from{transform:translateY(105%)}}
.open .row{display:flex;justify-content:space-between;align-items:end;gap:30px;flex-wrap:wrap;margin-top:2.6rem}
.open p{font-size:1.3rem;color:var(--muted);max-width:36ch}
/* the photo grows from a card to the whole screen as you scroll */
.grow{height:230vh;position:relative}
.grow .pin{position:sticky;top:0;height:100vh;display:grid;place-items:center;overflow:hidden}
.grow figure{margin:0;position:relative;width:calc(var(--w,62) * 1vw);height:calc(var(--h,56) * 1vh);border-radius:calc(var(--rad,32) * 1px);overflow:hidden;will-change:width,height}
.grow img{width:100%;height:100%;object-fit:cover}
.grow figcaption{position:absolute;inset:auto 0 0 0;padding:clamp(20px,5vw,64px);color:#fff;background:linear-gradient(transparent,rgb(0 0 0/.6));opacity:var(--cap,0)}
.grow figcaption h2{font-size:clamp(2rem,5vw,4.6rem);max-width:16ch}
/* a statement that fills in word by word */
.say{padding:clamp(80px,12vw,180px) 0}
.say p{font:600 clamp(1.9rem,4.4vw,4rem)/1.12 Outfit;letter-spacing:-.03em;max-width:24ch}
.say p span{color:#d4dbe3;transition:color .25s}.say p span.on{color:var(--ink)}
/* numbers */
.nums{display:grid;grid-template-columns:repeat(5,1fr);border-top:1px solid var(--line)}
.nums div{padding:28px 18px 0 0}.nums strong{display:block;font:600 clamp(2.4rem,5vw,4.6rem)/1 Outfit;letter-spacing:-.05em}
.nums span{display:block;margin-top:.8rem;color:var(--muted);font-size:.95rem;max-width:22ch}
/* stages: cards that pin and stack */
.stack{padding:clamp(80px,10vw,140px) 0 0}
.stack>.wrap>h2{font-size:clamp(2.4rem,6vw,5.4rem);max-width:14ch;margin-bottom:3rem}
.card{position:sticky;top:calc(84px + var(--i) * 22px);display:grid;grid-template-columns:1fr 1fr;min-height:72vh;margin-bottom:6vh;border-radius:36px;overflow:hidden;
 background:var(--bgc);color:var(--fg,#fff);transform-origin:50% 0;transform:scale(var(--s,1));box-shadow:0 -10px 40px -20px rgb(0 0 0/.3)}
.card .txt{padding:clamp(28px,4vw,56px);display:flex;flex-direction:column;justify-content:space-between;gap:30px}
.card small{font-weight:600;opacity:.75;font-size:1rem}.card h3{font-size:clamp(2.4rem,4.6vw,4.4rem);letter-spacing:-.045em}
.card h4{font:600 1.35rem/1.25 Outfit;margin:0}.card p{opacity:.82;margin-top:.7rem;max-width:42ch}
.card img{width:100%;height:100%;object-fit:cover}
/* life: a horizontal track driven by vertical scroll */
.side{height:calc(var(--n) * 55vh + 100vh);position:relative}
.side .pin{position:sticky;top:0;height:100vh;overflow:hidden;display:flex;flex-direction:column;justify-content:center;gap:40px}
.side h2{font-size:clamp(2.4rem,6vw,5.4rem);padding:0 clamp(16px,4vw,48px)}
.track{display:flex;gap:22px;padding:0 clamp(16px,4vw,48px);will-change:transform}
.track a{flex:0 0 clamp(280px,34vw,480px)}.track img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:28px}
.track h3{font-size:1.4rem;margin-top:1rem;letter-spacing:-.02em}.track span{color:var(--muted);font-size:.95rem}
/* one big voice */
.voice{padding:clamp(90px,12vw,180px) 0;text-align:left}
.voice blockquote{margin:0;font:600 clamp(2.2rem,5.4vw,5rem)/1.05 Outfit;letter-spacing:-.045em;max-width:18ch}
.voice figcaption{display:flex;align-items:center;gap:14px;margin-top:2rem}.voice figcaption img{width:56px;height:56px;border-radius:50%;object-fit:cover}
.voice small{display:block;color:var(--muted)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:4rem;padding-top:2rem;border-top:1px solid var(--line)}
.two p{font:500 1.2rem/1.5 Outfit}.two b{display:block;margin-top:1rem;font-size:.95rem}.two small{color:var(--muted)}
/* the ask */
.ask{background:var(--ink);color:#fff;padding:clamp(90px,12vw,170px) 0;border-radius:44px 44px 0 0}
.ask h2{font-size:clamp(2.8rem,8vw,8rem);letter-spacing:-.055em;max-width:12ch}
.ask p{color:#a9b6c6;font-size:1.2rem;margin-top:1.6rem;max-width:44ch}
.ask .ctas{display:flex;gap:12px;flex-wrap:wrap;margin-top:2.4rem}.ask .btn-line{box-shadow:inset 0 0 0 1.5px #fff}.ask .btn-line:hover{background:#fff;color:var(--ink)}
.ages{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:#26313f;margin-top:4rem;border-radius:20px;overflow:hidden}
.ages div{background:var(--ink);padding:22px}.ages b{display:block;font:600 1.3rem Outfit}.ages span{color:#a9b6c6;font-size:.92rem}
footer{background:var(--ink);color:#a9b6c6;padding:0 0 34px;font-size:.92rem}
footer .wrap{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;border-top:1px solid #26313f;padding-top:26px}
.soc{display:inline-block;width:34px;height:34px;margin-left:8px}.soc svg{width:100%;height:100%}
.rv{opacity:0;transform:translateY(30px);transition:opacity 1.1s var(--ease),transform 1.1s var(--ease)}.rv.in{opacity:1;transform:none}
@media (max-width:900px){.links{display:none}.nums{grid-template-columns:1fr 1fr}.nums div:last-child{grid-column:span 2}
 .card{grid-template-columns:1fr;min-height:0}.card img{height:260px}.two{grid-template-columns:1fr}.ages{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){.open h1 span i{animation:none}.rv{opacity:1;transform:none}.say p span{color:var(--ink)}}
"""
    words = "Akshara follows CBSE expectations and builds skills for an international context. Every stage has its own way of teaching.".split()
    say = " ".join(f"<span>{E(w)}</span>" for w in words)
    nums = "".join(f'<div class="rv">{fact_num(a, n, s)}<span>{d}</span></div>' for a, n, s, d in FACTS)
    colors = [("#0b5d95", "#fff"), ("#e7eef5", "#0a1220"), ("#d8392b", "#fff"), ("#0a1220", "#fff")]
    cards = "".join(
        f'<article class="card" style="--i:{i};--bgc:{bg};--fg:{fg}"><div class="txt"><div><small>{g}</small><h3>{n}</h3></div>'
        f'<div><h4>{E(h)}</h4><p>{E(p)}</p></div></div><img src="{img(im)}" alt="{n} stage at Akshara" loading="lazy"></article>'
        for i, ((k, n, g, im, ic, h, p), (bg, fg)) in enumerate(zip(STAGES, colors)))
    track = "".join(f'<a href="{page("life-akshara")}#{k}"><img src="{img(i)}" alt="{E(t)}" loading="lazy"><h3>{E(t)}</h3><span>{E(d)}</span></a>' for k, i, t, d in LIFE)
    q0 = QUOTES[0]
    two = "".join(f'<div class="rv"><p>&ldquo;{E(q)}&rdquo;</p><b>{E(n)}</b><small>{E(r)}</small></div>' for q, p, n, r in QUOTES[1:])
    ages = "".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in AGES)
    return head("Scroll storytelling", css) + f"""<body>
<nav class="nav" aria-label="Main"><div class="wrap">{brand()}<div class="links">{navlinks()}</div><a class="btn btn-red" href="{page("admission")}">Enquire</a></div></nav>
<header class="open"><div class="wrap">
 <a class="kick" href="{page("admission")}">{NOTICE[0]}. {NOTICE[1]} <i class="ph ph-arrow-right"></i></a>
 <h1><span><i>Nurturing young minds.</i></span><span><i>Tomorrow's leaders.</i></span></h1>
 <div class="row"><p>{LEDE}</p><div><a class="btn btn-red" href="{page("admission")}">Admissions enquiry</a> <a class="btn btn-line" href="{page("contact-us")}#visit">Book a campus visit</a></div></div>
</div></header>
<section class="grow" id="grow"><div class="pin"><figure><img src="{img("career-banner.jpg")}" alt="A teacher with students at their laptops">
 <figcaption><h2>Pre-KG to Grade XII, on one campus in Tiruchengode.</h2></figcaption></figure></div></section>
<section class="say"><div class="wrap"><p id="say">{say}</p></div></section>
<section><div class="wrap"><div class="nums">{nums}</div></div></section>
<section class="stack"><div class="wrap"><h2 class="rv">Four stages, one way of growing.</h2>{cards}</div></section>
<section class="side" id="side" style="--n:{len(LIFE)}"><div class="pin"><h2>More than a classroom.</h2><div class="track">{track}</div></div></section>
<section class="voice"><div class="wrap"><figure class="rv" style="margin:0"><blockquote>&ldquo;{E(q0[0])}&rdquo;</blockquote>
 <figcaption><img src="{img(q0[1])}" alt="" loading="lazy"><div><b>{q0[2]}</b><small>{q0[3]}</small></div></figcaption></figure><div class="two">{two}</div></div></section>
<section class="ask"><div class="wrap"><h2 class="rv">{ADMIT_H}</h2><p>{ADMIT_P}</p>
 <div class="ctas"><a class="btn btn-red" href="{page("admission")}">Admissions enquiry</a><a class="btn btn-line" href="tel:{build.TEL_1}">Call {build.PHONE_1}</a></div>
 <div class="ages">{ages}</div></div></section>
<footer><div class="wrap"><span>KSR Akshara Academy, KSR Kalvi Nagar, Tiruchengode 637 215</span><span>{socials()}</span></div></footer>
<script>{COMMON_JS}
// one rAF loop, active only while a scroll scene is on screen (no scroll listeners)
const grow = document.getElementById('grow'), fig = grow.querySelector('figure'), side = document.getElementById('side'), track = side.querySelector('.track');
const say = [...document.querySelectorAll('#say span')], sayBox = document.getElementById('say'), cards = [...document.querySelectorAll('.card')];
const prog = el => {{ const b = el.getBoundingClientRect(); return Math.min(1, Math.max(0, -b.top / (b.height - innerHeight))); }};
const live = new Set();
const vio = new IntersectionObserver(es => {{ es.forEach(e => e.isIntersecting ? live.add(e.target) : live.delete(e.target)); if (live.size) tick(); }});
[grow, side, sayBox.parentElement, document.querySelector('.stack')].forEach(el => vio.observe(el));
let raf = 0;
function tick() {{ if (raf) return; raf = requestAnimationFrame(() => {{ raf = 0; frame(); if (live.size) tick(); }}); }}
function frame() {{
  if (live.has(grow)) {{ const k = Math.min(1, prog(grow) * 1.4), e = 1 - Math.pow(1 - k, 3);
    fig.style.setProperty('--w', 62 + 38 * e); fig.style.setProperty('--h', 56 + 44 * e); fig.style.setProperty('--rad', 32 * (1 - e)); fig.style.setProperty('--cap', Math.max(0, (k - .7) / .3)); }}
  if (live.has(side)) {{ const k = prog(side); track.style.transform = `translateX(${{-k * (track.scrollWidth - innerWidth + 48)}}px)`; }}
  if (live.has(sayBox.parentElement)) {{ const b = sayBox.getBoundingClientRect(), k = Math.min(1, Math.max(0, (innerHeight * .85 - b.top) / (b.height + innerHeight * .35)));
    say.forEach((w, i) => w.classList.toggle('on', i / say.length < k)); }}
  cards.forEach((c, i) => {{ const n = cards[i + 1]; if (!n) return; const t = n.getBoundingClientRect().top, k = Math.min(1, Math.max(0, 1 - (t - 84) / innerHeight));
    c.style.setProperty('--s', 1 - k * .06); }});
}}
if (reduce) {{ fig.style.setProperty('--w', 100); fig.style.setProperty('--h', 100); fig.style.setProperty('--rad', 0); fig.style.setProperty('--cap', 1); say.forEach(w => w.classList.add('on')); }}
</script></body></html>"""


# ================================================================== 3. BOLD EDITORIAL
def editorial():
    css = """
:root{--ink:#0a1f3c;--paper:#f6f8fb;--red:#e0392a;--sky:#a9d8ff;--brand:#0b5d95;--ease:cubic-bezier(.2,.9,.25,1)}
*{box-sizing:border-box}html{overflow-x:clip}body{margin:0;font:400 17px/1.55 Figtree,system-ui,sans-serif;color:var(--ink);background:var(--paper);overflow-x:hidden}
img{display:block;max-width:100%}a{color:inherit;text-decoration:none}p{margin:0}
h1,h2,h3{font-family:Outfit,sans-serif;font-weight:800;letter-spacing:-.04em;line-height:.9;margin:0;text-transform:uppercase}
.wrap{max-width:1320px;margin:0 auto;padding:0 clamp(16px,3vw,36px)}
.top{border-bottom:2px solid var(--ink)}.top .wrap{display:flex;align-items:center;gap:26px;height:70px}
.brand{display:flex;align-items:center;gap:10px;margin-right:auto}.brand img{width:42px;height:42px;object-fit:contain}
.brand strong{display:block;font:800 1.05rem/1 Outfit;text-transform:uppercase;letter-spacing:-.01em}.brand small{font-size:.72rem;font-weight:600}
.links{display:flex;gap:22px;font-weight:600;font-size:.95rem}.links a{position:relative}.links a::after{content:"";position:absolute;left:0;right:0;bottom:-4px;height:2px;background:var(--red);transform:scaleX(0);transform-origin:left;transition:transform .35s var(--ease)}
.links a:hover::after{transform:none}
.btn{display:inline-flex;align-items:center;gap:.5rem;padding:.95rem 1.4rem;font-weight:700;text-transform:uppercase;letter-spacing:.02em;font-size:.92rem;border:2px solid var(--ink);transition:transform .2s,box-shadow .2s;white-space:nowrap}
.btn:hover{transform:translate(-3px,-3px);box-shadow:5px 5px 0 var(--ink)}.btn:active{transform:none;box-shadow:none}
.btn-red{background:var(--red);color:#fff}.btn-ink{background:var(--ink);color:#fff}.btn-white{background:#fff;color:var(--ink)}
/* hero: the name, huge, with a collage threaded through it */
.hero{position:relative;padding:28px 0 0;overflow-x:clip}
.mega{font:800 clamp(4.4rem,18.6vw,17.5rem)/.8 Outfit,sans-serif;letter-spacing:-.06em;color:var(--ink);white-space:nowrap}
.mega span{display:inline-block;animation:drop .9s var(--ease) both;animation-delay:calc(var(--d) * 50ms)}
@keyframes drop{from{transform:translateY(-40%);opacity:0}}
.collage{display:grid;grid-template-columns:1.1fr 1.3fr .9fr;gap:18px;margin-top:-3.6vw;position:relative;align-items:start}
.c1{position:relative;transform:rotate(-2.5deg);margin-top:5vw}.c1 img{border:2px solid var(--ink);aspect-ratio:4/5;object-fit:cover;width:100%}
.c2{background:var(--red);color:#fff;padding:clamp(22px,3vw,40px);border:2px solid var(--ink);position:relative;z-index:2}
.c2 h1{font-size:clamp(2rem,3.6vw,3.4rem);line-height:.95}
.c2 p{font-size:1.1rem;margin-top:1.2rem;max-width:36ch}
.c2 .ctas{display:flex;gap:10px;flex-wrap:wrap;margin-top:1.6rem}
.c3{transform:rotate(3deg);margin-top:2vw;position:relative}.c3 img{border:2px solid var(--ink);aspect-ratio:3/4;object-fit:cover;width:100%;background:#fff}
.badge{position:absolute;width:132px;height:132px;right:-18px;top:-50px;z-index:3;animation:spin 18s linear infinite}
.badge svg{width:100%;height:100%;overflow:visible}.badge text{font:800 11.5px Outfit;letter-spacing:2.4px;text-transform:uppercase;fill:var(--ink)}
.badge circle{fill:var(--sky);stroke:var(--ink);stroke-width:2}
@keyframes spin{to{transform:rotate(360deg)}}
.note{position:absolute;left:-10px;bottom:-22px;background:var(--sky);border:2px solid var(--ink);padding:.5rem .9rem;font:800 .9rem Outfit;text-transform:uppercase;transform:rotate(-4deg)}
/* the one marquee */
.marq{margin-top:clamp(40px,6vw,80px);background:var(--ink);color:#fff;border-block:2px solid var(--ink);overflow:hidden;transform:rotate(-1.2deg) scale(1.02)}
.marq div{display:flex;gap:40px;width:max-content;padding:16px 0;font:800 clamp(1.6rem,3.4vw,2.8rem)/1 Outfit;text-transform:uppercase;animation:mq 28s linear infinite}
.marq i{color:var(--red);font-size:.8em}
@keyframes mq{to{transform:translateX(-50%)}}
/* numbers as a ruled grid with colour blocks */
.nums{display:grid;grid-template-columns:repeat(5,1fr);border:2px solid var(--ink);margin-top:clamp(60px,8vw,110px)}
.nums div{padding:24px 20px 26px;border-right:2px solid var(--ink)}.nums div:last-child{border-right:0}
.nums div:nth-child(3){background:var(--ink);color:#fff}.nums div:nth-child(4){background:var(--red);color:#fff}
.nums strong{display:block;font:800 clamp(2.4rem,4.4vw,4.2rem)/1 Outfit;letter-spacing:-.05em}
.nums span{display:block;margin-top:.7rem;font-weight:600;font-size:.92rem;line-height:1.35}
.h2{font-size:clamp(2.6rem,7vw,6.4rem);margin:clamp(70px,9vw,130px) 0 30px}
.h2 em{font-style:normal;color:var(--red)}
/* stages: four colour blocks */
.stages{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border:2px solid var(--ink)}
.st{display:flex;flex-direction:column;border-right:2px solid var(--ink);background:var(--bg);color:var(--fg);transition:transform .3s var(--ease)}
.st:last-child{border-right:0}.st:hover{transform:translateY(-8px);z-index:1;box-shadow:0 8px 0 var(--ink)}
.st img{aspect-ratio:1;object-fit:cover;border-bottom:2px solid var(--ink);filter:saturate(1.1) contrast(1.05)}
.st div{padding:20px 18px 24px}.st small{font-weight:700;font-size:.85rem;text-transform:uppercase;letter-spacing:.04em}
.st h3{font-size:clamp(1.6rem,2.4vw,2.2rem);margin:.4rem 0 .7rem}.st p{font-size:.95rem;opacity:.9}
/* life collage */
.mosaic{display:grid;grid-template-columns:repeat(12,1fr);gap:18px}
.mosaic a{position:relative;display:block}.mosaic img{width:100%;object-fit:cover;border:2px solid var(--ink);transition:transform .4s var(--ease)}
.mosaic a:hover img{transform:rotate(-1deg) scale(1.02)}
.mosaic h3{font-size:clamp(1.1rem,1.6vw,1.5rem);margin-top:.7rem;line-height:1}.mosaic span{font-weight:600;font-size:.9rem;opacity:.75}
.m1{grid-column:span 7}.m1 img{aspect-ratio:16/10}.m2{grid-column:span 5}.m2 img{aspect-ratio:5/4}
.m3,.m4,.m5{grid-column:span 4}.m3 img,.m4 img,.m5 img{aspect-ratio:1}
.clubs{grid-column:span 12;display:flex;flex-wrap:wrap;gap:10px;align-items:center;border:2px solid var(--ink);padding:18px;background:#fff}
.clubs b{font:800 1.4rem Outfit;text-transform:uppercase;margin-right:12px}
.clubs span{padding:.45rem .9rem;border:2px solid var(--ink);border-radius:999px;font-weight:700;font-size:.92rem;background:var(--sky)}
.clubs span:nth-child(3n){background:#fff}.clubs span:nth-child(4n){background:var(--red);color:#fff}
/* voice: a navy block */
.voice{background:var(--ink);color:#fff;margin-top:clamp(70px,9vw,130px);padding:clamp(60px,8vw,110px) 0}
.voice .mark{font:800 10rem/0.6 Outfit;color:var(--red);height:70px}
.voice blockquote{margin:0;font:800 clamp(2rem,5vw,4.6rem)/1 Outfit;text-transform:uppercase;letter-spacing:-.04em;max-width:18ch}
.voice figcaption{margin-top:2rem;font-weight:700;display:flex;gap:14px;align-items:center}.voice figcaption img{width:56px;height:56px;border-radius:50%;border:2px solid #fff;object-fit:cover}
.voice small{display:block;font-weight:500;opacity:.75}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:3rem}.vs div{border:2px solid #fff;padding:22px}.vs p{font-size:1.1rem}.vs b{display:block;margin-top:1rem}
/* admissions: the red poster */
.admit{background:var(--red);color:#fff;border-bottom:2px solid var(--ink);padding:clamp(60px,8vw,110px) 0}
.admit h2{font-size:clamp(3rem,9vw,8.6rem);line-height:.86}
.admit p{font-size:1.2rem;margin-top:1.4rem;max-width:44ch}
.tix{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:2.4rem}
.tix div{background:#fff;color:var(--ink);border:2px solid var(--ink);padding:18px;transform:rotate(var(--r));box-shadow:5px 5px 0 var(--ink)}
.tix b{display:block;font:800 1.5rem Outfit;text-transform:uppercase}.tix span{font-weight:600;font-size:.92rem}
.admit .ctas{display:flex;gap:12px;flex-wrap:wrap;margin-top:2.4rem}
footer{background:var(--ink);color:#c9d6e6;padding:28px 0;font-weight:600;font-size:.92rem}
footer .wrap{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}
.soc{display:inline-block;width:34px;height:34px;margin-left:8px}.soc svg{width:100%;height:100%}
.rv{opacity:0;transform:translateY(30px);transition:opacity .8s var(--ease),transform .8s var(--ease)}.rv.in{opacity:1;transform:none}
@media (max-width:900px){.links{display:none}.collage{grid-template-columns:1fr 1fr}.c2{grid-column:span 2;order:-1}.badge{width:100px;height:100px;top:-30px}
 .nums{grid-template-columns:1fr 1fr}.nums div{border-bottom:2px solid var(--ink)}.nums div:last-child{grid-column:span 2}
 .stages{grid-template-columns:repeat(2,minmax(0,1fr))}.st h3{font-size:1.3rem;overflow-wrap:anywhere}.badge{right:4px}.st:nth-child(2){border-right:0}.st:nth-child(-n+2){border-bottom:2px solid var(--ink)}
 .m1,.m2{grid-column:span 12}.m3,.m4,.m5{grid-column:span 6}.vs,.tix{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.top .btn{display:none}.m3,.m4,.m5{grid-column:span 12}.vs{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){.marq div,.badge,.mega span{animation:none}.rv{opacity:1;transform:none}}
"""
    mega = "".join(f'<span style="--d:{i}">{c}</span>' for i, c in enumerate("AKSHARA"))
    words = ["Inquiry", "Sport", "The arts", "Values", "Pre-KG to XII", "Tiruchengode"]
    marq = "".join(f"<span>{w}</span><i class=\"ph ph-star\"></i>" for w in words) * 2
    nums = "".join(f'<div>{fact_num(a, n, s)}<span>{d}</span></div>' for a, n, s, d in FACTS)
    pal = [("var(--sky)", "var(--ink)"), ("#fff", "var(--ink)"), ("var(--ink)", "#fff"), ("var(--red)", "#fff")]
    stages = "".join(f'<a class="st rv" style="--bg:{bg};--fg:{fg}" href="{page("methodology")}#{k}"><img src="{img(im)}" alt="{n} stage" loading="lazy">'
                     f'<div><small>{g}</small><h3>{n}</h3><p>{E(h)}</p></div></a>' for (k, n, g, im, ic, h, p), (bg, fg) in zip(STAGES, pal))
    ms = "".join(f'<a class="m{i + 1} rv" href="{page("life-akshara")}#{k}"><img src="{img(im)}" alt="{E(t)}" loading="lazy"><h3>{E(t)}</h3><span>{E(d)}</span></a>'
                 for i, (k, im, t, d) in enumerate(LIFE[:5]))
    clubs = "".join(f"<span>{c}</span>" for c in CLUBS)
    q0 = QUOTES[0]
    vs = "".join(f'<div class="rv"><p>&ldquo;{E(q)}&rdquo;</p><b>{E(n)}, {E(r)}</b></div>' for q, p, n, r in QUOTES[1:])
    tix = "".join(f'<div style="--r:{r}deg"><b>{a}</b><span>{b}</span></div>' for (a, b), r in zip(AGES, [-2, 1.5, -1, 2]))
    return head("Bold editorial", css) + f"""<body>
<nav class="top" aria-label="Main"><div class="wrap">{brand()}<div class="links">{navlinks()}</div><a class="btn btn-red" href="{page("admission")}">Admissions</a></div></nav>
<header class="hero"><div class="wrap">
 <div class="mega" aria-label="Akshara">{mega}</div>
 <div class="collage">
  <figure class="c1" style="margin:0"><img src="{img("Fieldstrip.jpg")}" alt="Akshara students on a field trip"><span class="note">Field trips</span></figure>
  <div class="c2"><h1>{H1A} {H1B}</h1><p>{LEDE}</p>
   <div class="ctas"><a class="btn btn-white" href="{page("admission")}">Admissions enquiry <i class="ph ph-arrow-right"></i></a><a class="btn btn-ink" href="{page("contact-us")}#visit">Book a visit</a></div></div>
  <figure class="c3" style="margin:0"><div class="badge" aria-hidden="true"><svg viewBox="0 0 132 132"><circle cx="66" cy="66" r="64"/><path id="cp" d="M66,66 m-48,0 a48,48 0 1,1 96,0 a48,48 0 1,1 -96,0" fill="none"/>
   <text><textPath href="#cp">Admissions 2027-28 + Vijayadasami + </textPath></text></svg></div>
   <img src="{img("Students.jpg")}" alt="Students around a globe"></figure>
 </div></div>
 <div class="marq" aria-hidden="true"><div>{marq}</div></div>
</header>
<main class="wrap">
 <div class="nums rv">{nums}</div>
 <h2 class="h2 rv">One curriculum. <em>Four stages.</em></h2><div class="stages">{stages}</div>
 <h2 class="h2 rv">More than a <em>classroom.</em></h2><div class="mosaic">{ms}<div class="clubs rv"><b>Nine clubs</b>{clubs}</div></div>
</main>
<section class="voice"><div class="wrap"><div class="mark" aria-hidden="true">&ldquo;</div><figure style="margin:0" class="rv"><blockquote>{E(q0[0])}</blockquote>
 <figcaption><img src="{img(q0[1])}" alt="" loading="lazy"><div>{q0[2]}<small>{q0[3]}</small></div></figcaption></figure><div class="vs">{vs}</div></div></section>
<section class="admit"><div class="wrap"><h2 class="rv">Admissions open.</h2><p>{ADMIT_H} {ADMIT_P}</p><div class="tix">{tix}</div>
 <div class="ctas"><a class="btn btn-white" href="{page("admission")}">Admissions enquiry <i class="ph ph-arrow-right"></i></a><a class="btn btn-ink" href="tel:{build.TEL_1}"><i class="ph ph-phone"></i>Call {build.PHONE_1}</a></div></div></section>
<footer><div class="wrap"><span>KSR Akshara Academy. Tiruchengode 637 215. CBSE 1930318</span><span>{socials()}</span></div></footer>
<script>{COMMON_JS}</script></body></html>"""


# ================================================================== 4. PLAYFUL SOFT 3D
def playful():
    css = """
:root{--ink:#16304d;--muted:#5b6f86;--sky:#dff0ff;--blue:#2f86d6;--deep:#0b5d95;--coral:#ff6b5b;--sun:#ffd166;--mint:#bff0dc;--peach:#ffe1d6;--ease:cubic-bezier(.34,1.56,.64,1);--r:32px}
*{box-sizing:border-box}body{margin:0;font:400 17px/1.6 Figtree,system-ui,sans-serif;color:var(--ink);background:#f1f8ff;overflow-x:hidden}
img{display:block;max-width:100%}a{color:inherit;text-decoration:none}p{margin:0}
h1,h2,h3{font-family:Outfit,sans-serif;font-weight:700;letter-spacing:-.03em;line-height:1.05;margin:0;text-wrap:balance}
.wrap{max-width:1240px;margin:0 auto;padding:0 clamp(16px,4vw,40px)}
/* clay: soft top light, gentle inner shade, a long soft shadow */
.clay{background:#fff;border-radius:var(--r);box-shadow:inset 0 2px 0 rgb(255 255 255/.9),inset 0 -6px 0 rgb(22 48 77/.05),0 22px 40px -18px rgb(47 134 214/.35),0 4px 10px -4px rgb(22 48 77/.08)}
.nav{position:sticky;top:12px;z-index:20;margin-top:12px}
.nav .in{display:flex;align-items:center;gap:8px;padding:8px 8px 8px 12px;border-radius:999px}
.brand{display:flex;align-items:center;gap:10px;margin-right:auto}.brand img{width:42px;height:42px;border-radius:14px}
.brand strong{display:block;font:700 1.02rem/1.1 Outfit}.brand small{font-size:.74rem;color:var(--muted)}
.links{display:flex;gap:4px}.links a{padding:.6rem .95rem;border-radius:999px;font-weight:600;font-size:.95rem;transition:background .2s,transform .3s var(--ease)}
.links a:hover{background:var(--sky);transform:translateY(-2px)}
/* chunky buttons that press down */
.btn{display:inline-flex;align-items:center;gap:.55rem;padding:.95rem 1.5rem;border-radius:999px;font-weight:700;white-space:nowrap;transition:transform .25s var(--ease),box-shadow .25s}
.btn-coral{background:var(--coral);color:#fff;box-shadow:0 6px 0 #d94a3b,0 14px 24px -8px rgb(255 107 91/.6)}
.btn-coral:hover{transform:translateY(-3px);box-shadow:0 9px 0 #d94a3b,0 18px 28px -8px rgb(255 107 91/.6)}
.btn-coral:active{transform:translateY(5px);box-shadow:0 1px 0 #d94a3b}
.btn-white{background:#fff;box-shadow:0 6px 0 #c9dcef,0 14px 24px -10px rgb(47 134 214/.35)}
.btn-white:hover{transform:translateY(-3px);box-shadow:0 9px 0 #c9dcef}.btn-white:active{transform:translateY(5px);box-shadow:0 1px 0 #c9dcef}
/* hero */
.hero{display:grid;grid-template-columns:1fr 1fr;gap:30px;align-items:center;padding:clamp(40px,6vw,80px) 0 40px}
.hello{display:inline-flex;align-items:center;gap:.5rem;padding:.5rem 1rem;border-radius:999px;background:var(--sun);font-weight:700;font-size:.92rem;box-shadow:0 4px 0 #e9b63f}
.hero h1{font-size:clamp(2.6rem,5.4vw,4.8rem);margin-top:1.3rem}
.hero h1 em{font-style:normal;position:relative;white-space:nowrap;color:var(--deep)}
.hero h1 em::after{content:"";position:absolute;left:-2%;right:-2%;bottom:.04em;height:.32em;background:var(--sun);border-radius:999px;z-index:-1;transform:rotate(-1deg)}
.hero p{font-size:1.18rem;color:var(--muted);margin-top:1.2rem;max-width:42ch}
.ctas{display:flex;flex-wrap:wrap;gap:14px;margin-top:2rem}
.art{position:relative;aspect-ratio:1;max-width:560px;justify-self:center;width:100%}
.blob{position:absolute;inset:8%;border-radius:58% 42% 55% 45%/48% 56% 44% 52%;overflow:hidden;background:var(--sky);
 box-shadow:0 30px 60px -20px rgb(47 134 214/.5),inset 0 0 0 10px #fff;animation:morph 12s ease-in-out infinite}
.blob img{width:100%;height:100%;object-fit:cover}
@keyframes morph{50%{border-radius:44% 56% 42% 58%/56% 44% 56% 44%}}
/* CSS-only 3D shapes: lit spheres, a pill and a ring */
.sh{position:absolute;border-radius:50%;animation:float 6s ease-in-out infinite}
.ball{width:var(--s);height:var(--s);background:radial-gradient(circle at 32% 28%,#fff 0 6%,var(--c) 40%,var(--d) 100%);box-shadow:0 18px 30px -12px var(--d)}
.pillx{width:110px;height:46px;border-radius:999px;background:linear-gradient(180deg,#ffd98a,#f5b632);box-shadow:inset 0 4px 6px rgb(255 255 255/.6),0 16px 26px -10px #d99a12;transform:rotate(-24deg)}
.ring{width:96px;height:96px;border:20px solid transparent;background:conic-gradient(from 200deg,#8fd0ff,#2f86d6,#8fd0ff) border-box;
 -webkit-mask:radial-gradient(closest-side,transparent calc(100% - 22px),#000 calc(100% - 21px));mask:radial-gradient(closest-side,transparent calc(100% - 22px),#000 calc(100% - 21px))}
@keyframes float{50%{translate:0 -14px}}
.tag{position:absolute;padding:.7rem 1rem;border-radius:20px;font-weight:700;font-size:.92rem;display:flex;gap:.5rem;align-items:center;animation:float 7s ease-in-out infinite}
.tag i{width:30px;height:30px;border-radius:10px;display:grid;place-items:center;background:var(--sky);color:var(--deep);font-size:1.1rem}
/* facts: chunky pastel tiles */
.facts{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:20px}
.fact{padding:22px;border-radius:28px;background:var(--bg);box-shadow:inset 0 2px 0 rgb(255 255 255/.7),inset 0 -6px 0 rgb(0 0 0/.05),0 16px 30px -18px rgb(22 48 77/.35);transition:transform .4s var(--ease)}
.fact:hover{transform:translateY(-6px) rotate(-1.5deg)}
.fact strong{display:block;font:800 clamp(1.9rem,3vw,2.6rem)/1 Outfit;letter-spacing:-.03em}.fact span{display:block;margin-top:.5rem;font-size:.88rem;line-height:1.35;color:var(--muted)}
.sec{padding:clamp(70px,9vw,120px) 0 0}.sec h2{font-size:clamp(2rem,4vw,3.2rem);max-width:20ch}.sub{color:var(--muted);font-size:1.1rem;margin-top:.8rem;max-width:54ch}
/* stages */
.stages{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:2.2rem}
.st{padding:14px 14px 22px;transition:transform .45s var(--ease)}.st:hover{transform:translateY(-10px) rotate(var(--rot))}
.st img{border-radius:22px;aspect-ratio:4/3;object-fit:cover;width:100%}
.st .ic{width:54px;height:54px;border-radius:18px;display:grid;place-items:center;font-size:1.6rem;background:var(--bg);margin:-30px 0 0 14px;position:relative;box-shadow:0 5px 0 rgb(0 0 0/.08)}
.st h3{font-size:1.4rem;margin:.8rem 8px 0}.st small{display:block;margin:0 8px;color:var(--muted);font-weight:600}.st p{margin:.6rem 8px 0;font-size:.95rem;color:var(--muted)}
/* life: tilted photo cards */
.life{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;margin-top:2.4rem}
.lc{padding:12px 12px 18px;transform:rotate(var(--rot));transition:transform .5s var(--ease)}.lc:hover{transform:rotate(0) scale(1.04)}
.lc img{border-radius:22px;aspect-ratio:4/3;object-fit:cover;width:100%}.lc h3{font-size:1.15rem;margin:.9rem 6px 0}.lc span{display:block;margin:0 6px;color:var(--muted);font-size:.92rem}
.clubs{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}.clubs span{padding:.6rem 1.1rem;border-radius:999px;font-weight:700;background:var(--bg);box-shadow:0 4px 0 rgb(0 0 0/.07);transition:transform .3s var(--ease)}
.clubs span:hover{transform:translateY(-4px) rotate(-3deg)}
/* voices as speech bubbles */
.qs{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:2.4rem;align-items:start}
.q{padding:26px;position:relative}.q::after{content:"";position:absolute;left:36px;bottom:-14px;width:28px;height:28px;background:#fff;transform:rotate(45deg);border-radius:4px;box-shadow:6px 6px 14px -8px rgb(47 134 214/.3)}
.q blockquote{margin:0;font:600 1.08rem/1.5 Outfit}.who{display:flex;gap:12px;align-items:center;margin:26px 0 0 18px}
.who img{width:50px;height:50px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 4px #fff,0 6px 14px -4px rgb(22 48 77/.3)}.who small{display:block;color:var(--muted);font-size:.84rem}
/* admissions */
.admit{display:grid;grid-template-columns:1.1fr 1fr;gap:30px;padding:clamp(26px,4vw,52px);background:linear-gradient(160deg,#fff,#eaf5ff)}
.ages{display:flex;flex-wrap:wrap;gap:10px;margin-top:1.6rem}.ages div{padding:.7rem 1rem;border-radius:18px;background:var(--bg)}.ages b{font-family:Outfit;margin-right:.4rem}
.ages span{font-size:.9rem;color:var(--muted)}
.steps{list-style:none;margin:0;padding:0;display:grid;gap:14px;counter-reset:s}
.steps li{display:grid;grid-template-columns:56px 1fr;gap:14px;align-items:center;padding:16px;border-radius:24px;background:#fff;box-shadow:0 10px 20px -14px rgb(47 134 214/.5)}
.steps li::before{counter-increment:s;content:counter(s);width:56px;height:56px;border-radius:20px;display:grid;place-items:center;font:800 1.4rem Outfit;color:#fff;background:var(--c);box-shadow:0 5px 0 var(--d)}
.steps b{font-family:Outfit;font-size:1.1rem}.steps p{color:var(--muted);font-size:.94rem}
footer{padding:60px 0 36px}.foot{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;padding:20px 26px;border-radius:999px;color:var(--muted);font-size:.92rem;font-weight:600}
.soc{display:inline-block;width:38px;height:38px;margin-left:8px;transition:transform .3s var(--ease)}.soc:hover{transform:translateY(-4px) rotate(-8deg)}.soc svg{width:100%;height:100%}
.rv{opacity:0;transform:translateY(40px) scale(.96);transition:opacity .7s ease,transform .9s var(--ease)}.rv.in{opacity:1;transform:none}
@media (max-width:980px){.links{display:none}.hero{grid-template-columns:1fr}.facts{grid-template-columns:1fr 1fr}.fact:last-child{grid-column:span 2}
 .stages,.life{grid-template-columns:1fr 1fr}.qs,.admit{grid-template-columns:1fr}}
@media (max-width:560px){.nav .btn{display:none}.stages,.life{grid-template-columns:1fr}.tag{font-size:.8rem}.ring{width:70px;height:70px;right:2%!important}}
@media (prefers-reduced-motion:reduce){.sh,.tag,.blob{animation:none}.rv{opacity:1;transform:none}}
"""
    tints = ["#dff0ff", "#ffe1d6", "#fff1c9", "#d5f5e6", "#e7e3ff"]
    facts = "".join(f'<div class="fact rv" style="--bg:{t};transition-delay:{i * 60}ms">{fact_num(a, n, s)}<span>{d}</span></div>' for i, ((a, n, s, d), t) in enumerate(zip(FACTS, tints)))
    rots = [-1.5, 1.2, -1, 1.6]
    stages = "".join(f'<a class="st clay rv" style="--rot:{r}deg" href="{page("methodology")}#{k}"><img src="{img(im)}" alt="{n} stage" loading="lazy">'
                     f'<span class="ic" style="--bg:{t}"><i class="ph {ic}"></i></span><h3>{n}</h3><small>{g}</small><p>{E(h)}</p></a>'
                     for (k, n, g, im, ic, h, p), r, t in zip(STAGES, rots, tints))
    life = "".join(f'<a class="lc clay rv" style="--rot:{r}deg" href="{page("life-akshara")}#{k}"><img src="{img(im)}" alt="{E(t)}" loading="lazy"><h3>{E(t)}</h3><span>{E(d)}</span></a>'
                   for (k, im, t, d), r in zip(LIFE, [-2, 1.5, -1, 2, -1.5, 1]))
    clubs = "".join(f'<span style="--bg:{tints[i % 5]}">{c}</span>' for i, c in enumerate(CLUBS))
    qs = "".join(f'<figure class="rv" style="margin:0"><div class="q clay"><blockquote>&ldquo;{E(q)}&rdquo;</blockquote></div><figcaption class="who"><img src="{img(p)}" alt="" loading="lazy"><div><b>{E(n)}</b><small>{E(r)}</small></div></figcaption></figure>' for q, p, n, r in QUOTES)
    ages = "".join(f'<div style="--bg:{tints[i]}"><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate(AGES))
    stepc = [("#2f86d6", "#1f68ad"), ("#ff6b5b", "#d94a3b"), ("#f5b632", "#d99a12")]
    steps = "".join(f'<li style="--c:{c};--d:{d}"><div><b>{a}</b><p>{b}</p></div></li>' for (a, b), (c, d) in zip(STEPS, stepc))
    return head("Playful soft 3D", css) + f"""<body>
<div class="wrap nav"><nav class="in clay" aria-label="Main">{brand()}<div class="links">{navlinks()}</div><a class="btn btn-coral" href="{page("admission")}">Admissions enquiry</a></nav></div>
<header class="wrap hero">
 <div><a class="hello" href="{page("admission")}"><i class="ph ph-hand-waving"></i>{NOTICE[0]} is open</a>
  <h1>Nurturing young minds and hearts of <em>tomorrow's leaders.</em></h1><p>{LEDE}</p>
  <div class="ctas"><a class="btn btn-coral" href="{page("admission")}">Admissions enquiry <i class="ph ph-arrow-right"></i></a><a class="btn btn-white" href="{page("contact-us")}#visit"><i class="ph ph-map-pin"></i>Book a campus visit</a></div></div>
 <div class="art" aria-hidden="true">
  <div class="blob"><img src="{img("Students.jpg")}" alt=""></div>
  <span class="sh ball" style="--s:84px;--c:#ff8a7a;--d:#e0503f;right:2%;top:6%"></span>
  <span class="sh ball" style="--s:46px;--c:#7cc4ff;--d:#2f86d6;left:4%;top:18%;animation-delay:-2s"></span>
  <span class="sh pillx" style="left:-2%;bottom:20%;animation-delay:-3s"></span>
  <span class="sh ring" style="right:-2%;bottom:14%;animation-delay:-1s"></span>
  <span class="tag clay" style="left:6%;bottom:2%;animation-delay:-4s"><i class="ph ph-student"></i>Pre-KG to Grade XII</span>
  <span class="tag clay" style="right:4%;top:44%;animation-delay:-2.5s"><i class="ph ph-medal"></i>3x International School Award</span>
 </div>
</header>
<section class="wrap"><div class="facts">{facts}</div></section>
<section class="sec wrap"><h2 class="rv">One curriculum, four stages, shaped by the NEP.</h2><p class="sub rv">Every stage has its own way of teaching.</p><div class="stages">{stages}</div></section>
<section class="sec wrap"><h2 class="rv">More than a classroom, every single day.</h2><div class="life">{life}</div><div class="clubs">{clubs}</div></section>
<section class="sec wrap"><h2 class="rv">What visitors and parents say.</h2><div class="qs">{qs}</div></section>
<section class="sec wrap"><div class="admit clay rv"><div><h2>{ADMIT_H}</h2><p class="sub">{ADMIT_P}</p><div class="ages">{ages}</div>
 <div class="ctas"><a class="btn btn-coral" href="{page("admission")}">Admissions enquiry</a><a class="btn btn-white" href="tel:{build.TEL_1}"><i class="ph ph-phone"></i>Call {build.PHONE_1}</a></div></div>
 <ol class="steps">{steps}</ol></div></section>
<footer class="wrap"><div class="foot clay"><span>KSR Kalvi Nagar, Tiruchengode 637 215</span><span>{socials()}</span></div></footer>
<script>{COMMON_JS}</script></body></html>"""


# ================================================================== chooser
def chooser():
    items = [("glass", "Liquid Glass", "Apple-style frosted glass over big campus photos.", "KSR-children.jpg"),
             ("story", "Scroll storytelling", "Huge type, a photo that grows to full screen, cards that stack.", "career-banner.jpg"),
             ("editorial", "Bold editorial", "Oversized type, colour blocks, collage and a marquee.", "Fieldstrip.jpg"),
             ("playful", "Playful soft 3D", "Clay-soft cards, bouncy buttons and floating shapes.", "Students.jpg")]
    cards = "".join(f'<a href="{k}/index.html"><img src="../assets/img/{i}" alt=""><b>{t}</b><span>{d}</span></a>' for k, t, d, i in items)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Homepage concepts | KSR Akshara Academy</title><meta name="robots" content="noindex"><link rel="stylesheet" href="../assets/css/vendor.css">
<style>body{{margin:0;font:400 17px/1.5 Figtree,sans-serif;background:#f4f7fa;color:#0b1b2e}}main{{max-width:1180px;margin:0 auto;padding:48px 20px}}
h1{{font:700 2.4rem Outfit;margin:0}}p{{color:#56687c}}.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px;margin-top:28px}}
a{{text-decoration:none;color:inherit;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 12px 30px -16px rgb(11 61 104/.35);transition:transform .3s}}a:hover{{transform:translateY(-4px)}}
img{{width:100%;aspect-ratio:16/10;object-fit:cover;display:block}}b{{display:block;font:600 1.25rem Outfit;padding:16px 18px 0}}span{{display:block;padding:4px 18px 18px;color:#56687c;font-size:.95rem}}</style></head>
<body><main><h1>Four homepage concepts</h1><p>Same real content, four current design trends. Only the homepage is built for each.</p><div class="g">{cards}</div></main></body></html>"""


if __name__ == "__main__":
    for name, fn in [("glass", glass), ("story", story), ("editorial", editorial), ("playful", playful)]:
        d = HERE / name; d.mkdir(exist_ok=True)
        (d / "index.html").write_text(fn())
        print("built concepts/%s/index.html" % name)
    (HERE / "index.html").write_text(chooser())
    print("built concepts/index.html")
