#!/usr/bin/env python3
"""WOHLverde | Seitengenerator.
Erzeugt alle HTML-Seiten in ../website aus den Bausteinen unten.
Aufruf: python3 build/build.py   (aus dem Projektordner)
Texte stehen in build/inhalte.py, damit Aenderungen ohne HTML-Kenntnisse moeglich sind."""
import json, os, html, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
from inhalte import *  # noqa

ROOT = os.path.join(os.path.dirname(__file__), "..", "website")
DOMAIN = "https://wohlverde.de"
TODAY = datetime.date.today().isoformat()

# ---------- kleine Helfer ----------
def esc(s): return html.escape(s, quote=True)

ICONS = {
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="3"/><path d="M22 7l-10 6L2 7"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "insta": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/></svg>',
 "fb": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8.5V6.6c0-.9.6-1.1 1-1.1h2.6V1.6L14 1.5c-4 0-4.9 3-4.9 4.9v2.1H6.5v4h2.6V22.5H14V12.5h3.3l.4-4z"/></svg>',
 "quote": '<svg viewBox="0 0 48 48" fill="currentColor" aria-hidden="true"><path d="M20 10C11 13 6 20 6 29v9h14V24h-7c0-5 3-8 8-10zM42 10c-9 3-14 10-14 19v9h14V24h-7c0-5 3-8 8-10z"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>',
 "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>',
 "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6"/></svg>',
 "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2L3 14h9l-1 8 10-12h-9z"/></svg>',
 "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2l10 5-10 5L2 7z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/></svg>',
 "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.2-6"/></svg>',
 "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
}
ICONS["flake"] = '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M24 4v40M6.7 14l34.6 20M6.7 34l34.6-20M24 4l-5 5M24 4l5 5M24 44l-5-5M24 44l5-5M6.7 14l1.8 6.8M6.7 14l6.8-1.8M41.3 34l-1.8-6.8M41.3 34l-6.8 1.8M6.7 34l6.8 1.8M6.7 34l1.8-6.8M41.3 14l-6.8-1.8M41.3 14l-1.8 6.8"/></svg>'
def ic(n): return ICONS[n]

def art(kind, depth, cls=""):
    """Grafikflaeche fuer Leistungen ohne passendes Foto (Hausmeister, Winterdienst)."""
    p = pre(depth)
    if kind == "winter":
        import random
        random.seed(7)
        fl = "".join(f'<span class="flake" style="left:{random.randint(2,92)}%;top:{random.randint(-10,70)}%;width:{random.randint(14,46)}px;height:{random.randint(14,46)}px;animation-duration:{random.randint(9,18)}s;animation-delay:-{random.randint(0,12)}s;opacity:{random.choice([.35,.55,.9])}">{ICONS["flake"]}</span>' for _ in range(14))
        return f'<div class="art {cls}" aria-hidden="true">{fl}<img class="art-ic" src="{p}assets/icons/rechen_neg.png" alt="" style="opacity:.25;width:40%"></div>'
    return f'<div class="art {cls}" aria-hidden="true"><img class="art-ic" src="{p}assets/icons/schraubenzieher_neg.png" alt=""><img class="art-ic k2" src="{p}assets/icons/schluessel_neg.png" alt=""></div>'

def pre(depth):  # relativer Pfad zur Wurzel
    return "../" * depth

def pic(name, alt, depth, sizes="(max-width: 900px) 100vw, 50vw", eager=False, cls="", w=1200, h=1800, pos=""):
    p = pre(depth) + "assets/img/"
    load = 'fetchpriority="high" loading="eager"' if eager else 'loading="lazy"'
    return (f'<picture{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>'
            f'<source type="image/webp" srcset="{p}{name}-900.webp 900w, {p}{name}.webp {w}w" sizes="{sizes}">'
            f'<img src="{p}{name}-900.jpg" srcset="{p}{name}-900.jpg 900w, {p}{name}.jpg {w}w" sizes="{sizes}" alt="{esc(alt)}" width="{w}" height="{h}" {load} decoding="async"{(' style="object-position:' + pos + '"') if pos else ""}></picture>')

def btn(href, text, kind="", icon="arrow"):
    k = f" btn--{kind}" if kind else ""
    return f'<a class="btn{k}" href="{href}"><span>{text}</span>{ic(icon) if icon else ""}</a>'

# ---------- Strukturierte Daten ----------
ORG_ID = DOMAIN + "/#unternehmen"
def org_schema():
    return {
      "@type": ["LocalBusiness", "ProfessionalService"],
      "@id": ORG_ID,
      "name": "WOHLverde",
      "alternateName": ["H&G WOHL", "Haus & Garten WOHL", "WOHLverde Grünpflege & Gebäudereinigung"],
      "slogan": "Die Garten- und Gebäudemanager",
      "description": FIRMA["kurz"],
      "url": DOMAIN + "/",
      "logo": DOMAIN + "/assets/img/logo-pos.png",
      "image": DOMAIN + "/assets/img/team-fahrzeug.jpg",
      "telephone": FIRMA["tel_int"],
      "email": FIRMA["mail"],
      "foundingDate": "2020-10",
      "founder": {"@type": "Person", "name": "Nico Sica", "jobTitle": "Gründer und Geschäftsführer"},
      "numberOfEmployees": {"@type": "QuantitativeValue", "minValue": 20},
      "vatID": "DE325441678",
      "address": {"@type": "PostalAddress", "streetAddress": "Kronauer Allee 1", "postalCode": "76694", "addressLocality": "Forst", "addressRegion": "Baden-Württemberg", "addressCountry": "DE"},
      "areaServed": [{"@type": "City", "name": o} for o in EINSATZORTE_ALLE],
      "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:00", "closes": "17:00"}],
      "knowsAbout": ["Grünpflege", "Garten- und Landschaftspflege", "Gebäudereinigung", "Unterhaltsreinigung", "Glasreinigung", "Hausmeisterservice", "Objektbetreuung", "Winterdienst", "Baumpflege"],
      "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Leistungen", "itemListElement": [
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": l["name"], "url": DOMAIN + l["url"]}} for l in LEISTUNGEN]},
      "sameAs": [FIRMA["instagram"], FIRMA["facebook"], FIRMA["karriere"]],
      "priceRange": "Angebot nach Vor-Ort-Termin",
    }

def crumbs_schema(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + u} for i, (n, u) in enumerate(items)]}

def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def ld(*objs, page_url, page_name, page_type="WebPage", desc=""):
    graph = [org_schema(),
             {"@type": "WebSite", "@id": DOMAIN + "/#website", "url": DOMAIN + "/", "name": "WOHLverde", "inLanguage": "de-DE", "publisher": {"@id": ORG_ID}},
             {"@type": page_type, "@id": DOMAIN + page_url + "#seite", "url": DOMAIN + page_url, "name": page_name, "description": desc,
              "isPartOf": {"@id": DOMAIN + "/#website"}, "about": {"@id": ORG_ID}, "inLanguage": "de-DE", "dateModified": TODAY}]
    graph += [o for o in objs if o]
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False) + "</script>"

