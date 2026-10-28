"""Write WebP copies of every photo, sized for how the site shows them.

Run after adding photos:  /tmp/ksrvenv/bin/python optimize_images.py   (needs Pillow)
build.py then points pages at the .webp files (the .jpg originals stay for social previews).
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
IMG = ROOT / "assets/img"
BANNERS = {"KSR-children.jpg", "why-akshara.jpg", "ksr-contact-banner.jpg", "management-banner.jpg",
           "career-banner.jpg", "transport-banner.jpg", "banner-sports.jpg", "banner-admission.jpg", "banner-hostel.jpg", "banner-careers.jpg"}


def width_for(p):
    if p.parent.name == "news":
        return 640          # card thumbnails
    if p.name == "logo-emblem.jpg":
        return 128          # shown at 50px
    if p.name in BANNERS:
        return 1600         # full-width page banners
    if p.stat().st_size < 12_000:
        return 240          # small portraits
    return 960              # everything else is shown at half the page or less


def main():
    before = after = 0
    for p in sorted(IMG.rglob("*.jpg")):
        out = p.with_suffix(".webp")
        im = Image.open(p).convert("RGB")
        w = min(width_for(p), im.width)
        if im.width > w:
            im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        im.save(out, "WEBP", quality=78, method=6)
        before += p.stat().st_size; after += out.stat().st_size
    print(f"jpg {before // 1024} KB -> webp {after // 1024} KB")


if __name__ == "__main__":
    main()
