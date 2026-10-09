/* WOHLverde | Seitenlogik ohne externe Bibliotheken */
(function () {
  "use strict";
  var d = document, root = d.documentElement;
  var me = d.currentScript || d.querySelector('script[src*="assets/js/app.js"]');
  var BASE = me ? me.getAttribute("src").replace(/assets\/js\/app\.js.*$/, "") : "/";
  var still = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  root.classList.remove("no-js");

  /* Kopfzeile beim Scrollen, mobile Leiste ausblenden am Seitenende */
  var top = d.querySelector(".top"), mbar = d.querySelector(".mbar"), foot = d.querySelector(".foot");
  function onScroll() {
    var y = window.scrollY || 0;
    if (top) top.classList.toggle("scrolled", y > 30);
    if (mbar && foot) mbar.classList.toggle("hide", foot.getBoundingClientRect().top < window.innerHeight - 40);
  }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  /* Menue */
  var burger = d.querySelector(".burger");
  if (burger) burger.addEventListener("click", function () {
    var open = d.body.classList.toggle("menu-open");
    burger.setAttribute("aria-expanded", open ? "true" : "false");
  });
  d.querySelectorAll(".nav a").forEach(function (a) {
    a.addEventListener("click", function () { d.body.classList.remove("menu-open"); if (burger) burger.setAttribute("aria-expanded", "false"); });
  });
  d.querySelectorAll(".dd > .navbtn").forEach(function (b) {
    b.addEventListener("click", function () {
      var p = b.parentElement, open = p.classList.toggle("open");
      b.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });
  d.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { d.body.classList.remove("menu-open"); d.querySelectorAll(".dd.open").forEach(function (x) { x.classList.remove("open"); }); }
  });

  /* Ueberschrift Wort fuer Wort einblenden */
  d.querySelectorAll("h1.wordsplit").forEach(function (h) {
    var i = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = d.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (t) {
            if (!t) return;
            if (/^\s+$/.test(t)) { frag.appendChild(d.createTextNode(t)); return; }
            var w = d.createElement("span"); w.className = "w";
            var inner = d.createElement("span"); inner.textContent = t; inner.style.animationDelay = (0.08 * i++ + 0.1) + "s";
            w.appendChild(inner); frag.appendChild(w);
          });
          n.parentNode.replaceChild(frag, n);
        } else if (n.nodeType === 1) walk(n);
      });
    })(h);
  });

  /* Einblenden und Zaehler */
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add("in");
      if (e.target.hasAttribute("data-count")) count(e.target);
      io.unobserve(e.target);
    });
  }, { rootMargin: "0px 0px -8% 0px" }) : null;
  d.querySelectorAll(".rv,.reveal-img,[data-count]").forEach(function (el) { io ? io.observe(el) : el.classList.add("in"); });
  function count(el) {
    var end = parseFloat(el.getAttribute("data-count")), suf = el.getAttribute("data-suffix") || "", t0 = null;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) { el.textContent = end + suf; return; }
    function f(t) { if (!t0) t0 = t; var p = Math.min((t - t0) / 1400, 1); el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suf; if (p < 1) requestAnimationFrame(f); }
    requestAnimationFrame(f);
  }

  /* Vorher Nachher */
  d.querySelectorAll(".ba").forEach(function (ba) {
    var r = ba.querySelector("input"); if (!r) return;
    function set() { ba.style.setProperty("--pos", r.value + "%"); }
    r.addEventListener("input", set); set();
  });

  /* Anfrageformular: Pruefung im Browser, Versand an anfrage-senden.php, Rueckfall Mailprogramm */
  var form = d.getElementById("anfrage");
  if (form) {
    var ts = form.querySelector("[name=ts]"); if (ts) ts.value = Date.now();
    /* Woher kommt die Anfrage? Seite und Kampagnen-Parameter der aktuellen Adresse (nichts wird gespeichert) */
    var sf = form.querySelector("[name=seite]"); if (sf) sf.value = location.pathname;
    var kf = form.querySelector("[name=kampagne]");
    if (kf) { var q = new URLSearchParams(location.search), k = [];
      ["utm_source", "utm_medium", "utm_campaign", "utm_term", "gclid"].forEach(function (x) { if (q.get(x)) k.push(x + "=" + q.get(x).slice(0, 80)); });
      kf.value = k.join(" | "); }
    /* Auf Seiten mit Formular springen "Angebot anfragen"-Knoepfe direkt dorthin */
    d.querySelectorAll('a[href$="kontakt/#anfrage-form"]').forEach(function (a) { a.setAttribute("href", "#anfrage-form"); });
    var msg = form.querySelector(".form-msg");
    function check(fld) {
      var inp = fld.querySelector("input,textarea,select"); if (!inp) return true;
      var ok = inp.type === "checkbox" ? inp.checked : inp.value.trim() !== "";
      if (ok && inp.type === "email") ok = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(inp.value.trim());
      fld.classList.toggle("invalid", !ok); return ok;
    }
    form.querySelectorAll(".fld.req").forEach(function (f) {
      var i = f.querySelector("input,textarea,select");
      i && i.addEventListener("blur", function () { check(f); });
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true, first = null;
      form.querySelectorAll(".fld.req").forEach(function (f) { if (!check(f)) { ok = false; first = first || f; } });
      if (!ok) { first.querySelector("input,textarea,select").focus(); return; }
      var btn = form.querySelector("button[type=submit]"); btn.disabled = true; btn.querySelector("span").textContent = "Wird gesendet …";
      var data = new FormData(form);
      fetch(form.getAttribute("action"), { method: "POST", body: data, headers: { "Accept": "application/json" } })
        .then(function (r) { return r.json().catch(function () { return { ok: false }; }); })
        .then(function (j) {
          if (j && j.ok) {
            msg.className = "form-msg ok";
            msg.textContent = "Danke! Ihre Anfrage ist bei uns angekommen. Wir melden uns in der Regel innerhalb eines Werktags.";
            form.reset(); btn.querySelector("span").textContent = "Gesendet"; if (window.aoConversion) window.aoConversion("anfrage");
          } else { throw new Error("x"); }
        })
        .catch(function () {
          var body = [];
          data.forEach(function (v, k) { if (["website", "ts", "datenschutz", "seite", "kampagne"].indexOf(k) < 0 && v) body.push(k + ": " + v); });
          msg.className = "form-msg bad";
          msg.innerHTML = 'Der Versand hat leider nicht geklappt. <a href="mailto:info@wohlverde.de?subject=' + encodeURIComponent("Anfrage über wohlverde.de") + "&body=" + encodeURIComponent(body.join("\n")) + '">Anfrage per E-Mail senden</a> oder rufen Sie uns an: <a href="tel:+4972513924446">07251 3924446</a>.';
          btn.disabled = false; btn.querySelector("span").textContent = "Anfrage senden";
        });
    });
  }

  /* Klick auf Telefonnummer als Conversion (nur mit Einwilligung, siehe einwilligung.js) */
  d.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href^="tel:"]');
    if (a && window.aoConversion) window.aoConversion("anruf");
  });

  /* Bildausschnitt: Gesicht immer im oberen Drittel des sichtbaren Bereichs */
  function fokus(img) {
    var f = (img.getAttribute("data-focus") || "").split(" ");
    if (f.length < 2) return;
    var fx = parseFloat(f[0]) / 100, fy = parseFloat(f[1]) / 100;
    var iw = img.naturalWidth || parseFloat(img.getAttribute("width")), ih = img.naturalHeight || parseFloat(img.getAttribute("height"));
    var bw = img.clientWidth, bh = img.clientHeight;
    if (!iw || !ih || !bw || !bh) return;
    var sc = Math.max(bw / iw, bh / ih), vw = bw / sc / iw, vh = bh / sc / ih;
    function pos(c, v, ziel) { if (v >= 0.999) return 50; var t = Math.min(Math.max(c - ziel * v, 0), 1 - v); return t / (1 - v) * 100; }
    img.style.objectPosition = pos(fx, vw, 0.5).toFixed(1) + "% " + pos(fy, vh, 0.36).toFixed(1) + "%";
  }
  var fimgs = d.querySelectorAll("img[data-focus]");
  fimgs.forEach(function (img) { if (img.complete) fokus(img); img.addEventListener("load", function () { fokus(img); }); });
  if ("ResizeObserver" in window) { var ro = new ResizeObserver(function (es) { es.forEach(function (e) { fokus(e.target); }); }); fimgs.forEach(function (i) { ro.observe(i); }); }

  /* Werkzeuge und Schriftzug im Hintergrund der Petrol-Flaechen */
  var WZ = ["heckenschere", "scheibenabzieher", "schraubenzieher", "rechen", "spruehflasche", "laubblaeser", "schluessel", "rasenmaeher", "staubwedel"];
  d.querySelectorAll(".hero, .phead, section.dark, .cta").forEach(function (sec, si) {
    var deko = d.createElement("div"); deko.className = "deko"; deko.setAttribute("aria-hidden", "true");
    var n = sec.classList.contains("cta") ? 3 : 6;
    for (var i = 0; i < n; i++) {
      var im = d.createElement("img"); im.alt = ""; im.loading = "lazy";
      im.src = BASE + "assets/icons/" + WZ[(si * 3 + i) % WZ.length] + "_neg.png";
      var sz = 70 + ((si * 37 + i * 53) % 110);
      im.style.width = sz + "px"; im.style.left = ((i * 23 + si * 17) % 92) + "%"; im.style.top = ((i * 41 + si * 29) % 85) + "%";
      im.style.animationDelay = (-i * 3.7) + "s"; im.setAttribute("data-depth", (0.4 + (i % 3) * 0.35).toFixed(2));
      deko.appendChild(im);
    }
    sec.insertBefore(deko, sec.firstChild);
    if (!sec.classList.contains("hero") && !sec.classList.contains("cta")) {
      var mk = d.createElement("span"); mk.className = "mark"; mk.setAttribute("aria-hidden", "true"); mk.textContent = "WOHLverde";
      sec.insertBefore(mk, sec.firstChild);
    }
    if (still || !window.matchMedia("(hover: hover)").matches) return;
    var glow = d.createElement("span"); glow.className = "cursor-glow"; sec.insertBefore(glow, sec.firstChild);
    sec.addEventListener("mousemove", function (e) {
      var r = sec.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
      glow.style.left = x + "px"; glow.style.top = y + "px";
      var dx = (x / r.width - 0.5), dy = (y / r.height - 0.5);
      deko.querySelectorAll("img").forEach(function (im) { var k = parseFloat(im.getAttribute("data-depth")) * 30; im.style.transform = "translate(" + (-dx * k) + "px," + (-dy * k) + "px)"; });
    });
  });

  /* Jahr im Fuss */
  d.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