# ---------- Rahmen ----------
def head(title, desc, url, depth, schema, og_img="team-fahrzeug.jpg", light=False):
    p = pre(depth)
    return f'''<!doctype html>
<html lang="de" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{DOMAIN}{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#003a41">
<meta name="geo.region" content="DE-BW"><meta name="geo.placename" content="Forst (Baden)">
<meta property="og:type" content="website"><meta property="og:locale" content="de_DE"><meta property="og:site_name" content="WOHLverde">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{DOMAIN}{url}"><meta property="og:image" content="{DOMAIN}/assets/img/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{p}favicon.ico" sizes="any"><link rel="icon" type="image/png" href="{p}assets/img/favicon-192.png">
<link rel="apple-touch-icon" href="{p}assets/img/apple-touch-icon.png"><link rel="manifest" href="{p}site.webmanifest">
<link rel="preconnect" href="https://use.typekit.net" crossorigin>
<link rel="stylesheet" href="https://use.typekit.net/rma2wag.css">
<link rel="stylesheet" href="{p}assets/css/style.css">
{schema}
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
'''

def header(depth, active=""):
    p = pre(depth)
    def a(href, text, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{p}{href}"{cur}>{text}</a>'
    dd = "".join(f'<a href="{p}{l["url"].lstrip("/")}"><img src="{p}assets/icons/{l["icon"]}_pos.png" alt="" width="34" height="34"><span>{l["name"]}<small>{l["dd"]}</small></span></a>' for l in LEISTUNGEN)
    return f'''<header class="top">
<div class="wrap">
<a class="logo" href="{p}" aria-label="WOHLverde Startseite"><img class="l-light" src="{p}assets/img/logo-neg.png" alt="WOHLverde Grünpflege und Gebäudereinigung" width="1212" height="265"><img class="l-dark" src="{p}assets/img/logo-pos.png" alt="WOHLverde Grünpflege und Gebäudereinigung" width="1212" height="265"></a>
<button class="burger" aria-label="Menü öffnen" aria-expanded="false" aria-controls="hauptnav"><span></span><span></span><span></span></button>
<nav class="nav" id="hauptnav" aria-label="Hauptnavigation">
<div class="dd"><button class="navbtn" aria-expanded="false" aria-haspopup="true">Leistungen <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dd-menu">{dd}</div></div>
{a("einsatzgebiet/", "Einsatzgebiet", "einsatz")}
{a("ueber-uns/", "Über uns", "ueber")}
<a href="{FIRMA["karriere"]}" rel="noopener">Karriere</a>
{a("kontakt/", "Kontakt", "kontakt")}
<a class="btn" href="{p}kontakt/#anfrage-form"><span>Angebot anfragen</span></a>
</nav>
</div>
</header>
<main id="inhalt">
'''

def footer(depth):
    p = pre(depth)
    lst = "".join(f'<li><a href="{p}{l["url"].lstrip("/")}">{l["name"]}</a></li>' for l in LEISTUNGEN)
    orte = "".join(f'<li><a href="{p}einsatzgebiet/{o["slug"]}/">{o["name"]}</a></li>' for o in ORTE)
    return f'''</main>
<footer class="foot">
<div class="wrap">
<div class="foot-grid">
<div>
<img class="flogo" src="{p}assets/img/logo-neg.png" alt="WOHLverde" width="1212" height="265" loading="lazy">
<p>Grünpflege, Gebäudereinigung und Hausmeisterservice für Unternehmen, Hausverwaltungen und Kommunen im Raum Bruchsal, Karlsruhe und Bretten.</p>
<p>Aus <strong>H&amp;G WOHL</strong> wurde <strong>WOHLverde</strong>: gleiches Team, gleicher Anspruch.</p>
<div class="soc"><a href="{FIRMA["instagram"]}" rel="noopener" aria-label="WOHLverde auf Instagram">{ic("insta")}</a><a href="{FIRMA["facebook"]}" rel="noopener" aria-label="WOHLverde auf Facebook">{ic("fb")}</a></div>
</div>
<div><h4>Leistungen</h4><ul>{lst}</ul></div>
<div><h4>Einsatzgebiet</h4><ul>{orte}<li><a href="{p}einsatzgebiet/">Alle Orte</a></li></ul></div>
<div><h4>Kontakt</h4><ul>
<li>WOHLverde<br>Kronauer Allee 1<br>76694 Forst</li>
<li><a href="tel:{FIRMA["tel_int"]}">{FIRMA["tel"]}</a></li>
<li><a href="mailto:{FIRMA["mail"]}">{FIRMA["mail"]}</a></li>
<li>Mo bis Fr: 8 bis 17 Uhr<br>Sa: nach Vereinbarung</li>
</ul></div>
</div>
<div class="foot-bottom">
<span>© <span data-year>2026</span> WOHLverde, Forst</span>
<nav aria-label="Rechtliches"><a href="{p}impressum/">Impressum</a><a href="{p}datenschutz/">Datenschutz</a><a href="{p}hinweis-zur-gleichstellung/">Hinweis zur Gleichstellung</a><a href="#" data-einwilligung hidden>Cookie-Einstellungen</a><a href="{FIRMA["karriere"]}" rel="noopener">Karriere</a></nav>
</div>
</div>
</footer>
<div class="mbar" aria-label="Schnellkontakt"><a class="m1" href="tel:{FIRMA["tel_int"]}">{ic("phone")}Anrufen</a><a class="m2" href="{p}kontakt/#anfrage-form">Angebot anfragen</a></div>
<script src="{p}assets/js/ao-konfiguration.js"></script>
<script src="{p}assets/js/einwilligung.js"></script>
<script src="{p}assets/js/app.js" defer></script>
</body>
</html>
'''

def crumbs_html(items, depth):
    p = pre(depth)
    li = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            li.append(f'<li aria-current="page">{n}</li>')
        else:
            li.append(f'<li><a href="{p}{u.lstrip("/")}">{n}</a></li>')
    return f'<nav class="crumbs" aria-label="Brotkrumen"><ol>{"".join(li)}</ol></nav>'

# ---------- Bausteine ----------
def ticker(items, dark=False):
    s = "".join(f"<span>{t}</span>" for t in items)
    return f'<div class="ticker{" ticker--dark" if dark else ""}" aria-hidden="true"><div class="ticker-in">{s}{s}</div></div>'

def faq_html(faqs):
    return '<div class="faq">' + "".join(
        f'<details class="rv"><summary>{esc(q)}</summary><div class="a"><p>{esc(a)}</p></div></details>' for q, a in faqs) + "</div>"

def steps_html(dark=False):
    s = "".join(f'<div class="step rv d{i}"><h3>{t}</h3><p>{x}</p></div>' for i, (t, x) in enumerate(ABLAUF))
    return f'<div class="steps">{s}</div>'

def refs_html():
    s = "".join(f"<span>{r}</span>" for r in REFERENZEN)
    return f'<div class="refs" role="list" aria-label="Referenzkunden"><div class="refs-in">{s}{s}</div></div>'

def cta_html(depth, title="Ihr Objekt verdient einen Partner, der mitdenkt.", text="Erzählen Sie uns kurz, worum es geht. Wir melden uns in der Regel innerhalb eines Werktags und vereinbaren einen Vor-Ort-Termin."):
    p = pre(depth)
    return f'''<section class="sec--tight"><div class="wrap"><div class="cta rv">
<div><span class="eyebrow">Unverbindlich anfragen</span><h2>{title}</h2><p class="lead" style="color:#d3e0e1;margin:0">{text}</p></div>
<div class="btns">{btn(p + "kontakt/#anfrage-form", "Angebot anfragen")}<a class="btn btn--ghost" href="tel:{FIRMA["tel_int"]}"><span>{FIRMA["tel"]}</span>{ic("phone")}</a></div>
</div></div></section>'''

def career_html(depth):
    return f'''<section class="sec--tight"><div class="wrap"><div class="career rv">
<div class="txt"><span class="eyebrow">Karriere bei WOHLverde</span><h2>Mach mit. Wir bilden dich aus.</h2>
<p style="font-size:19px">Du suchst einen Job mit Abwechslung, festem Team und echten Perspektiven? Auch handwerklich begabte Quereinsteiger sind bei uns willkommen, denn wir bieten Fortbildungen und Schulungen für jeden Fachbereich.</p>
<div class="btns">{btn(FIRMA["karriere"], "Offene Stellen ansehen", "petrol")}</div></div>
{pic("team-baum", "Das WOHLverde-Team gemeinsam an einem Baum auf einem Firmengelände", depth, "(max-width: 860px) 100vw, 45vw", w=1800, h=1200)}
</div></div></section>'''

def form_html(depth, dark=True):
    p = pre(depth)
    obj = "".join(f"<option>{o}</option>" for o in ["Bürogebäude", "Gewerbe- oder Industriefläche", "Wohnanlage / Hausverwaltung", "Kommunale Einrichtung", "Hotel / Gastronomie", "Privat", "Sonstiges"])
    chips = "".join(f'<label><input type="checkbox" name="leistung[]" value="{l}"><span>{l}</span></label>' for l in ["Grünpflege", "Gebäudereinigung", "Hausmeisterservice", "Winterdienst", "Alles aus einer Hand"])
    return f'''<form class="form" id="anfrage" action="{p}anfrage-senden.php" method="post" novalidate>
<h3 style="color:var(--petrol)">Anfrage für Ihr Objekt</h3>
<p class="form-note" style="margin:0 0 20px">Felder mit * sind Pflicht. Dauert etwa eine Minute.</p>
<div class="row">
<div class="fld"><label for="f-firma">Unternehmen / Einrichtung</label><input id="f-firma" name="firma" autocomplete="organization"></div>
<div class="fld req"><label for="f-name">Ansprechpartner *</label><input id="f-name" name="name" autocomplete="name" required><span class="err">Bitte geben Sie Ihren Namen an.</span></div>
</div>
<div class="row">
<div class="fld req"><label for="f-mail">E-Mail *</label><input id="f-mail" name="email" type="email" autocomplete="email" required><span class="err">Bitte geben Sie eine gültige E-Mail-Adresse an.</span></div>
<div class="fld"><label for="f-tel">Telefon</label><input id="f-tel" name="telefon" type="tel" autocomplete="tel"></div>
</div>
<div class="row">
<div class="fld"><label for="f-obj">Art des Objekts</label><select id="f-obj" name="objekt"><option value="">Bitte wählen</option>{obj}</select></div>
<div class="fld"><label for="f-ort">Ort des Objekts</label><input id="f-ort" name="ort" placeholder="z. B. Bruchsal"></div>
</div>
<fieldset class="fld"><legend>Was dürfen wir übernehmen?</legend><div class="chips">{chips}</div></fieldset>
<div class="fld req"><label for="f-msg">Ihre Nachricht *</label><textarea id="f-msg" name="nachricht" required placeholder="Größe der Fläche, gewünschter Rhythmus, Startzeitpunkt …"></textarea><span class="err">Bitte beschreiben Sie kurz Ihr Anliegen.</span></div>
<div class="hp" aria-hidden="true"><label for="f-web">Bitte frei lassen</label><input id="f-web" name="website" tabindex="-1" autocomplete="off"></div>
<input type="hidden" name="ts" value="">
<div class="fld req" style="margin:0"><label class="consent"><input type="checkbox" name="datenschutz" value="ja" required><span>Ich bin einverstanden, dass meine Angaben zur Bearbeitung der Anfrage verwendet werden. Mehr dazu in der <a href="{p}datenschutz/">Datenschutzerklärung</a>. *</span></label><span class="err">Bitte stimmen Sie der Verarbeitung zu.</span></div>
<button class="btn btn--petrol" type="submit" style="width:100%"><span>Anfrage senden</span>{ic("arrow")}</button>
<div class="form-msg" role="status" aria-live="polite"></div>
</form>'''

def contact_list():
    return f'''<ul class="contact-list">
<li><i>{ic("phone")}</i><div><small>Telefon</small><a href="tel:{FIRMA["tel_int"]}">{FIRMA["tel"]}</a></div></li>
<li><i>{ic("mail")}</i><div><small>E-Mail</small><a href="mailto:{FIRMA["mail"]}">{FIRMA["mail"]}</a></div></li>
<li><i>{ic("pin")}</i><div><small>Standort</small><a href="https://www.google.com/maps/search/?api=1&amp;query=WOHLverde+Kronauer+Allee+1+76694+Forst" rel="noopener">Kronauer Allee 1, 76694 Forst</a></div></li>
<li><i>{ic("clock")}</i><div><small>Erreichbarkeit</small><strong>Mo bis Fr 8 bis 17 Uhr, Sa nach Vereinbarung</strong></div></li>
</ul>'''

def insta_html(depth):
    imgs = [("reinigung-duo", "Zwei WOHLverde-Reinigungskräfte im Treppenhaus"), ("garten-hecke-sommer", "Heckenschnitt im Sommer"), ("reinigung-tisch", "Reinigung eines Besprechungstischs"),
            ("juni-portrait-hut", "WOHLverde-Mitarbeiter im Einsatz"), ("reinigung-fenster", "Glasreinigung im Büro"), ("fahrzeug-transporter", "WOHLverde-Transporter")]
    g = "".join(f'<a href="{FIRMA["instagram"]}" rel="noopener" aria-label="Instagram: {esc(a)}">{pic(n, a, depth, "(max-width: 860px) 33vw, 16vw")}</a>' for n, a in imgs)
    return f'''<section class="sec sand"><div class="wrap social">
<div class="rv"><span class="eyebrow">Hinter den Kulissen</span><h2>Folge uns auf Instagram: <span class="hl">@wohlverde</span></h2>
<p class="lead">Echte Einsätze, echtes Team, echte Ergebnisse. Auf Instagram zeigen wir, wie unser Alltag zwischen Hecke, Treppenhaus und Werkstatt aussieht.</p>
<div class="btns">{btn(FIRMA["instagram"], "Zu Instagram", "petrol", "insta")}<a class="btn btn--ghost on-light" style="color:var(--petrol)" href="{FIRMA["facebook"]}" rel="noopener"><span>Facebook</span>{ic("fb")}</a></div></div>
<div class="insta-grid rv d1">{g}</div>
</div></section>'''

def feats(items, dark=False):
    return '<div class="feats">' + "".join(
        f'<div class="feat rv d{i % 2}"><div class="ic">{ic(icn)}</div><div><h3>{t}</h3><p>{x}</p></div></div>' for i, (icn, t, x) in enumerate(items)) + "</div>"

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("geschrieben", path)

# ---------- Seiten ----------
def page_home():
    d = 0
    title = "Grünpflege & Gebäudereinigung in Bruchsal & Karlsruhe | WOHLverde"
    desc = "WOHLverde aus Forst betreut Gewerbeimmobilien, Hausverwaltungen und Kommunen im Raum Bruchsal, Karlsruhe und Bretten: Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst. Festes Team, keine Subunternehmen."
    schema = ld(faq_schema(FAQ_START), page_url="/", page_name=title, desc=desc)
    cards = []
    cls = ["c-a", "c-b", "c-c", "c-d"]
    for i, l in enumerate(LEISTUNGEN):
        media = art(l["art"], d) if l.get("art") else pic(l.get("karte", l["bild"]), l["bild_alt"], d, "(max-width: 900px) 100vw, 60vw", pos=l.get("karte_pos", ""))
        cards.append(f'''<a class="card {cls[i]}{" art" if l.get("art") else ""} rv d{i % 2}" href="{l["url"].lstrip("/")}">{media}
<span class="ic"><img src="assets/icons/{l["icon"]}_neg.png" alt="" width="38" height="38"></span>
<h3>{l["name"]}</h3><p>{l["teaser"]}</p><span class="more">Mehr erfahren {ic("arrow")}</span></a>''')
    who = "".join(f'<div class="rv d{i % 4}"><span class="n">{i + 1}</span><b>{t}</b><p>{x}</p></div>' for i, (t, x) in enumerate(ZIELGRUPPEN))
    places = "".join(f'<a class="place rv d{i % 4}" href="einsatzgebiet/{o["slug"]}/"><b>{o["name"]}</b><span>{o["zeile"]} {ic("arrow")}</span></a>' for i, o in enumerate(ORTE))
    towns = "".join(f"<span>{t}</span>" for t in EINSATZORTE_ALLE)
    body = f'''
<section class="hero">
<span class="blob b-a"></span><span class="blob b-b"></span>
<div class="wrap hero-grid">
<div>
<span class="eyebrow" style="color:var(--lime)">Grünpflege &amp; Gebäudereinigung im Raum Bruchsal &amp; Karlsruhe</span>
<h1 class="wordsplit">Wir pflegen, was <span class="l">Werte</span> schafft.</h1>
<p class="h1-sub">Drinnen wie draußen.</p>
<p class="lead">Objektbetreuung für Gewerbeimmobilien, Industrieflächen, Wohnanlagen und Kommunen. Mit festen Teams, festen Ansprechpartnern und dokumentierten Abläufen.</p>
<div class="btns">{btn("kontakt/#anfrage-form", "Angebot anfragen")}<a class="btn btn--ghost" href="#leistungen"><span>Leistungen entdecken</span></a></div>
<p style="margin:24px 0 0"><a class="hero-call" href="tel:{FIRMA["tel_int"]}"><i>{ic("phone")}</i><span><small>Direkt sprechen, Mo bis Fr 8 bis 17 Uhr</small>{FIRMA["tel"]}</span></a></p>
</div>
<div class="hero-media">
<div class="frame grade">{pic("garten-heckenschere", "Lächelnder WOHLverde-Mitarbeiter mit Heckenschere auf einer Gewerbefläche", d, "(max-width: 960px) 100vw, 40vw", eager=True)}</div>
<div class="badge b1"><img src="assets/icons/heckenschere_pos.png" alt="" width="36" height="36"><span><b>20+</b>Profis im Team</span></div>
<div class="badge b2"><span><b>0</b>Subunternehmen</span></div>
<div class="badge b3"><img src="assets/icons/scheibenabzieher_pos.png" alt="" width="36" height="36"><span>Alles aus<br>einer Hand</span></div>
</div>
</div>
<div class="wrap hero-strip"><ul>
<li>Festangestellte, deutschsprachige Teams</li><li>Feste Ansprechpartner</li><li>Dokumentierte Objektkontrollen</li><li>Seit 2020 in der Region</li>
</ul></div>
</section>
{ticker(["Grünpflege", "Gebäudereinigung", "Hausmeisterservice", "Winterdienst", "Baumpflege", "Glasreinigung", "Unterhaltsreinigung", "Objektbetreuung"])}

<section class="sec" id="leistungen"><div class="wrap">
<div class="head"><div><span class="eyebrow">Unsere Leistungen</span><h2>Ein Partner für Ihr <span class="hl">ganzes Objekt</span>.</h2></div>
<p class="lead rv">Grünpflege, Gebäudereinigung, technischer Objektservice und Winterdienst greifen bei uns ineinander. Für Sie heißt das: weniger Abstimmung, klare Zuständigkeiten und planbare Qualität.</p></div>
<p class="kurz rv"><strong>Kurz gesagt:</strong> WOHLverde ist ein Dienstleister für Objektbetreuung aus Forst bei Bruchsal. Wir übernehmen Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst für Unternehmen, Hausverwaltungen und Kommunen im Raum Bruchsal, Karlsruhe und Bretten, ausschließlich mit eigenem, festangestelltem Personal.</p>
<div class="bento">{"".join(cards)}</div>
</div></section>

<section class="sec dark"><div class="wrap">
<div class="head"><div><span class="eyebrow">Warum Unternehmen mit uns arbeiten</span><h2>Qualität, die man <span class="hl">planen</span> kann.</h2></div>
<p class="lead rv">Wir kennen die Anforderungen von Gewerbeimmobilien und kommunalen Einrichtungen vor Ort. Darum arbeiten wir strukturiert, termintreu und nachvollziehbar.</p></div>
<div class="stats" style="margin-bottom:18px">
<div class="stat rv"><b data-count="20" data-suffix="+">20+</b><span>Kolleginnen und Kollegen</span></div>
<div class="stat rv d1"><b data-count="100" data-suffix=" %">100 %</b><span>festangestellt</span></div>
<div class="stat rv d2"><b>0</b><span>Subunternehmen</span></div>
<div class="stat rv d3"><b>2020</b><span>gegründet in Forst</span></div>
</div>
{feats(VORTEILE, True)}
</div></section>

<section class="sec"><div class="wrap split">
<div class="split-media rv"><div class="frame grade para reveal-img">{pic("objekt-abstimmung", "Zwei WOHLverde-Mitarbeitende dokumentieren eine Objektkontrolle auf dem Tablet", d)}</div><span class="tag">Dokumentiert statt versprochen</span></div>
<div class="rv d1"><span class="eyebrow">Objektservice für Gewerbe</span><h2>Wir sehen hin, bevor es teuer wird.</h2>
<p class="lead">Regelmäßige Objektkontrollen mit Dokumentation, laufende Instandhaltung und schnelle Reaktion: So bleibt Ihre Immobilie funktional, sicher und im Wert erhalten.</p>
<ul class="checks cols"><li>Feste Teams und Ansprechpartner</li><li>Schnelle Reaktionszeiten</li><li>Objektkontrollen mit Protokoll</li><li>Kleinreparaturen und Instandhaltung</li><li>Koordination externer Dienstleister</li><li>Unterstützung im laufenden Betrieb</li></ul>
{btn("hausmeister-service/", "Zum Hausmeisterservice", "petrol")}</div>
</div></section>

<section class="sec sand"><div class="wrap vn">
<div class="rv"><span class="eyebrow">Vorher und nachher</span><h2>Ergebnisse, die man <span class="hl">sieht</span>.</h2>
<p class="lead">Unkrautbeseitigung auf der Pflasterfläche eines Firmengeländes. Gleiche Stelle, ein Arbeitseinsatz.</p>
<ul class="checks"><li>Grün- und Grauflächen</li><li>Umweltschonende Methoden</li><li>Fester Pflegeplan statt Einzelaktion</li></ul>
{btn("garten-und-landschaftspflege/", "Zur Grünpflege", "petrol")}</div>
<div class="vn-pics">
<figure class="rv">{pic("vorher-pflaster", "Pflasterfläche auf einem Firmengelände mit Unkraut in den Fugen, vor dem Einsatz", d, "(max-width: 900px) 50vw, 25vw", w=1050, h=1400)}<span class="lbl l1">Vorher</span></figure>
<figure class="rv d2">{pic("nachher-pflaster", "Dieselbe Pflasterfläche nach der Unkrautbeseitigung durch WOHLverde", d, "(max-width: 900px) 50vw, 25vw", w=1050, h=1400)}<span class="lbl l2">Nachher</span></figure>
</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head"><div><span class="eyebrow">Für wen wir arbeiten</span><h2>Gemacht für <span class="hl">Profis</span> mit Verantwortung.</h2></div>
<p class="lead rv">Ob Verwaltungsgebäude, Gewerbepark oder Wohnanlage: Wir richten Leistungsumfang und Rhythmus nach Ihrem Objekt, nicht nach einem Standardpaket.</p></div>
<div class="who">{who}</div>
</div></section>

<section class="sec--tight"><div class="wrap">
<p class="eyebrow" style="justify-content:center;width:100%">Unternehmen und Einrichtungen, die uns vertrauen</p>
{refs_html()}
</div></section>

<section class="sec dark"><div class="wrap">
<div class="head"><div><span class="eyebrow">So läuft die Zusammenarbeit</span><h2>In vier Schritten zum <span class="hl">gepflegten Objekt</span>.</h2></div>
<p class="lead rv">Transparent von der ersten Anfrage bis zur laufenden Betreuung. Sie wissen jederzeit, wer zuständig ist und was als Nächstes passiert.</p></div>
{steps_html(True)}
</div></section>

<section class="sec"><div class="wrap split rev">
<div class="split-media wide"><div class="frame grade para reveal-img" style="border-radius:var(--radius)">{pic("team-unterwegs", "Das WOHLverde-Team läuft mit Werkzeug über ein Firmengelände", d, "(max-width: 900px) 100vw, 50vw", w=1800, h=1200)}</div></div>
<div class="rv d1"><span class="eyebrow">Ein Team, kein Wechselpersonal</span><h2>Bei uns kennen Sie die Menschen, die bei Ihnen arbeiten.</h2>
<p class="lead">Wir arbeiten ausschließlich mit festangestellten, deutschsprachigen Mitarbeitenden. Regelmäßige Schulungen sichern den Standard, klare Kommunikation sorgt dafür, dass nichts verloren geht.</p>
{btn("ueber-uns/", "Lernen Sie uns kennen", "petrol")}</div>
</div></section>

<section class="sec dark"><div class="wrap">
<div class="head"><div><span class="eyebrow">Einsatzgebiet</span><h2>Zu Hause in Forst. <span class="hl">Schnell vor Ort</span> in der Region.</h2></div>
<p class="lead rv">Kurze Wege bedeuten schnelle Reaktionszeiten. Wir betreuen Objekte im Raum Bruchsal, Karlsruhe, Bretten und Umgebung.</p></div>
<div class="places">{places}</div>
<div class="towns rv">{towns}</div>
</div></section>

<div class="big-ticker" aria-hidden="true"><div class="ticker-in">{"".join(f"<span>{t}</span>" for t in ["Grünpflege","Gebäudereinigung","Hausmeisterservice","Winterdienst"]*2)}</div></div>
<section class="sec sand"><div class="wrap faq-grid">
<div class="rv"><span class="eyebrow">Häufige Fragen</span><h2>Kurz und klar beantwortet.</h2><p class="lead">Ihre Frage ist nicht dabei? Rufen Sie uns an oder schreiben Sie uns, wir antworten gern persönlich.</p>{btn("kontakt/", "Kontakt aufnehmen", "petrol")}</div>
{faq_html(FAQ_START)}
</div></section>

{insta_html(d)}
{career_html(d)}
{cta_html(d)}
'''
    write("index.html", head(title, desc, "/", d, schema) + header(d) + body + footer(d))

def page_leistung(l):
    d = 1
    url = l["url"]
    title = l["title"]
    desc = l["desc"]
    crumbs = [("Startseite", "/"), (l["name"], url)]
    service = {"@type": "Service", "@id": DOMAIN + url + "#leistung", "name": l["name"], "serviceType": l["name"], "description": l["kurz"],
               "provider": {"@id": ORG_ID}, "areaServed": [{"@type": "City", "name": o} for o in EINSATZORTE_ALLE],
               "audience": {"@type": "BusinessAudience", "name": "Unternehmen, Hausverwaltungen, Kommunen"},
               "hasOfferCatalog": {"@type": "OfferCatalog", "name": l["name"], "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": t}} for t, _ in l["punkte"]]}}
    schema = ld(service, crumbs_schema(crumbs), faq_schema(l["faq"]), page_url=url, page_name=title, desc=desc)
    punkte = "".join(f'<div class="feat rv d{i % 2}"><div class="ic"><img src="../assets/icons/{l["icon"]}_neg.png" alt="" width="36" height="36"></div><div><h3>{t}</h3><p>{x}</p></div></div>' for i, (t, x) in enumerate(l["punkte"]))
    others = [o for o in LEISTUNGEN if o["url"] != url]
    other = "".join(f'<a class="place rv d{i}" style="background:var(--petrol);min-height:150px" href="../{o["url"].lstrip("/")}"><b>{o["name"]}</b><span>{o["dd"]} {ic("arrow")}</span></a>' for i, o in enumerate(others))
    body = f'''
<section class="phead"><div class="wrap phead-grid">
<div>{crumbs_html(crumbs, d)}
<span class="eyebrow" style="color:var(--lime)">{l["eyebrow"]}</span>
<h1>{l["h1"]}</h1>
<p class="lead">{l["intro"]}</p>
<div class="btns">{btn("../kontakt/#anfrage-form", "Angebot anfragen")}<a class="btn btn--ghost" href="tel:{FIRMA["tel_int"]}"><span>{FIRMA["tel"]}</span>{ic("phone")}</a></div>
</div>
<div class="phead-media">{art(l["kopf_art"], d, "frame") if l.get("kopf_art") else '<div class="frame grade">' + pic(l["bild"], l["bild_alt"], d, "(max-width: 860px) 100vw, 45vw", eager=True) + '</div>'}<span class="chip">{l["chip"]}</span></div>
</div></section>
{ticker([t for t, _ in l["punkte"]], dark=False)}

<section class="sec"><div class="wrap">
<p class="kurz rv"><strong>Kurz gesagt:</strong> {l["kurz"]}</p>
<div class="head"><div><span class="eyebrow">Leistungsumfang</span><h2>{l["h2_leistung"]}</h2></div><p class="lead rv">{l["leistung_text"]}</p></div>
<div class="feats">{punkte}</div>
</div></section>

<section class="sec sand"><div class="wrap split">
<div class="split-media"><div class="frame grade para reveal-img" style="border-radius:var(--radius)">{pic(l["bild2"], l["bild2_alt"], d)}</div><span class="tag">{l["tag"]}</span></div>
<div class="rv d1"><span class="eyebrow">Ihr Vorteil</span><h2>{l["h2_vorteil"]}</h2><p class="lead">{l["vorteil_text"]}</p>
<ul class="checks">{"".join(f"<li>{c}</li>" for c in l["checks"])}</ul>
{btn("../kontakt/#anfrage-form", "Jetzt unverbindlich anfragen", "petrol")}</div>
</div></section>

<section class="sec dark"><div class="wrap">
<div class="head"><div><span class="eyebrow">Ablauf</span><h2>So starten wir <span class="hl">gemeinsam</span>.</h2></div><p class="lead rv">Vom ersten Kontakt bis zur laufenden Betreuung mit festen Zuständigkeiten.</p></div>
{steps_html(True)}
</div></section>

<section class="sec"><div class="wrap faq-grid">
<div class="rv"><span class="eyebrow">Fragen und Antworten</span><h2>{l["name"]}: das wollen Kunden wissen.</h2>{btn("../kontakt/", "Frage stellen", "petrol")}</div>
{faq_html(l["faq"])}
</div></section>

<section class="sec--tight sand"><div class="wrap">
<span class="eyebrow">Alles aus einer Hand</span><h2 style="margin-bottom:28px">Weitere Leistungen</h2>
<div class="places places--3">{other}</div>
</div></section>
{cta_html(d)}
'''
    write(url.strip("/") + "/index.html", head(title, desc, url, d, schema, og_img=l["bild"] + ".jpg") + header(d) + body + footer(d))

