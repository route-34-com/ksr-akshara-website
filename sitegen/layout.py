"""The page shell: head tags, header, navigation, footer."""
from .config import CUR, EMAIL, GA_ID, NAV, PHONE_1, PHONE_2, SCHOOL_LD, SITE, TEL_1, TEL_2, VER, WA_LOGO

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


def analytics():
    if not GA_ID:
        return ""
    return (f'\n<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>'
            f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());'
            f'gtag("config","{GA_ID}",{{allow_google_signals:false,allow_ad_personalization_signals:false}})</script>')


def layout(r, cur, title, desc, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{cur + "/" if cur else ""}">
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
<script type="application/ld+json">{SCHOOL_LD}</script>{analytics()}
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
        <a class="icon-btn" href="https://www.facebook.com/ksrakshara" aria-label="Facebook"><i class="ph ph-facebook-logo"></i></a>
        <a class="icon-btn" href="https://www.instagram.com/ksrakshara2010/" aria-label="Instagram"><i class="ph ph-instagram-logo"></i></a>
        <a class="icon-btn" href="https://www.youtube.com/@ksrakshara" aria-label="YouTube"><i class="ph ph-youtube-logo"></i></a>
        <a class="icon-btn" href="https://wa.me/919894932323" aria-label="WhatsApp"><i>{WA_LOGO}</i></a>
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
<a class="fab" href="https://wa.me/919894932323" aria-label="Chat with the admissions office on WhatsApp">{WA_LOGO}</a>
<script src="{r}assets/js/site.js?v={VER}" defer></script>
</body>
</html>
"""
