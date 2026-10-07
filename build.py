#!/usr/bin/env python3
"""Static site generator for the KSR Akshara Academy redesign concept.

Every page keeps the same URL slug as the live WordPress site (SEO-safe migration).
Run:  python3 build.py   then   python3 -m http.server 8000
"""
import html
import json
import re
from pathlib import Path
import time

ROOT = Path(__file__).parent
PHONE_1, PHONE_2 = "98949 32323", "95009 32323"
TEL_1, TEL_2 = "+919894932323", "+919500932323"
EMAIL, EMAIL_2 = "ksrakshara@gmail.com", "info@ksrakshara.org"
YT_ID = "gTh-rg_z7QY"
VER = str(int(time.time()))  # cache-buster: every build forces browsers to refetch CSS/JS
UP = "https://ksrakshara.org/wp-content/uploads"
MAP = ("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3911.6832562329355!2d77.82999147584292"
       "!3d11.357830148198989!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ba96401149b187f%3A0x691ed7b03dd6cb5e"
       "!2sK.S.R.%20AKSHARA%20ACADEMY%20(Senior%20Secondary%20School)!5e0!3m2!1sen!2sin!4v1732605201318!5m2!1sen!2sin")

# slug -> (nav label) ; used for links + aria-current
NAV = [
    ("About", [("Our story", "about-us"), ("Management", "about-us/management"),
               ("Why Akshara?", "about-us/why-akshara"), ("The Akshara tree", "akshara-tree"), ("Testimonials", "testimonial"),
               ("Documents & disclosure", "about-us/documents-information")]),
    ("Academics", "methodology"),
    ("Student life", [("Life at Akshara", "life-akshara"), ("Sports", "sports"), ("Holiday assignments", "holiday-assignments")]),
    ("Campus", [("Hostel", "facilities-hostel"), ("Transport", "facilities-transport")]),
    ("News", "events"),
    ("Careers", "join-us"),
    ("Contact", "contact-us"),
]


CUR = ' aria-current="page"'
CONTAIN = ' style="object-fit:contain;background:var(--surface-2)"'


NEWS = json.loads((ROOT / "assets/data/news.json").read_text()) if (ROOT / "assets/data/news.json").exists() else []
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


# Official brand marks (path data from Simple Icons, CC0), drawn the way each brand shows its own logo
_SI = {'facebook': 'M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z', 'instagram': 'M7.0301.084c-1.2768.0602-2.1487.264-2.911.5634-.7888.3075-1.4575.72-2.1228 1.3877-.6652.6677-1.075 1.3368-1.3802 2.127-.2954.7638-.4956 1.6365-.552 2.914-.0564 1.2775-.0689 1.6882-.0626 4.947.0062 3.2586.0206 3.6671.0825 4.9473.061 1.2765.264 2.1482.5635 2.9107.308.7889.72 1.4573 1.388 2.1228.6679.6655 1.3365 1.0743 2.1285 1.38.7632.295 1.6361.4961 2.9134.552 1.2773.056 1.6884.069 4.9462.0627 3.2578-.0062 3.668-.0207 4.9478-.0814 1.28-.0607 2.147-.2652 2.9098-.5633.7889-.3086 1.4578-.72 2.1228-1.3881.665-.6682 1.0745-1.3378 1.3795-2.1284.2957-.7632.4966-1.636.552-2.9124.056-1.2809.0692-1.6898.063-4.948-.0063-3.2583-.021-3.6668-.0817-4.9465-.0607-1.2797-.264-2.1487-.5633-2.9117-.3084-.7889-.72-1.4568-1.3876-2.1228C21.2982 1.33 20.628.9208 19.8378.6165 19.074.321 18.2017.1197 16.9244.0645 15.6471.0093 15.236-.005 11.977.0014 8.718.0076 8.31.0215 7.0301.0839m.1402 21.6932c-1.17-.0509-1.8053-.2453-2.2287-.408-.5606-.216-.96-.4771-1.3819-.895-.422-.4178-.6811-.8186-.9-1.378-.1644-.4234-.3624-1.058-.4171-2.228-.0595-1.2645-.072-1.6442-.079-4.848-.007-3.2037.0053-3.583.0607-4.848.05-1.169.2456-1.805.408-2.2282.216-.5613.4762-.96.895-1.3816.4188-.4217.8184-.6814 1.3783-.9003.423-.1651 1.0575-.3614 2.227-.4171 1.2655-.06 1.6447-.072 4.848-.079 3.2033-.007 3.5835.005 4.8495.0608 1.169.0508 1.8053.2445 2.228.408.5608.216.96.4754 1.3816.895.4217.4194.6816.8176.9005 1.3787.1653.4217.3617 1.056.4169 2.2263.0602 1.2655.0739 1.645.0796 4.848.0058 3.203-.0055 3.5834-.061 4.848-.051 1.17-.245 1.8055-.408 2.2294-.216.5604-.4763.96-.8954 1.3814-.419.4215-.8181.6811-1.3783.9-.4224.1649-1.0577.3617-2.2262.4174-1.2656.0595-1.6448.072-4.8493.079-3.2045.007-3.5825-.006-4.848-.0608M16.953 5.5864A1.44 1.44 0 1 0 18.39 4.144a1.44 1.44 0 0 0-1.437 1.4424M5.8385 12.012c.0067 3.4032 2.7706 6.1557 6.173 6.1493 3.4026-.0065 6.157-2.7701 6.1506-6.1733-.0065-3.4032-2.771-6.1565-6.174-6.1498-3.403.0067-6.156 2.771-6.1496 6.1738M8 12.0077a4 4 0 1 1 4.008 3.9921A3.9996 3.9996 0 0 1 8 12.0077', 'youtube': 'M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z', 'whatsapp': 'M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z'}
BRAND_SVG = {
    "facebook": f'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="#fff"/><path fill="#0866ff" d="{_SI["facebook"]}"/></svg>',
    "instagram": ('<svg viewBox="0 0 24 24" aria-hidden="true"><defs><radialGradient id="ig-g" cx="30%" cy="107%" r="150%">'
                  '<stop offset="0" stop-color="#fdf497"/><stop offset=".05" stop-color="#fdf497"/><stop offset=".45" stop-color="#fd5949"/>'
                  '<stop offset=".6" stop-color="#d6249f"/><stop offset=".9" stop-color="#285aeb"/></radialGradient></defs>'
                  f'<rect width="24" height="24" rx="6.5" fill="url(#ig-g)"/><path fill="#fff" transform="translate(4.2 4.2) scale(.65)" d="{_SI["instagram"]}"/></svg>'),
    "youtube": f'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="8" y="8" width="9" height="8" fill="#fff"/><path fill="#ff0000" d="{_SI["youtube"]}"/></svg>',
    "whatsapp": f'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="12" fill="#25d366"/><path fill="#fff" transform="translate(4.8 4.8) scale(.6)" d="{_SI["whatsapp"]}"/></svg>',
    "whatsapp-glyph": f'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="{_SI["whatsapp"]}"/></svg>',
}


def fmt_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[int(m) - 1]} {y}"


def news_card(r, n, i=0, big=False, h="h3"):
    """One news item: thumbnail that plays the video in place, date, title, summary."""
    return (f'<article class="news-card{" big" if big else ""} reveal" style="--i:{i % 3}">'
            f'<div class="film news-media"><button type="button" data-yt="{n["id"]}" aria-label="Play: {html.escape(n["title"])}">'
            f'<span class="play"><i class="ph-fill ph-play"></i></span></button>'
            f'<img src="{r}assets/img/news/{n["id"]}.jpg" alt="" loading="lazy"></div>'
            f'<div class="news-body"><time datetime="{n["date"]}">{fmt_date(n["date"])}</time>'
            f'<{h}>{html.escape(n["title"])}</{h}><p>{html.escape(n["summary"])}</p></div></article>')


def href(r, slug):
    return f"{r}{slug + '/' if slug else ''}index.html"


def nav_html(r, cur):
    out = []
    for label, target in NAV:
        if isinstance(target, str):
            ac = ' aria-current="page"' if cur == target else ""
            out.append(f'<li><a href="{href(r, target)}"{ac}>{label}</a></li>')
        else:
            active = any(cur == s for _, s in target)
            items = "".join(
                f'<li><a href="{href(r, s)}"{CUR if cur == s else ""}>{t}</a></li>' for t, s in target)
            style = ' style="color:var(--brand)"' if active else ""
            out.append(f'<li class="has-dd"><button type="button" aria-haspopup="true"{style}>{label}'
                       f'<i class="ph ph-caret-down caret" aria-hidden="true"></i></button><ul class="dropdown">{items}</ul></li>')
    return "".join(out)


def drawer_html(r):
    groups = []
    simple = []
    for label, target in NAV:
        if isinstance(target, str):
            simple.append(f'<li><a href="{href(r, target)}">{label}</a></li>')
        else:
            items = "".join(f'<li><a href="{href(r, s)}">{t}</a></li>' for t, s in target)
            groups.append(f'<p class="drawer-label">{label}</p><ul>{items}</ul>')
    return (f'<div class="drawer" aria-hidden="false"><div class="drawer-scrim"></div>'
            f'<nav class="drawer-panel" aria-label="Mobile">'
            f'<div class="drawer-head"><a class="brand" href="{href(r, "")}"><img class="brand-mark" src="{r}assets/img/logo-emblem.jpg" alt="KSR Akshara Academy logo"></a>'
            f'<button class="icon-btn" data-drawer-close aria-label="Close menu"><i class="ph ph-x"></i></button></div>'
            f'<ul><li><a href="{href(r, "")}">Home</a></li></ul>{"".join(groups)}<p class="drawer-label">More</p><ul>{"".join(simple)}</ul>'
            f'<a class="btn btn-primary" href="{href(r, "admission")}">Admissions enquiry</a></nav></div>')


