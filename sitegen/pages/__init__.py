"""Every page on the site: slug, title, description, function. Slugs match the live WordPress URLs."""
from .about import about, documents, management, why_akshara
from .academics import methodology
from .admission import admission
from .campus import hostel, transport
from .careers import careers
from .contact import contact
from .home import home
from .life import holiday, life, sports
from .guide import guide
from .news import news_page
from .testimonials import testimonials
from .tree import akshara_tree

PAGES = [
    ("", "KSR Akshara Academy | CBSE School in Tiruchengode", "CBSE-affiliated school in Tiruchengode, Tamil Nadu, from Pre-KG to Grade XII. Admissions open from Vijayadasami.", home),
    ("about-us", "About KSR Akshara Academy | CBSE School in Tiruchengode", "KSR Akshara Academy is a CBSE school in Tiruchengode committed to holistic education.", about),
    ("about-us/management", "Management | KSR Akshara Academy, Tiruchengode", "Meet the founder, director and principal of KSR Akshara Academy, Tiruchengode.", management),
    ("about-us/why-akshara", "Why Akshara? | CBSE School in Tiruchengode", "Eight reasons parents choose KSR Akshara Academy, a CBSE school in Tiruchengode.", why_akshara),
    ("about-us/documents-information", "Documents and Mandatory Disclosure | KSR Akshara Academy", "CBSE mandatory public disclosure and certificates for KSR Akshara Academy, Tiruchengode.", documents),
    ("methodology", "Curriculum and Methodology | KSR Akshara Academy, Tiruchengode", "Foundation, preparatory, middle and secondary stages as per NEP at KSR Akshara Academy, Tiruchengode.", methodology),
    ("life-akshara", "Life at KSR Akshara Academy, Tiruchengode", "International School Award, ATL, TED-Ed, STEAM, MUN, NCC and more at KSR Akshara Academy, Tiruchengode.", life),
    ("sports", "Sports | KSR Akshara Academy, Tiruchengode", "Football turf, skating, cricket, basketball and more at KSR Akshara Academy, Tiruchengode.", sports),
    ("holiday-assignments", "Holiday Assignments | KSR Akshara Academy, Tiruchengode", "Download summer holiday assignments by grade for KSR Akshara Academy, Tiruchengode.", holiday),
    ("facilities-hostel", "School Hostel in Tiruchengode | KSR Akshara Academy", "Five-day and full-time boarding for boys and girls at KSR Akshara Academy, Tiruchengode.", hostel),
    ("facilities-transport", "School Transport in Tiruchengode | KSR Akshara Academy", "GPS-tracked school buses across a 25 km radius of KSR Akshara Academy, Tiruchengode.", transport),
    ("admission", "Admissions 2027-28 | KSR Akshara Academy, Tiruchengode", "Age eligibility, admission process and enquiry form for KSR Akshara Academy, a CBSE school in Tiruchengode.", admission),
    ("parent-guide", "CBSE School Guide for Parents in Tiruchengode | KSR Akshara Academy", "How to compare CBSE schools in Tiruchengode: what to check, what to ask, and how CBSE differs from Matriculation.", guide),
    ("testimonial", "Testimonials | KSR Akshara Academy, Tiruchengode", "What parents and guests say about KSR Akshara Academy, Tiruchengode.", testimonials),
    ("events", "News and Events | KSR Akshara Academy, Tiruchengode", "Latest news, celebrations, trips and achievements from KSR Akshara Academy, Tiruchengode.", news_page),
    ("join-us", "Careers | KSR Akshara Academy, Tiruchengode", "Teaching careers at KSR Akshara Academy, Tiruchengode.", careers),
    ("akshara-tree", "The Akshara Tree | KSR Akshara Academy", "Explore the KSR Akshara Academy emblem: every leaf of the tree is a part of school life.", akshara_tree),
    ("contact-us", "Contact KSR Akshara Academy, Tiruchengode", "Address, phone, email and campus visit booking for KSR Akshara Academy, Tiruchengode.", contact),
]
