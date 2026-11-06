"""Parent guide: how to compare CBSE schools in Tiruchengode."""
from ..components import cta_band, page_head
from ..layout import href

CHECKS = [
    ("Confirm the affiliation",
     'Every CBSE school has an affiliation number that you can look up on the CBSE SARAS portal. '
     'Check the level as well, because a Secondary school stops at Class X and a Senior Secondary school goes to Class XII. '
     '<a href="https://saras.cbse.gov.in/SARAS/AffiliatedList/AfflicationDetails/1930318" target="_blank" rel="noopener">'
     'See KSR Akshara Academy on SARAS (1930318)</a>.'),
    ("Read the mandatory public disclosure",
     "CBSE schools must publish their details and certificates online. See how recent the documents are."),
    ("Ask for results with class sizes",
     "A 100% pass rate says more when you know how many students sat the exam. Ask for subject averages too."),
    ("Check the journey",
     "Ask whether a bus reaches your area, where the nearest stop is, and how long your child would travel."),
    ("Get the full fees in writing",
     "Ask what the fee covers, and what is charged separately for transport, hostel, books and activities."),
    ("Visit during a school day",
     "Walk the classrooms and labs, meet the Principal, and see how students and teachers speak to each other."),
]


def guide(r):
    items = "".join(f"<h3>{t}</h3><p>{b}</p>" for t, b in CHECKS)
    return page_head(r, [("Admissions", "admission"), ("Parent guide", None)],
                     "A parent's guide to choosing a CBSE school in Tiruchengode.",
                     "What to compare, what to ask, and how to check a school for yourself.") + f"""
<section class="section" style="padding-top:36px"><div class="wrap stack-lg" style="max-width:72ch">
  <div class="reveal">
    <h2>CBSE or Matriculation?</h2>
    <p style="margin-top:.75rem">CBSE is a national board with schools across India, and it follows one curriculum wherever a family moves.
    Matriculation schools in Tamil Nadu follow the State Board syllabus. Neither suits every child, so compare the school as well as the board.</p>
  </div>
  <div class="reveal">
    <h2>Six checks before you choose</h2>
    <div class="faq">{items}</div>
  </div>
  <div class="reveal">
    <h2>Applying to KSR Akshara Academy</h2>
    <p style="margin-top:.75rem">Admissions are open from Vijayadasami to March for the following academic year.
    See the <a href="{href(r, "admission")}">admissions page</a> for age eligibility and steps, or
    <a href="{href(r, "contact-us")}#visit">book a campus visit</a>.</p>
  </div>
</div></section>""" + cta_band(r)
