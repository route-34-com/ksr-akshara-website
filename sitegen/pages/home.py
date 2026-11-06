"""Homepage."""
from ..components import enquiry_form
from ..config import YT_ID
from ..layout import href
from ..news import NEWS, news_card
from .tree import tree_parts

def home(r):
    img = lambda n: f"{r}assets/img/{n}"
    stages = [
        ("foundation", "Foundation", "Pre-KG to Grade II", "KSR-children-2.jpg",
         "Play-based learning across eight domains of development",
         "A holistic, discovery-based early years programme following NEP ECCE guidance. Children build cognitive, social, emotional, creative and physical skills in a classroom rich in sensory experiences."),
        ("preparatory", "Preparatory", "Grades III to V", "career-banner.jpg",
         "Structured learning with room to explore",
         "An interdisciplinary, technology-rich curriculum with active learning. Skill development is planned into every term so learners grasp concepts and grow into confident individuals."),
        ("middle", "Middle", "Grades VI to VIII", "ATL-school.jpg",
         "Projects that connect to the real world",
         "Project-based, hands-on learning, group discussions, seminars, quizzes and e-research. Students start in the Atal Tinkering Lab and the integrated IIT and NEET foundation from Grade VI."),
        ("secondary", "Secondary", "Grades IX to XII", "KSR-higher.jpg",
         "Ready for India's best colleges, and abroad",
         "A multidisciplinary system with a choice of subject combinations, skill enhancement and career guidance. The integrated NEET and JEE programme includes classroom instruction, interactive sessions and mock tests."),
    ]
    tabs = "".join(
        f'<button class="stage-tab" role="tab" id="tab-{k}" aria-controls="panel-{k}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">'
        f'<strong>{n}</strong><span>{g}</span><i class="ph ph-arrow-right"></i></button>'
        for i, (k, n, g, *_rest) in enumerate(stages))
    panels = "".join(
        f'<div class="stage-panel" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}"{"" if i == 0 else " hidden"}>'
        f'<img src="{img(im)}" alt="{n} stage students at Akshara" loading="lazy"><div class="stack"><h3>{h}</h3><p class="muted">{p}</p>'
        f'<a class="link-arrow" href="{href(r, "methodology")}#{k}">How the {n.lower()} stage works <i class="ph ph-arrow-right"></i></a></div></div>'
        for i, (k, n, g, im, h, p) in enumerate(stages))

    why = [
        ("Learning", [
            ("ph-flask", "Researched curriculum", "Scientifically researched and planned, aligned to CBSE and NEP."),
            ("ph-lightbulb", "Four ways to learn", "Active, skill-based, experiential and blended learning."),
            ("ph-chalkboard-teacher", "Well-trained educators", "Periodic training keeps teaching methods current."),
            ("ph-medal", "Scholastic and co-scholastic", "Equal weight on academics, values and activities."),
        ]),
        ("Safety", [
            ("ph-security-camera", "24 x 7 CCTV", "Every corner of the campus is monitored round the clock."),
            ("ph-bus", "GPS-tracked buses", "Caretakers on board and live tracking on every route."),
        ]),
        ("Living", [
            ("ph-bed", "Weekly and regular boarding", "Five-day boarding or full-time, with house parents."),
            ("ph-soccer-ball", "Sports and performing arts", "A floodlit turf, skating rink, dance, drama and music."),
        ]),
    ]
    why_html = "".join(
        f'<div class="why-group reveal"><h3>{g}</h3><div class="why-items">' + "".join(
            f'<div class="why-item"><i class="ph {ic}"></i><div><strong>{t}</strong><p>{d}</p></div></div>' for ic, t, d in items)
        + "</div></div>" for g, items in why)

    quotes = [
        ("lead", "I very much hope to see many chemists coming from this school.", "professor.jpg", "Prof. Dr. Robert Huber", "Nobel Laureate in Chemistry, 1988", None),
        ("", "My son Nithin Rohit completed Grade XII here and went on to study Electrical Engineering at IIT Jodhpur. The JEE programme was truly amazing.", "Kumar-120x120.jpg", "K. Kumar", "Parent of Nithin Rohit", "IIT Jodhpur"),
        ("", "The NEET coaching gave my twins the knowledge and the confidence to pursue medicine. Both are now in medical college.", "Vanitha-srinivasan.jpg", "Vanitha Srinivasan", "Parent of Kanimozhi and Kayalvizhi", "Madras and Vellore Medical Colleges"),
        ("", "Amazing children. Amazing infrastructure. Looking forward to more laurels from the school.", "jaikumar.jpg", "Jaikumar Christhu Rajan", "Director, St. Joseph's College of Engineering, Chennai", None),
        ("", "Skill competency and house competitions have visibly increased my daughter's confidence and her ability to face challenges.", "Chitra-120x120.jpg", "S. Chitra", "Mother of A.S. Anmithashree", None),
        ("", "I am deeply impressed. I do wish you success. Take your chance.", "Hartmut-Michel.jpg", "Prof. Hartmut Michel", "Nobel Laureate in Chemistry, 1988", None),
    ]
    q_html = "".join(
        f'<figure class="quote {c}">' + (f'<span class="result"><i class="ph ph-graduation-cap"></i>{res}</span>' if res else "")
        + f'<blockquote>&ldquo;{q}&rdquo;</blockquote><figcaption><img src="{img(p)}" alt="" loading="lazy"><div><strong>{n}</strong><span>{role}</span></div></figcaption></figure>'
        for c, q, p, n, role, res in quotes)

    sports = [("sgfleet.jpg", "Athletics"), ("Skatings_sports.jpg", "Skating"), ("basketball.jpg", "Basketball"),
              ("cricket.jpg", "Cricket"), ("vollyball.jpg", "Volleyball"), ("handball.jpg", "Handball"),
              ("ches.jpg", "Chess"), ("House-system.jpg", "House competitions")]
    s_items = "".join(f'<figure class="sport"><img src="{img(i)}" alt="{t} at Akshara" loading="lazy"><figcaption>{t}</figcaption></figure>' for i, t in sports)
    s_dupe = "".join(f'<figure class="sport" aria-hidden="true"><img src="{img(i)}" alt="" loading="lazy"><figcaption>{t}</figcaption></figure>' for i, t in sports)

    ages = [("Pre-KG", "2 years 5 months by June"), ("Junior KG", "3 years 2 months"), ("Senior KG", "4 years 2 months"), ("Grade I", "5 years 2 months")]
    ages_html = "".join(f'<div class="age"><strong>{a}</strong><span>{b}</span></div>' for a, b in ages)

    tree = tree_parts(r)
    latest = "".join(news_card(r, n, i) for i, n in enumerate(NEWS[:3]))
    return f"""
<div class="notice-bar"><div class="wrap"><i class="ph ph-megaphone-simple"></i><span><strong>Admissions 2027-28</strong> open from Vijayadasami for all classes.</span>
  <a href="{href(r, "admission")}">Enquire now <i class="ph ph-arrow-right"></i></a></div></div>
<section class="hero"><div class="wrap hero-grid">
  <div class="intro">
    <h1><span class="eyebrow"><i class="ph-fill ph-seal-check"></i>KSR Akshara Academy, CBSE school in Tiruchengode</span>Nurturing young minds and hearts of <em>tomorrow's leaders.</em></h1>
    <p class="lede">From Pre-KG to Grade XII, Aksharites learn through inquiry, sport, the arts and strong values.</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" href="{href(r, "admission")}">Admissions enquiry <i class="ph ph-arrow-right"></i></a>
      <a class="btn btn-ghost" href="{href(r, "contact-us")}#visit"><i class="ph ph-map-pin"></i>Book a campus visit</a>
    </div>
  </div>
  <div class="hero-tree" data-tree="mini" data-link="{href(r, "akshara-tree")}" data-sway-x="{tree["sx"]}" data-sway-y="720">
    <div class="tree-stage" style="aspect-ratio:{tree["ratio"]}">{tree["svg"]}<div class="tree-tip" aria-hidden="true"></div></div>
    <a class="link-arrow hero-tree-link" href="{href(r, "akshara-tree")}">Every leaf of our emblem tells a story <i class="ph ph-arrow-right"></i></a>
  </div>
</div></section>
{tree["data"]}

<section class="facts" aria-label="Akshara at a glance"><div class="wrap facts-grid">
  <div class="fact reveal"><strong>1984</strong><span>KSR Educational and Charitable Trust founded</span></div>
  <div class="fact reveal" style="--i:1"><strong>16</strong><span>KSR institutions, from Pre-KG to Ph.D.</span></div>
  <div class="fact reveal" style="--i:2"><strong>4,500+</strong><span>students across the three KSR schools</span></div>
  <div class="fact reveal" style="--i:3"><strong>3x</strong><span>British Council International School Award</span></div>
  <div class="fact reveal" style="--i:4"><strong>25 km</strong><span>GPS-tracked bus network around Tiruchengode</span></div>
</div></section>

<section class="section section-tint latest"><div class="wrap">
  <div class="voices-head reveal"><h2>Latest from Akshara</h2>
    <a class="link-arrow" href="{href(r, "events")}">All news and events <i class="ph ph-arrow-right"></i></a></div>
  <div class="news-grid news-grid-3">{latest}</div>
</div></section>

<section class="section" id="academics"><div class="wrap">
  <div class="stack reveal" style="max-width:62ch"><h2>One curriculum, four stages, shaped by the NEP.</h2>
  <p class="lede">Akshara follows CBSE expectations and builds skills for an international context. Every stage has its own way of teaching.</p></div>
  <div class="stages" data-tabs>
    <div class="stage-tabs" role="tablist" aria-label="Stages of learning">{tabs}</div>
    <div>{panels}</div>
  </div>
</div></section>

<section class="section section-tint"><div class="wrap">
  <span class="eyebrow reveal">Life at Akshara</span>
  <h2 class="reveal" style="margin-top:.9rem;max-width:22ch">More than a classroom, every single day.</h2>
  <div class="bento">
    <a class="tile photo t-isa reveal" href="{href(r, "life-akshara")}#isa"><img src="{img("Fieldstrip.jpg")}" alt="Akshara students on a field trip" loading="lazy">
      <h3>International School Award, three times in a row</h3><p>The British Council honours schools that bring the world into the classroom. Akshara has earned it for 2022 to 2025.</p></a>
    <a class="tile photo t-atl reveal" style="--i:1" href="{href(r, "life-akshara")}#atl"><img src="{img("Robotics.jpg")}" alt="Robotics kit being assembled" loading="lazy"><h3>Atal Tinkering Lab</h3><p>Grades VI to XII</p></a>
    <a class="tile photo t-ted reveal" style="--i:2" href="{href(r, "life-akshara")}#ted"><img src="{img("ted.jpg")}" alt="A student giving a TED-Ed talk" loading="lazy"><h3>TED-Ed Club</h3><p>Student talks, global sessions</p></a>
    <div class="tile tint t-clubs reveal" style="--i:1"><div class="chips">
      <span class="chip"><i class="ph ph-palette"></i>Art</span><span class="chip"><i class="ph ph-cooking-pot"></i>Cookery</span>
      <span class="chip"><i class="ph ph-camera"></i>Photography</span><span class="chip"><i class="ph ph-leaf"></i>Nature</span>
      <span class="chip"><i class="ph ph-question"></i>Quiz</span><span class="chip"><i class="ph ph-book-open"></i>Reading</span>
      <span class="chip"><i class="ph ph-globe-hemisphere-east"></i>MUN</span><span class="chip"><i class="ph ph-microphone-stage"></i>TED-Ed</span>
      <span class="chip"><i class="ph ph-function"></i>Math</span></div>
      <div><h3>Nine clubs to choose from</h3><p class="muted">Every student joins at least one.</p></div></div>
    <a class="tile brand t-robo reveal" href="{href(r, "life-akshara")}#steam"><i class="ph ph-cpu big-icon"></i><h3>STEAM and Robotics</h3><p>From Kindergarten to Grade 8</p></a>
    <a class="tile brand t-mun reveal" style="--i:1;background:var(--accent)" href="{href(r, "life-akshara")}#mun"><i class="ph ph-globe big-icon"></i><h3>Model UN with IIMUN</h3><p style="color:#fff">Students debate as diplomats</p></a>
    <a class="tile photo t-ncc reveal" style="--i:2" href="{href(r, "life-akshara")}#ncc"><img src="{img("ncc.jpg")}" alt="NCC cadets marching in formation" loading="lazy"><h3>NCC, Scouts and Guides</h3><p>Drill, first aid, map reading and camp training</p></a>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <h2 class="reveal" style="max-width:24ch">See a day at Akshara.</h2>
  <div class="film reveal">
    <button type="button" data-yt="{YT_ID}" aria-label="Play the campus film"><span class="play"><i class="ph-fill ph-play"></i></span>
      <span><strong>The Akshara campus film</strong><small>Classrooms, labs, stage and turf in a few minutes.</small></span></button>
    <img src="{img("why-akshara.jpg")}" alt="Campus of KSR Akshara Academy, Tiruchengode" loading="lazy">
  </div>
</div></section>

<section class="section section-tint"><div class="wrap why">
  <div class="why-aside reveal"><h2>Eight reasons parents choose Akshara.</h2>
    <p class="lede" style="margin-top:1rem">Quality and international standards of education, in an Indian context.</p>
    <img src="{img("KSR-children.jpg")}" alt="Four smiling Akshara students in uniform" loading="lazy"></div>
  <div class="why-groups">{why_html}</div>
</div></section>

<section class="section"><div class="wrap" data-carousel>
  <div class="voices-head reveal"><h2 style="max-width:18ch">What visitors and parents say.</h2>
    <div class="carousel-btns"><button class="icon-btn" data-dir="-1" aria-label="Previous"><i class="ph ph-arrow-left"></i></button>
    <button class="icon-btn" data-dir="1" aria-label="Next"><i class="ph ph-arrow-right"></i></button></div></div>
  <div class="carousel reveal" tabindex="0" aria-label="Testimonials">{q_html}</div>
  <a class="link-arrow" href="{href(r, "testimonial")}">Read all testimonials <i class="ph ph-arrow-right"></i></a>
</div></section>

<section class="section section-tint" style="overflow:hidden"><div class="wrap">
  <div class="stack reveal" style="max-width:60ch"><h2>A floodlit football turf, and a sport for every child.</h2>
  <p class="lede">After-school coaching in cricket, athletics, volleyball, football, basketball and more, planned around study time.</p>
  <a class="link-arrow" href="{href(r, "sports")}">Explore sports <i class="ph ph-arrow-right"></i></a></div></div>
  <div class="marquee"><div class="marquee-track">{s_items}{s_dupe}</div></div>
</section>

<section class="section" id="admissions"><div class="wrap admit">
  <div class="reveal">
    <span class="eyebrow">Admissions 2027-28</span>
    <h2 style="margin-top:.9rem">Admissions open from Vijayadasami to March.</h2>
    <p class="lede" style="margin-top:1rem">Seats are offered first come, first served. Late applications in April depend on availability.</p>
    <div class="ages">{ages_html}</div>
    <ol class="steps">
      <li><div><strong>Enquire</strong><p>By phone or in person. Meet the Principal or Vice Principals.</p></div></li>
      <li><div><strong>Collect the application</strong><p>Available at the school office on payment.</p></div></li>
      <li><div><strong>Entrance assessment</strong><p>From Senior KG onwards. Submit the form on the day.</p></div></li>
    </ol>
  </div>
  <div class="reveal" style="--i:1">{enquiry_form()}</div>
</div></section>
"""
