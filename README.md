# KSR Akshara Academy: redesign concept

A pitch prototype for a new ksrakshara.org. It uses the school's own content, photos and logo.

## Run it

```bash
python3 build.py              # regenerates every page from build.py
python3 -m http.server 8000   # then open http://localhost:8000
```

Opening `index.html` directly also works, but the map and the campus film need a server.

## What's in it

15 pages, each at the **same URL slug as the live site**, so existing Google rankings and links carry over:
`/`, `/about-us/`, `/about-us/management/`, `/about-us/why-akshara/`, `/about-us/documents-information/`,
`/methodology/`, `/life-akshara/`, `/sports/`, `/holiday-assignments/`, `/facilities-hostel/`,
`/facilities-transport/`, `/admission/`, `/testimonial/`, `/join-us/`, `/contact-us/`.

New page: `/akshara-tree/`, the school emblem's tree as a full-screen interactive piece. Each leaf is traced from the emblem along its white gaps, in the leaf's own blue from the logo (`tree_geometry.py`, data in `assets/data/akshara-tree-logo.json`). Wind sways the crown and rustles each leaf, leaves drift across the screen, the pointer stirs nearby leaves, and a switch in the dock pauses it all (it stays off for visitors who prefer reduced motion). Tapping a leaf lights it up and opens its story in a glass card. Links like `/akshara-tree/#football` open a specific leaf.

New page: `/events/` (News and events), the same slug their WordPress events page used. Stories come from the school's YouTube channel: `python3 news_feed.py` pulls the latest videos (title, date, summary, thumbnail) into `assets/data/news.json`, and the next build shows them. The three newest also appear on the homepage.

## Keeping it fast

| Script | When to run | What it does |
| --- | --- | --- |
| `python3 build.py` | after any content change | builds every page, pointing photos at their WebP copies |
| `python3 news_feed.py` | to refresh news | pulls the latest YouTube videos and thumbnails |
| `/tmp/ksrvenv/bin/python optimize_images.py` | after adding photos | writes WebP copies sized for display (needs Pillow) |
| `/tmp/ksrvenv/bin/python vendor_assets.py` | after using a new icon | self-hosted fonts plus an icon font cut down to the icons in use (needs fonttools) |

### Measured (Lighthouse 12, mobile, simulated slow 4G)

| Page | Current site: perf / a11y / best practices / SEO | This concept | Page weight (current → concept) |
| --- | --- | --- | --- |
| Homepage | 46 / 71 / 57 / 77, main content at 4.1 s | 96 / 100 / 100 / 100, main content at 2.4 s | 4,020 KB → 333 KB |
| Life @ Akshara | 55 / 81 / 61 / 92, main content at 9.6 s | 96 / 100 / 100 / 100, main content at 2.7 s | 1,954 KB → 511 KB |

The concept was measured on a local server; real hosting will add some network time.

## Pitch talking points (current site vs. this concept)

| Current site | This concept |
| --- | --- |
| The homepage has three teaser cards and one paragraph. | The homepage tells the whole story: stages, awards, results, sport, admissions. |
| The strongest proof is buried on inner pages: 3x British Council ISA award, Nobel laureate visits, IIT Jodhpur and medical college results. | That proof sits on the homepage, in the facts band, the bento grid and the testimonials. |
| Admission dates and age eligibility are only on the Admission page. | Dates, ages, steps and an enquiry form are on the homepage. |
| The enquiry form has three fields and no validation. | Inline validation, error states, success state and a boarding preference. Ready to connect to email, WhatsApp or a CRM. |
| The "Eight domains" appear only as an image, so Google and screen readers can't read them. | They are real text. |
| Some background images load over plain `http://` (mixed content). | Everything is local or HTTPS. |
| The logo is a 2560px JPG. | Optimised assets (about 3.8 MB for all images). |
| No news: the events plugin is installed but empty. | News and events that update automatically from their YouTube channel, plus a notices panel. |
| Homepage weighs 4 MB and scores 46 for performance on a phone. | Homepage weighs 333 KB and scores 96; accessibility, best practices and SEO all 100. |
| No dark mode, no WhatsApp shortcut, no structured data. | Light and dark themes, a floating WhatsApp button, and `School` schema.org data for Google. |
| The mobile menu is a plain list. | A slide-in drawer with grouped navigation. |

## Before going live

- Connect the forms (admissions, careers, campus visit). They are demo-only right now.
- Get sign-off on the copy (lightly edited from the live site) and the photo choices.
- Move document and holiday-assignment PDFs off the old WordPress uploads, or keep that path working.
- Self-host the fonts (Outfit, Figtree) and icons (Phosphor) for production.
