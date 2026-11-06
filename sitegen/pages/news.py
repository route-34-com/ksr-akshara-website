"""News and events page."""
from ..components import cta_band, page_head
from ..layout import href
from ..news import NEWS, news_card

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
<section class="section" style="padding-top:40px"><div class="wrap news-layout">
  <div>
    {news_card(r, lead, 0, big=True, h="h2") if lead else ""}
    <div class="news-grid">{"".join(news_card(r, n, i, h="h2") for i, n in enumerate(rest))}</div>
  </div>
  <aside class="notices"><h2>Notices</h2>{notice_html}
    <p class="note">Stories on this page come from the school's YouTube channel, so every new video shows up here automatically.</p>
    <a class="btn btn-ghost" href="https://www.youtube.com/@ksrakshara" target="_blank" rel="noopener"><i class="ph ph-youtube-logo"></i>Our YouTube channel</a>
  </aside>
</div></section>""" + cta_band(r)