def page_einsatz():
    d = 1
    url = "/einsatzgebiet/"
    title = "Einsatzgebiet: Bruchsal, Karlsruhe, Bretten & Umgebung | WOHLverde"
    desc = "WOHLverde betreut Objekte von Forst aus im Raum Bruchsal, Karlsruhe, Bretten und Umgebung: Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst mit kurzen Wegen."
    crumbs = [("Startseite", "/"), ("Einsatzgebiet", url)]
    schema = ld(crumbs_schema(crumbs), page_url=url, page_name=title, desc=desc, page_type="CollectionPage")
    places = "".join(f'<a class="place rv d{i % 4}" href="{o["slug"]}/"><b>{o["name"]}</b><span>{o["zeile"]} {ic("arrow")}</span></a>' for i, o in enumerate(ORTE))
    towns = "".join(f"<span>{t}</span>" for t in EINSATZORTE_ALLE)
    body = f'''
<section class="phead"><div class="wrap">
{crumbs_html(crumbs, d)}
<span class="eyebrow" style="color:var(--lime)">Einsatzgebiet</span>
<h1>Regional verwurzelt. Schnell vor Ort.</h1>
<p class="lead">Unser Standort liegt in Forst, direkt neben Bruchsal. Von hier aus betreuen wir Gewerbeimmobilien, Wohnanlagen und kommunale Einrichtungen im Raum Bruchsal, Karlsruhe, Bretten und Umgebung.</p>
<div class="places" style="margin-top:40px">{places}</div>
<div class="towns">{towns}</div>
</div></section>
<section class="sec"><div class="wrap split">
<div class="rv"><span class="eyebrow">Warum regional</span><h2>Kurze Wege sind die beste <span class="hl">Reaktionszeit</span>.</h2>
<p class="lead">Wenn nach einem Sturm Äste auf dem Parkplatz liegen oder im Winter früh geräumt werden muss, zählt jede Minute. Unsere Teams sind in der Region unterwegs und kennen die Objekte, die sie betreuen.</p>
<p>Ihr Objekt liegt nicht in einem der genannten Orte? Fragen Sie uns trotzdem. Wir prüfen gern, ob wir Sie zuverlässig betreuen können.</p>
{btn("../kontakt/#anfrage-form", "Anfrage stellen", "petrol")}</div>
<div class="split-media wide rv d1">{pic("team-fahrzeug", "Das WOHLverde-Team mit Fahrzeug vor einem Bürogebäude", d, "(max-width: 900px) 100vw, 50vw", w=1800, h=1200)}</div>
</div></section>
{cta_html(d)}
'''
    write("einsatzgebiet/index.html", head(title, desc, url, d, schema) + header(d, "einsatz") + body + footer(d))

