// KSR Akshara Academy - site interactions (no dependencies)
(() => {
  const root = document.documentElement;

  // Theme toggle (remembered per browser)
  const setIcon = () => {
    const dark = root.dataset.theme === "dark" ||
      (!root.dataset.theme && matchMedia("(prefers-color-scheme: dark)").matches);
    document.querySelectorAll("[data-theme-toggle] i").forEach(i => {
      i.className = dark ? "ph ph-sun" : "ph ph-moon";
    });
  };
  try { const t = localStorage.getItem("ksr-theme"); if (t) root.dataset.theme = t; } catch (e) {}
  setIcon();
  document.querySelectorAll("[data-theme-toggle]").forEach(b => b.addEventListener("click", () => {
    const dark = root.dataset.theme === "dark" ||
      (!root.dataset.theme && matchMedia("(prefers-color-scheme: dark)").matches);
    root.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("ksr-theme", root.dataset.theme); } catch (e) {}
    setIcon();
  }));

  // Header border once the page has scrolled (sentinel, no scroll listener)
  const header = document.querySelector(".site-header");
  const sentinel = document.createElement("div");
  sentinel.style.cssText = "position:absolute;top:0;height:1px;width:1px";
  document.body.prepend(sentinel);
  new IntersectionObserver(([e]) => header && header.classList.toggle("is-scrolled", !e.isIntersecting)).observe(sentinel);

  // Full menu whenever it fits; the menu button only when it would overflow
  const nav = header && header.querySelector(".nav");
  const fitNav = () => {
    header.classList.remove("nav-compact");
    if (nav.scrollWidth > nav.clientWidth + 1) header.classList.add("nav-compact");
  };
  if (nav) {
    fitNav();
    addEventListener("resize", fitNav);
    document.fonts && document.fonts.ready.then(fitNav);
  }

  // Mobile drawer
  const drawer = document.querySelector(".drawer");
  const openers = document.querySelectorAll("[data-drawer-open]");
  const closeDrawer = () => { drawer.classList.remove("open"); document.body.style.overflow = ""; };
  openers.forEach(b => b.addEventListener("click", () => {
    drawer.classList.add("open"); document.body.style.overflow = "hidden";
    drawer.querySelector("[data-drawer-close]").focus();
  }));
  drawer && drawer.querySelectorAll("[data-drawer-close], .drawer-scrim").forEach(el => el.addEventListener("click", closeDrawer));
  document.addEventListener("keydown", e => { if (e.key === "Escape" && drawer) closeDrawer(); });

  // Scroll reveal
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const reveals = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach(el => el.classList.add("in"));
  } else {
    const io = new IntersectionObserver(entries => entries.forEach(en => {
      if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
    }), { rootMargin: "0px 0px -8% 0px", threshold: .08 });
    reveals.forEach(el => io.observe(el));
  }

  // Stage tabs (keyboard accessible)
  document.querySelectorAll("[data-tabs]").forEach(group => {
    const tabs = [...group.querySelectorAll('[role="tab"]')];
    const select = tab => {
      tabs.forEach(t => {
        const on = t === tab;
        t.setAttribute("aria-selected", on);
        t.tabIndex = on ? 0 : -1;
        const panel = document.getElementById(t.getAttribute("aria-controls"));
        panel.hidden = !on;
        if (on) { panel.classList.remove("is-in"); void panel.offsetWidth; panel.classList.add("is-in"); }
      });
    };
    tabs.forEach((t, i) => {
      t.addEventListener("click", () => select(t));
      t.addEventListener("keydown", e => {
        const d = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[e.key];
        if (d) { e.preventDefault(); const n = tabs[(i + d + tabs.length) % tabs.length]; n.focus(); select(n); }
      });
    });
  });

  // Carousel buttons
  document.querySelectorAll("[data-carousel]").forEach(wrap => {
    const track = wrap.querySelector(".carousel");
    wrap.querySelectorAll("[data-dir]").forEach(b => b.addEventListener("click", () => {
      const card = track.firstElementChild;
      const step = card ? card.getBoundingClientRect().width + 16 : 320;
      track.scrollBy({ left: step * Number(b.dataset.dir), behavior: reduce ? "auto" : "smooth" });
    }));
  });

  // Click-to-load YouTube film (no third-party cost until asked)
  document.querySelectorAll("[data-yt]").forEach(btn => btn.addEventListener("click", () => {
    const box = btn.closest(".film");
    const f = document.createElement("iframe");
    f.src = `https://www.youtube-nocookie.com/embed/${btn.dataset.yt}?autoplay=1&rel=0`;
    f.title = "KSR Akshara Academy campus film";
    f.allow = "autoplay; encrypted-media; picture-in-picture";
    f.allowFullscreen = true;
    box.innerHTML = ""; box.appendChild(f);
  }));

  // Active chip in sticky page TOC
  const toc = document.querySelector(".toc");
  if (toc) {
    // fade whichever edge still hides chips
    const edges = () => {
      toc.classList.toggle("more-l", toc.scrollLeft > 4);
      toc.classList.toggle("more-r", toc.scrollLeft + toc.clientWidth < toc.scrollWidth - 4);
    };
    toc.addEventListener("scroll", edges, { passive: true });
    addEventListener("resize", edges);
    edges();
  }
  if (toc && "IntersectionObserver" in window) {
    const links = [...toc.querySelectorAll("a")];
    const io = new IntersectionObserver(entries => entries.forEach(en => {
      if (en.isIntersecting) {
        links.forEach(l => l.classList.toggle("is-active", l.hash === "#" + en.target.id));
        // keep the active chip in view; scrollTo moves only the strip, never the page
        const on = links.find(l => l.hash === "#" + en.target.id);
        if (on && (on.offsetLeft < toc.scrollLeft || on.offsetLeft + on.offsetWidth > toc.scrollLeft + toc.clientWidth))
          toc.scrollTo({ left: on.offsetLeft - 16, behavior: reduce ? "auto" : "smooth" });
      }
    }), { rootMargin: "-40% 0px -55% 0px" });
    links.forEach(l => { const s = document.querySelector(l.hash); s && io.observe(s); });
  }

  // Date picker: a styled calendar on mouse devices; touch keeps the phone's own picker
  if (matchMedia("(pointer: fine)").matches) document.querySelectorAll('.field input[type="date"]').forEach(input => {
    const MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const today = new Date(); today.setHours(0, 0, 0, 0);
    const iso = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
    const wrap = document.createElement("div");
    wrap.className = "datefield";
    input.replaceWith(wrap);
    // the form submits the ISO date; the visible box shows a readable one
    const value = document.createElement("input");
    value.type = "hidden"; value.name = input.name || input.id;
    input.removeAttribute("name");
    input.type = "text"; input.inputMode = "none"; input.autocomplete = "off"; input.placeholder = "Select a date";
    input.setAttribute("aria-haspopup", "dialog");
    const cal = document.createElement("div");
    cal.className = "cal"; cal.hidden = true; cal.setAttribute("role", "dialog"); cal.setAttribute("aria-label", "Choose a date");
    const icon = document.createElement("i");
    icon.className = "ph ph-calendar-check"; icon.setAttribute("aria-hidden", "true");
    wrap.append(input, icon, value, cal);

    let view = new Date(today.getFullYear(), today.getMonth(), 1), picked = null;
    const render = focusDay => {
      const y = view.getFullYear(), m = view.getMonth();
      const lead = new Date(y, m, 1).getDay(), count = new Date(y, m + 1, 0).getDate();
      const atStart = y === today.getFullYear() && m === today.getMonth();
      let cells = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"].map(d => `<span>${d}</span>`).join("") + "<i></i>".repeat(lead);
      for (let d = 1; d <= count; d++) {
        const day = new Date(y, m, d), key = iso(day);
        cells += `<button type="button" data-day="${key}"${day < today ? " disabled" : ""}${key === iso(today) ? ' class="today"' : ""}` +
                 ` aria-selected="${picked === key}" aria-label="${day.toDateString()}">${d}</button>`;
      }
      cal.innerHTML = `<div class="cal-head"><button type="button" data-step="-1" aria-label="Previous month"${atStart ? " disabled" : ""}><i class="ph ph-arrow-left"></i></button>` +
        `<strong aria-live="polite">${MONTHS[m]} ${y}</strong><button type="button" data-step="1" aria-label="Next month"><i class="ph ph-arrow-right"></i></button></div>` +
        `<div class="cal-grid">${cells}</div>`;
      if (focusDay) (cal.querySelector(`[data-day="${focusDay}"]:not(:disabled)`) || cal.querySelector("[data-day]:not(:disabled)")).focus();
    };
    const open = () => { if (!cal.hidden) return; render(); cal.hidden = false; input.setAttribute("aria-expanded", "true"); };
    const close = refocus => { cal.hidden = true; input.setAttribute("aria-expanded", "false"); refocus && input.focus(); };
    const choose = key => {
      picked = key; value.value = key;
      const [y, m, d] = key.split("-").map(Number);
      input.value = new Date(y, m - 1, d).toLocaleDateString("en-GB", { weekday: "short", day: "numeric", month: "short", year: "numeric" });
      close(true);
      input.dispatchEvent(new Event("input", { bubbles: true }));
    };
    input.addEventListener("click", open);
    input.addEventListener("keydown", e => {
      if (["Enter", " ", "ArrowDown"].includes(e.key)) { e.preventDefault(); open(); render(picked || iso(today)); }
      else if (e.key === "Escape") close();
      else if (e.key !== "Tab") e.preventDefault();
    });
    cal.addEventListener("click", e => {
      const step = e.target.closest("[data-step]"), day = e.target.closest("[data-day]");
      if (step && !step.disabled) { view.setMonth(view.getMonth() + Number(step.dataset.step)); render(); }
      else if (day && !day.disabled) choose(day.dataset.day);
    });
    cal.addEventListener("keydown", e => {
      const day = e.target.closest("[data-day]");
      if (e.key === "Escape") { e.stopPropagation(); close(true); return; }
      const move = { ArrowLeft: -1, ArrowRight: 1, ArrowUp: -7, ArrowDown: 7 }[e.key];
      if (!day || !move) return;
      e.preventDefault();
      const [y, m, d] = day.dataset.day.split("-").map(Number), next = new Date(y, m - 1, d + move);
      if (next < today) return;
      if (next.getMonth() !== view.getMonth()) view = new Date(next.getFullYear(), next.getMonth(), 1);
      render(iso(next));
    });
    document.addEventListener("click", e => { if (!wrap.contains(e.target)) close(); });
  });

  // Forms: inline validation + success state (demo, not connected to a backend)
  document.querySelectorAll("form[data-demo]").forEach(form => {
    const validate = field => {
      const input = field.querySelector("input, select, textarea");
      if (!input) return true;
      let ok = input.checkValidity();
      if (ok && input.type === "tel") ok = /^[6-9]\d{9}$/.test(input.value.replace(/[\s+-]/g, "").replace(/^91/, ""));
      field.classList.toggle("invalid", !ok);
      input.setAttribute("aria-invalid", !ok);
      return ok;
    };
    form.querySelectorAll(".field").forEach(f => {
      const input = f.querySelector("input, select, textarea");
      input && input.addEventListener("blur", () => { if (input.value) validate(f); });
      input && input.addEventListener("input", () => f.classList.contains("invalid") && validate(f));
    });
    form.addEventListener("submit", e => {
      e.preventDefault();
      const fields = [...form.querySelectorAll(".field")];
      const bad = fields.filter(f => !validate(f));
      if (bad.length) { bad[0].querySelector("input, select, textarea").focus(); return; }
      const btn = form.querySelector('button[type="submit"]');
      btn.classList.add("is-loading"); btn.lastChild.textContent = " Sending";
      setTimeout(() => form.classList.add("is-sent"), 900);
    });
  });
})();

