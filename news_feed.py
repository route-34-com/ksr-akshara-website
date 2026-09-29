"""News for the site, pulled from the school's YouTube channel (their most active channel).

Run: python3 news_feed.py   -> refreshes assets/data/news.json and the thumbnails.
build.py only reads the saved JSON, so the build still works offline.
"""
import html
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
CHANNEL = "UCpNRbGPD-dezKovCcMgTsWg"  # youtube.com/@ksrakshara
FEED = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL}"
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿️‍]")


def clean(text):
    text = EMOJI.sub("", html.unescape(text))
    text = re.sub(r"\s+", " ", text).strip(" -|")
    return text.replace("–", "-").replace("—", "-")


def shrink(path, width=800):
    """Resize a thumbnail with macOS sips if available (keeps the page light)."""
    import subprocess
    subprocess.run(["sips", "-Z", str(width), "-s", "formatOptions", "72", str(path)], capture_output=True)


def fetch():
    xml = urllib.request.urlopen(FEED, timeout=20).read().decode()
    items = []
    for e in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        vid = re.search(r"<yt:videoId>(.*?)</yt:videoId>", e).group(1)
        desc = re.search(r"<media:description>(.*?)</media:description>", e, re.S)
        desc = clean(desc.group(1)) if desc else ""
        desc = re.sub(r"#\w+", "", desc)
        desc = re.sub(r"\.(?=[A-Z])", ". ", desc)                          # "Salem.Their" -> "Salem. Their"
        desc = re.sub(r"(\s*\.){2,}\s*$|\s+\.(?=\s|$)", "", desc).strip()  # stray " . ." endings
        desc = re.sub(r"\s*(Watch now!?|Watch the video!?)\s*", " ", desc).strip()
        title = clean(re.search(r"<title>(.*?)</title>", e).group(1))
        if desc.lower().startswith(title.lower()):
            desc = desc[len(title):].strip()
        summary = ""
        for sentence in re.split(r"(?<=[.!?])(?<!Ms\.)(?<!Mr\.)(?<!Dr\.)(?<!Mrs\.)\s+", desc):
            if summary and len(summary) + len(sentence) > 170:
                break
            summary = (summary + " " + sentence).strip()
        if len(summary) > 200:
            summary = summary[:190].rsplit(" ", 1)[0].rstrip(",;:") + "…"
        items.append({"id": vid, "date": re.search(r"<published>(.*?)</published>", e).group(1)[:10],
                      "title": title, "summary": summary})
    for it in items:
        out = ROOT / "assets/img/news" / f"{it['id']}.jpg"
        if not out.exists():
            for size in ("maxresdefault", "sddefault", "hqdefault"):
                try:
                    data = urllib.request.urlopen(f"https://i.ytimg.com/vi/{it['id']}/{size}.jpg", timeout=20).read()
                    if len(data) > 5000:
                        out.write_bytes(data); shrink(out); break
                except Exception:
                    continue
    (ROOT / "assets/data/news.json").write_text(json.dumps(items, indent=1, ensure_ascii=False))
    print(f"saved {len(items)} items")


if __name__ == "__main__":
    fetch()
