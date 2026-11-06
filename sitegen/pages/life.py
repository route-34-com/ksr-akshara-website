"""Student life: life at Akshara, sports, holiday assignments."""
from ..components import cta_band, page_head
from ..config import CONTAIN

def life(r):
    img = lambda n: f"{r}assets/img/{n}"
    progs = [
        ("isa", "ISA-AWARD-Image.jpg", "International School Award, British Council",
         "Akshara consciously raises teaching and learning to an international standard. The British Council's International School Award recognises schools that go the extra mile, and Akshara has now received it for the third consecutive time (2022 to 2025). Students worked on projects with partner schools abroad and exchanged ideas on a wide range of topics.", None),
        ("houses", "House-system.jpg", "House system",
         "The house system builds good work ethics: attitude, behaviour, communication and how we work with others. Regular inter-house competitions create leadership opportunities and grow creativity, critical thinking, collaboration, communication and compassion.", "houses"),
        ("clubs", "Cooks-act.jpg", "Clubs and activities",
         "Every student is encouraged to join at least one club: Art, Cookery, Photography, Nature, Quiz, Reading, MUN, TED-Ed and Math.", None),
        ("atl", "ATL-school.jpg", "Atal Tinkering Lab (ATL)",
         "A space for students in Grades VI to XII to explore through innovation, tinkering and collaboration. The lab builds design mindset, computational thinking, adaptive learning and physical computing.", None),
        ("ted", "ted.jpg", "TED-Ed Club",
         "Akshara is part of TED's youth and education initiative. Students discover, research and present their big ideas as short TED-style talks, and join global collaborative sessions with schools in other countries.", None),
        ("steam", "Robotics.jpg", "STEAM and Robotics",
         "Science, Technology, Engineering, Arts and Mathematics are taught through activities from Kindergarten to Grade 8, designed for each grade. Robotics brings every STEAM subject together and prepares Aksharites for the future.", None),
        ("iit", "KSR-higher.jpg", "IIT and NEET integrated programme",
         "From Grade VI to XII, an integrated programme prepares students for medical and engineering entrance exams. It combines classroom instruction, interactive sessions and mock tests with personalised coaching, for students aiming at the IITs, NITs and medical colleges.", None),
        ("mun", "admission-image.jpg", "Model United Nations",
         "A comprehensive MUN programme in collaboration with IIMUN. Students act as diplomats, debate international affairs and build public speaking, negotiation and problem-solving skills, guided by experts.", None),
        ("trips", "Fieldstrip.jpg", "Field trips",
         "National and international trips take Aksharites out of the classroom to see new sights, try new things and learn valuable life lessons.", None),
        ("ncc", "ncc.jpg", "NCC, Scouts and Guides",
         "The National Cadet Corps builds discipline and patriotism through drill, shooting, fitness, first aid, map reading, sailing and camp training. Scouts and Guides develop teamwork, communication and decision-making.", None),
        ("arts", "Arts.jpg", "Visual and performing arts",
         "Drama, dance, music and visual arts are woven into the curriculum as per the NEP. Every year the Fine Arts Department stages multidisciplinary performances, with students leading choreography and set design.", None),
    ]
    houses = ('<div class="houses"><div class="house" style="background:#c62f45">Anthuriums</div><div class="house" style="background:#2f62c6">Bluebells</div>'
              '<div class="house" style="background:#8f6b00">Daffodils</div><div class="house" style="background:#7d3fb0">Tulips</div></div>')
    toc = "".join(f'<a href="#{k}">{t.split(",")[0].split(" (")[0]}</a>' for k, _, t, *_ in progs)
    rows = "".join(
        f'<article class="program" id="{k}"><figure class="reveal"><img src="{img(im)}" alt="{t}" loading="lazy"'
        f'{CONTAIN if k == "isa" else ""}></figure>'
        f'<div class="stack reveal"><h2>{t}</h2><p class="muted">{p}</p>{houses if extra == "houses" else ""}</div></article>'
        for k, im, t, p, extra in progs)
    return page_head(r, [("Life at Akshara", None)], "Life at Akshara.",
                     "Spacious classrooms, laboratories, a library, playground, swimming pool, gym and indoor stadium, and a programme that uses all of them.") + f"""
<section class="section" style="padding-top:32px"><div class="wrap"><nav class="toc" aria-label="Programmes">{toc}</nav>{rows}</div></section>""" + cta_band(r)