// Akshara tree: wind in the leaves, hover lifts a leaf, tap opens its story
(() => {
  const svg = document.querySelector(".tree-svg");
  if (!svg) return;
  const hero = svg.closest("[data-tree]");
  // "full": the tree page; "mini": the homepage, where a leaf opens it on the tree page
  const mini = hero.dataset.tree === "mini";
  const data = JSON.parse(document.getElementById("tree-data").textContent);
  const stage = svg.closest(".tree-stage");
  const tip = stage.querySelector(".tree-tip");
  const card = hero.querySelector(".tree-card");
  const cardIn = card && card.querySelector(".tree-card-in");
  const chips = [...hero.querySelectorAll(".leaf-chips button")];
  const leaves = [...svg.querySelectorAll(".leaf")];
  const order = leaves.map(l => l.dataset.key);
  const liftHover = svg.querySelector(".lift-hover");
  const liftSel = svg.querySelector(".lift-sel");
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const canHover = matchMedia("(hover: hover)").matches;
  let active = null, hovered = null;

  // ---------------------------------------------------------------- lifted copies
  // Hover and selection show a copy of the leaf (a <use>) in the top layer, so the
  // leaves themselves are never re-ordered or re-animated.
  const liftTrunk = svg.querySelector(".lift-trunk");  // sits under the crown, like the trunk itself
  const follow = new Map();  // lifted copy -> leaf key whose wind it should follow
  const copyFor = (leaf, sel) => leaf.dataset.key === "trunk" ? liftTrunk : (sel ? liftSel : liftHover);
  const show = (use, leaf) => {
    use.classList.remove("on");
    use.setAttribute("href", "#lv-" + leaf.dataset.key);
    ["--dx", "--dy"].forEach(p => use.style.setProperty(p, leaf.style.getPropertyValue(p)));
    const sel = use.classList.contains("lift-sel");
    if (sel) use.style.removeProperty("--fill");  // the selected look comes from CSS
    else use.style.setProperty("--fill", getComputedStyle(leaf).getPropertyValue("--fill"));
    use.style.transformOrigin = leaf.style.transformOrigin;
    use.setAttribute("filter", sel ? "url(#lift-sel)" : "url(#lift-hover)");
    follow.set(use, leaf.dataset.key);
    void use.getBoundingClientRect();
    use.classList.add("on");
  };
  const hide = use => {
    use.classList.remove("on"); use.removeAttribute("filter"); follow.delete(use); use.parentNode.removeAttribute("transform");
    if (use === liftTrunk) use.classList.remove("lift-sel");
  };

  const raise = leaf => {
    if (leaf === active || leaf === hovered) return;
    hovered = leaf; show(copyFor(leaf, false), leaf);
  };
  const lower = leaf => { if (hovered === leaf) { hovered = null; if (leaf !== active) hide(copyFor(leaf, false)); } };

  leaves.forEach(leaf => {
    leaf.addEventListener("pointerenter", () => {
      raise(leaf);
      if (canHover) { tip.textContent = data[leaf.dataset.key].title; tip.classList.add("show"); }
    });
    leaf.addEventListener("pointerleave", () => { lower(leaf); tip.classList.remove("show"); });
    leaf.addEventListener("pointermove", e => {
      if (!canHover) return;
      const r = stage.getBoundingClientRect();
      tip.style.left = (e.clientX - r.left) + "px"; tip.style.top = (e.clientY - r.top) + "px";
    });
    leaf.addEventListener("focus", () => raise(leaf));
    leaf.addEventListener("blur", () => lower(leaf));
    leaf.addEventListener("click", () => select(leaf.dataset.key, true));
    leaf.addEventListener("keydown", e => {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); select(leaf.dataset.key, false); }
      const d = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
      if (d) { e.preventDefault(); const n = leaves[(order.indexOf(leaf.dataset.key) + d + leaves.length) % leaves.length]; n.focus(); select(n.dataset.key, false); }
    });
  });
  chips.forEach(c => c.addEventListener("click", () => select(c.dataset.key, false)));
  card && card.querySelector(".tree-close").addEventListener("click", deselect);
  document.addEventListener("keydown", e => { if (e.key === "Escape" && active) deselect(); });

  function select(key, fromPointer) {
    const d = data[key]; if (!d) return;
    if (mini) { location.href = hero.dataset.link + "#" + key; return; }
    const leaf = leaves.find(l => l.dataset.key === key);
    if (active && active !== leaf) hide(copyFor(active, true));
    if (hovered === leaf) { hovered = null; if (key !== "trunk") hide(liftHover); }
    leaves.forEach(l => l.classList.toggle("is-active", l === leaf));
    active = leaf;
    const use = copyFor(leaf, true);
    use.classList.add("lift-sel");
    show(use, leaf);
    chips.forEach(c => c.setAttribute("aria-pressed", c.dataset.key === key));
    const chip = chips.find(c => c.dataset.key === key);
    chip && chip.classList.add("seen");
    chip && chip.scrollIntoView({ block: "nearest", inline: "center", behavior: reduce ? "auto" : "smooth" });
    tip.classList.remove("show");
    history.replaceState(null, "", "#" + key);
    const visual = d.img
      ? `<figure><img src="${d.img}" alt="${d.alt}"></figure>`
      : `<figure><div class="icon-hero"><i class="ph ${d.icon}"></i></div></figure>`;
    cardIn.innerHTML = `${visual}<div class="body">
      <span class="kicker"><i class="ph ${d.icon}"></i>${d.kicker}</span>
      <h2>${d.title}</h2><p>${d.text}</p>
      <a class="link-arrow" href="${d.href}">${d.cta} <i class="ph ph-arrow-right"></i></a></div>`;
    card.hidden = false;
    card.classList.remove("swap"); void card.offsetWidth; card.classList.add("swap", "open");
    gust(1);  // a small rustle when a leaf is chosen
  }

  function deselect() {
    if (active) hide(copyFor(active, true));
    active = null;
    leaves.forEach(l => l.classList.remove("is-active"));
    chips.forEach(c => c.setAttribute("aria-pressed", "false"));
    card && card.classList.remove("open");
    history.replaceState(null, "", location.pathname);
  }

  // ---------------------------------------------------------------- grow in (once)
  // Leaves are fully visible by default, so if this never runs nothing is hidden.
  if (!reduce && document.visibilityState === "visible" && svg.animate) {
    svg.querySelectorAll(".leaf-in, .trunk-in").forEach(g => {
      const i = Number(g.closest(".leaf").style.getPropertyValue("--i")) || 0;
      const trunk = g.classList.contains("trunk-in");
      g.animate(trunk
        ? [{ transform: "translateY(24px)", opacity: 0 }, { transform: "none", opacity: 1 }]
        : [{ transform: "scale(.2)", opacity: 0 }, { opacity: 1, offset: .5 }, { transform: "none", opacity: 1 }],
        { duration: trunk ? 600 : 750, delay: trunk ? 0 : 200 + i * 55, easing: "cubic-bezier(.34, 1.4, .64, 1)", fill: "backwards" });
    });
  }

  const initial = decodeURIComponent(location.hash.slice(1));
  if (!mini && data[initial]) setTimeout(() => select(initial, false), reduce ? 0 : 1100);

  // ---------------------------------------------------------------- wind
  // Transforms are written as SVG attributes each frame (no CSS keyframes on SVG
  // groups), and the <use> copies follow automatically because they mirror the leaf.
  const toggle = hero.querySelector(".wind-toggle");
  let windOn = !reduce;
  if (!windOn && toggle) { toggle.setAttribute("aria-pressed", "false"); toggle.setAttribute("aria-label", "Start the wind"); }
  toggle && toggle.addEventListener("click", () => {
    windOn = !windOn;
    toggle.setAttribute("aria-pressed", windOn);
    toggle.setAttribute("aria-label", windOn ? "Pause the wind" : "Start the wind");
    if (windOn) start(); else rest();
  });

  const canopy = svg.querySelector(".canopy");
  const liftLayer = svg.querySelector(".lift-layer");
  const trunkWind = svg.querySelector(".trunk-wind");
  const swayX = Number(hero.dataset.swayX), swayY = Number(hero.dataset.swayY);
  const winds = [...svg.querySelectorAll(".wind")].map((g, i) => ({
    g, key: (g.closest(".leaf") || {}).dataset?.key, px: +g.dataset.px, py: +g.dataset.py, tf: "",
    flex: Math.min(1, +g.dataset.reach / 120),    // longer leaves bend more
    f: .9 + (i * 37 % 10) / 14, ph: i * 1.7, kick: 0,
  }));

  const byKey = Object.fromEntries(winds.filter(w => w.key).map(w => [w.key, w]));
  let trunkTf = "";
  let strength = .35, target = .35, nextGust = 0, t = 0, last = 0, raf = 0, visible = true;
  const gust = (amount = .6 + Math.random() * .4) => { target = amount; nextGust = t + 1.6 + Math.random() * 1.4; };

  // pointer breeze: leaves near a moving pointer get a push
  let pointer = null;
  stage.addEventListener("pointermove", e => {
    const p = svg.createSVGPoint(); p.x = e.clientX; p.y = e.clientY;
    const q = p.matrixTransform(svg.getScreenCTM().inverse());
    if (pointer) {
      const v = Math.min(Math.hypot(q.x - pointer.x, q.y - pointer.y), 30);
      winds.forEach(w => { const d = Math.hypot(w.px - q.x, w.py - q.y); if (d < 180) w.kick = Math.min(w.kick + v * (1 - d / 180) * .12, 4); });
    }
    pointer = q;
  });
  stage.addEventListener("pointerleave", () => { pointer = null; });

  // a soft light follows the pointer across the stage (a plain layer, moved with a transform)
  const spot = hero.querySelector(".tree-spot");
  if (spot && canHover && !reduce) {
    hero.addEventListener("pointermove", e => {
      const r = hero.getBoundingClientRect();
      spot.style.transform = `translate(${e.clientX - r.left}px, ${e.clientY - r.top}px)`;
      hero.classList.add("lit");
    });
    hero.addEventListener("pointerleave", () => hero.classList.remove("lit"));
  }

  // drifting leaves and wind streaks on a canvas behind the cards
  const canvas = hero.querySelector(".wind-canvas");
  const ctx = canvas ? canvas.getContext("2d") : null;
  const blues = ["#2b8fd6", "#0b6fb5", "#4fa9e6", "#0a5d98", "#7cc0ef"];
  let W = 0, H = 0, dpr = 1, drift = [], streaks = [];
  const size = () => {
    if (!ctx) return;
    dpr = Math.min(devicePixelRatio || 1, 1.5);
    W = hero.clientWidth; H = hero.clientHeight;
    canvas.width = W * dpr; canvas.height = H * dpr;
    const n = Math.round(Math.min(22, W / 60));
    drift = Array.from({ length: n }, () => ({
      x: Math.random() * W, y: Math.random() * H, s: 5 + Math.random() * 8, r: Math.random() * 6.28,
      vr: (Math.random() - .5) * 2, bob: Math.random() * 6.28, c: blues[Math.random() * blues.length | 0], a: .35 + Math.random() * .45,
    }));
  };
  new ResizeObserver(size).observe(hero);

  function drawLeaf(p) {
    ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.r); ctx.globalAlpha = p.a; ctx.fillStyle = p.c;
    ctx.beginPath(); ctx.moveTo(-p.s, 0);
    ctx.quadraticCurveTo(0, -p.s * .8, p.s, 0); ctx.quadraticCurveTo(0, p.s * .8, -p.s, 0);
    ctx.fill(); ctx.restore();
  }

  function frame(now) {
    raf = requestAnimationFrame(frame);
    const dt = Math.min((now - last) / 1000 || 0, .05); last = now; t += dt;
    if (t > nextGust) Math.random() < .5 ? gust() : (target = .2 + Math.random() * .2, nextGust = t + 2 + Math.random() * 3);
    strength += (target - strength) * Math.min(dt * 1.2, 1);

    // the crown leans with the wind; the trunk bends to follow
    const lean = strength * (1.1 * Math.sin(t * .8) + .5 * Math.sin(t * 1.9 + 1)) + strength * .6;
    const sway = `rotate(${lean.toFixed(3)} ${swayX} ${swayY})`;
    canopy.setAttribute("transform", sway);
    liftLayer.setAttribute("transform", sway);
    const k = Math.tan(-lean * Math.PI / 180);
    trunkTf = `matrix(1 0 ${k.toFixed(4)} 1 ${(-k * swayY).toFixed(2)} 0)`;
    trunkWind.setAttribute("transform", trunkTf);

    // every leaf rustles on its own rhythm
    winds.forEach(w => {
      w.kick *= Math.pow(.2, dt);
      const a = (strength * 3.2 + w.kick) * w.flex * (Math.sin(t * w.f * 2.6 + w.ph) * .7 + Math.sin(t * w.f * 5.3 + w.ph * 2) * .3);
      w.tf = `rotate(${a.toFixed(3)} ${w.px} ${w.py})`;
      w.g.setAttribute("transform", w.tf);
    });
    // lifted copies mirror a still leaf, so give them that leaf's wind on their wrapper
    follow.forEach((key, use) => { const tf = key === "trunk" ? trunkTf : (byKey[key] || {}).tf; tf && use.parentNode.setAttribute("transform", tf); });

    // drifting leaves and streaks
    if (!ctx) return;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    const speed = 30 + strength * 190;
    if (strength > .55 && Math.random() < dt * 3 && streaks.length < 7) {
      streaks.push({ x: -200, y: H * (.15 + Math.random() * .7), len: 120 + Math.random() * 180, life: 0, amp: 8 + Math.random() * 14 });
    }
    ctx.lineCap = "round";
    streaks = streaks.filter(s => {
      s.x += speed * 3.2 * dt; s.life += dt;
      const alpha = Math.max(0, Math.min(1, s.life * 2) * (1 - s.x / (W + 200))) * .35;
      ctx.strokeStyle = `rgba(74, 163, 232, ${alpha})`; ctx.lineWidth = 1.6;
      ctx.beginPath();
      for (let i = 0; i <= 12; i++) {
        const x = s.x + (i / 12) * s.len, y = s.y + Math.sin((x / 90) + t * 2) * s.amp;
        i ? ctx.lineTo(x, y) : ctx.moveTo(x, y);
      }
      ctx.stroke();
      return s.x < W + 50;
    });
    drift.forEach(p => {
      p.bob += dt * 1.6;
      p.x += (speed + p.s * 6) * dt;
      p.y += Math.sin(p.bob) * 22 * dt + 6 * dt;
      p.r += (p.vr + strength * 2) * dt;
      if (p.x > W + 20) { p.x = -20; p.y = Math.random() * H; }
      if (p.y > H + 20) p.y = -20;
      drawLeaf(p);
    });
  }

  function start() { if (!raf && windOn && visible) { last = performance.now(); raf = requestAnimationFrame(frame); } }
  function rest() {
    cancelAnimationFrame(raf); raf = 0;
    if (windOn) return;
    // wind switched off: let everything settle straight
    canopy.removeAttribute("transform"); liftLayer.removeAttribute("transform"); trunkWind.removeAttribute("transform");
    winds.forEach(w => { w.g.removeAttribute("transform"); w.tf = ""; });
    follow.forEach((key, use) => use.parentNode.removeAttribute("transform"));
    ctx && ctx.clearRect(0, 0, canvas.width, canvas.height);
  }
  // only animate while the tree is on screen
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; visible ? start() : rest(); }).observe(hero);
  size();
  if (windOn) setTimeout(start, reduce ? 0 : 900);
})();