def page_ort(o):
    d = 2
    url = f"/einsatzgebiet/{o['slug']}/"
    n = o["name"]
    title = f"Gebäudereinigung, Grünpflege & Hausmeister in {n} | WOHLverde"
    desc = f"Objektbetreuung in {n}: WOHLverde übernimmt Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst für Unternehmen, Hausverwaltungen und Kommunen. Festes Team aus Forst, keine Subunternehmen."
    crumbs = [("Startseite", "/"), ("Einsatzgebiet", "/einsatzgebiet/"), (n, url)]
    faqs = [
        (f"Bietet WOHLverde Gebäudereinigung und Grünpflege in {n} an?", f"Ja. {n} gehört zu unserem Einsatzgebiet. Wir übernehmen dort Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst, einzeln oder als Gesamtpaket aus einer Hand."),
        (f"Wie schnell ist WOHLverde in {n} vor Ort?", o["faq_weg"]),
        (f"Für welche Objekte in {n} ist WOHLverde der richtige Partner?", "Für Bürogebäude, Gewerbe- und Industrieflächen, Wohnanlagen von Hausverwaltungen sowie kommunale Einrichtungen. Auf Anfrage betreuen wir auch Privatkunden."),
        (f"Was kostet die Objektbetreuung in {n}?", "Jedes Objekt ist anders. Nach einem Vor-Ort-Termin erhalten Sie ein transparent kalkuliertes Angebot mit klar definierten Leistungen. Der Termin ist für Sie unverbindlich."),
    ]
    service = {"@type": "Service", "name": f"Objektbetreuung in {n}", "provider": {"@id": ORG_ID}, "areaServed": {"@type": "City", "name": n},
               "serviceType": "Grünpflege, Gebäudereinigung, Hausmeisterservice, Winterdienst"}
    schema = ld(service, crumbs_schema(crumbs), faq_schema(faqs), page_url=url, page_name=title, desc=desc)
    cards = "".join(f'<a class="place rv d{i % 4}" style="background:var(--petrol);min-height:170px" href="../../{l["url"].lstrip("/")}"><b>{l["name"]}</b><span>in {n} {ic("arrow")}</span></a>' for i, l in enumerate(LEISTUNGEN))
    body = f'''
<section class="phead"><div class="wrap phead-grid">
<div>{crumbs_html(crumbs, d)}
<span class="eyebrow" style="color:var(--lime)">Objektbetreuung in {n}</span>
<h1>Gebäudereinigung &amp; Grünpflege in {n}</h1>
<p class="lead">{o["intro"]}</p>
<div class="btns">{btn("../../kontakt/#anfrage-form", "Angebot anfragen")}<a class="btn btn--ghost" href="tel:{FIRMA["tel_int"]}"><span>{FIRMA["tel"]}</span>{ic("phone")}</a></div>
</div>
<div class="phead-media"><div class="frame grade">{pic(o["bild"], o["bild_alt"], d, "(max-width: 860px) 100vw, 45vw", eager=True)}</div><span class="chip">{o["zeile"]}</span></div>
</div></section>
<section class="sec"><div class="wrap">
<p class="kurz rv"><strong>Kurz gesagt:</strong> WOHLverde betreut Objekte in {n} mit eigenem, festangestelltem Team. Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst kommen aus einer Hand, mit festen Ansprechpartnern und dokumentierten Abläufen. {o["kurz_extra"]}</p>
<div class="head"><div><span class="eyebrow">Leistungen in {n}</span><h2>Alles, was Ihr Objekt <span class="hl">braucht</span>.</h2></div><p class="lead rv">{o["text"]}</p></div>
<div class="places">{cards}</div>
</div></section>
<section class="sec dark"><div class="wrap">
<div class="head"><div><span class="eyebrow">Darum WOHLverde in {n}</span><h2>Regional, verlässlich, <span class="hl">ohne Umwege</span>.</h2></div></div>
{feats(VORTEILE, True)}
</div></section>
<section class="sec sand"><div class="wrap faq-grid">
<div class="rv"><span class="eyebrow">Fragen aus {n}</span><h2>Gut zu wissen.</h2>{btn("../../kontakt/", "Kontakt aufnehmen", "petrol")}</div>
{faq_html(faqs)}
</div></section>
{cta_html(d, f"Objekt in {n}? Wir schauen es uns an.")}
'''
    write(f"einsatzgebiet/{o['slug']}/index.html", head(title, desc, url, d, schema, og_img=o["bild"] + ".jpg") + header(d, "einsatz") + body + footer(d))

