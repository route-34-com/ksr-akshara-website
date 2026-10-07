// KSR Akshara Academy - "cosmos" version: starfield, edge light, tilt and count-up (no dependencies)
(() => {
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fine = matchMedia("(pointer: fine)").matches;

  // Starfield: three depths of stars that drift with the page and twinkle, plus a rare shooting star.
  // Plain 2D canvas, capped pixel ratio, paused when the tab is hidden.
  const canvas = document.querySelector(".starfield");
  if (canvas) {
    const ctx = canvas.getContext("2d");
    const dpr = Math.min(devicePixelRatio || 1, 1.5);
    let w = 0, h = 0, stars = [], shot = null, nextShot = performance.now() + 4000, running = true;
    const resize = () => {
      w = innerWidth; h = innerHeight;
      canvas.width = w * dpr; canvas.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const n = Math.min(420, Math.round(w * h / 4200));
      stars = Array.from({ length: n }, () => {
        const z = Math.random();                       // depth: 0 far, 1 near
        return { x: Math.random() * w, y: Math.random() * h, z, r: .35 + z * 1.1, p: Math.random() * 6.28, s: .6 + Math.random() * 1.6,
                 c: Math.random() < .12 ? "255,214,204" : Math.random() < .5 ? "190,225,255" : "255,255,255" };
      });
    };
    const draw = t => {
      ctx.clearRect(0, 0, w, h);
      const sy = scrollY;
      for (const s of stars) {
        const y = ((s.y - sy * (.04 + s.z * .22)) % h + h) % h;   // nearer stars move faster with scroll
        const a = reduce ? .7 : .45 + .55 * Math.abs(Math.sin(s.p + t * .001 * s.s));
        ctx.fillStyle = `rgba(${s.c},${(a * (.35 + s.z * .65)).toFixed(3)})`;
        ctx.beginPath(); ctx.arc(s.x, y, s.r, 0, 6.283); ctx.fill();
      }
      if (!reduce) {
        if (!shot && t > nextShot) { shot = { x: Math.random() * w * .7 + w * .2, y: Math.random() * h * .35, life: 0 }; }
        if (shot) {
          shot.life += 16; const k = shot.life / 900, x = shot.x - k * 420, y = shot.y + k * 180;
          const g = ctx.createLinearGradient(x, y, x + 120, y - 52);
          g.addColorStop(0, `rgba(220,240,255,${(1 - k).toFixed(2)})`); g.addColorStop(1, "rgba(220,240,255,0)");
          ctx.strokeStyle = g; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + 120, y - 52); ctx.stroke();
          if (k >= 1) { shot = null; nextShot = t + 6000 + Math.random() * 7000; }
        }
      }
    };
    const loop = t => { if (!running) return; draw(t); requestAnimationFrame(loop); };
    resize(); addEventListener("resize", resize);
    if (reduce) draw(0);
    else {
      requestAnimationFrame(loop);
      document.addEventListener("visibilitychange", () => { running = !document.hidden; if (running) requestAnimationFrame(loop); });
    }
  }

  // Edge light: every glass panel's border brightens where the pointer is
  if (fine) {
    const lit = ".section > .wrap, .page-head > .wrap, .tile, .site-footer > .wrap, .form-card, .cta-band, .news-card, .quote, .stage-tab";
    document.addEventListener("pointermove", e => {
      const el = e.target.closest && e.target.closest(lit);
      if (el) { const b = el.getBoundingClientRect(); el.style.setProperty("--mx", `${e.clientX - b.left}px`); el.style.setProperty("--my", `${e.clientY - b.top}px`); }
      // the panel around a tile lights too
      const outer = el && el.parentElement && el.parentElement.closest(lit);
      if (outer) { const b = outer.getBoundingClientRect(); outer.style.setProperty("--mx", `${e.clientX - b.left}px`); outer.style.setProperty("--my", `${e.clientY - b.top}px`); }
    }, { passive: true });
  }

  // Photo tiles lean toward the pointer
  if (fine && !reduce) {
    document.querySelectorAll(".bento .tile.photo").forEach(t => {
      t.addEventListener("pointermove", e => {
        const b = t.getBoundingClientRect(), x = (e.clientX - b.left) / b.width - .5, y = (e.clientY - b.top) / b.height - .5;
        t.style.setProperty("--ry", `${(x * 7).toFixed(2)}deg`); t.style.setProperty("--rx", `${(-y * 7).toFixed(2)}deg`);
      });
      t.addEventListener("pointerleave", () => { t.style.setProperty("--ry", "0deg"); t.style.setProperty("--rx", "0deg"); });
    });
  }

  // Telemetry numbers count up once they come into view
  const counters = document.querySelectorAll("[data-count]");
  if (counters.length && !reduce && "IntersectionObserver" in window) {
    const fmt = n => n.toLocaleString("en-IN");
    const io = new IntersectionObserver(entries => entries.forEach(en => {
      if (!en.isIntersecting) return;
      io.unobserve(en.target);
      const el = en.target, end = +el.dataset.count, suf = el.dataset.suffix || "", t0 = performance.now(), dur = 1600;
      const step = t => { const k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 4);
        el.textContent = fmt(Math.round(end * e)) + suf; if (k < 1) requestAnimationFrame(step); };
      el.textContent = "0" + suf; requestAnimationFrame(step);
    }), { threshold: .6 });
    counters.forEach(c => io.observe(c));
  }
})();
