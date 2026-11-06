"""Careers page."""
from ..components import page_head

def careers(r):
    return page_head(r, [("Careers", None)], "Build your career at Akshara.",
                     "Are you passionate about teaching? Your skills can build the future of many young minds.",
                     "banner-careers.jpg", "The Akshara teaching staff gathered on campus") + f"""
<section class="section"><div class="wrap split top">
  <div class="stack-lg reveal"><h2>Lead in the classroom.</h2>
    <p class="lede">Akshara is looking for young, energetic, enthusiastic and dedicated teachers who are fluent in English and ready to lead.</p>
    <ul class="checklist"><li><i class="ph ph-chalkboard-teacher"></i>Periodic training in new teaching methods</li>
      <li><i class="ph ph-buildings"></i>Part of a group of 16 KSR institutions</li>
      <li><i class="ph ph-globe-hemisphere-east"></i>Global exposure through the British Council, TED-Ed and MUN</li></ul></div>
  <form class="form-card reveal" data-demo novalidate><h3>Apply to teach</h3>
    <div class="form-grid">
      <div class="form-row"><div class="field"><label for="cn">Name</label><input id="cn" required autocomplete="name"><span class="err">Please enter your name.</span></div>
      <div class="field"><label for="cp">Phone</label><input id="cp" type="tel" required inputmode="numeric" placeholder="10-digit mobile"><span class="err">Enter a valid 10-digit mobile number.</span></div></div>
      <div class="form-row"><div class="field"><label for="ce">Email</label><input id="ce" type="email" required autocomplete="email"><span class="err">Enter a valid email address.</span></div>
      <div class="field"><label for="cl">Location</label><input id="cl" required><span class="err">Please enter your location.</span></div></div>
      <div class="field"><label for="cs">Subject you teach</label><input id="cs" required placeholder="For example, Physics"><span class="err">Please tell us your subject.</span></div>
      <div class="field"><label for="cr">Resume</label><input id="cr" type="file" accept=".pdf,.doc,.docx" required><span class="help">PDF or Word, up to 5 MB.</span><span class="err">Please attach your resume.</span></div>
      <button class="btn btn-primary" type="submit"><i class="ph ph-paper-plane-tilt"></i> Send application</button>
      <p class="note">Demo form for the redesign concept. Not connected yet.</p></div>
    <div class="form-success" role="status"><i class="ph ph-check-circle"></i><h3>Application received.</h3><p>Our HR team will be in touch if there is a match.</p></div></form>
</div></section>"""
