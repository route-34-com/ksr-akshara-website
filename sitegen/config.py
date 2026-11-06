"""Site-wide constants: contact details, navigation, SEO identity."""
import json
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent
PHONE_1, PHONE_2 = "98949 32323", "95009 32323"
TEL_1, TEL_2 = "+919894932323", "+919500932323"
EMAIL, EMAIL_2 = "ksrakshara@gmail.com", "info@ksrakshara.org"
YT_ID = "gTh-rg_z7QY"
VER = str(int(time.time()))  # cache-buster: every build forces browsers to refetch CSS/JS
# WhatsApp's own brand mark (a phone in a speech bubble), drawn in the text colour
WA_LOGO = ('<svg class="wa-logo" viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>')
SITE = "https://ksrakshara.org"
GA_ID = ""  # the school's GA4 ID, set at launch once the account owner is confirmed
SCHOOL_LD = json.dumps({
    "@context": "https://schema.org", "@type": "School", "name": "KSR Akshara Academy", "url": SITE + "/",
    "logo": SITE + "/assets/img/logo-emblem.jpg", "image": SITE + "/assets/img/KSR-children.jpg",
    "telephone": TEL_1, "email": EMAIL,
    "sameAs": ["https://www.facebook.com/ksrakshara", "https://www.instagram.com/ksrakshara2010/", "https://www.youtube.com/@ksrakshara"],
    "address": {"@type": "PostalAddress", "streetAddress": "KSR Kalvi Nagar", "addressLocality": "Tiruchengode",
                "addressRegion": "Tamil Nadu", "postalCode": "637215", "addressCountry": "IN"},
    "geo": {"@type": "GeoCoordinates", "latitude": 11.3578249, "longitude": 77.8325664}})
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
