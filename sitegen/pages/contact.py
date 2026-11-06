"""Contact page."""
from ..components import page_head
from ..config import EMAIL, EMAIL_2, MAP, PHONE_1, PHONE_2, TEL_1, TEL_2, WA_LOGO

def contact(r):
    return page_head(r, [("Contact", None)], "We are here to help.",
                     "Call, write or visit. The admissions office is open on all working days.") + f"""
<section class="section" style="padding-top:36px" id="visit"><div class="wrap split top">
  <div class="contact-list reveal">
    <div class="contact-item"><i class="ph ph-map-pin"></i><div><strong>Visit us</strong><span class="muted">KSR Akshara Academy, KSR Kalvi Nagar, Tiruchengode 637 215, Namakkal District, Tamil Nadu</span></div></div>
    <div class="contact-item"><i class="ph ph-phone"></i><div><strong>Call us</strong><a href="tel:{TEL_1}">{PHONE_1}</a> / <a href="tel:{TEL_2}">{PHONE_2}</a></div></div>
    <div class="contact-item"><i class="ph ph-envelope-simple"></i><div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="mailto:{EMAIL_2}">{EMAIL_2}</a></div></div>
    <div class="contact-item"><i>{WA_LOGO}</i><div><strong>WhatsApp</strong><a href="https://wa.me/919894932323">Chat with the admissions office</a></div></div>
  </div>
  <form class="form-card reveal" data-demo novalidate><h2 class="form-title">Book a campus visit</h2>
    <div class="form-grid">
      <div class="form-row"><div class="field"><label for="vn">Your name</label><input id="vn" required autocomplete="name"><span class="err">Please enter your name.</span></div>
      <div class="field"><label for="vp">Phone</label><input id="vp" type="tel" required inputmode="numeric" placeholder="10-digit mobile"><span class="err">Enter a valid 10-digit mobile number.</span></div></div>
      <div class="field"><label for="vd">Preferred date</label><input id="vd" type="date" required><span class="err">Please pick a date.</span></div>
      <div class="field"><label for="vm">Message</label><textarea id="vm" placeholder="Anything we should know before your visit?"></textarea></div>
      <button class="btn btn-primary" type="submit"><i class="ph ph-calendar-check"></i> Request visit</button>
      <p class="note">Demo form for the redesign concept. Not connected yet.</p></div>
    <div class="form-success" role="status"><i class="ph ph-check-circle"></i><h3>Visit requested.</h3><p>We will call to confirm a time.</p></div></form>
</div>
<div class="wrap"><div class="map reveal"><iframe src="{MAP}" loading="lazy" title="Map to KSR Akshara Academy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>"""