def page_ueber():
    d = 1
    url = "/ueber-uns/"
    title = "Über uns: das Team hinter WOHLverde aus Forst | WOHLverde"
    desc = "WOHLverde, früher H&G WOHL, wurde 2020 von Nico Sica in Forst gegründet. Über 20 festangestellte Kolleginnen und Kollegen betreuen Objekte im Raum Bruchsal und Karlsruhe."
    crumbs = [("Startseite", "/"), ("Über uns", url)]
    schema = ld(crumbs_schema(crumbs), page_url=url, page_name=title, desc=desc, page_type="AboutPage")
    werte = "".join(f'<div class="rv d{i % 4}"><span class="n">{i + 1}</span><b>{t}</b><p>{x}</p></div>' for i, (t, x) in enumerate(WERTE))
    body = f'''
<section class="phead"><div class="wrap phead-grid">
<div>{crumbs_html(crumbs, d)}
<span class="eyebrow" style="color:var(--lime)">Über uns</span>
<h1>Jung, erfahren und mit <span style="color:var(--lime)">Herzblut</span> dabei.</h1>
<p class="lead">Wir sind das Team aus Forst, das sich mit Leidenschaft um Objekte in der Region kümmert. Gegründet mit einer klaren Mission: den Wert von Immobilien durch kompetente Betreuung zu steigern.</p>
</div>
<div class="phead-media"><div class="frame grade">{pic("marke-schild", "WOHLverde-Firmenschild am Standort", d, "(max-width: 860px) 100vw, 45vw", eager=True)}</div><span class="chip">Seit 2020 in Forst</span></div>
</div></section>
{ticker(["Ehrlichkeit", "Verantwortungsbewusstsein", "Wachstum", "Persönlichkeit", "Gründlichkeit", "Qualität", "Leidenschaft"])}
<section class="sec"><div class="wrap split">
<div class="rv"><span class="eyebrow">Unsere Geschichte</span><h2>Von H&amp;G WOHL zu <span class="hl">WOHLverde</span>.</h2>
<p class="lead">Gegründet im Oktober 2020, sind wir schnell gewachsen: Erst vertrauten uns Privathaushalte, bald auch namhafte Gewerbekunden und Industrieparks.</p>
<p>Mit jedem Auftrag haben wir unsere Kenntnisse und Fähigkeiten weiter ausgebaut. Heute sind wir ein komplett deutschsprachiges Team mit über 20 Kolleginnen und Kollegen. Unter dem neuen Namen WOHLverde machen wir genau so weiter wie bisher: gleiches Team, gleicher Service, gleicher Qualitätsanspruch.</p>
<p>Wir haben uns auf Gewerbe und Kommunen spezialisiert und kümmern uns vollumfänglich um das Wohl Ihrer Immobilie, in drei Kernbereichen: Grünpflege, Gebäudereinigung und Instandhaltung.</p></div>
<div class="split-media wide rv d1">{pic("team-gruppe", "Gruppenfoto des WOHLverde-Teams vor dem Bürogebäude", d, "(max-width: 900px) 100vw, 50vw", w=1800, h=1200)}</div>
</div></section>
<section class="sec--tight sand"><div class="wrap">
<figure class="quote rv">{ic("quote")}<div><blockquote>Ich habe die Firma WOHLverde im Oktober 2020 gegründet und bin unglaublich stolz, dieses Team, diese Arbeit und unsere Kunden zu vertreten. Am meisten Spaß macht mir unsere Teamkultur und das Ausbilden meines Teams.</blockquote>
<figcaption><b>Nico Sica</b>, Gründer. Verantwortlich für Optimierung, Finanzen und Vertrieb</figcaption></div></figure>
</div></section>
<section class="sec dark"><div class="wrap">
<div class="stats">
<div class="stat rv"><b data-count="20" data-suffix="+">20+</b><span>Kolleginnen und Kollegen</span></div>
<div class="stat rv d1"><b data-count="100" data-suffix=" %">100 %</b><span>deutschsprachig</span></div>
<div class="stat rv d2"><b>0</b><span>Subunternehmen</span></div>
<div class="stat rv d3"><b>2020</b><span>gegründet in Forst</span></div>
</div></div></section>
<section class="sec"><div class="wrap">
<div class="head"><div><span class="eyebrow">Unsere Werte</span><h2>Wofür wir <span class="hl">stehen</span>.</h2></div><p class="lead rv">Werte stehen bei uns nicht nur an der Wand. Sie entscheiden, wie wir arbeiten, ausbilden und miteinander umgehen.</p></div>
<div class="who">{werte}</div>
</div></section>
<section class="sec sand"><div class="wrap">
<div class="head"><div><span class="eyebrow">Das Team</span><h2>Die Menschen hinter <span class="hl">WOHLverde</span>.</h2></div><p class="lead rv">Draußen auf den Flächen, drinnen in den Gebäuden und im Büro in Forst: Bei uns arbeiten Profis, die Verantwortung übernehmen.</p></div>
<div class="insta-grid" style="grid-template-columns:repeat(4,1fr)">
{pic("reinigung-treppenhaus", "WOHLverde-Reinigungskraft im Treppenhaus", d, "25vw")}
{pic("juni-portrait-hut", "WOHLverde-Mitarbeiter im Sommer", d, "25vw")}
{pic("garten-pflanzen", "WOHLverde-Mitarbeiterin beim Pflanzen", d, "25vw")}
{pic("team-azubi", "Junger WOHLverde-Mitarbeiter im Büro", d, "25vw")}
</div></div></section>
{career_html(d)}
{cta_html(d, "Lernen wir uns kennen.")}
'''
    write("ueber-uns/index.html", head(title, desc, url, d, schema, og_img="team-gruppe.jpg") + header(d, "ueber") + body + footer(d))

