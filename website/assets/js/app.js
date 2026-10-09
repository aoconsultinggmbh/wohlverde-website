/* WOHLverde | Seitenlogik ohne externe Bibliotheken */
(function () {
  "use strict";
  var d = document, root = d.documentElement;
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

  /* Einblenden und Zaehler */
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add("in");
      if (e.target.hasAttribute("data-count")) count(e.target);
      io.unobserve(e.target);
    });
  }, { rootMargin: "0px 0px -8% 0px" }) : null;
  d.querySelectorAll(".rv,[data-count]").forEach(function (el) { io ? io.observe(el) : el.classList.add("in"); });
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
          data.forEach(function (v, k) { if (["website", "ts", "datenschutz"].indexOf(k) < 0 && v) body.push(k + ": " + v); });
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

  /* Jahr im Fuss */
  d.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