def sports(r):
    img = lambda n: f"{r}assets/img/{n}"
    grid = [("cricket.jpg", "Cricket"), ("ches.jpg", "Chess"), ("handball.jpg", "Handball"), ("basketball.jpg", "Basketball"),
            ("Skatings_sports.jpg", "Skating"), ("vollyball.jpg", "Volleyball"), ("sgfleet.jpg", "Athletics"), ("House-system.jpg", "Inter-house events")]
    return page_head(r, [("Student life", None), ("Sports", None)], "Sports at Akshara.",
                     "An after-school programme that lets students explore and excel in sport, with a timetable that protects study time.",
                     "banner-sports.jpg", "Students playing basketball on the Akshara court") + f"""
<section class="section"><div class="wrap split top">
  <div class="stack reveal"><h2>World-class football turf.</h2>
    <p class="lede">An international-standard artificial turf built for drills, full matches and evening training under floodlights.</p>
    <ul class="checklist cols-2" style="margin-top:1.5rem">
      <li><i class="ph ph-check-circle"></i>Precise international dimensions</li><li><i class="ph ph-check-circle"></i>Durable, eco-friendly artificial grass</li>
      <li><i class="ph ph-check-circle"></i>Advanced drainage</li><li><i class="ph ph-check-circle"></i>Floodlights for evening sessions</li>
      <li><i class="ph ph-check-circle"></i>Perimeter fencing and goal netting</li><li><i class="ph ph-check-circle"></i>Changing rooms and showers</li>
      <li><i class="ph ph-check-circle"></i>Daily practice with expert coaches</li><li><i class="ph ph-check-circle"></i>Specialist goalkeeper and striker coaching</li></ul></div>
  <div class="grid-auto reveal" style="grid-template-columns:1fr">
    <div class="card"><h3>How a session runs</h3>
      <ol class="steps" style="margin-top:1rem">
        <li><div><strong>Warm-up and fitness</strong><p>15 minutes of stretching, jogging and basic exercises.</p></div></li>
        <li><div><strong>Skill development</strong><p>Drills and practice with personal attention from coaches.</p></div></li>
        <li><div><strong>Team play</strong><p>Teamwork, leadership and sportsmanship.</p></div></li>
        <li><div><strong>Cool-down and reflection</strong><p>Students review their game and set goals.</p></div></li>
      </ol></div></div>
</div></section>
<section class="section section-tint"><div class="wrap">
  <h2 class="reveal">Eight ways to play</h2>
  <div class="sport-grid" style="margin-top:2rem">{"".join(f'<figure class="reveal" style="--i:{i % 4}"><img src="{img(a)}" alt="{b}" loading="lazy"><figcaption>{b}</figcaption></figure>' for i, (a, b) in enumerate(grid))}</div>
  <p class="muted reveal" style="margin-top:2rem;max-width:60ch">Students compete in inter-school, district and state-level tournaments, plus friendly matches with neighbouring schools.</p>
</div></section>""" + cta_band(r)


def holiday(r):
    grades = [("Junior KG", "JKG"), ("Senior KG", "SKG")] + [(f"Grade {n}", f"Grade-{i}") for i, n in enumerate(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"], 1)]
    cards = "".join(f'<a class="card doc-link reveal" style="--i:{i % 3}" href="{r}assets/docs/2025/05/{f}-Holiday-Assignment.pdf" target="_blank" rel="noopener"><i class="ph ph-file-pdf"></i><span>{g}</span><i class="ph ph-download-simple"></i></a>'
                    for i, (g, f) in enumerate(grades))
    return page_head(r, [("Student life", None), ("Holiday assignments", None)], "Summer holiday assignments.",
                     "Download your child's assignment for the 2025 summer break.") + f"""
<section class="section" style="padding-top:36px"><div class="wrap"><div class="grid-auto">{cards}</div>
<p class="note" style="margin-top:1.5rem">In the new site, teachers upload these from the admin panel each term. No developer needed.</p></div></section>"""