def page_kontakt():
    d = 1
    url = "/kontakt/"
    title = "Kontakt & Angebot anfragen | WOHLverde Forst bei Bruchsal"
    desc = "Angebot für Grünpflege, Gebäudereinigung, Hausmeisterservice oder Winterdienst anfragen: WOHLverde, Kronauer Allee 1, 76694 Forst. Telefon 07251 3924446, info@wohlverde.de."
    crumbs = [("Startseite", "/"), ("Kontakt", url)]
    schema = ld(crumbs_schema(crumbs), page_url=url, page_name=title, desc=desc, page_type="ContactPage")
    body = f'''
<section class="phead" id="anfrage-form"><div class="wrap form-wrap">
<div>{crumbs_html(crumbs, d)}
<span class="eyebrow" style="color:var(--lime)">Kontakt</span>
<h1>Lassen Sie uns über Ihr Objekt sprechen.</h1>
<p class="lead">Schreiben Sie uns kurz, worum es geht. Wir melden uns in der Regel innerhalb eines Werktags, besprechen Ihre Anforderungen und vereinbaren einen unverbindlichen Vor-Ort-Termin.</p>
{contact_list()}
</div>
{form_html(d)}
</div></section>
<section class="sec"><div class="wrap">
<div class="head"><div><span class="eyebrow">Nach Ihrer Anfrage</span><h2>So geht es <span class="hl">weiter</span>.</h2></div></div>
{steps_html()}
</div></section>
'''
    write("kontakt/index.html", head(title, desc, url, d, schema) + header(d, "kontakt") + body + footer(d))

