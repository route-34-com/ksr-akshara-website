"""Campus facilities: hostel and transport."""
from ..components import cta_band, page_head
from ..config import PHONE_1

def hostel(r):
    img = lambda n: f"{r}assets/img/{n}"
    return page_head(r, [("Campus", None), ("Hostel", None)], "A hi-tech, home-away-from-home hostel.",
                     "Residential life at Akshara helps students grow independent in a safe, secure environment.",
                     "banner-hostel.jpg", "Rows of bunk beds in an Akshara hostel dormitory") + f"""
<section class="section"><div class="wrap split">
  <div class="stack reveal"><h2>Two ways to board.</h2>
    <div class="grid-auto" style="grid-template-columns:repeat(2,minmax(0,1fr));margin-top:1.25rem">
      <div class="card"><i class="ph ph-calendar-check" style="font-size:1.8rem;color:var(--brand)"></i><h3 style="margin-top:.75rem">Five-day boarding</h3><p>Monday to Friday at school, weekends at home. The best of both worlds.</p></div>
      <div class="card"><i class="ph ph-house-line" style="font-size:1.8rem;color:var(--brand)"></i><h3 style="margin-top:.75rem">Full-time boarding</h3><p>A nurturing, home-away-from-home environment.</p></div>
    </div></div>
  <img class="media reveal" src="{img("Akshara-hostel.jpg")}" alt="Hostel dormitory with bunk beds" loading="lazy">
</div></section>
<section class="section section-tint"><div class="wrap">
  <h2 class="reveal">Cared for, every day.</h2>
  <ul class="checklist cols-2 reveal" style="margin-top:2rem;max-width:960px">
    <li><i class="ph ph-users"></i>Dedicated house parents tailor routines to each student</li>
    <li><i class="ph ph-gender-intersex"></i>Separate accommodation for boys and girls</li>
    <li><i class="ph ph-first-aid"></i>Medical needs handled by trained professionals</li>
    <li><i class="ph ph-student"></i>Trained mentors monitor academic progress</li>
    <li><i class="ph ph-bowl-food"></i>Nutritious breakfast, lunch, snack and dinner</li>
    <li><i class="ph ph-fork-knife"></i>Non-vegetarian menu three days a week</li>
    <li><i class="ph ph-security-camera"></i>Campus secured with 24 x 7 CCTV</li>
  </ul>
</div></section>""" + cta_band(r, "See the hostel in person.", "Book a visit and our team will walk you through the rooms, dining hall and study areas.")


def transport(r):
    img = lambda n: f"{r}assets/img/{n}"
    towns = ["Tiruchengode", "Erode", "Kumaramangalam", "Sankari", "Pallipalayam", "Veppadai"]
    return page_head(r, [("Campus", None), ("Transport", None)], "Getting your child to school safely.",
                     "Transporting your children safely is our utmost priority.") + f"""
<section class="section" style="padding-top:36px"><div class="wrap split">
  <img class="media reveal" src="{img("transport-right.jpg")}" alt="Senior students walking to the bus" loading="lazy">
  <div class="stack-lg reveal">
    <div class="stat-row"><div><strong>~1,400</strong><span>students served daily</span></div><div><strong>25 km</strong><span>route radius</span></div></div>
    <ul class="checklist">
      <li><i class="ph ph-navigation-arrow"></i>State-of-the-art GPS tracking on every vehicle</li>
      <li><i class="ph ph-hand-waving"></i>Caretakers on board for safe boarding and alighting</li>
      <li><i class="ph ph-wrench"></i>Regular maintenance and full compliance with state regulations</li></ul>
    <div><p style="font-weight:600;margin-bottom:.75rem">Routes cover</p><div class="chips">{"".join(f'<span class="chip"><i class="ph ph-map-pin"></i>{t}</span>' for t in towns)}</div></div>
  </div>
</div></section>""" + cta_band(r, "Check if we cover your area.", f"Call the transport desk on {PHONE_1} with your pickup point.")