def layout(r, cur, title, desc, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{r}assets/img/KSR-children.jpg">
<meta name="theme-color" content="#07406a">
<link rel="icon" href="{r}assets/img/favicon.ico?v={VER}" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="{r}assets/img/favicon-32.png?v={VER}">
<link rel="icon" type="image/png" sizes="16x16" href="{r}assets/img/favicon-16.png?v={VER}">
<link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png?v={VER}">
<script>try{{var t=localStorage.getItem("ksr-theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<link rel="preload" href="{r}assets/fonts/outfit-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{r}assets/fonts/figtree-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/css/vendor.css?v={VER}">
<link rel="stylesheet" href="{r}assets/css/site.css?v={VER}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"School","name":"KSR Akshara Academy","url":"https://ksrakshara.org","telephone":"{TEL_1}","email":"{EMAIL}","address":{{"@type":"PostalAddress","streetAddress":"KSR Kalvi Nagar","addressLocality":"Tiruchengode","addressRegion":"Tamil Nadu","postalCode":"637215","addressCountry":"IN"}}}}</script>
</head>
<body{' class="immersive"' if cur == "akshara-tree" else ""}>
<a class="skip" href="#main">Skip to content</a>
<div class="utility"><div class="wrap">
  <div class="u-left"><span><i class="ph ph-seal-check"></i>CBSE Affiliation No. 1930318</span><span>Accredited with NIOS</span></div>
  <div class="u-right"><a href="tel:{TEL_1}"><i class="ph ph-phone"></i>{PHONE_1}</a><a href="mailto:{EMAIL}"><i class="ph ph-envelope-simple"></i>{EMAIL}</a></div>
</div></div>
<header class="site-header"><div class="wrap nav">
  <a class="brand" href="{href(r, "")}">
    <img class="brand-mark" src="{r}assets/img/logo-emblem.jpg" alt="" width="50" height="50">
    <span class="brand-text"><strong>KSR Akshara Academy</strong><span>Tiruchengode, since 2010</span></span>
  </a>
  <ul class="nav-links">{nav_html(r, cur)}</ul>
  <div class="nav-cta">
    <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode"><i class="ph ph-moon"></i></button>
    <a class="btn btn-primary" href="{href(r, "admission")}">Admissions enquiry</a>
    <button class="icon-btn menu-toggle" data-drawer-open aria-label="Open menu"><i class="ph ph-list"></i></button>
  </div>
</div></header>
{drawer_html(r)}
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
  <div class="foot-grid">
    <div>
      <a class="brand" href="{href(r, "")}"><img class="brand-mark" src="{r}assets/img/logo-emblem.jpg" alt="" width="50" height="50"><span class="brand-text"><strong>KSR Akshara Academy</strong><span>Nurturing young minds</span></span></a>
      <address>KSR Kalvi Nagar, Tiruchengode 637 215<br>Namakkal District, Tamil Nadu</address>
      <div class="socials">
        <a class="social" href="https://www.facebook.com/ksrakshara" aria-label="Facebook">{BRAND_SVG["facebook"]}</a>
        <a class="social" href="https://www.instagram.com/ksrakshara2010/" aria-label="Instagram">{BRAND_SVG["instagram"]}</a>
        <a class="social" href="https://www.youtube.com/@ksrakshara" aria-label="YouTube">{BRAND_SVG["youtube"]}</a>
        <a class="social" href="https://wa.me/919894932323" aria-label="WhatsApp">{BRAND_SVG["whatsapp"]}</a>
      </div>
    </div>
    <div><h2 class="foot-title">School</h2><ul>
      <li><a href="{href(r, "about-us")}">Our story</a></li><li><a href="{href(r, "about-us/management")}">Management</a></li>
      <li><a href="{href(r, "about-us/why-akshara")}">Why Akshara?</a></li><li><a href="{href(r, "akshara-tree")}">The Akshara tree</a></li><li><a href="{href(r, "methodology")}">Academics</a></li>
      <li><a href="{href(r, "about-us/documents-information")}">Mandatory disclosure</a></li></ul></div>
    <div><h2 class="foot-title">Student life</h2><ul>
      <li><a href="{href(r, "life-akshara")}">Life at Akshara</a></li><li><a href="{href(r, "sports")}">Sports</a></li>
      <li><a href="{href(r, "facilities-hostel")}">Hostel</a></li><li><a href="{href(r, "facilities-transport")}">Transport</a></li>
      <li><a href="{href(r, "holiday-assignments")}">Holiday assignments</a></li><li><a href="{href(r, "events")}">News and events</a></li></ul></div>
    <div><h2 class="foot-title">Get in touch</h2><ul>
      <li><a href="tel:{TEL_1}">{PHONE_1}</a></li><li><a href="tel:{TEL_2}">{PHONE_2}</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{href(r, "admission")}">Admissions</a></li>
      <li><a href="{href(r, "join-us")}">Careers</a></li><li><a href="{href(r, "testimonial")}">Testimonials</a></li></ul></div>
  </div>
  <div class="foot-bottom"><span>&copy; 2026 KSR Akshara Academy. A KSR Educational and Charitable Trust institution.</span><span>CBSE Affiliation No. 1930318</span></div>
</div></footer>
<a class="fab" href="https://wa.me/919894932323" aria-label="Chat with the admissions office on WhatsApp">{BRAND_SVG["whatsapp-glyph"]}</a>
<script src="{r}assets/js/site.js?v={VER}" defer></script>
</body>
</html>
"""


def page_head(r, crumbs, h1, lede, banner=None, alt=""):
    c = f'<li><a href="{href(r, "")}">Home</a></li>' + "".join(
        f'<li><a href="{href(r, s)}">{t}</a></li>' if s else f'<li aria-current="page">{t}</li>' for t, s in crumbs)
    b = f'<figure class="page-banner reveal" style="margin-left:0;margin-right:0"><img src="{r}assets/img/{banner}" alt="{alt}"></figure>' if banner else ""
    return f"""<section class="page-head"><div class="wrap">
<nav aria-label="Breadcrumb"><ol class="crumbs">{c}</ol></nav>
<h1>{h1}</h1><p class="lede">{lede}</p>{b}</div></section>"""


def cta_band(r, h="Visit the campus before you decide.", p="Walk the classrooms, labs, library and turf with our admissions team. Admissions open every year from Vijayadasami to March."):
    return f"""<section class="section"><div class="wrap"><div class="cta-band reveal">
<div><h2>{h}</h2><p>{p}</p></div>
<div class="actions"><a class="btn btn-primary" href="{href(r, "admission")}">Admissions enquiry</a>
<a class="btn btn-ghost" href="tel:{TEL_1}"><i class="ph ph-phone"></i>Call {PHONE_1}</a></div>
</div></div></section>"""


def enquiry_form(title="Admissions enquiry", sub="Share a few details and our admissions office will call you back."):
    grades = "".join(f"<option>{g}</option>" for g in
                     ["Pre-KG", "Junior KG", "Senior KG"] + [f"Grade {n}" for n in
                     ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]])
    return f"""<form class="form-card" data-demo novalidate>
<h3>{title}</h3><p class="muted" style="margin-top:.4rem">{sub}</p>
<div class="form-grid">
  <div class="field"><label for="sn">Student name</label><input id="sn" name="student" required autocomplete="off" placeholder="Full name">
    <span class="err">Please enter the student's name.</span></div>
  <div class="form-row">
    <div class="field"><label for="gr">Grade applying for</label><select id="gr" name="grade" required><option value="">Select grade</option>{grades}</select>
      <span class="err">Please choose a grade.</span></div>
    <div class="field"><label for="ph">Parent phone</label><input id="ph" name="phone" type="tel" required inputmode="numeric" placeholder="10-digit mobile">
      <span class="err">Enter a valid 10-digit mobile number.</span></div>
  </div>
  <div class="field"><label for="bd">Boarding preference</label><select id="bd" name="boarding"><option>Day scholar</option><option>Weekly boarding (Mon to Fri)</option><option>Full-time boarding</option></select>
    <span class="help">You can change this later.</span></div>
  <button class="btn btn-primary" type="submit"><i class="ph ph-paper-plane-tilt"></i> Send enquiry</button>
  <p class="note">Demo form for the redesign concept. Not connected yet.</p>
</div>
<div class="form-success" role="status"><i class="ph ph-check-circle"></i><h3>Thank you. Enquiry received.</h3>
<p>Our admissions office will call you within one working day.</p></div>
</form>"""


# ---------------------------------------------------------------- HOME
def home(r):
    img = lambda n: f"{r}assets/img/{n}"
    stages = [
        ("foundation", "Foundation", "Pre-KG to Grade II", "KSR-children-2.jpg",
         "Play-based learning across eight domains of development",
         "A holistic, discovery-based early years programme following NEP ECCE guidance. Children build cognitive, social, emotional, creative and physical skills in a classroom rich in sensory experiences."),
        ("preparatory", "Preparatory", "Grades III to V", "career-banner.jpg",
         "Structured learning with room to explore",
         "An interdisciplinary, technology-rich curriculum with active learning. Skill development is planned into every term so learners grasp concepts and grow into confident individuals."),
        ("middle", "Middle", "Grades VI to VIII", "ATL-school.jpg",
         "Projects that connect to the real world",
         "Project-based, hands-on learning, group discussions, seminars, quizzes and e-research. Students start in the Atal Tinkering Lab and the integrated IIT and NEET foundation from Grade VI."),
        ("secondary", "Secondary", "Grades IX to XII", "KSR-higher.jpg",
         "Ready for India's best colleges, and abroad",
         "A multidisciplinary system with a choice of subject combinations, skill enhancement and career guidance. The integrated NEET and JEE programme includes classroom instruction, interactive sessions and mock tests."),
    ]
    tabs = "".join(
        f'<button class="stage-tab" role="tab" id="tab-{k}" aria-controls="panel-{k}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">'
        f'<strong>{n}</strong><span>{g}</span><i class="ph ph-arrow-right"></i></button>'
        for i, (k, n, g, *_rest) in enumerate(stages))
    panels = "".join(
        f'<div class="stage-panel" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}"{"" if i == 0 else " hidden"}>'
        f'<img src="{img(im)}" alt="{n} stage students at Akshara" loading="lazy"><div class="stack"><h3>{h}</h3><p class="muted">{p}</p>'
        f'<a class="link-arrow" href="{href(r, "methodology")}#{k}">How the {n.lower()} stage works <i class="ph ph-arrow-right"></i></a></div></div>'
        for i, (k, n, g, im, h, p) in enumerate(stages))

    why = [
        ("Learning", [
            ("ph-flask", "Researched curriculum", "Scientifically researched and planned, aligned to CBSE and NEP."),
            ("ph-lightbulb", "Four ways to learn", "Active, skill-based, experiential and blended learning."),
            ("ph-chalkboard-teacher", "Well-trained educators", "Periodic training keeps teaching methods current."),
            ("ph-medal", "Scholastic and co-scholastic", "Equal weight on academics, values and activities."),
        ]),
        ("Safety", [
            ("ph-security-camera", "24 x 7 CCTV", "Every corner of the campus is monitored round the clock."),
            ("ph-bus", "GPS-tracked buses", "Caretakers on board and live tracking on every route."),
        ]),
        ("Living", [
            ("ph-bed", "Weekly and regular boarding", "Five-day boarding or full-time, with house parents."),
            ("ph-soccer-ball", "Sports and performing arts", "A floodlit turf, skating rink, dance, drama and music."),
        ]),
    ]
    quotes = [
        ("lead", "I very much hope to see many chemists coming from this school.", "professor.jpg", "Prof. Dr. Robert Huber", "Nobel Laureate in Chemistry, 1988", None),
        ("", "My son Nithin Rohit completed Grade XII here and went on to study Electrical Engineering at IIT Jodhpur. The JEE programme was truly amazing.", "Kumar-120x120.jpg", "K. Kumar", "Parent of Nithin Rohit", "IIT Jodhpur"),
        ("", "The NEET coaching gave my twins the knowledge and the confidence to pursue medicine. Both are now in medical college.", "Vanitha-srinivasan.jpg", "Vanitha Srinivasan", "Parent of Kanimozhi and Kayalvizhi", "Madras and Vellore Medical Colleges"),
        ("", "Amazing children. Amazing infrastructure. Looking forward to more laurels from the school.", "jaikumar.jpg", "Jaikumar Christhu Rajan", "Director, St. Joseph's College of Engineering, Chennai", None),
        ("", "Skill competency and house competitions have visibly increased my daughter's confidence and her ability to face challenges.", "Chitra-120x120.jpg", "S. Chitra", "Mother of A.S. Anmithashree", None),
        ("", "I am deeply impressed. I do wish you success. Take your chance.", "Hartmut-Michel.jpg", "Prof. Hartmut Michel", "Nobel Laureate in Chemistry, 1988", None),
    ]
    q_html = "".join(
        f'<figure class="quote {c}">' + (f'<span class="result"><i class="ph ph-graduation-cap"></i>{res}</span>' if res else "")
        + f'<blockquote>&ldquo;{q}&rdquo;</blockquote><figcaption><img src="{img(p)}" alt="" loading="lazy"><div><strong>{n}</strong><span>{role}</span></div></figcaption></figure>'
        for c, q, p, n, role, res in quotes)

    sports = [("sgfleet.jpg", "Athletics"), ("Skatings_sports.jpg", "Skating"), ("basketball.jpg", "Basketball"),
              ("cricket.jpg", "Cricket"), ("vollyball.jpg", "Volleyball"), ("handball.jpg", "Handball"),
              ("ches.jpg", "Chess")]
    s_items = "".join(f'<figure class="sport"><img src="{img(i)}" alt="{t} at Akshara" loading="lazy"><figcaption>{t}</figcaption></figure>' for i, t in sports)
    s_dupe = "".join(f'<figure class="sport" aria-hidden="true"><img src="{img(i)}" alt="" loading="lazy"><figcaption>{t}</figcaption></figure>' for i, t in sports)

    ages = [("Pre-KG", "2 years 5 months by June"), ("Junior KG", "3 years 2 months"), ("Senior KG", "4 years 2 months"), ("Grade I", "5 years 2 months")]
    ages_html = "".join(f'<div class="age"><strong>{a}</strong><span>{b}</span></div>' for a, b in ages)

    tree = tree_parts(r)
    lead, *rest = NEWS[:3]
    latest = news_card(r, lead, 0, h="h3") + "".join(
        news_card(r, n, i + 1).replace('class="news-card reveal"', 'class="news-card compact reveal"') for i, n in enumerate(rest))
    why_tiles = "".join(
        f'<div class="tile why-tile w-{g.lower()} reveal" style="--i:{i}"><h3 class="why-label">{g}</h3><div class="why-items">' + "".join(
            f'<div class="why-item"><i class="ph {ic}"></i><div><strong>{t}</strong><p>{d}</p></div></div>' for ic, t, d in items)
        + "</div></div>" for i, (g, items) in enumerate(why))
    return f"""
<section class="hero"><div class="wrap hero-bento">
  <div class="panel intro">
    <a class="announce" href="{href(r, "admission")}"><span>Admissions 2027-28</span>Open from Vijayadasami for all classes <i class="ph ph-arrow-right"></i></a>
    <h1>Nurturing young minds and hearts of <em>tomorrow's leaders.</em></h1>
    <p class="lede">From Pre-KG to Grade XII, Aksharites learn through inquiry, sport, the arts and strong values.</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" href="{href(r, "admission")}">Admissions enquiry <i class="ph ph-arrow-right"></i></a>
      <a class="btn btn-ghost" href="{href(r, "contact-us")}#visit"><i class="ph ph-map-pin"></i>Book a campus visit</a>
    </div>
  </div>
  <div class="panel tree-panel hero-tree" data-tree="mini" data-link="{href(r, "akshara-tree")}" data-sway-x="{tree["sx"]}" data-sway-y="720">
    <div class="tree-stage" style="aspect-ratio:{tree["ratio"]}">{tree["svg"]}<div class="tree-tip" aria-hidden="true"></div></div>
    <a class="link-arrow hero-tree-link" href="{href(r, "akshara-tree")}">Every leaf of our emblem tells a story <i class="ph ph-arrow-right"></i></a>
  </div>
  <ul class="facts" aria-label="Akshara at a glance">
    <li class="fact reveal"><strong>1984</strong><span>KSR Educational and Charitable Trust founded</span></li>
    <li class="fact reveal" style="--i:1"><strong>16</strong><span>KSR institutions, from Pre-KG to Ph.D.</span></li>
    <li class="fact fact-deep reveal" style="--i:2"><strong>4,500+</strong><span>students across the three KSR schools</span></li>
    <li class="fact reveal" style="--i:3"><strong>3x</strong><span>British Council International School Award</span></li>
    <li class="fact reveal" style="--i:4"><strong>25 km</strong><span>GPS-tracked bus network around Tiruchengode</span></li>
  </ul>
</div></section>
{tree["data"]}

<section class="section latest"><div class="wrap">
  <div class="voices-head reveal"><h2>Latest from Akshara</h2>
    <a class="link-arrow" href="{href(r, "events")}">All news and events <i class="ph ph-arrow-right"></i></a></div>
  <div class="news-bento">{latest}</div>
</div></section>

<section class="section section-tint" id="academics"><div class="wrap">
  <div class="stack reveal" style="max-width:62ch"><h2>One curriculum, four stages, shaped by the NEP.</h2>
  <p class="lede">Akshara follows CBSE expectations and builds skills for an international context. Every stage has its own way of teaching.</p></div>
  <div class="stages" data-tabs>
    <div class="stage-tabs" role="tablist" aria-label="Stages of learning">{tabs}</div>
    <div>{panels}</div>
  </div>
</div></section>

<section class="section bare"><div class="wrap">
  <div class="bento">
    <div class="tile head t-head reveal"><h2>More than a classroom, every single day.</h2>
      <a class="link-arrow" href="{href(r, "life-akshara")}">Life at Akshara <i class="ph ph-arrow-right"></i></a></div>
    <a class="tile photo t-isa reveal" href="{href(r, "life-akshara")}#isa"><img src="{img("Fieldstrip.jpg")}" alt="Akshara students on a field trip" loading="lazy">
      <h3>International School Award, three times in a row</h3><p>The British Council honours schools that bring the world into the classroom. Akshara has earned it for 2022 to 2025.</p></a>
    <a class="tile photo t-atl reveal" style="--i:1" href="{href(r, "life-akshara")}#atl"><img src="{img("Robotics.jpg")}" alt="Robotics kit being assembled" loading="lazy"><h3>Atal Tinkering Lab</h3><p>Grades VI to XII</p></a>
    <a class="tile photo t-ted reveal" style="--i:2" href="{href(r, "life-akshara")}#ted"><img src="{img("ted.jpg")}" alt="A student giving a TED-Ed talk" loading="lazy"><h3>TED-Ed Club</h3><p>Student talks, global sessions</p></a>
    <a class="tile photo t-ncc reveal" href="{href(r, "life-akshara")}#ncc"><img src="{img("ncc.jpg")}" alt="NCC cadets marching in formation" loading="lazy"><h3>NCC, Scouts and Guides</h3><p>Drill, first aid, map reading and camp training</p></a>
    <a class="tile brand t-robo reveal" style="--i:1" href="{href(r, "life-akshara")}#steam"><i class="ph ph-cpu big-icon"></i><h3>STEAM and Robotics</h3><p>From Kindergarten to Grade 8</p></a>
    <a class="tile accent t-mun reveal" style="--i:2" href="{href(r, "life-akshara")}#mun"><i class="ph ph-globe big-icon"></i><h3>Model UN with IIMUN</h3><p>Students debate as diplomats</p></a>
    <div class="tile tint t-clubs reveal" style="--i:1"><div class="chips">
      <span class="chip"><i class="ph ph-palette"></i>Art</span><span class="chip"><i class="ph ph-cooking-pot"></i>Cookery</span>
      <span class="chip"><i class="ph ph-camera"></i>Photography</span><span class="chip"><i class="ph ph-leaf"></i>Nature</span>
      <span class="chip"><i class="ph ph-question"></i>Quiz</span><span class="chip"><i class="ph ph-book-open"></i>Reading</span>
      <span class="chip"><i class="ph ph-globe-hemisphere-east"></i>MUN</span><span class="chip"><i class="ph ph-microphone-stage"></i>TED-Ed</span>
      <span class="chip"><i class="ph ph-function"></i>Math</span></div>
      <div><h3>Nine clubs to choose from</h3><p class="muted">Every student joins at least one.</p></div></div>
  </div>
</div></section>

<section class="section bare"><div class="wrap">
  <div class="film reveal">
    <button type="button" data-yt="{YT_ID}" aria-label="Play the campus film"><span class="play"><i class="ph-fill ph-play"></i></span>
      <span><strong>See a day at Akshara</strong><small>Classrooms, labs, stage and turf in a few minutes.</small></span></button>
    <img src="{img("why-akshara.jpg")}" alt="" loading="lazy">
  </div>
</div></section>

<section class="section bare"><div class="wrap why-bento">
  <div class="tile head why-head reveal"><div class="stack"><h2>Eight reasons parents choose Akshara.</h2>
    <p class="lede">Quality and international standards of education, in an Indian context.</p></div>
    <img src="{img("KSR-children.jpg")}" alt="Four smiling Akshara students in uniform" loading="lazy"></div>
  {why_tiles}
</div></section>

<section class="section"><div class="wrap" data-carousel>
  <div class="voices-head reveal"><h2 style="max-width:18ch">What visitors and parents say.</h2>
    <div class="carousel-btns"><button class="icon-btn" data-dir="-1" aria-label="Previous"><i class="ph ph-arrow-left"></i></button>
    <button class="icon-btn" data-dir="1" aria-label="Next"><i class="ph ph-arrow-right"></i></button></div></div>
  <div class="carousel reveal" tabindex="0" aria-label="Testimonials">{q_html}</div>
  <a class="link-arrow" href="{href(r, "testimonial")}">Read all testimonials <i class="ph ph-arrow-right"></i></a>
</div></section>

<section class="section section-deep"><div class="wrap">
  <div class="stack reveal" style="max-width:60ch"><h2>A floodlit football turf, and a sport for every child.</h2>
  <p class="lede">After-school coaching in cricket, athletics, volleyball, football, basketball and more, planned around study time.</p>
  <a class="link-arrow" href="{href(r, "sports")}">Explore sports <i class="ph ph-arrow-right"></i></a></div>
  <div class="marquee"><div class="marquee-track">{s_items}{s_dupe}</div></div>
</div></section>

<section class="section bare" id="admissions"><div class="wrap admit">
  <div class="tile admit-info reveal">
    <span class="eyebrow">Admissions 2027-28</span>
    <h2 style="margin-top:.9rem">Admissions open from Vijayadasami to March.</h2>
    <p class="lede" style="margin-top:1rem">Seats are offered first come, first served. Late applications in April depend on availability.</p>
    <div class="ages">{ages_html}</div>
    <ol class="steps">
      <li><div><strong>Enquire</strong><p>By phone or in person. Meet the Principal or Vice Principals.</p></div></li>
      <li><div><strong>Collect the application</strong><p>Available at the school office on payment.</p></div></li>
      <li><div><strong>Entrance assessment</strong><p>From Senior KG onwards. Submit the form on the day.</p></div></li>
    </ol>
  </div>
  <div class="tile admit-form reveal" style="--i:1">{enquiry_form()}</div>
</div></section>
"""


# ---------------------------------------------------------------- ABOUT
def about(r):
    return page_head(r, [("About", None)], "A vibrant learning community in Tiruchengode.",
                     "KSR Akshara Academy is a CBSE-affiliated school committed to holistic education: academic excellence, personal growth and character.",
                     "ksr-contact-banner.jpg", "The KSR Akshara Academy school building") + f"""
<section class="section"><div class="wrap split top">
  <p class="pull reveal">We welcome students of all backgrounds and abilities, and help them <span>achieve their dreams.</span></p>
  <div class="prose reveal">
    <p>Akshara emphasises the development of 21st century skills. These skills matter in today's fast-paced, technology-driven world, and by developing them Akshara prepares Aksharites for a wide range of future opportunities.</p>
    <p>Our educators are the building blocks of the school. They are approachable, vibrant and curious, and they take part in periodic training programmes to keep pace with changing teaching and learning methods.</p>
    <p>Alongside a strong academic programme, Akshara promotes kindness, respect and responsibility, so that students grow into responsible and compassionate members of society.</p>
    <p>By focusing on the whole person, Akshara helps shape the next generation of leaders, innovators and problem-solvers.</p>
  </div>
</div></section>
<section class="section section-tint"><div class="wrap">
  <div class="split top">
    <div class="stack reveal"><h2>Vision</h2><p class="lede">To nurture and excel in all fields, fostering our children as lifelong learners with values and leadership qualities, contributing to the global society.</p></div>
    <div class="stack reveal"><h2>Mission</h2><p class="lede">Nurturing young minds and hearts of tomorrow's leaders.</p></div>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <h2 class="reveal">Explore Akshara</h2>
  <div class="grid-auto" style="margin-top:2rem">
    <a class="card doc-link reveal" href="{href(r, "about-us/management")}"><i class="ph ph-users-three"></i><span>Management and leadership</span><i class="ph ph-arrow-right"></i></a>
    <a class="card doc-link reveal" style="--i:1" href="{href(r, "about-us/why-akshara")}"><i class="ph ph-star"></i><span>Why Akshara?</span><i class="ph ph-arrow-right"></i></a>
    <a class="card doc-link reveal" style="--i:2" href="{href(r, "methodology")}"><i class="ph ph-books"></i><span>Curriculum and methodology</span><i class="ph ph-arrow-right"></i></a>
    <a class="card doc-link reveal" style="--i:3" href="{href(r, "about-us/documents-information")}"><i class="ph ph-file-text"></i><span>Documents and mandatory disclosure</span><i class="ph ph-arrow-right"></i></a>
  </div>
</div></section>""" + cta_band(r)


def management(r):
    img = lambda n: f"{r}assets/img/{n}"
    return page_head(r, [("About", "about-us"), ("Management", None)], "The people behind Akshara.",
                     "Founded under the KSR Educational and Charitable Trust, established in 1984.") + f"""
<section class="section"><div class="wrap">
  <article class="leader reveal"><img src="{img("founder.jpg")}" alt="Lion Thiruvalar Dr. K.S. Rangasamy" style="object-position:40% 30%">
    <div><span class="role">Founder Chairman</span><h2>Lion Thievathiru Dr. K.S. Rangasamy MJF</h2>
    <div class="prose"><p>Known as KSR, he was a prominent educationist, philanthropist and visionary leader who made it his life's mission to make quality education accessible to children and young adults across the country and abroad.</p>
    <p>He placed Tiruchengode on the global map through innovative ventures in education. Under his leadership, 16 institutions now provide education from Pre-KG to Ph.D. KSR Akshara Academy is the 15th.</p></div>
    <div class="stat-row" style="margin-top:1.75rem"><div><strong>1984</strong><span>Trust founded</span></div><div><strong>16</strong><span>Institutions</span></div><div><strong>4,500+</strong><span>Students in KSR schools</span></div></div></div></article>
  <article class="leader reveal"><img src="{img("Director_ksr.jpg")}" alt="Ms. Amutha Asaithambi, Director of KSR Schools">
    <div><span class="role">Director, KSR Schools</span><h2>Ms. Amutha Asaithambi</h2>
    <div class="prose"><p>A highly respected education leader in Tamil Nadu, she leads the three KSR schools in Tiruchengode: KSR Akshara Academy (CBSE), K.S.R. Matriculation Hr. Sec. School and Avvai KSR Matriculation School.</p>
    <p>Under her leadership Akshara has become one of the top CBSE schools in Tiruchengode, introducing cutting-edge technology and a focus on experiential learning.</p>
    <p>She is committed to equity and accessibility in education, so that every student, regardless of background or ability, can reach their full potential.</p></div></div></article>
  <article class="leader reveal"><img src="{img("PRINCIPAL-MAM-PHOTO.jpg")}" alt="Ms. Vijayalakshmi R., Principal" style="object-position:30% 50%">
    <div><span class="role">Principal</span><h2>Ms. Vijayalakshmi R.</h2>
    <div class="prose"><p>A highly qualified educationist with a Master's degree in Education and extensive experience in teaching and administration.</p>
    <p>Under her leadership Akshara has introduced innovative teaching methods and a wide range of educational programmes, ensuring students receive a holistic education. She is a role model for students and highly respected by Akshara's educators.</p></div></div></article>
</div></section>""" + cta_band(r)


def why_akshara(r):
    items = [("ph-flask", "Scientifically researched and planned curriculum"),
             ("ph-lightbulb", "Active, skill-based, experiential and blended learning"),
             ("ph-security-camera", "Unmatched safety with 24 x 7 CCTV security"),
             ("ph-chalkboard-teacher", "Highly well-trained educators"),
             ("ph-navigation-arrow", "GPS tracking on every school vehicle"),
             ("ph-bed", "Weekly and regular boarding"),
             ("ph-music-notes", "Dynamic sports and performing arts"),
             ("ph-medal", "Importance to scholastic and co-scholastic growth")]
    cards = "".join(f'<div class="card reveal" style="--i:{i % 4}"><i class="ph {ic}" style="font-size:1.8rem;color:var(--brand)"></i><h3 style="margin-top:1rem">{t}</h3></div>'
                    for i, (ic, t) in enumerate(items))
    return page_head(r, [("About", "about-us"), ("Why Akshara?", None)], "Why Akshara?",
                     "Akshara has mastered the art of imparting quality, international-standard education in the Indian context, in an atmosphere that lets every learner reach their full potential.",
                     "why-akshara.jpg", "Akshara students reading together on the lawn") + f"""
<section class="section"><div class="wrap">
  <h2 class="reveal">Akshara at a glance</h2>
  <div class="grid-auto" style="margin-top:2rem">{cards}</div>
</div></section>
<section class="section section-tint"><div class="wrap split">
  <img class="media reveal" src="{r}assets/img/transport-banner.jpg" alt="Senior students giving a thumbs up" loading="lazy">
  <div class="stack reveal"><h2>Vision and mission</h2>
  <p class="lede">To nurture and excel in all fields, fostering our children as lifelong learners with values and leadership qualities, contributing to the global society.</p>
  <p class="pull" style="font-size:1.4rem">Nurturing young minds and hearts of <span>tomorrow's leaders.</span></p></div>
</div></section>""" + cta_band(r)


def documents(r):
    docs = [("Affiliation, upgradation and extension of affiliation", "S-NO-1-AFFILIATION-COPY.pdf"),
            ("Society, trust or company registration and renewal", "S-NO-2-Trust-Deed.pdf"),
            ("No objection certificate (NOC) from the State Government", "S-NO-3-NOC-2011.pdf"),
            ("Recognition certificate under the RTE Act, 2009", "S-NO-4-Certificate-of-Recognition.pdf"),
            ("Building safety certificate (National Building Code)", "S-NO-5-Building-Safety.pdf"),
            ("Fire safety certificate", "S-NO-6-FIRE-SAFETY.pdf"),
            ("DEO certificate or self certification", "S-NO-7-DEO-CERTIFICATE.pdf"),
            ("Water, health and sanitation certificates", "S-NO-8-HEALTH-AND-SANITATION.pdf")]
    acad = [("Fee structure", "S-NO-9-FEE-STRUCTURE.pdf"), ("Annual academic calendar", "S-NO-10-ACADEMIC-CALENDAR.pdf"),
            ("School Management Committee (SMC)", "S-NO-11-SMC.pdf"), ("Board examination results, last three years", "S-NO-12-LAST-THREE-YEAR-RESULT.pdf")]
    link = lambda t, f, i: f'<a class="card doc-link reveal" style="--i:{i % 3}" href="{UP}/2022/03/{f}" target="_blank" rel="noopener"><i class="ph ph-file-pdf"></i><span>{t}</span><i class="ph ph-arrow-up-right"></i></a>'
    return page_head(r, [("About", "about-us"), ("Documents & disclosure", None)], "Documents and mandatory disclosure.",
                     "Everything CBSE requires us to publish, in one place. Each document opens as a PDF.") + f"""
<section class="section"><div class="wrap stack-lg">
  <a class="btn btn-brand reveal" href="{UP}/2023/06/Mandatory-Public-Disclosure.pdf" target="_blank" rel="noopener"><i class="ph ph-download-simple"></i>Mandatory public disclosure (PDF)</a>
  <h2 class="reveal" style="padding-top:1.5rem">Certificates and approvals</h2>
  <div class="grid-auto">{"".join(link(t, f, i) for i, (t, f) in enumerate(docs))}</div>
  <h2 class="reveal" style="padding-top:2rem">Results and academics</h2>
  <div class="grid-auto">{"".join(link(t, f, i) for i, (t, f) in enumerate(acad))}</div>
</div></section>"""


# ---------------------------------------------------------------- ACADEMICS
def methodology(r):
    img = lambda n: f"{r}assets/img/{n}"
    domains = ["Sensory", "Fine motor", "Language", "Social skills", "Emotional", "Self help", "Cognition", "Physical and gross motor"]
    return page_head(r, [("Academics", None)], "Curriculum and methodology.",
                     "The curriculum complies with CBSE expectations and builds skills for an international context. As per the New Education Policy, Akshara's classes are grouped into four stages.") + f"""
<section class="section"><div class="wrap">
  <nav class="toc" aria-label="Stages"><a href="#foundation">Foundation</a><a href="#preparatory">Preparatory</a><a href="#middle">Middle</a><a href="#secondary">Secondary</a></nav>
  <article class="program" id="foundation"><figure class="reveal"><img src="{img("KSR-children-2.jpg")}" alt="Young learners building with blocks" loading="lazy"></figure>
    <div class="stack reveal"><span class="muted">Pre-KG to Grade II</span><h2>Foundation stage</h2>
    <p class="muted">A holistic, play-based, discovery-based programme that develops every aspect of the child: cognitive, social, emotional, creative and physical. Following NEP ECCE guidance, it prepares children for reading, writing, arithmetic and EVS in a classroom rich in sensory experiences.</p>
    <p style="font-weight:600;margin-top:1.25rem">The Multi-Domain system focuses on eight domains of development:</p>
    <div class="chips">{"".join(f'<span class="chip">{d}</span>' for d in domains)}</div></div></article>
  <article class="program" id="preparatory"><figure class="reveal"><img src="{img("career-banner.jpg")}" alt="A teacher guiding young students at their desks" loading="lazy"></figure>
    <div class="stack reveal"><span class="muted">Grades III to V</span><h2>Preparatory stage</h2>
    <p class="muted">Structured learning experiences support scholastic, interpersonal, cultural and social development. The interdisciplinary, technology-rich curriculum gives students the tools to apply what they learn, and planned skill-building activities help every learner grasp each concept.</p></div></article>
  <article class="program" id="middle"><figure class="reveal"><img src="{img("ATL-school.jpg")}" alt="Students working with a robot in the tinkering lab" loading="lazy"></figure>
    <div class="stack reveal"><span class="muted">Grades VI to VIII</span><h2>Middle stage</h2>
    <p class="muted">An engaging, challenging environment that builds confidence, global understanding and civic responsibility. Teaching is project-based and hands-on, connected to real-world situations.</p>
    <ul class="checklist"><li><i class="ph ph-check-circle"></i>Group discussions, seminars and quizzes</li><li><i class="ph ph-check-circle"></i>E-research and presentations</li><li><i class="ph ph-check-circle"></i>Integrated IIT and NEET foundation begins</li></ul></div></article>
  <article class="program" id="secondary"><figure class="reveal"><img src="{img("KSR-higher.jpg")}" alt="Senior students conducting a chemistry experiment" loading="lazy"></figure>
    <div class="stack reveal"><span class="muted">Grades IX to XII</span><h2>Secondary stage</h2>
    <p class="muted">Preparing students for the most selective colleges and universities in India and abroad. A multidisciplinary system offers a range of subject combinations, with a skill enhancement programme and career guidance to help learners make confident choices.</p>
    <a class="link-arrow" href="{href(r, "life-akshara")}#iit">About the IIT and NEET programme <i class="ph ph-arrow-right"></i></a></div></article>
</div></section>""" + cta_band(r)


# ---------------------------------------------------------------- LIFE
def life(r):
    img = lambda n: f"{r}assets/img/{n}"
    progs = [
        ("isa", "ISA-AWARD-Image.jpg", "International School Award, British Council",
         "Akshara consciously raises teaching and learning to an international standard. The British Council's International School Award recognises schools that go the extra mile, and Akshara has now received it for the third consecutive time (2022 to 2025). Students worked on projects with partner schools abroad and exchanged ideas on a wide range of topics.", None),
        ("houses", "House-system.jpg", "House system",
         "The house system builds good work ethics: attitude, behaviour, communication and how we work with others. Regular inter-house competitions create leadership opportunities and grow creativity, critical thinking, collaboration, communication and compassion.", "houses"),
        ("clubs", "Cooks-act.jpg", "Clubs and activities",
         "Every student is encouraged to join at least one club: Art, Cookery, Photography, Nature, Quiz, Reading, MUN, TED-Ed and Math.", None),
        ("atl", "ATL-school.jpg", "Atal Tinkering Lab (ATL)",
         "A space for students in Grades VI to XII to explore through innovation, tinkering and collaboration. The lab builds design mindset, computational thinking, adaptive learning and physical computing.", None),
        ("ted", "ted.jpg", "TED-Ed Club",
         "Akshara is part of TED's youth and education initiative. Students discover, research and present their big ideas as short TED-style talks, and join global collaborative sessions with schools in other countries.", None),
        ("steam", "Robotics.jpg", "STEAM and Robotics",
         "Science, Technology, Engineering, Arts and Mathematics are taught through activities from Kindergarten to Grade 8, designed for each grade. Robotics brings every STEAM subject together and prepares Aksharites for the future.", None),
        ("iit", "KSR-higher.jpg", "IIT and NEET integrated programme",
         "From Grade VI to XII, an integrated programme prepares students for medical and engineering entrance exams. It combines classroom instruction, interactive sessions and mock tests with personalised coaching, for students aiming at the IITs, NITs and medical colleges.", None),
        ("mun", "admission-image.jpg", "Model United Nations",
         "A comprehensive MUN programme in collaboration with IIMUN. Students act as diplomats, debate international affairs and build public speaking, negotiation and problem-solving skills, guided by experts.", None),
        ("trips", "Fieldstrip.jpg", "Field trips",
         "National and international trips take Aksharites out of the classroom to see new sights, try new things and learn valuable life lessons.", None),
        ("ncc", "ncc.jpg", "NCC, Scouts and Guides",
         "The National Cadet Corps builds discipline and patriotism through drill, shooting, fitness, first aid, map reading, sailing and camp training. Scouts and Guides develop teamwork, communication and decision-making.", None),
        ("arts", "Arts.jpg", "Visual and performing arts",
         "Drama, dance, music and visual arts are woven into the curriculum as per the NEP. Every year the Fine Arts Department stages multidisciplinary performances, with students leading choreography and set design.", None),
    ]
    houses = ('<div class="houses"><div class="house" style="background:#c62f45">Anthuriums</div><div class="house" style="background:#2f62c6">Bluebells</div>'
              '<div class="house" style="background:#b98a00">Daffodils</div><div class="house" style="background:#7d3fb0">Tulips</div></div>')
    toc = "".join(f'<a href="#{k}">{t.split(",")[0].split(" (")[0]}</a>' for k, _, t, *_ in progs)
    rows = "".join(
        f'<article class="program" id="{k}"><figure class="reveal"><img src="{img(im)}" alt="{t}" loading="lazy"'
        f'{CONTAIN if k == "isa" else ""}></figure>'
        f'<div class="stack reveal"><h2>{t}</h2><p class="muted">{p}</p>{houses if extra == "houses" else ""}</div></article>'
        for k, im, t, p, extra in progs)
    return page_head(r, [("Life at Akshara", None)], "Life at Akshara.",
                     "Spacious classrooms, laboratories, a library, playground, swimming pool, gym and indoor stadium, and a programme that uses all of them.") + f"""
<section class="section"><div class="wrap"><nav class="toc" aria-label="Programmes">{toc}</nav>{rows}</div></section>""" + cta_band(r)


def sports(r):
    img = lambda n: f"{r}assets/img/{n}"
    grid = [("cricket.jpg", "Cricket"), ("ches.jpg", "Chess"), ("handball.jpg", "Handball"), ("basketball.jpg", "Basketball"),
            ("sgfleet.jpg", "Athletics"), ("Skatings_sports.jpg", "Skating"), ("vollyball.jpg", "Volleyball")]
    return page_head(r, [("Student life", None), ("Sports", None)], "Sports at Akshara.",
                     "An after-school programme that lets students explore and excel in sport, with a timetable that protects study time.",
                     "Skatings_sports.jpg", "Students skating on the Akshara rink") + f"""
<section class="section"><div class="wrap split top">
  <div class="stack reveal"><h2>World-class football turf.</h2>
    <p class="lede">An international-standard artificial turf built for drills, full matches and evening training under floodlights.</p>
    <ul class="checklist cols-2" style="margin-top:1.5rem">
      <li><i class="ph ph-check-circle"></i>Precise international dimensions</li><li><i class="ph ph-check-circle"></i>Durable, eco-friendly artificial grass</li>
      <li><i class="ph ph-check-circle"></i>Advanced drainage</li><li><i class="ph ph-check-circle"></i>Floodlights for evening sessions</li>
      <li><i class="ph ph-check-circle"></i>Perimeter fencing and goal netting</li><li><i class="ph ph-check-circle"></i>Changing rooms and showers</li>
      <li><i class="ph ph-check-circle"></i>Daily practice with expert coaches</li><li><i class="ph ph-check-circle"></i>Specialist goalkeeper and striker coaching</li></ul></div>
  <div class="grid-auto reveal" style="grid-template-columns:1fr">
    <div class="card"><h3>How a session runs</h3>
      <ol class="steps" style="margin-top:1rem">
        <li><div><strong>Warm-up and fitness</strong><p>15 minutes of stretching, jogging and basic exercises.</p></div></li>
        <li><div><strong>Skill development</strong><p>Drills and practice with personal attention from coaches.</p></div></li>
        <li><div><strong>Team play</strong><p>Teamwork, leadership and sportsmanship.</p></div></li>
        <li><div><strong>Cool-down and reflection</strong><p>Students review their game and set goals.</p></div></li>
      </ol></div></div>
</div></section>
<section class="section section-tint"><div class="wrap">
  <h2 class="reveal">Eight ways to play</h2>
  <div class="sport-grid" style="margin-top:2rem">{"".join(f'<figure class="reveal{" wide" if b == "Athletics" else ""}" style="--i:{i % 4}"><img src="{img(a)}" alt="{b}" loading="lazy"><figcaption>{b}</figcaption></figure>' for i, (a, b) in enumerate(grid))}</div>
  <p class="muted reveal" style="margin-top:2rem;max-width:60ch">Students compete in inter-school, district and state-level tournaments, plus friendly matches with neighbouring schools.</p>
</div></section>""" + cta_band(r)


def holiday(r):
    grades = [("Senior KG", "SKG"), ("Junior KG", "JKG")] + [(f"Grade {n}", f"Grade-{i}") for i, n in enumerate(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"], 1)]
    cards = "".join(f'<a class="card doc-link reveal" style="--i:{i % 3}" href="{UP}/2025/05/{f}-Holiday-Assignment.pdf" target="_blank" rel="noopener"><i class="ph ph-file-pdf"></i><span>{g}</span><i class="ph ph-download-simple"></i></a>'
                    for i, (g, f) in enumerate(grades))
    return page_head(r, [("Student life", None), ("Holiday assignments", None)], "Summer holiday assignments.",
                     "Download your child's assignment for the 2025 summer break.") + f"""
<section class="section"><div class="wrap"><div class="grid-auto">{cards}</div>
<p class="note" style="margin-top:1.5rem">In the new site, teachers upload these from the admin panel each term. No developer needed.</p></div></section>"""


# ---------------------------------------------------------------- CAMPUS
def hostel(r):
    img = lambda n: f"{r}assets/img/{n}"
    return page_head(r, [("Campus", None), ("Hostel", None)], "A hi-tech, home-away-from-home hostel.",
                     "Residential life at Akshara helps students grow independent in a safe, secure environment.",
                     "KSR-Hostels.jpg", "A bright twin room in the Akshara hostel") + f"""
<section class="section"><div class="wrap split">
  <div class="stack reveal"><h2>Two ways to board.</h2>
    <div class="grid-auto" style="grid-template-columns:1fr 1fr;margin-top:1.25rem">
      <div class="card"><i class="ph ph-calendar-check" style="font-size:1.8rem;color:var(--brand)"></i><h3 style="margin-top:.75rem">Five-day boarding</h3><p>Monday to Friday at school, weekends at home. The best of both worlds.</p></div>
      <div class="card"><i class="ph ph-house-line" style="font-size:1.8rem;color:var(--brand)"></i><h3 style="margin-top:.75rem">Full-time boarding</h3><p>A nurturing, home-away-from-home environment.</p></div>
    </div></div>
  <img class="media reveal" src="{img("Akshara-hostel.jpg")}" alt="Hostel dormitory with bunk beds" loading="lazy">
</div></section>
<section class="section section-tint"><div class="wrap">
  <h2 class="reveal">Cared for, every day.</h2>
  <ul class="checklist cols-2 reveal" style="margin-top:2rem;max-width:960px">
    <li><i class="ph ph-users"></i>Dedicated house parents tailor routines to each student</li>
    <li><i class="ph ph-gender-intersex"></i>Separate accommodation for boys and girls</li>
    <li><i class="ph ph-first-aid"></i>Medical needs handled by trained professionals</li>
    <li><i class="ph ph-student"></i>Trained mentors monitor academic progress</li>
    <li><i class="ph ph-bowl-food"></i>Nutritious breakfast, lunch, snack and dinner</li>
    <li><i class="ph ph-fork-knife"></i>Non-vegetarian menu three days a week</li>
    <li><i class="ph ph-security-camera"></i>Campus secured with 24 x 7 CCTV</li>
  </ul>
</div></section>""" + cta_band(r, "See the hostel in person.", "Book a visit and our team will walk you through the rooms, dining hall and study areas.")


def transport(r):
    img = lambda n: f"{r}assets/img/{n}"
    towns = ["Tiruchengode", "Erode", "Kumaramangalam", "Sankari", "Pallipalayam", "Veppadai"]
    return page_head(r, [("Campus", None), ("Transport", None)], "Getting your child to school safely.",
                     "Transporting your children safely is our utmost priority.") + f"""
<section class="section"><div class="wrap split">
  <img class="media reveal" src="{img("transport-right.jpg")}" alt="Senior students walking to the bus" loading="lazy">
  <div class="stack-lg reveal">
    <div class="stat-row"><div><strong>~1,400</strong><span>students served daily</span></div><div><strong>25 km</strong><span>route radius</span></div></div>
    <ul class="checklist">
      <li><i class="ph ph-navigation-arrow"></i>State-of-the-art GPS tracking on every vehicle</li>
      <li><i class="ph ph-hand-waving"></i>Caretakers on board for safe boarding and alighting</li>
      <li><i class="ph ph-wrench"></i>Regular maintenance and full compliance with state regulations</li></ul>
    <div><p style="font-weight:600;margin-bottom:.75rem">Routes cover</p><div class="chips">{"".join(f'<span class="chip"><i class="ph ph-map-pin"></i>{t}</span>' for t in towns)}</div></div>
  </div>
</div></section>""" + cta_band(r, "Check if we cover your area.", f"Call the transport desk on {PHONE_1} with your pickup point.")


# ---------------------------------------------------------------- ADMISSION
def admission(r):
    ages = [("Pre-KG", "2 years 5 months as of June"), ("Junior KG", "3 years 2 months"), ("Senior KG", "4 years 2 months"), ("Grade I", "5 years 2 months")]
    return page_head(r, [("Admissions", None)], "Admissions.",
                     "Admissions are open for all classes from Vijayadasami to March for the following academic year.",
                     "admission-image.jpg", "Senior students reviewing notes together") + f"""
<section class="section"><div class="wrap admit">
  <div class="stack-lg reveal">
    <h2>Eligibility by age</h2>
    <div class="ages" style="margin-top:0">{"".join(f'<div class="age"><strong>{a}</strong><span>{b}</span></div>' for a, b in ages)}</div>
    <h2 style="padding-top:1.5rem">How to apply</h2>
    <ol class="steps" style="margin-top:0">
      <li><div><strong>Enquire</strong><p>Call us or visit in person and fill in an enquiry form. You can meet the Principal or Vice Principals.</p></div></li>
      <li><div><strong>Collect the application form</strong><p>Available at the school office on payment.</p></div></li>
      <li><div><strong>Entrance examination</strong><p>For Senior KG onwards. Submit the completed form on the day of the exam.</p></div></li>
      <li><div><strong>Confirmation</strong><p>Seats are offered first come, first served. If you miss the window, April admissions depend on availability.</p></div></li>
    </ol>
  </div>
  <div class="reveal" style="position:sticky;top:100px">{enquiry_form()}</div>
</div></section>"""


# ---------------------------------------------------------------- TESTIMONIALS
def testimonials(r):
    img = lambda n: f"{r}assets/img/{n}"
    guests = [("Prof. Dr. Robert Huber", "Nobel Laureate in Chemistry, 1988", "professor.jpg", "I very much hope to see many chemists coming from this school."),
              ("Prof. Hartmut Michel", "Nobel Laureate in Chemistry, 1988", "Hartmut-Michel.jpg", "I am deeply impressed. I do wish you success. Take your chance."),
              ("C.K. Kumaravel", "CEO and co-founder, Naturals salon chain", "Kumaravel.jpg", "Your dreams, your signature. Make sure the entire world knows it. Together let us build a beautiful world."),
              ("Madhampatty Rangaraj", "Chairman, Madhampatty Thangavelu Hospitality", "Madhampatty-rangaraj.jpg", "I can feel a very energetic vibe overall with the students. Wonderful programme."),
              ("Jaikumar Christhu Rajan", "Director, St. Joseph's College of Engineering, Chennai", "jaikumar.jpg", "Amazing children. Amazing infrastructure. Looking forward to more laurels from the school."),
              ("Dr. Saranya Jaikumar", "Educational Psychologist, SCPCR", "saranya-jaikumar.jpg", "Had an amazing time speaking with higher secondary girls on safety and the prevention of abuse.")]
    parents = [("K. Kumar", "Parent of Nithin Rohit", "Kumar-120x120.jpg", "IIT Jodhpur", "The JEE training programme was truly amazing. My son completed Grade XII here and now studies Electrical Engineering at IIT Jodhpur."),
               ("Vanitha Srinivasan", "Parent of Kanimozhi and Kayalvizhi", "Vanitha-srinivasan.jpg", "Madras and Vellore Medical Colleges", "My twins moved from Matric to Akshara for Classes XI and XII. With excellent NEET coaching and follow-up, both got into medical college."),
              ("Dr. Sengottuvel and Dr. Sathyabama", "Parents of Mithira Prathiksa and Samrutha Sree", "dr.Sengottuvel-Sathyabama-120x120.jpg", None, "Value-education classes have encouraged logical and critical thinking. When she faces a practical problem, she applies what she learnt."),
              ("S. Chitra", "Mother of A.S. Anmithashree", "Chitra-120x120.jpg", None, "Skill competency activities and house competitions have visibly increased her confidence and her ability to face challenges."),
              ("Ishwarya Dhanasekaran", "Mother of Samantha, Grade 7", "Ishwaraya-120x120.jpg", None, "The teachers are dedicated, caring and truly invested. The individual attention has helped my child make great strides.")]
    q = lambda n, role, p, text, res=None: (f'<figure class="quote reveal">' + (f'<span class="result"><i class="ph ph-graduation-cap"></i>{res}</span>' if res else "")
        + f'<blockquote>&ldquo;{text}&rdquo;</blockquote><figcaption><img src="{img(p)}" alt="" loading="lazy"><div><strong>{n}</strong><span>{role}</span></div></figcaption></figure>')
    return page_head(r, [("Testimonials", None)], "In their words.",
                     "Nobel laureates, industry leaders and Akshara parents on what they have seen at the school.") + f"""
<section class="section"><div class="wrap">
  <h2 class="reveal">Parents</h2>
  <div class="grid-auto" style="margin-top:1.75rem;grid-template-columns:repeat(auto-fill,minmax(320px,1fr))">{"".join(q(n, ro, p, t, res) for n, ro, p, res, t in parents)}</div>
  <h2 class="reveal" style="margin-top:4rem">Guests</h2>
  <div class="grid-auto" style="margin-top:1.75rem;grid-template-columns:repeat(auto-fill,minmax(320px,1fr))">{"".join(q(n, ro, p, t) for n, ro, p, t in guests)}</div>
</div></section>""" + cta_band(r)


# ---------------------------------------------------------------- CAREERS
def careers(r):
    return page_head(r, [("Careers", None)], "Build your career at Akshara.",
                     "Are you passionate about teaching? Your skills can build the future of many young minds.",
                     "House-system.jpg", "Akshara staff and students at the house investiture") + f"""
<section class="section"><div class="wrap split top">
  <div class="stack-lg reveal"><h2>Lead in the classroom.</h2>
    <p class="lede">Akshara is looking for young, energetic, enthusiastic and dedicated teachers who are fluent in English and ready to lead.</p>
    <ul class="checklist"><li><i class="ph ph-chalkboard-teacher"></i>Periodic training in new teaching methods</li>
      <li><i class="ph ph-buildings"></i>Part of a group of 16 KSR institutions</li>
      <li><i class="ph ph-globe-hemisphere-east"></i>Global exposure through the British Council, TED-Ed and MUN</li></ul></div>
  <form class="form-card reveal" data-demo novalidate><h3>Apply to teach</h3>
    <div class="form-grid">
      <div class="form-row"><div class="field"><label for="cn">Name</label><input id="cn" required autocomplete="name"><span class="err">Please enter your name.</span></div>
      <div class="field"><label for="cp">Phone</label><input id="cp" type="tel" required inputmode="numeric" placeholder="10-digit mobile"><span class="err">Enter a valid 10-digit mobile number.</span></div></div>
      <div class="form-row"><div class="field"><label for="ce">Email</label><input id="ce" type="email" required autocomplete="email"><span class="err">Enter a valid email address.</span></div>
      <div class="field"><label for="cl">Location</label><input id="cl" required><span class="err">Please enter your location.</span></div></div>
      <div class="field"><label for="cs">Subject you teach</label><input id="cs" required placeholder="For example, Physics"><span class="err">Please tell us your subject.</span></div>
      <div class="field"><label for="cr">Resume</label><input id="cr" type="file" accept=".pdf,.doc,.docx" required><span class="help">PDF or Word, up to 5 MB.</span><span class="err">Please attach your resume.</span></div>
      <button class="btn btn-primary" type="submit"><i class="ph ph-paper-plane-tilt"></i> Send application</button>
      <p class="note">Demo form for the redesign concept. Not connected yet.</p></div>
    <div class="form-success" role="status"><i class="ph ph-check-circle"></i><h3>Application received.</h3><p>Our HR team will be in touch if there is a match.</p></div></form>
</div></section>"""


# ---------------------------------------------------------------- CONTACT
def contact(r):
    return page_head(r, [("Contact", None)], "We are here to help.",
                     "Call, write or visit. The admissions office is open on all working days.") + f"""
<section class="section" id="visit"><div class="wrap split top">
  <div class="contact-list reveal">
    <div class="contact-item"><i class="ph ph-map-pin"></i><div><strong>Visit us</strong><span class="muted">KSR Akshara Academy, KSR Kalvi Nagar,<br>Tiruchengode 637 215, Namakkal District, Tamil Nadu</span></div></div>
    <div class="contact-item"><i class="ph ph-phone"></i><div><strong>Call us</strong><a href="tel:{TEL_1}">{PHONE_1}</a> / <a href="tel:{TEL_2}">{PHONE_2}</a></div></div>
    <div class="contact-item"><i class="ph ph-envelope-simple"></i><div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="mailto:{EMAIL_2}">{EMAIL_2}</a></div></div>
    <div class="contact-item"><i class="ph ph-whatsapp-logo"></i><div><strong>WhatsApp</strong><a href="https://wa.me/919894932323">Chat with the admissions office</a></div></div>
  </div>
  <form class="form-card reveal" data-demo novalidate><h3>Book a campus visit</h3>
    <div class="form-grid">
      <div class="form-row"><div class="field"><label for="vn">Your name</label><input id="vn" required autocomplete="name"><span class="err">Please enter your name.</span></div>
      <div class="field"><label for="vp">Phone</label><input id="vp" type="tel" required inputmode="numeric" placeholder="10-digit mobile"><span class="err">Enter a valid 10-digit mobile number.</span></div></div>
      <div class="field"><label for="vd">Preferred date</label><input id="vd" type="date" required><span class="err">Please pick a date.</span></div>
      <div class="field"><label for="vm">Message</label><textarea id="vm" placeholder="Anything we should know before your visit?"></textarea></div>
      <button class="btn btn-primary" type="submit"><i class="ph ph-calendar-check"></i> Request visit</button>
      <p class="note">Demo form for the redesign concept. Not connected yet.</p></div>
    <div class="form-success" role="status"><i class="ph ph-check-circle"></i><h3>Visit requested.</h3><p>We will call to confirm a time.</p></div></form>
</div>
<div class="wrap"><div class="map reveal"><iframe src="{MAP}" loading="lazy" title="Map to KSR Akshara Academy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>"""


# ---------------------------------------------------------------- AKSHARA TREE (interactive emblem)
LEAVES = {
    "dancer": ("ph-person-simple-tai-chi", "Performing arts", "Dance and drama",
               "Dance, drama, music and the visual arts are woven into the curriculum. Each year students lead the choreography and set design for a multidisciplinary show.",
               "Arts.jpg", "Students performing a classical dance", "life-akshara#arts", "Visual and performing arts"),
    "pencil": ("ph-pencil-simple", "Pre-KG to Grade II", "The foundation years",
               "Young learners grow through play and discovery across eight domains of development, from sensory and fine motor skills to language and cognition.",
               "KSR-children-2.jpg", "Young children building with blocks", "methodology#foundation", "The foundation stage"),
    "molecules": ("ph-atom", "Grades VI to XII", "Science and the IIT and NEET track",
                  "An integrated programme builds strong concepts, problem-solving and mock-test practice for the IITs, NITs and medical colleges.",
                  "KSR-higher.jpg", "Senior students in the chemistry lab", "life-akshara#iit", "IIT and NEET programme"),
    "football": ("ph-soccer-ball", "After school", "Sport for every child",
                 "A floodlit, international-standard football turf, plus cricket, athletics, basketball, volleyball, handball, skating and chess.",
                 "sgfleet.jpg", "Students running on the athletics track", "sports", "Explore sports"),
    "lab": ("ph-flask", "Grades VI to XII", "Atal Tinkering Lab",
            "A lab built for curiosity, where students design, build and tinker, developing computational thinking and a design mindset.",
            "ATL-school.jpg", "Students building a robot in the tinkering lab", "life-akshara#atl", "About the ATL"),
    "compass": ("ph-compass-tool", "Kindergarten to Grade 8", "STEAM and robotics",
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
    icons = json.loads((ROOT / "assets/data/tree-icons.json").read_text())
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
                f'{tg.icon(icons[tg.GLYPH[k]], ix, iy, l["icon"])}</g></g></g>')

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
      <p class="tree-progress">0 of {len(chip_keys)} leaves explored</p>
      <button class="icon-btn wind-toggle" type="button" aria-pressed="true" aria-label="Pause the wind"><i class="ph ph-wind"></i></button>
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


def news_page(r):
    lead, rest = (NEWS[0], NEWS[1:]) if NEWS else (None, [])
    notices = [
        ("ph-megaphone-simple", "Admissions 2027-28", "Open from Vijayadasami for all classes. Entrance assessment from Senior KG onwards.", href(r, "admission"), "Admission details"),
        ("ph-file-text", "Mandatory public disclosure", "CBSE certificates, fee structure, academic calendar and board results.", href(r, "about-us/documents-information"), "View documents"),
        ("ph-book-open-text", "Holiday assignments", "Summer holiday assignments for SKG to Grade IX.", href(r, "holiday-assignments"), "Download"),
    ]
    notice_html = "".join(f'<a class="notice reveal" style="--i:{i}" href="{u}"><i class="ph {ic}"></i><div><strong>{t}</strong><p>{d}</p>'
                          f'<span class="link-arrow">{c} <i class="ph ph-arrow-right"></i></span></div></a>' for i, (ic, t, d, u, c) in enumerate(notices))
    return page_head(r, [("News and events", None)], "News and events.",
                     "Celebrations, trips, competitions and classroom moments from across Akshara.") + f"""
<section class="section"><div class="wrap news-layout">
  <div>
    {news_card(r, lead, 0, big=True, h="h2") if lead else ""}
    <div class="news-grid">{"".join(news_card(r, n, i, h="h2") for i, n in enumerate(rest))}</div>
  </div>
  <aside class="notices"><h2>Notices</h2>{notice_html}
    <p class="note">Stories on this page come from the school's YouTube channel, so every new video shows up here automatically.</p>
    <a class="btn btn-ghost" href="https://www.youtube.com/@ksrakshara" target="_blank" rel="noopener"><i class="ph ph-youtube-logo"></i>Our YouTube channel</a>
  </aside>
</div></section>""" + cta_band(r)


def webp(page):
    """Point every photo at its .webp copy (made by optimize_images.py), except og:image."""
    def swap(m):
        path = m.group(1)
        local = ROOT / re.sub(r"^(\.\./)+", "", path)
        return path + (".webp" if local.with_suffix(".webp").exists() else ".jpg")
    lines = page.split("\n")
    return "\n".join(l if 'property="og:image"' in l else re.sub(r"((?:\.\./)*assets/img/[\w./-]+?)\.jpg", swap, l) for l in lines)


PAGES = [
    ("", "KSR Akshara Academy | CBSE School in Tiruchengode", "CBSE-affiliated school in Tiruchengode, Tamil Nadu, from Pre-KG to Grade XII. Admissions open from Vijayadasami.", home),
    ("about-us", "About Us | KSR Akshara Academy", "KSR Akshara Academy is a CBSE school in Tiruchengode committed to holistic education.", about),
    ("about-us/management", "Management | KSR Akshara Academy", "Meet the founder, director and principal of KSR Akshara Academy.", management),
    ("about-us/why-akshara", "Why Akshara? | KSR Akshara Academy", "Eight reasons parents choose KSR Akshara Academy.", why_akshara),
    ("about-us/documents-information", "Documents & Mandatory Disclosure | KSR Akshara Academy", "CBSE mandatory public disclosure and certificates.", documents),
    ("methodology", "Curriculum & Methodology | KSR Akshara Academy", "Foundation, preparatory, middle and secondary stages as per NEP.", methodology),
    ("life-akshara", "Life at Akshara | KSR Akshara Academy", "International School Award, ATL, TED-Ed, STEAM, MUN, NCC and more.", life),
    ("sports", "Sports | KSR Akshara Academy", "Football turf, skating, cricket, basketball and more.", sports),
    ("holiday-assignments", "Holiday Assignments | KSR Akshara Academy", "Download summer holiday assignments by grade.", holiday),
    ("facilities-hostel", "Hostel | KSR Akshara Academy", "Five-day and full-time boarding for boys and girls.", hostel),
    ("facilities-transport", "Transport | KSR Akshara Academy", "GPS-tracked buses across a 25 km radius.", transport),
    ("admission", "Admissions | KSR Akshara Academy", "Eligibility, admission process and enquiry form.", admission),
    ("testimonial", "Testimonials | KSR Akshara Academy", "What parents and guests say about Akshara.", testimonials),
    ("events", "News and Events | KSR Akshara Academy", "Latest news, celebrations, trips and achievements from KSR Akshara Academy.", news_page),
    ("join-us", "Careers | KSR Akshara Academy", "Teaching careers at KSR Akshara Academy.", careers),
    ("akshara-tree", "The Akshara Tree | KSR Akshara Academy", "Explore the KSR Akshara Academy emblem: every leaf of the tree is a part of school life.", akshara_tree),
    ("contact-us", "Contact Us | KSR Akshara Academy", "Address, phone, email and campus visit booking.", contact),
]

if __name__ == "__main__":
    for slug, title, desc, fn in PAGES:
        depth = len([p for p in slug.split("/") if p])
        r = "../" * depth
        out = ROOT / slug / "index.html" if slug else ROOT / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(webp(layout(r, slug, title, desc, fn(r))), encoding="utf-8")
        print("built", out.relative_to(ROOT))
