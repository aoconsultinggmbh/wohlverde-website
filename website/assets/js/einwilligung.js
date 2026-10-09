/* WOHLverde | Einwilligung fuer Google Ads (eigene Loesung, kein externer Anbieter)
   Laedt das Google-Skript erst nach ausdruecklicher Zustimmung.
   Schlaeft, solange in ao-konfiguration.js keine Google-Ads-Kennung steht. */
(function () {
  "use strict";
  var K = window.AO_KONFIG || {}, KEY = "wv-einwilligung-v1", d = document;
  window.aoConversion = function () {};
  if (!K.googleAds) return;

  function lesen() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function speichern(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }

  var geladen = false;
  function ladeGoogle() {
    if (geladen) return; geladen = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("consent", "default", { ad_storage: "granted", ad_user_data: "granted", ad_personalization: "granted", analytics_storage: "denied" });
    window.gtag("js", new Date());
    window.gtag("config", K.googleAds, { anonymize_ip: true });
    var s = d.createElement("script"); s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(K.googleAds);
    d.head.appendChild(s);
  }
  window.aoConversion = function (art) {
    if (!geladen || !window.gtag) return;
    var label = art === "anruf" ? K.conversionAnruf : K.conversionAnfrage;
    if (label) window.gtag("event", "conversion", { send_to: K.googleAds + "/" + label });
  };

  var box;
  function zeigen() {
    if (box) { box.hidden = false; box.querySelector("button").focus(); return; }
    box = d.createElement("div");
    box.className = "consent-box"; box.setAttribute("role", "dialog"); box.setAttribute("aria-live", "polite"); box.setAttribute("aria-label", "Einwilligung");
    box.innerHTML =
      '<p><strong>Dürfen wir messen, ob unsere Werbung wirkt?</strong> Mit Ihrer Zustimmung nutzen wir Google Ads Conversion-Tracking. Dabei werden Cookies gesetzt und Daten an Google übertragen, auch in die USA. ' +
      '<a href="' + (K.datenschutzUrl || "/datenschutz/") + '">Mehr erfahren</a></p>' +
      '<div class="consent-btns"><button type="button" class="btn btn--petrol" data-v="ja"><span>Zustimmen</span></button>' +
      '<button type="button" class="btn btn--ghost on-light" data-v="nein" style="color:var(--petrol)"><span>Ablehnen</span></button></div>';
    d.body.appendChild(box);
    box.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-v]"); if (!b) return;
      speichern(b.getAttribute("data-v")); box.hidden = true;
      if (b.getAttribute("data-v") === "ja") ladeGoogle();
      else if (geladen) location.reload();
    });
  }

  d.addEventListener("DOMContentLoaded", function () {
    d.querySelectorAll("[data-einwilligung]").forEach(function (a) {
      a.hidden = false;
      a.addEventListener("click", function (e) { e.preventDefault(); zeigen(); });
    });
    var v = lesen();
    if (v === "ja") ladeGoogle(); else if (v !== "nein") zeigen();
  });
})();
