"""Testimonials page."""
from ..components import cta_band, page_head

def testimonials(r):
    img = lambda n: f"{r}assets/img/{n}"
    guests = [("Prof. Dr. Robert Huber", "Nobel Laureate in Chemistry, 1988", "professor.jpg", "I very much hope to see many chemists coming from this school."),
              ("Prof. Hartmut Michel", "Nobel Laureate in Chemistry, 1988", "Hartmut-Michel.jpg", "I am deeply impressed. I do wish you success. Take your chance."),
              ("C.K. Kumaravel", "CEO and co-founder, Naturals salon chain", "Kumaravel.jpg", "Your dreams, your signature. Make sure the entire world knows it. Together let us build a beautiful world."),
              ("Madhampatty Rangaraj", "Chairman, Madhampatty Thangavelu Hospitality", "Madhampatty-rangaraj.jpg", "I can feel a very energetic vibe overall with the students. Wonderful programme."),
              ("Jaikumar Christhu Rajan", "Director, St. Joseph's College of Engineering, Chennai", "jaikumar.jpg", "Amazing children. Amazing infrastructure. Looking forward to more laurels from the school."),
              ("Dr. Saranya Jaikumar", "Educational Psychologist, SCPCR", "saranya-jaikumar.jpg", "Had an amazing time speaking with higher secondary girls on safety and the prevention of abuse.")]
    parents = [("K. Kumar", "Parent of Nithin Rohit", "Kumar-120x120.jpg", "IIT Jodhpur", "The JEE training programme was truly amazing. My son completed Grade XII here and now studies Electrical Engineering at IIT Jodhpur."),
               ("Vanitha Srinivasan", "Parent of Kanimozhi and Kayalvizhi", "Vanitha-srinivasan.jpg", "Madras and Vellore Medical Colleges", "My twins moved from Matric to Akshara for Classes XI and XII. With excellent NEET coaching and follow-up, both got into medical college."),
              ("Dr. Sengottuvel and Dr. Sathyabama", "Parents of Mithira Prathiksa and Samrutha Sree", "dr.Sengottuvel-Sathyabama-120x120.jpg", None, "Value-education classes have encouraged logical and critical thinking. When she faces a practical problem, she applies what she learnt."),
              ("S. Chitra", "Mother of A.S. Anmithashree", "Chitra-120x120.jpg", None, "Skill competency activities and house competitions have visibly increased her confidence and her ability to face challenges."),
              ("Ishwarya Dhanasekaran", "Mother of Samantha, Grade 7", "Ishwaraya-120x120.jpg", None, "The teachers are dedicated, caring and truly invested. The individual attention has helped my child make great strides.")]
    q = lambda n, role, p, text, res=None: (f'<figure class="quote reveal">' + (f'<span class="result"><i class="ph ph-graduation-cap"></i>{res}</span>' if res else "")
        + f'<blockquote>&ldquo;{text}&rdquo;</blockquote><figcaption><img src="{img(p)}" alt="" loading="lazy"><div><strong>{n}</strong><span>{role}</span></div></figcaption></figure>')
    return page_head(r, [("Testimonials", None)], "In their words.",
                     "Nobel laureates, industry leaders and Akshara parents on what they have seen at the school.") + f"""
<section class="section" style="padding-top:36px"><div class="wrap">
  <h2 class="reveal">Parents</h2>
  <div class="grid-auto" style="margin-top:1.75rem;grid-template-columns:repeat(auto-fill,minmax(min(320px,100%),1fr))">{"".join(q(n, ro, p, t, res) for n, ro, p, res, t in parents)}</div>
  <h2 class="reveal" style="margin-top:4rem">Guests</h2>
  <div class="grid-auto" style="margin-top:1.75rem;grid-template-columns:repeat(auto-fill,minmax(min(320px,100%),1fr))">{"".join(q(n, ro, p, t) for n, ro, p, t in guests)}</div>
</div></section>""" + cta_band(r)