def page_recht(slug, title, h1, content, desc):
    d = 1
    url = f"/{slug}/"
    crumbs = [("Startseite", "/"), (h1, url)]
    schema = ld(crumbs_schema(crumbs), page_url=url, page_name=title, desc=desc)
    body = f'''
<section class="phead" style="padding-bottom:56px"><div class="wrap">{crumbs_html(crumbs, d)}<h1>{h1}</h1></div></section>
<section class="sec--tight"><div class="wrap prose">{content}</div></section>
'''
    write(f"{slug}/index.html", head(title, desc, url, d, schema).replace('content="index, follow, max-image-preview:large"', 'content="noindex, follow"') + header(d) + body + footer(d))

def page_404():
    d = 0
    html_ = head("Seite nicht gefunden | WOHLverde", "Diese Seite gibt es nicht (mehr).", "/404.html", d, "").replace('content="index, follow, max-image-preview:large"', 'content="noindex"')
    # 404 kann aus Unterordnern ausgeliefert werden: absolute Pfade verwenden
    body = f'''<section class="phead nf"><div class="wrap"><b>404</b><h1>Hier wächst leider nichts.</h1><p class="lead" style="margin:0 auto 28px">Die Seite gibt es nicht (mehr). Vielleicht hilft Ihnen einer dieser Wege weiter.</p>
<div class="btns" style="justify-content:center"><a class="btn" href="/"><span>Zur Startseite</span>{ic("arrow")}</a><a class="btn btn--ghost" href="/kontakt/"><span>Kontakt</span></a></div></div></section>'''
    out = html_ + header(d) + body + footer(d)
    out = out.replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/').replace('href="favicon', 'href="/favicon').replace('href="site.', 'href="/site.')
    for k in ["einsatzgebiet/", "ueber-uns/", "kontakt/", "impressum/", "datenschutz/", "hinweis-zur-gleichstellung/"] + [l["url"].lstrip("/") for l in LEISTUNGEN]:
        out = out.replace(f'href="{k}', f'href="/{k}')
    out = out.replace('href="" aria-label="WOHLverde Startseite"', 'href="/" aria-label="WOHLverde Startseite"')
    write("404.html", out)

