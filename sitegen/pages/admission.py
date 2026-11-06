"""Admissions page."""
from ..layout import href
from ..components import enquiry_form, page_head

def admission(r):
    ages = [("Pre-KG", "2 years 5 months as of June"), ("Junior KG", "3 years 2 months"), ("Senior KG", "4 years 2 months"), ("Grade I", "5 years 2 months")]
    return page_head(r, [("Admissions", None)], "Admissions 2027-28.",
                     "Admissions at KSR Akshara Academy, Tiruchengode, are open for all classes from Vijayadasami to March for the following academic year.",
                     "banner-admission.jpg", "Young Aksharites smiling in their school uniform") + f"""
<section class="section"><div class="wrap admit">
  <div class="stack-lg reveal">
    <h2>Eligibility by age</h2>
    <div class="ages" style="margin-top:1rem">{"".join(f'<div class="age"><strong>{a}</strong><span>{b}</span></div>' for a, b in ages)}</div>
    <h2 style="padding-top:1.5rem">How to apply</h2>
    <ol class="steps" style="margin-top:1rem">
      <li><div><strong>Enquire</strong><p>Call us or visit in person and fill in an enquiry form. You can meet the Principal or Vice Principals.</p></div></li>
      <li><div><strong>Collect the application form</strong><p>Available at the school office on payment.</p></div></li>
      <li><div><strong>Entrance examination</strong><p>For Senior KG onwards. Submit the completed form on the day of the exam.</p></div></li>
      <li><div><strong>Confirmation</strong><p>Seats are offered first come, first served. If you miss the window, April admissions depend on availability.</p></div></li>
    </ol>
    <h2 style="padding-top:1.5rem">Common questions</h2>
    <div class="faq">
      <h3>When can I apply?</h3><p>From Vijayadasami to March for the following academic year. April admissions depend on availability.</p>
      <h3>Which classes does the school have?</h3><p>Pre-KG to Grade XII. KSR Akshara Academy is a CBSE school, affiliation number 1930318.</p>
      <h3>Is there an entrance examination?</h3><p>Yes, for Senior KG onwards. Submit the completed form on the day of the exam.</p>
      <h3>Where do I get the application form?</h3><p>At the school office, on payment.</p>
      <h3>Where is the school?</h3><p>KSR Kalvi Nagar, Tiruchengode, Tamil Nadu 637215.</p>
      <h3>Do you offer transport and a hostel?</h3><p>Yes. GPS-tracked buses cover a 25 km radius, and the hostel offers five-day and full-time boarding for boys and girls.</p>
    </div>
    <p style="margin-top:1.25rem">Comparing schools? Read our <a href="{href(r, "parent-guide")}">guide to choosing a CBSE school in Tiruchengode</a>.</p>
  </div>
  <div class="reveal" style="position:sticky;top:100px">{enquiry_form()}</div>
</div></section>"""
