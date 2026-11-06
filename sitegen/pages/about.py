"""About section: story, management, why Akshara, documents."""
from ..components import cta_band, page_head
from ..layout import href

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
<section class="section" style="padding-top:12px"><div class="wrap">
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
             ("ph-chalkboard-teacher", "Highly well‑trained educators"),
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
    link = lambda t, f, i: f'<a class="card doc-link reveal" style="--i:{i % 3}" href="{r}assets/docs/2022/03/{f}" target="_blank" rel="noopener"><i class="ph ph-file-pdf"></i><span>{t}</span><i class="ph ph-arrow-up-right"></i></a>'
    return page_head(r, [("About", "about-us"), ("Documents & disclosure", None)], "Documents and mandatory disclosure.",
                     "Everything CBSE requires us to publish, in one place. Each document opens as a PDF.") + f"""
<section class="section" style="padding-top:36px"><div class="wrap stack-lg">
  <a class="btn btn-brand reveal" href="{r}assets/docs/2023/06/Mandatory-Public-Disclosure.pdf" target="_blank" rel="noopener"><i class="ph ph-download-simple"></i>Mandatory public disclosure (PDF)</a>
  <h2 class="reveal" style="padding-top:1.5rem">Certificates and approvals</h2>
  <div class="grid-auto">{"".join(link(t, f, i) for i, (t, f) in enumerate(docs))}</div>
  <h2 class="reveal" style="padding-top:2rem">Results and academics</h2>
  <div class="grid-auto">{"".join(link(t, f, i) for i, (t, f) in enumerate(acad))}</div>
</div></section>"""
