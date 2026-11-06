"""Building blocks shared by several pages."""
from .config import PHONE_1, TEL_1
from .layout import href

def page_head(r, crumbs, h1, lede, banner=None, alt=""):
    c = f'<li><a href="{href(r, "")}">Home</a></li>' + "".join(
        f'<li><a href="{href(r, s)}">{t}</a></li>' if s else f'<li aria-current="page">{t}</li>' for t, s in crumbs)
    b = f'<figure class="page-banner reveal" style="margin-left:0;margin-right:0"><img src="{r}assets/img/{banner}" alt="{alt}"></figure>' if banner else ""
    return f"""<section class="page-head"><div class="wrap">
<nav aria-label="Breadcrumb"><ol class="crumbs">{c}</ol></nav>
<h1>{h1}</h1><p class="lede">{lede}</p>{b}</div></section>"""


def cta_band(r, h="Visit the campus before you decide.", p="Walk the classrooms, labs, library and turf with our admissions team. Admissions open every year from Vijayadasami to March."):
    return f"""<section class="section"><div class="wrap"><div class="cta-band reveal">
<div><h2>{h}</h2><p>{p}</p></div>
<div class="actions"><a class="btn btn-primary" href="{href(r, "admission")}">Admissions enquiry</a>
<a class="btn btn-ghost" href="tel:{TEL_1}"><i class="ph ph-phone"></i>Call {PHONE_1}</a></div>
</div></div></section>"""


def enquiry_form(title="Admissions enquiry", sub="Share a few details and our admissions office will call you back."):
    grades = "".join(f"<option>{g}</option>" for g in
                     ["Pre-KG", "Junior KG", "Senior KG"] + [f"Grade {n}" for n in
                     ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]])
    return f"""<form class="form-card" data-demo novalidate>
<h3>{title}</h3><p class="muted" style="margin-top:.4rem">{sub}</p>
<div class="form-grid">
  <div class="field"><label for="sn">Student name</label><input id="sn" name="student" required autocomplete="off" placeholder="Full name">
    <span class="err">Please enter the student's name.</span></div>
  <div class="form-row">
    <div class="field"><label for="gr">Grade applying for</label><select id="gr" name="grade" required><option value="">Select grade</option>{grades}</select>
      <span class="err">Please choose a grade.</span></div>
    <div class="field"><label for="ph">Parent phone</label><input id="ph" name="phone" type="tel" required inputmode="numeric" placeholder="10-digit mobile">
      <span class="err">Enter a valid 10-digit mobile number.</span></div>
  </div>
  <div class="field"><label for="bd">Boarding preference</label><select id="bd" name="boarding"><option>Day scholar</option><option>Weekly boarding (Mon to Fri)</option><option>Full-time boarding</option></select>
    <span class="help">You can change this later.</span></div>
  <button class="btn btn-primary" type="submit"><i class="ph ph-paper-plane-tilt"></i> Send enquiry</button>
  <p class="note">Demo form for the redesign concept. Not connected yet.</p>
</div>
<div class="form-success" role="status"><i class="ph ph-check-circle"></i><h3>Thank you. Enquiry received.</h3>
<p>Our admissions office will call you within one working day.</p></div>
</form>"""
