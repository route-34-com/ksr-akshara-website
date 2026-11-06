"""Curriculum and methodology."""
from ..components import cta_band, page_head
from ..layout import href

def methodology(r):
    img = lambda n: f"{r}assets/img/{n}"
    domains = ["Sensory", "Fine motor", "Language", "Social skills", "Emotional", "Self help", "Cognition", "Physical and gross motor"]
    return page_head(r, [("Academics", None)], "Curriculum and methodology.",
                     "The curriculum complies with CBSE expectations and builds skills for an international context. As per the New Education Policy, Akshara's classes are grouped into four stages.") + f"""
<section class="section" style="padding-top:32px"><div class="wrap">
  <nav class="toc" aria-label="Stages"><a href="#foundation">Foundation</a><a href="#preparatory">Preparatory</a><a href="#middle">Middle</a><a href="#secondary">Secondary</a></nav>
  <article class="program" id="foundation"><figure class="reveal"><img src="{img("KSR-children-2.jpg")}" alt="Young learners building with blocks" loading="lazy"></figure>
    <div class="stack reveal"><span class="muted">Pre-KG to Grade II</span><h2>Foundation stage</h2>
    <p class="muted">A holistic, play-based, discovery-based programme that develops every aspect of the child: cognitive, social, emotional, creative and physical. Following NEP ECCE guidance, it prepares children for reading, writing, arithmetic and EVS in a classroom rich in sensory experiences.</p>
    <p style="font-weight:600;margin-top:1.25rem">The Multi-Domain system focuses on eight domains of development:</p>
    <div class="chips">{"".join(f'<span class="chip">{d}</span>' for d in domains)}</div></div></article>
  <article class="program" id="preparatory"><figure class="reveal"><img src="{img("career-banner.jpg")}" alt="A teacher guiding young students at their desks" loading="lazy"></figure>
    <div class="stack reveal"><span class="muted">Grades III to V</span><h2>Preparatory stage</h2>
    <p class="muted">Structured learning experiences support scholastic, interpersonal, cultural and social development. The interdisciplinary, technology-rich curriculum gives students the tools to apply what they learn, and planned skill-building activities help every learner grasp each concept.</p></div></article>
  <article class="program" id="middle"><figure class="reveal"><img src="{img("ATL-school.jpg")}" alt="Students working with a robot in the tinkering lab" loading="lazy"></figure>
    <div class="stack reveal"><span class="muted">Grades VI to VIII</span><h2>Middle stage</h2>
    <p class="muted">An engaging, challenging environment that builds confidence, global understanding and civic responsibility. Teaching is project-based and hands-on, connected to real-world situations.</p>
    <ul class="checklist"><li><i class="ph ph-check-circle"></i>Group discussions, seminars and quizzes</li><li><i class="ph ph-check-circle"></i>E-research and presentations</li><li><i class="ph ph-check-circle"></i>Integrated IIT and NEET foundation begins</li></ul></div></article>
  <article class="program" id="secondary"><figure class="reveal"><img src="{img("KSR-higher.jpg")}" alt="Senior students conducting a chemistry experiment" loading="lazy"></figure>
    <div class="stack reveal"><span class="muted">Grades IX to XII</span><h2>Secondary stage</h2>
    <p class="muted">Preparing students for the most selective colleges and universities in India and abroad. A multidisciplinary system offers a range of subject combinations, with a skill enhancement programme and career guidance to help learners make confident choices.</p>
    <a class="link-arrow" href="{href(r, "life-akshara")}#iit">About the IIT and NEET programme <i class="ph ph-arrow-right"></i></a></div></article>
</div></section>""" + cta_band(r)