def extras():
    urls = ["/"] + [l["url"] for l in LEISTUNGEN] + ["/einsatzgebiet/"] + [f"/einsatzgebiet/{o['slug']}/" for o in ORTE] + ["/ueber-uns/", "/kontakt/"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{DOMAIN}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /anfrage-senden.php\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    lines = [f"# WOHLverde", "", f"> {FIRMA['kurz']}", "",
             "WOHLverde (früher H&G WOHL) ist ein Dienstleister für Objektbetreuung mit Sitz in Forst (Baden), gegründet im Oktober 2020 von Nico Sica. "
             "Über 20 festangestellte, deutschsprachige Mitarbeitende. Keine Subunternehmen. Zielgruppe: Unternehmen, Gewerbeimmobilien, Hausverwaltungen, Industrie und Kommunen; auf Anfrage auch Privatkunden.", "",
             "## Kontakt", f"- Adresse: Kronauer Allee 1, 76694 Forst, Deutschland", f"- Telefon: {FIRMA['tel']}", f"- E-Mail: {FIRMA['mail']}",
             "- Erreichbarkeit: Montag bis Freitag 8 bis 17 Uhr, Samstag nach Vereinbarung", f"- Angebot anfragen: {DOMAIN}/kontakt/", "",
             "## Leistungen"] + [f"- [{l['name']}]({DOMAIN}{l['url']}): {l['kurz']}" for l in LEISTUNGEN] + ["",
             "## Einsatzgebiet", "Raum Bruchsal, Karlsruhe, Bretten und Umgebung: " + ", ".join(EINSATZORTE_ALLE) + ".", ""] + [f"- [{o['name']}]({DOMAIN}/einsatzgebiet/{o['slug']}/)" for o in ORTE] + ["",
             "## Häufige Fragen"] + [f"- **{q}** {a}" for q, a in FAQ_START] + ["",
             "## Weitere Seiten", f"- [Über uns]({DOMAIN}/ueber-uns/)", f"- [Karriere]({FIRMA['karriere']})", f"- [Instagram]({FIRMA['instagram']})", f"- [Impressum]({DOMAIN}/impressum/)", ""]
    write("llms.txt", "\n".join(lines))
    write("site.webmanifest", json.dumps({"name": "WOHLverde", "short_name": "WOHLverde", "start_url": "/", "display": "standalone", "background_color": "#003a41", "theme_color": "#003a41",
                                         "icons": [{"src": "/assets/img/favicon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/img/favicon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    page_home()
    for l in LEISTUNGEN: page_leistung(l)
    page_einsatz()
    for o in ORTE: page_ort(o)
    page_ueber()
    page_kontakt()
    page_recht("impressum", "Impressum | WOHLverde", "Impressum", IMPRESSUM, "Impressum von WOHLverde, Kronauer Allee 1, 76694 Forst.")
    page_recht("datenschutz", "Datenschutzerklärung | WOHLverde", "Datenschutz", DATENSCHUTZ, "Datenschutzerklärung von WOHLverde.")
    page_recht("hinweis-zur-gleichstellung", "Hinweis zur Gleichstellung | WOHLverde", "Hinweis zur Gleichstellung", GLEICHSTELLUNG, "Hinweis zur Gleichstellung.")
    page_404()
    extras()
