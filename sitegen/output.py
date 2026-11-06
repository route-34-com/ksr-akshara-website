"""Writes the generated site to disk: pages, sitemap.xml and robots.txt."""
import re

from .config import ROOT, SITE
from .layout import layout
from .pages import PAGES


def webp(page):
    """Point every photo at its .webp copy (made by optimize_images.py), except og:image."""
    def swap(m):
        path = m.group(1)
        local = ROOT / re.sub(r"^(\.\./)+", "", path)
        return path + (".webp" if local.with_suffix(".webp").exists() else ".jpg")
    lines = page.split("\n")
    return "\n".join(l if 'property="og:image"' in l else re.sub(r"((?:\.\./)*assets/img/[\w./-]+?)\.jpg", swap, l) for l in lines)


def write_pages():
    for slug, title, desc, fn in PAGES:
        depth = len([p for p in slug.split("/") if p])
        r = "../" * depth
        out = ROOT / slug / "index.html" if slug else ROOT / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(webp(layout(r, slug, title, desc, fn(r))), encoding="utf-8")
        print("built", out.relative_to(ROOT))


def write_sitemap():
    urls = "".join(f"<url><loc>{SITE}/{slug + '/' if slug else ''}</loc></url>" for slug, *_ in PAGES)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n',
        encoding="utf-8")


def write_robots():
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")


def build():
    write_pages()
    write_sitemap()
    write_robots()
