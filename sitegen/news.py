"""News items from assets/data/news.json and the card that shows one."""
import html
import json
from .config import ROOT

NEWS = json.loads((ROOT / "assets/data/news.json").read_text(encoding="utf-8")) if (ROOT / "assets/data/news.json").exists() else []
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def fmt_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[int(m) - 1]} {y}"


def news_card(r, n, i=0, big=False, h="h3"):
    """One news item: thumbnail that plays the video in place, date, title, summary."""
    return (f'<article class="news-card{" big" if big else ""} reveal" style="--i:{i % 3}">'
            f'<div class="film news-media"><button type="button" data-yt="{n["id"]}" aria-label="Play: {html.escape(n["title"])}">'
            f'<span class="play"><i class="ph-fill ph-play"></i></span></button>'
            f'<img src="{r}assets/img/news/{n["id"]}.jpg" alt="{html.escape(n["title"], quote=True)}" loading="lazy"></div>'
            f'<div class="news-body"><time datetime="{n["date"]}">{fmt_date(n["date"])}</time>'
            f'<{h}>{html.escape(n["title"])}</{h}><p>{html.escape(n["summary"])}</p></div></article>')
