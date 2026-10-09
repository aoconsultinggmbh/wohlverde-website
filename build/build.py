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
VER = datetime.datetime.now().strftime("%Y%m%d%H%M")

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
ICONS["star"] = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'
ICONS["flake"] = '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M24 4v40M6.7 14l34.6 20M6.7 34l34.6-20M24 4l-5 5M24 4l5 5M24 44l-5-5M24 44l5-5M6.7 14l1.8 6.8M6.7 14l6.8-1.8M41.3 34l-1.8-6.8M41.3 34l-6.8 1.8M6.7 34l6.8 1.8M6.7 34l1.8-6.8M41.3 14l-6.8-1.8M41.3 14l-1.8 6.8"/></svg>'
def ic(n): return ICONS[n]

def art(kind, depth, cls=""):
    """Grafikflaeche mit Markenicons statt Foto. kind: garten, reinigung, werkzeug, winter."""
    import random
    p = pre(depth)
    random.seed(len(kind) * 7)
    teile = ""
    if kind == "winter":
        teile = "".join(f'<span class="flake" style="left:{random.randint(2,92)}%;top:{random.randint(-10,70)}%;width:{random.randint(14,46)}px;height:{random.randint(14,46)}px;animation-duration:{random.randint(9,18)}s;animation-delay:-{random.randint(0,12)}s;opacity:{random.choice([.35,.55,.9])}">{ICONS["flake"]}</span>' for _ in range(14))
        haupt, neben = "rechen", None
    elif kind == "garten":
        teile = "".join(f'<span class="leaf" style="left:{random.randint(2,92)}%;top:{random.randint(-10,60)}%;width:{random.randint(16,34)}px;height:{random.randint(16,34)}px;animation-duration:{random.randint(10,20)}s;animation-delay:-{random.randint(0,14)}s;opacity:{random.choice([.3,.5,.8])}">{ICONS["leaf"]}</span>' for _ in range(10))
        haupt, neben = "heckenschere", "rasenmaeher"
    elif kind == "reinigung":
        teile = "".join(f'<span class="bubble" style="left:{random.randint(4,90)}%;width:{(z:=random.randint(12,44))}px;height:{z}px;animation-duration:{random.randint(8,16)}s;animation-delay:-{random.randint(0,14)}s"></span>' for _ in range(12))
        haupt, neben = "scheibenabzieher", "spruehflasche"
    else:
        haupt, neben = "schraubenzieher", "schluessel"
    k2 = f'<img class="art-ic k2" src="{p}assets/icons/{neben}_neg.png" alt="">' if neben else ""
    return f'<div class="art {cls}" aria-hidden="true">{teile}<img class="art-ic" src="{p}assets/icons/{haupt}_neg.png" alt="">{k2}</div>'

FOCUS = {'baum-motorsaege': (47, 12), 'baum-schnitt': (75, 20), 'baum-kletterer': (55, 35), 'baum-ast': (50, 40), 'fahrzeug-transporter': (50, 45), 'garten-graeser': (50, 22), 'garten-hecke-sommer': (60, 13), 'garten-heckenschere': (45, 15), 'garten-maeher': (52, 17), 'garten-pflanzen': (48, 15), 'hausmeister-kehren': (45, 38), 'hausmeister-portrait': (50, 20), 'hausmeister-runde': (45, 22), 'hausmeister-fenster': (55, 24), 'juni-portrait-hut': (52, 22), 'marke-schild': (52, 30), 'nachher-pflaster': (50, 50), 'vorher-pflaster': (50, 50), 'objekt-abstimmung': (50, 19), 'reinigung-buero': (55, 12), 'reinigung-buero-wisch': (35, 8), 'reinigung-duo': (55, 15), 'reinigung-fenster': (52, 27), 'reinigung-fenster-ruecken': (50, 28), 'reinigung-tisch': (50, 12), 'reinigung-treppe-ruecken': (45, 16), 'reinigung-treppenhaus': (40, 30), 'team-azubi': (50, 20), 'team-baum': (50, 45), 'team-fahrzeug': (50, 45), 'team-gruppe': (50, 35), 'team-unterwegs': (50, 50)}  # Gesichtsposition in Prozent (x, y), damit kein Kopf abgeschnitten wird

def pre(depth):  # relativer Pfad zur Wurzel
    return "../" * depth

def pic(name, alt, depth, sizes="(max-width: 900px) 100vw, 50vw", eager=False, cls="", w=1200, h=1800, pos=""):
    p = pre(depth) + "assets/img/"
    load = 'fetchpriority="high" loading="eager"' if eager else 'loading="lazy"'
    return (f'<picture{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>'
            f'<source type="image/webp" srcset="{p}{name}-900.webp 900w, {p}{name}.webp {w}w" sizes="{sizes}">'
            f'<img src="{p}{name}-900.jpg" srcset="{p}{name}-900.jpg 900w, {p}{name}.jpg {w}w" sizes="{sizes}" alt="{esc(alt)}" width="{w}" height="{h}" {load} decoding="async"{(' data-focus="%d %d"' % FOCUS[name]) if name in FOCUS else ""}></picture>')

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
      "sameAs": [FIRMA["instagram"], FIRMA["facebook"], FIRMA["karriere"], FIRMA["google"]],
      "hasMap": FIRMA["google"],
      "geo": {"@type": "GeoCoordinates", "latitude": 49.1544712, "longitude": 8.5799538},
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
def head(title, desc, url, depth, schema, og_img="og-wohlverde.jpg", light=False):
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
<link rel="stylesheet" href="{p}assets/css/style.css?v={VER}">
{schema}
</head>
<body class="mix">
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
'''

def header(depth, active=""):
    p = pre(depth)
    def a(href, text, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{p}{href}"{cur}>{text}</a>'
    dd = "".join(f'<a href="{p}{l["url"].lstrip("/")}"><img src="{p}assets/icons/{l["icon"]}_pos.png" alt="" width="34" height="34"><span>{l["name"]}<small>{l["dd"]}</small></span></a>' for l in LEISTUNGEN)
    dd_orte = "".join(f'<a href="{p}einsatzgebiet/{o["slug"]}/"><span class="pin">{ic("pin")}</span><span>{o["name"]}<small>{o["zeile"]}</small></span></a>' for o in ORTE) + f'<a class="dd-all" href="{p}einsatzgebiet/"><span>Alle Orte im Überblick</span>{ic("arrow")}</a>'
    return f'''<header class="top">
<div class="wrap">
<a class="logo" href="{p}" aria-label="WOHLverde Startseite"><img class="l-light" src="{p}assets/img/logo-neg.png" alt="WOHLverde Grünpflege und Gebäudereinigung" width="1212" height="265"><img class="l-dark" src="{p}assets/img/logo-pos.png" alt="WOHLverde Grünpflege und Gebäudereinigung" width="1212" height="265"></a>
<button class="burger" aria-label="Menü öffnen" aria-expanded="false" aria-controls="hauptnav"><span></span><span></span><span></span></button>
<nav class="nav" id="hauptnav" aria-label="Hauptnavigation">
<div class="dd"><button class="navbtn" aria-expanded="false" aria-haspopup="true">Leistungen <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dd-menu">{dd}</div></div>
<div class="dd"><button class="navbtn" aria-expanded="false" aria-haspopup="true">Einsatzgebiet <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dd-menu dd-orte">{dd_orte}</div></div>
<div class="dd"><button class="navbtn" aria-expanded="false" aria-haspopup="true">Über uns <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dd-menu dd-orte"><a href="{p}ueber-uns/"><span class="pin">{ic("users")}</span><span>Über uns<small>Team, Werte, Geschichte</small></span></a><a href="{p}referenzen/"><span class="pin">{ic("star")}</span><span>Referenzen<small>Kunden und Ergebnisse</small></span></a><a href="{p}ratgeber/"><span class="pin">{ic("doc")}</span><span>Ratgeber<small>Wissen für Objektverantwortliche</small></span></a><a href="{p}ratgeber/glossar/"><span class="pin">{ic("layers")}</span><span>Glossar<small>{len(GLOSSAR)} Fachbegriffe erklärt</small></span></a></div></div>
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
    lst = "".join(f'<li><a href="{p}{l["url"].lstrip("/")}">{l["name"]}</a></li>' for l in LEISTUNGEN) + "".join(f'<li class="sub"><a href="{p}{dt["parent"].lstrip("/")}{dt["slug"]}/">{dt["name"]}</a></li>' for dt in DETAILS)
    orte = "".join(f'<li><a href="{p}einsatzgebiet/{o["slug"]}/">{o["name"]}</a></li>' for o in ORTE)
    return f'''</main>
<footer class="foot">
<div class="wrap">
<div class="foot-grid">
<div>
<a class="flogo-link" href="{p}" aria-label="WOHLverde Startseite"><img class="flogo" src="{p}assets/img/logo-neg.png" alt="WOHLverde Logo" width="1212" height="265" loading="lazy"></a>
<p>Grünpflege, Gebäudereinigung und Hausmeisterservice für Unternehmen, Hausverwaltungen und Kommunen im Raum Bruchsal, Karlsruhe und Bretten.</p>
<p>Aus <strong>H&amp;G WOHL</strong> wurde <strong>WOHLverde</strong>: gleiches Team, gleicher Anspruch.</p>
<div class="soc"><a href="{FIRMA["instagram"]}" rel="noopener" aria-label="WOHLverde auf Instagram">{ic("insta")}</a><a href="{FIRMA["facebook"]}" rel="noopener" aria-label="WOHLverde auf Facebook">{ic("fb")}</a></div>
</div>
<div><h4>Leistungen</h4><ul>{lst}</ul></div>
<div><h4>Einsatzgebiet</h4><ul>{orte}<li><a href="{p}einsatzgebiet/">Alle Orte</a></li></ul><h4 style="margin-top:28px">WOHLverde</h4><ul><li><a href="{p}ueber-uns/">Über uns</a></li><li><a href="{p}referenzen/">Referenzen</a></li><li><a href="{p}ratgeber/">Ratgeber</a></li><li><a href="{p}ratgeber/glossar/">Glossar</a></li></ul></div>
<div><h4>Kontakt</h4><ul>
<li>WOHLverde<br>Kronauer Allee 1<br>76694 Forst</li>
<li><a href="tel:{FIRMA["tel_int"]}">{FIRMA["tel"]}</a></li>
<li><a href="mailto:{FIRMA["mail"]}">{FIRMA["mail"]}</a></li>
<li>Mo bis Fr: 8 bis 17 Uhr<br>Sa: nach Vereinbarung</li>
</ul></div>
</div>
<div class="foot-bottom">
<span>© <span data-year>2026</span> WOHLverde, Forst</span>
<nav aria-label="Rechtliches"><a href="{p}impressum/" target="_blank">Impressum</a><a href="{p}datenschutz/" target="_blank">Datenschutz</a><a href="{p}hinweis-zur-gleichstellung/" target="_blank">Hinweis zur Gleichstellung</a><a href="#" data-einwilligung hidden>Cookie-Einstellungen</a><a href="{FIRMA["karriere"]}" rel="noopener">Karriere</a></nav>
</div>
</div>
<span class="mark" aria-hidden="true">WOHLverde</span>
</footer>
<div class="mbar" aria-label="Schnellkontakt"><a class="m1" href="tel:{FIRMA["tel_int"]}">{ic("phone")}Anrufen</a><a class="m2" href="{p}kontakt/#anfrage-form">Angebot anfragen</a></div>
<script src="{p}assets/js/ao-konfiguration.js?v={VER}"></script>
<script src="{p}assets/js/einwilligung.js?v={VER}"></script>
<script src="{p}assets/js/app.js?v={VER}" defer></script>
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
    """Ablauf als Zeitstrahl: Linie fuellt sich beim Scrollen, je Schritt ein Icon."""
    icons = ["chat", "users", "doc", "shield"]
    items = "".join(f'''<li class="tl-item rv d{i}"><span class="tl-dot">{ic(icons[i])}<em>{i+1}</em></span><h3>{t}</h3><p>{x}</p></li>''' for i, (t, x) in enumerate(ABLAUF))
    return f'<div class="timeline{" timeline--dark" if dark else ""}"><span class="tl-line"><span class="tl-fill"></span></span><ol>{items}</ol></div>'

def steps_kacheln(dark=False):
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
<p class="form-titel">Anfrage für Ihr Objekt</p>
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
<input type="hidden" name="ts" value=""><input type="hidden" name="seite" value=""><input type="hidden" name="kampagne" value="">
<div class="fld req" style="margin:0"><label class="consent"><input type="checkbox" name="datenschutz" value="ja" required><span>Ich bin einverstanden, dass meine Angaben zur Bearbeitung der Anfrage verwendet werden. Mehr dazu in der <a href="{p}datenschutz/" target="_blank">Datenschutzerklärung</a>. *</span></label><span class="err">Bitte stimmen Sie der Verarbeitung zu.</span></div>
<button class="btn btn--petrol" type="submit" style="width:100%"><span>Anfrage senden</span>{ic("arrow")}</button>
<div class="form-msg" role="status" aria-live="polite"></div>
</form>'''

def form_section(depth, title="Lassen Sie uns über Ihr Objekt sprechen.", text="Schreiben Sie uns kurz, worum es geht. Wir melden uns in der Regel innerhalb eines Werktags und vereinbaren einen unverbindlichen Vor-Ort-Termin."):
    return f'''<section class="sec dark" id="anfrage-form"><div class="wrap form-wrap">
<div class="rv"><span class="eyebrow">Angebot anfragen</span><h2>{title}</h2><p class="lead">{text}</p>{rating("on-dark")}{contact_list()}</div>
<div class="rv d1">{form_html(depth)}</div>
</div></section>'''

def live(cls=""):
    """Live-Anzeige "Jetzt erreichbar" (Mo bis Fr 8 bis 17 Uhr), wird in app.js berechnet."""
    return f'<span class="live {cls}" data-live><i></i><span>Mo bis Fr 8 bis 17 Uhr erreichbar</span></span>'

def rating(cls=""):
    st = ic("star") * 5
    return f'<a class="rating {cls}" href="{FIRMA["google"]}" rel="noopener" aria-label="{FIRMA["sterne"]} von 5 Sternen bei {FIRMA["rezensionen"]} Google-Rezensionen ansehen"><span class="stars">{st}</span><b>{FIRMA["sterne"]}</b><span>{FIRMA["rezensionen"]} Google-Rezensionen</span></a>'

def contact_list():
    return f'''<ul class="contact-list">
<li><i>{ic("phone")}</i><div><small>Telefon</small><a href="tel:{FIRMA["tel_int"]}">{FIRMA["tel"]}</a></div></li>
<li><i>{ic("mail")}</i><div><small>E-Mail</small><a href="mailto:{FIRMA["mail"]}">{FIRMA["mail"]}</a></div></li>
<li><i>{ic("pin")}</i><div><small>Standort</small><a href="https://www.google.com/maps/search/?api=1&amp;query=WOHLverde+Kronauer+Allee+1+76694+Forst" rel="noopener">Kronauer Allee 1, 76694 Forst</a></div></li>
<li><i>{ic("clock")}</i><div><small>Erreichbarkeit</small><strong>Mo bis Fr 8 bis 17 Uhr, Sa nach Vereinbarung</strong><br>{live("klein")}</div></li>
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

def neuer_tab(html_):
    """Externe Links (Instagram, Facebook, Google, Karriere, AO) oeffnen in neuem Tab, damit Besucher auf der Seite bleiben."""
    import re as _re
    def f(m):
        tag = m.group(0)
        if "target=" in tag: return tag
        tag = tag.replace(' rel="noopener"', "")
        return tag[:-1] + ' target="_blank" rel="noopener">'
    return _re.sub(r'<a [^>]*href="https?://[^"]*"[^>]*>', f, html_)

def write(path, content):
    if path.endswith(".html"): content = neuer_tab(content)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("geschrieben", path)

# ---------- Seiten ----------
def page_home():
    """Startseite 3.0: Mischung aus erster und zweiter Fassung zum Vergleich (noindex, nicht in der Sitemap)."""
    d = 0
    title = "Grünpflege & Gebäudereinigung Bruchsal & Karlsruhe | WOHLverde"
    desc = "Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst für Gewerbe, Hausverwaltungen und Kommunen im Raum Bruchsal und Karlsruhe. 5,0 Sterne bei Google."
    schema = ld(faq_schema(FAQ_START), page_url="/", page_name=title, desc=desc)
    cls = ["c-a", "c-b", "c-c", "c-d"]
    cards = "".join(f'''<a class="card {cls[i]} art rv d{i % 2}" href="{l["url"].lstrip("/")}">{art(l["art"], d)}
<span class="ic"><img src="assets/icons/{l["icon"]}_neg.png" alt="" width="38" height="38"></span>
<h3>{l["name"]}</h3><p>{l["teaser"]}</p><span class="more">Mehr erfahren {ic("arrow")}</span></a>''' for i, l in enumerate(LEISTUNGEN))
    who = "".join(f"<span>{t}</span>" for t, _ in ZIELGRUPPEN)
    places = "".join(f'<a class="place rv d{i % 4}" href="einsatzgebiet/{o["slug"]}/"><b>{o["name"]}</b><span>{o["zeile"]} {ic("arrow")}</span></a>' for i, o in enumerate(ORTE))
    body = f'''
<section class="hero">
<span class="blob b-a"></span><span class="blob b-b"></span>
<div class="wrap hero-grid">
<div>
<span class="eyebrow" style="color:var(--lime)">Grünpflege &amp; Gebäudereinigung im Raum Bruchsal &amp; Karlsruhe</span>
<h1 class="wordsplit">Wir pflegen, was <span class="l">Werte</span> schafft.</h1>
<p class="h1-sub">Drinnen wie draußen.</p>
<p class="lead">Objektbetreuung für Gewerbeimmobilien, Industrieflächen, Wohnanlagen und Kommunen. Mit festen Teams, festen Ansprechpartnern und dokumentierten Abläufen.</p>
<div class="btns">{btn("#anfrage-form", "Angebot anfragen")}<a class="btn btn--ghost" href="#leistungen"><span>Leistungen entdecken</span></a></div>
<div class="hero-meta"><a class="hero-call" href="tel:{FIRMA["tel_int"]}"><i>{ic("phone")}</i><span><small>Direkt sprechen</small>{FIRMA["tel"]}</span></a>{live()}</div>
</div>
<div class="hero-media">
<div class="frame grade">{pic("garten-heckenschere", "Lächelnder WOHLverde-Mitarbeiter mit Heckenschere auf einer Gewerbefläche", d, "(max-width: 960px) 100vw, 40vw", eager=True)}</div>
<div class="badge b1"><img src="assets/icons/heckenschere_pos.png" alt="" width="36" height="36"><span><b>20+</b>Profis im Team</span></div>
<a class="badge b3 badge-rating" href="{FIRMA["google"]}" rel="noopener"><span><span class="stars">{ic("star")*5}</span><b>{FIRMA["sterne"]}</b>{FIRMA["rezensionen"]} Google-Rezensionen</span></a>
</div>
</div>
<div class="wrap hero-strip"><ul>
<li>Festangestellte, deutschsprachige Teams</li><li>Keine Subunternehmen</li><li>Dokumentierte Objektkontrollen</li><li>Seit 2020 in der Region</li>
</ul></div>
</section>
{ticker(["Grünpflege", "Gebäudereinigung", "Hausmeisterservice", "Winterdienst", "Baumpflege", "Glasreinigung", "Unterhaltsreinigung", "Objektbetreuung"])}

<section class="sec" id="leistungen"><div class="wrap">
<div class="kopf2"><div class="rv"><span class="eyebrow">Unsere Leistungen</span><h2>Ein Partner für Ihr <span class="hl">ganzes Objekt</span>.</h2></div>
<div class="rv d1"><p class="lead">WOHLverde ist ein Dienstleister für Objektbetreuung aus Forst bei Bruchsal. Wir übernehmen Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst für Unternehmen, Hausverwaltungen und Kommunen im Raum Bruchsal, Karlsruhe und Bretten, ausschließlich mit eigenem, festangestelltem Personal.</p><div class="fuer">{who}</div></div></div>
<div class="bento">{cards}</div>
</div></section>

<section class="sec dark"><div class="wrap split">
<div class="rv"><span class="eyebrow">Warum WOHLverde</span><h2>Bei uns kennen Sie die Menschen, die bei Ihnen arbeiten.</h2>
<p class="lead">Kein Wechselpersonal, keine Subunternehmen. Feste Teams, feste Ansprechpartner und regelmäßige Objektkontrollen mit Protokoll. So bleibt Qualität planbar.</p>
<div class="stats stats--2">
<div class="stat"><b data-count="20" data-suffix="+">20+</b><span>Kolleginnen und Kollegen</span></div>
<div class="stat"><b>0</b><span>Subunternehmen</span></div>
<div class="stat"><b data-count="100" data-suffix=" %">100 %</b><span>festangestellt</span></div>
<div class="stat"><b>2020</b><span>gegründet in Forst</span></div>
</div></div>
<div class="split-media rv d1"><div class="frame grade reveal-img" style="border-radius:var(--radius)">{pic("team-gruppe", "Gruppenfoto des WOHLverde-Teams vor einem Bürogebäude", d, "(max-width: 900px) 100vw, 50vw", w=1800, h=1200)}</div></div>
</div></section>

<section class="sec"><div class="wrap split">
<div class="split-media rv"><div class="frame grade para reveal-img">{pic("objekt-abstimmung", "Zwei WOHLverde-Mitarbeitende dokumentieren eine Objektkontrolle auf dem Tablet", d)}</div><span class="tag">Dokumentiert statt versprochen</span></div>
<div class="rv d1"><span class="eyebrow">Objektservice für Gewerbe</span><h2>Wir sehen hin, bevor es teuer wird.</h2>
<p class="lead">Regelmäßige Objektkontrollen mit Dokumentation, laufende Instandhaltung und schnelle Reaktion: So bleibt Ihre Immobilie funktional, sicher und im Wert erhalten.</p>
<ul class="checks cols"><li>Feste Teams und Ansprechpartner</li><li>Schnelle Reaktionszeiten</li><li>Objektkontrollen mit Protokoll</li><li>Kleinreparaturen und Instandhaltung</li></ul>
{btn("hausmeister-service/", "Zum Hausmeisterservice", "petrol")}</div>
</div></section>

<section class="sec sand"><div class="wrap vn">
<div class="rv"><span class="eyebrow">Vorher und nachher</span><h2>Ergebnisse, die man <span class="hl">sieht</span>.</h2>
<p class="lead">Unkrautbeseitigung auf der Pflasterfläche eines Firmengeländes. Gleiche Stelle, ein Arbeitseinsatz.</p>
{btn("garten-und-landschaftspflege/", "Zur Grünpflege", "petrol")}</div>
<div class="vn-pics">
<figure class="rv">{pic("vorher-pflaster", "Pflasterfläche mit Unkraut in den Fugen, vor dem Einsatz", d, "(max-width: 900px) 50vw, 25vw", w=1050, h=1400)}<span class="lbl l1">Vorher</span></figure>
<figure class="rv d2">{pic("nachher-pflaster", "Dieselbe Pflasterfläche nach der Unkrautbeseitigung", d, "(max-width: 900px) 50vw, 25vw", w=1050, h=1400)}<span class="lbl l2">Nachher</span></figure>
</div>
</div></section>

<section class="sec--tight"><div class="wrap">
<div class="trust">{rating("big")}<p class="eyebrow" style="margin:0">Unternehmen und Einrichtungen, die uns vertrauen</p></div>
{refs_html()}
</div></section>

<section class="sec"><div class="wrap">
<div class="mitte rv"><span class="eyebrow">So läuft die Zusammenarbeit</span><h2>Vier Schritte. Ein fester Ansprechpartner.</h2></div>
{steps_html()}
</div></section>

<div class="big-ticker" aria-hidden="true"><div class="ticker-in">{"".join(f"<span>{t}</span>" for t in ["Grünpflege","Gebäudereinigung","Hausmeisterservice","Winterdienst"]*2)}</div></div>

<section class="sec dark"><div class="wrap">
<div class="mitte rv"><span class="eyebrow">Einsatzgebiet</span><h2>Zu Hause in Forst. Schnell vor Ort in der Region.</h2></div>
<div class="places">{places}</div>
<div class="towns rv" style="justify-content:center">{"".join(f"<span>{t}</span>" for t in EINSATZORTE_ALLE)}</div>
</div></section>

<section class="sec sand"><div class="wrap faq-grid">
<div class="rv"><span class="eyebrow">Häufige Fragen</span><h2>Kurz und klar beantwortet.</h2><p class="lead">Ihre Frage ist nicht dabei? Rufen Sie uns an, wir antworten gern persönlich.</p></div>
{faq_html(FAQ_START)}
</div></section>

{insta_html(d)}
<section class="sec--tight"><div class="wrap">
<a class="streifen-item lime rv" href="{FIRMA["karriere"]}" rel="noopener">{ic("users")}<span><small>Karriere bei WOHLverde</small>Mach mit. Feste Teams, echte Perspektiven, auch für Quereinsteiger.</span>{ic("arrow")}</a>
</div></section>

{form_section(d)}
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
    DMAP = {"Hecken- und Gehölzschnitt": "heckenschnitt", "Baumpflege": "baumpflege", "Unkrautbeseitigung": "unkrautbeseitigung",
            "Unterhalts- und Büroreinigung": "unterhaltsreinigung", "Treppenhausreinigung": "treppenhausreinigung", "Glas- und Fensterreinigung": "glasreinigung"}
    def feat(i, t, x):
        inner = f'<div class="ic"><img src="../assets/icons/{l["icon"]}_neg.png" alt="" width="36" height="36"></div><div><h3>{t}</h3><p>{x}</p>'
        if t in DMAP:
            return f'<a class="feat feat--link rv d{i % 2}" href="{DMAP[t]}/">{inner}<span class="more">Mehr erfahren {ic("arrow")}</span></div></a>'
        return f'<div class="feat rv d{i % 2}">{inner}</div></div>'
    punkte = "".join(feat(i, t, x) for i, (t, x) in enumerate(l["punkte"]))
    others = [o for o in LEISTUNGEN if o["url"] != url]
    other = "".join(f'<a class="place place--solid rv d{i}" href="../{o["url"].lstrip("/")}"><b>{o["name"]}</b><span>{o["dd"]} {ic("arrow")}</span></a>' for i, o in enumerate(others))
    body = f'''
<section class="phead"><div class="wrap phead-grid">
<div>{crumbs_html(crumbs, d)}
<span class="eyebrow" style="color:var(--lime)">{l["eyebrow"]}</span>
<h1>{l["h1"]}</h1>
<p class="lead">{l["intro"]}</p>
<div class="btns">{btn("../kontakt/#anfrage-form", "Angebot anfragen")}<a class="btn btn--ghost" href="tel:{FIRMA["tel_int"]}"><span>{FIRMA["tel"]}</span>{ic("phone")}</a></div>
<div style="margin-top:22px">{rating("on-dark")}</div>
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
{form_section(d, f"Angebot für {l['name']} anfragen.")}
'''
    write(url.strip("/") + "/index.html", head(title, desc, url, d, schema, og_img=l["bild"] + ".jpg") + header(d) + body + footer(d))

def page_einsatz():
    d = 1
    url = "/einsatzgebiet/"
    title = "Einsatzgebiet Bruchsal, Karlsruhe, Bretten | WOHLverde"
    desc = "WOHLverde betreut Objekte von Forst aus im Raum Bruchsal, Karlsruhe und Bretten: Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst."
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
    title = f"Gebäudereinigung & Grünpflege {n} | WOHLverde"
    desc = f"Objektbetreuung in {n}: Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst für Gewerbe, Hausverwaltungen und Kommunen. Festes Team aus Forst."
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
    cards = "".join(f'<a class="place place--solid rv d{i % 4}" href="../../{l["url"].lstrip("/")}"><b>{l["name"]}</b><span>in {n} {ic("arrow")}</span></a>' for i, l in enumerate(LEISTUNGEN))
    body = f'''
<section class="phead"><div class="wrap phead-grid">
<div>{crumbs_html(crumbs, d)}
<span class="eyebrow" style="color:var(--lime)">Objektbetreuung in {n}</span>
<h1>Gebäudereinigung &amp; Grünpflege in {n}</h1>
<p class="lead">{o["intro"]}</p>
<div class="btns">{btn("../../kontakt/#anfrage-form", "Angebot anfragen")}<a class="btn btn--ghost" href="tel:{FIRMA["tel_int"]}"><span>{FIRMA["tel"]}</span>{ic("phone")}</a></div>
<div style="margin-top:22px">{rating("on-dark")}</div>
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
{form_section(d, f"Objekt in {n}? Wir schauen es uns an.")}
'''
    write(f"einsatzgebiet/{o['slug']}/index.html", head(title, desc, url, d, schema, og_img=o["bild"] + ".jpg") + header(d, "einsatz") + body + footer(d))

def page_ueber():
    d = 1
    url = "/ueber-uns/"
    title = "Über uns: das Team hinter WOHLverde aus Forst | WOHLverde"
    desc = "WOHLverde, früher H&G WOHL, 2020 von Nico Sica in Forst gegründet: über 20 festangestellte Profis für Objektbetreuung im Raum Bruchsal und Karlsruhe."
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

def page_detail(dt):
    d = 2
    parent = next(l for l in LEISTUNGEN if l["url"] == dt["parent"])
    url = dt["parent"] + dt["slug"] + "/"
    crumbs = [("Startseite", "/"), (parent["name"], dt["parent"]), (dt["name"], url)]
    service = {"@type": "Service", "@id": DOMAIN + url + "#leistung", "name": dt["name"], "serviceType": dt["name"], "description": dt["kurz"],
               "provider": {"@id": ORG_ID}, "isRelatedTo": {"@type": "Service", "name": parent["name"], "url": DOMAIN + parent["url"]},
               "areaServed": [{"@type": "City", "name": o} for o in EINSATZORTE_ALLE]}
    schema = ld(service, crumbs_schema(crumbs), faq_schema(dt["faq"]), page_url=url, page_name=dt["title"], desc=dt["desc"])
    umfang = "".join(f"<li>{u}</li>" for u in dt["umfang"])
    fuer = "".join(f"<span>{f}</span>" for f in dt["fuer"])
    geschw = [x for x in DETAILS if x["parent"] == dt["parent"] and x["slug"] != dt["slug"]]
    rel = "".join(f'<a class="place place--solid rv d{i}" href="../{x["slug"]}/"><b>{x["name"]}</b><span>Mehr erfahren {ic("arrow")}</span></a>' for i, x in enumerate(geschw))
    rel += f'<a class="place place--solid rv d{len(geschw)}" href="../"><b>Alles zu {parent["name"]}</b><span>Übersicht {ic("arrow")}</span></a>'
    vn = ""
    if dt.get("vn"):
        vn = f"""<section class="sec sand"><div class="wrap vn">
<div class="rv"><span class="eyebrow">Vorher und nachher</span><h2>Ergebnisse, die man <span class="hl">sieht</span>.</h2><p class="lead">Pflasterfläche auf einem Firmengelände. Gleiche Stelle, ein Arbeitseinsatz.</p></div>
<div class="vn-pics"><figure class="rv">{pic("vorher-pflaster", "Pflasterfläche mit Unkraut, vor dem Einsatz", d, "(max-width: 900px) 50vw, 25vw", w=1050, h=1400)}<span class="lbl l1">Vorher</span></figure>
<figure class="rv d2">{pic("nachher-pflaster", "Dieselbe Pflasterfläche nach der Unkrautbeseitigung", d, "(max-width: 900px) 50vw, 25vw", w=1050, h=1400)}<span class="lbl l2">Nachher</span></figure></div>
</div></section>"""
    body = f"""
<section class="phead"><div class="wrap phead-grid">
<div>{crumbs_html(crumbs, d)}
<span class="eyebrow" style="color:var(--lime)">{parent["name"]}</span>
<h1>{dt["h1"]}</h1>
<p class="lead">{dt["intro"]}</p>
<div class="btns">{btn("#anfrage-form", "Angebot anfragen")}<a class="btn btn--ghost" href="tel:{FIRMA["tel_int"]}"><span>{FIRMA["tel"]}</span>{ic("phone")}</a></div>
<div style="margin-top:22px">{rating("on-dark")}</div>
</div>
<div class="phead-media"><div class="frame grade">{pic(dt["bild"], dt["bild_alt"], d, "(max-width: 860px) 100vw, 45vw", eager=True, w=1200, h=1600 if dt["bild"]=="baum-kletterer" else 1800)}</div><span class="chip">Raum Bruchsal &amp; Karlsruhe</span></div>
</div></section>

<section class="sec"><div class="wrap split">
<div class="rv"><span class="eyebrow">Leistungsumfang</span><h2>Was dazugehört</h2>
<p class="kurz"><strong>Kurz gesagt:</strong> {dt["kurz"]}</p>
<ul class="checks cols">{umfang}</ul>
<p style="margin:26px 0 10px;font-weight:700;color:var(--petrol)">Für wen</p><div class="fuer" style="justify-content:flex-start;margin:0">{fuer}</div></div>
<div class="split-media rv d1"><div class="frame grade para reveal-img">{pic(dt["bild2"], dt["bild2_alt"], d)}</div></div>
</div></section>
{vn}
<section class="sec dark"><div class="wrap">
<div class="mitte rv"><span class="eyebrow">Ablauf</span><h2>So starten wir gemeinsam.</h2></div>
{steps_html(True)}
</div></section>

<section class="sec"><div class="wrap faq-grid">
<div class="rv"><span class="eyebrow">Fragen und Antworten</span><h2>{dt["name"]}: gut zu wissen.</h2></div>
{faq_html(dt["faq"])}
</div></section>

<section class="sec--tight sand"><div class="wrap">
<span class="eyebrow">Weitere Leistungen</span><h2 style="margin-bottom:28px">Passt dazu</h2>
<div class="places places--3">{rel}</div>
</div></section>
{form_section(d, f"Angebot für {dt['name']} anfragen.")}
"""
    write(url.strip("/") + "/index.html", head(dt["title"], dt["desc"], url, d, schema, og_img=dt["bild"] + ".jpg") + header(d) + body + footer(d))

def page_referenzen():
    d = 1
    url = "/referenzen/"
    title = "Referenzen: Kunden und Ergebnisse | WOHLverde"
    desc = "Unternehmen und Einrichtungen, die WOHLverde vertrauen, 5,0 Sterne bei Google und Ergebnisse aus der Praxis. Objektbetreuung im Raum Bruchsal und Karlsruhe."
    crumbs = [("Startseite", "/"), ("Referenzen", url)]
    schema = ld(crumbs_schema(crumbs), page_url=url, page_name=title, desc=desc, page_type="CollectionPage")
    kunden = "".join(f'<div class="kunde rv d{i % 4}"><span class="pin">{ic("shield")}</span><b>{k}</b></div>' for i, k in enumerate(REFERENZEN))
    body = f"""
<section class="phead"><div class="wrap phead-grid">
<div>{crumbs_html(crumbs, d)}
<span class="eyebrow" style="color:var(--lime)">Referenzen</span>
<h1>Vertrauen, das man nachlesen kann.</h1>
<p class="lead">Unternehmen, Einrichtungen und Hausverwaltungen aus der Region verlassen sich auf WOHLverde. Und bei Google stehen wir bei {FIRMA["sterne"]} Sternen.</p>
<div style="margin-top:22px">{rating("on-dark")}</div>
</div>
<div class="phead-media"><div class="frame grade">{pic("team-gruppe", "Das WOHLverde-Team", d, "(max-width: 860px) 100vw, 45vw", eager=True, w=1800, h=1200)}</div><span class="chip">Seit 2020 in der Region</span></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="kopf2"><div class="rv"><span class="eyebrow">Unsere Kunden</span><h2>Diese Unternehmen und Einrichtungen vertrauen uns.</h2></div>
<div class="rv d1"><p class="lead">Eine Auswahl unserer Kunden, die einer Nennung als Referenz zugestimmt haben. Gern stellen wir auf Anfrage den Kontakt zu Referenzkunden her.</p></div></div>
<div class="kunden">{kunden}</div>
</div></section>

<section class="sec sand"><div class="wrap vn">
<div class="rv"><span class="eyebrow">Ergebnisse</span><h2>Vorher und <span class="hl">nachher</span>.</h2>
<p class="lead">Unkrautbeseitigung auf der Pflasterfläche eines Firmengeländes. Gleiche Stelle, ein Arbeitseinsatz.</p>
{btn("../garten-und-landschaftspflege/unkrautbeseitigung/", "Zur Unkrautbeseitigung", "petrol")}</div>
<div class="vn-pics"><figure class="rv">{pic("vorher-pflaster", "Pflasterfläche mit Unkraut, vor dem Einsatz", d, "(max-width: 900px) 50vw, 25vw", w=1050, h=1400)}<span class="lbl l1">Vorher</span></figure>
<figure class="rv d2">{pic("nachher-pflaster", "Dieselbe Pflasterfläche nach der Unkrautbeseitigung", d, "(max-width: 900px) 50vw, 25vw", w=1050, h=1400)}<span class="lbl l2">Nachher</span></figure></div>
</div></section>

<section class="sec dark"><div class="wrap split">
<div class="rv"><span class="eyebrow">Google-Bewertungen</span><h2>{FIRMA["sterne"]} von 5 Sternen.</h2>
<p class="lead">Bei {FIRMA["rezensionen"]} Rezensionen auf Google. Lesen Sie selbst, was unsere Kunden über die Zusammenarbeit sagen.</p>
{btn(FIRMA["google"], "Bewertungen bei Google lesen")}</div>
<div class="rv d1" style="text-align:center"><div class="big-stars">{ic("star")*5}</div><p class="big-score">{FIRMA["sterne"]}</p></div>
</div></section>
{insta_html(d)}
{form_section(d, "Werden Sie unsere nächste Referenz.")}
"""
    write("referenzen/index.html", head(title, desc, url, d, schema, og_img="team-gruppe.jpg") + header(d, "ueber") + body + footer(d))

def page_ratgeber_index():
    d = 1
    url = "/ratgeber/"
    title = "Ratgeber für Objektverantwortliche | WOHLverde"
    desc = "Wissen rund um Gebäudereinigung, Grünpflege und Winterdienst für Unternehmen, Hausverwaltungen und Kommunen. Kurz und verständlich erklärt von WOHLverde."
    crumbs = [("Startseite", "/"), ("Ratgeber", url)]
    schema = ld(crumbs_schema(crumbs), page_url=url, page_name=title, desc=desc, page_type="CollectionPage")
    karten = "".join(f'<a class="artikel rv d{i}" href="{a["slug"]}/"><div class="frame">{pic(a["bild"], a["bild_alt"], d, "(max-width: 900px) 100vw, 33vw")}</div><div class="artikel-txt"><h2>{a["title"]}</h2><p>{a["teaser"]}</p><span class="more">Weiterlesen {ic("arrow")}</span></div></a>' for i, a in enumerate(RATGEBER))
    body = f"""
<section class="phead" style="padding-bottom:56px"><div class="wrap">{crumbs_html(crumbs, d)}
<span class="eyebrow" style="color:var(--lime)">Ratgeber</span><h1>Wissen für Objektverantwortliche.</h1>
<p class="lead">Kurze Antworten auf Fragen, die uns Unternehmen, Hausverwaltungen und Kommunen oft stellen.</p></div></section>
<section class="sec"><div class="wrap">
<a class="glossar-teaser rv" href="glossar/"><span class="pin">{ic("doc")}</span><span><small>Glossar</small><b>{len(GLOSSAR)} Fachbegriffe kurz erklärt</b>Von Bauendreinigung bis Winterdienst</span>{ic("arrow")}</a>
<div class="artikel-grid">{karten}</div></div></section>
{form_section(d)}
"""
    write("ratgeber/index.html", head(title, desc, url, d, schema) + header(d, "ueber") + body + footer(d))

def page_ratgeber(a):
    d = 2
    url = f"/ratgeber/{a['slug']}/"
    crumbs = [("Startseite", "/"), ("Ratgeber", "/ratgeber/"), (a["title"], url)]
    art_schema = {"@type": "Article", "headline": a["title"], "description": a["desc"], "datePublished": "2026-10-09", "dateModified": TODAY,
                  "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}, "image": DOMAIN + "/assets/img/" + a["bild"] + ".jpg",
                  "mainEntityOfPage": DOMAIN + url, "inLanguage": "de-DE"}
    schema = ld(art_schema, crumbs_schema(crumbs), page_url=url, page_name=a["title"] + " | WOHLverde", desc=a["desc"])
    teile = "".join(f"<h2>{h}</h2><p>{t}</p>" for h, t in a["abschnitte"])
    def name_fuer(u):
        for l in LEISTUNGEN:
            if l["url"] == u: return l["name"]
        for dt in DETAILS:
            if dt["parent"] + dt["slug"] + "/" == u: return dt["name"]
        return u
    links = "".join(f'<a class="place place--solid rv d{i}" href="../..{u}"><b>{name_fuer(u)}</b><span>Zur Leistung {ic("arrow")}</span></a>' for i, u in enumerate(a["links"]))
    andere = "".join(f'<li><a href="../{x["slug"]}/">{x["title"]}</a></li>' for x in RATGEBER if x["slug"] != a["slug"])
    body = f"""
<section class="phead" style="padding-bottom:56px"><div class="wrap phead-grid">
<div>{crumbs_html(crumbs, d)}<span class="eyebrow" style="color:var(--lime)">Ratgeber</span><h1 style="font-size:clamp(32px,3.6vw,56px)">{a["title"]}</h1>
<p class="lead">{a["teaser"]}</p></div>
<div class="phead-media"><div class="frame grade">{pic(a["bild"], a["bild_alt"], d, "(max-width: 860px) 100vw, 40vw", eager=True, w=1800 if a["bild"].startswith("team") else 1200, h=1200 if a["bild"].startswith("team") else 1800)}</div></div>
</div></section>
<section class="sec"><div class="wrap artikel-wrap">
<article class="prose rv">
<p class="kurz-box"><strong>Kurz gesagt:</strong> {a["kurz"]}</p>
{teile}
<p class="stand">Stand: Oktober 2026. Dieser Ratgeber ersetzt keine Rechtsberatung.</p>
</article>
<aside class="artikel-aside"><h4>Passende Leistungen</h4><div class="places" style="grid-template-columns:1fr">{links}</div><h4 style="margin-top:28px">Weitere Ratgeber</h4><ul class="aside-links">{andere}</ul></aside>
</div></section>
{form_section(d)}
"""
    write(f"ratgeber/{a['slug']}/index.html", head(a["seo_title"], a["desc"], url, d, schema, og_img=a["bild"] + ".jpg") + header(d, "ueber") + body + footer(d))

def slugify(t):
    import unicodedata, re as _re
    t = t.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return _re.sub(r"[^a-z0-9]+", "-", t).strip("-")

def page_glossar():
    d = 2
    url = "/ratgeber/glossar/"
    title = "Glossar Gebäudereinigung & Grünpflege | WOHLverde"
    desc = "Fachbegriffe aus Gebäudereinigung, Grünpflege, Hausmeisterservice und Winterdienst kurz erklärt: von Bauendreinigung bis Winterdienst. Das WOHLverde-Glossar."
    crumbs = [("Startseite", "/"), ("Ratgeber", "/ratgeber/"), ("Glossar", url)]
    terms = sorted(GLOSSAR, key=lambda x: x[0].lower())
    dts = {"@type": "DefinedTermSet", "@id": DOMAIN + url + "#glossar", "name": "WOHLverde Glossar", "description": desc,
           "hasDefinedTerm": [{"@type": "DefinedTerm", "@id": DOMAIN + url + "#" + slugify(t), "name": t, "description": x, "inDefinedTermSet": DOMAIN + url + "#glossar", "url": DOMAIN + url + "#" + slugify(t)} for t, x, _ in terms]}
    schema = ld(dts, crumbs_schema(crumbs), page_url=url, page_name=title, desc=desc, page_type="CollectionPage")
    buchst = sorted(set(t[0][0].upper() for t in terms))
    az = "".join(f'<a href="#b-{b}">{b}</a>' for b in buchst)
    teile, aktuell = [], None
    for t, x, link in terms:
        b = t[0].upper()
        if b != aktuell:
            if aktuell: teile.append("</div></div>")
            teile.append(f'<div class="g-gruppe"><h2 class="g-buchstabe" id="b-{b}">{b}</h2><div class="g-liste">')
            aktuell = b
        ziel = "../.." + link if link != "/" else "../../"
        teile.append(f'<div class="g-term rv" id="{slugify(t)}"><h3>{t}</h3><p>{x}</p><a class="g-mehr" href="{ziel}">Mehr dazu {ic("arrow")}</a></div>')
    teile.append("</div></div>")
    body = f"""
<section class="phead" style="padding-bottom:56px"><div class="wrap">{crumbs_html(crumbs, d)}
<span class="eyebrow" style="color:var(--lime)">Glossar</span><h1>Fachbegriffe kurz erklärt.</h1>
<p class="lead">{len(terms)} Begriffe aus Gebäudereinigung, Grünpflege, Hausmeisterservice und Winterdienst, verständlich und auf den Punkt.</p>
<nav class="g-az" aria-label="Alphabet">{az}</nav></div></section>
<section class="sec"><div class="wrap glossar">{"".join(teile)}
<p class="stand">Stand: Oktober 2026. Die Erklärungen ersetzen keine Rechtsberatung.</p></div></section>
{form_section(d)}
"""
    write("ratgeber/glossar/index.html", head(title, desc, url, d, schema) + header(d, "ueber") + body + footer(d))


def page_danke():
    d = 1
    html_ = head("Danke für Ihre Anfrage | WOHLverde", "Ihre Anfrage ist bei WOHLverde angekommen.", "/danke/", d, "").replace('content="index, follow, max-image-preview:large"', 'content="noindex, nofollow"')
    body = f"""<section class="phead nf"><div class="wrap"><div class="tl-dot" style="margin:0 auto 26px;background:var(--lime);color:var(--petrol)">{ic("shield")}</div>
<h1>Danke! Ihre Anfrage ist angekommen.</h1>
<p class="lead" style="margin:0 auto 28px">Wir melden uns in der Regel innerhalb eines Werktags bei Ihnen. Eine Eingangsbestätigung haben Sie per E-Mail erhalten. Dringend? Rufen Sie uns an: <a href="tel:{FIRMA["tel_int"]}" style="color:var(--lime)">{FIRMA["tel"]}</a></p>
<div class="btns" style="justify-content:center">{btn("../", "Zur Startseite")}<a class="btn btn--ghost" href="../referenzen/"><span>Referenzen ansehen</span></a></div></div></section>"""
    write("danke/index.html", html_ + header(d) + body + footer(d))


def page_kontakt():
    d = 1
    url = "/kontakt/"
    title = "Kontakt & Angebot anfragen | WOHLverde Forst bei Bruchsal"
    desc = "Angebot anfragen bei WOHLverde, Kronauer Allee 1, 76694 Forst: Grünpflege, Gebäudereinigung, Hausmeisterservice, Winterdienst. Telefon 07251 3924446."
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
    for k in ["einsatzgebiet/", "ueber-uns/", "kontakt/", "impressum/", "datenschutz/", "hinweis-zur-gleichstellung/", "referenzen/", "ratgeber/"] + [l["url"].lstrip("/") for l in LEISTUNGEN]:
        out = out.replace(f'href="{k}', f'href="/{k}')
    out = out.replace('href="" aria-label="WOHLverde Startseite"', 'href="/" aria-label="WOHLverde Startseite"')
    write("404.html", out)

def extras():
    urls = ["/"] + [l["url"] for l in LEISTUNGEN] + ["/einsatzgebiet/"] + [f"/einsatzgebiet/{o['slug']}/" for o in ORTE] + ["/ueber-uns/", "/kontakt/", "/referenzen/", "/ratgeber/"] + [dt["parent"] + dt["slug"] + "/" for dt in DETAILS] + [f"/ratgeber/{a['slug']}/" for a in RATGEBER] + ["/ratgeber/glossar/"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{DOMAIN}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /anfrage-senden.php\nDisallow: /danke/\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    lines = [f"# WOHLverde", "", f"> {FIRMA['kurz']}", "",
             f"Google-Bewertung: {FIRMA['sterne']} von 5 Sternen bei {FIRMA['rezensionen']} Rezensionen (Stand Oktober 2026): {FIRMA['google']}\n\n" "WOHLverde (früher H&G WOHL) ist ein Dienstleister für Objektbetreuung mit Sitz in Forst (Baden), gegründet im Oktober 2020 von Nico Sica. "
             "Über 20 festangestellte, deutschsprachige Mitarbeitende. Keine Subunternehmen. Zielgruppe: Unternehmen, Gewerbeimmobilien, Hausverwaltungen, Industrie und Kommunen; auf Anfrage auch Privatkunden.", "",
             "## Kontakt", f"- Adresse: Kronauer Allee 1, 76694 Forst, Deutschland", f"- Telefon: {FIRMA['tel']}", f"- E-Mail: {FIRMA['mail']}",
             "- Erreichbarkeit: Montag bis Freitag 8 bis 17 Uhr, Samstag nach Vereinbarung", f"- Angebot anfragen: {DOMAIN}/kontakt/", "",
             "## Leistungen"] + [f"- [{l['name']}]({DOMAIN}{l['url']}): {l['kurz']}" for l in LEISTUNGEN] + ["",
             "## Einsatzgebiet", "Raum Bruchsal, Karlsruhe, Bretten und Umgebung: " + ", ".join(EINSATZORTE_ALLE) + ".", ""] + [f"- [{o['name']}]({DOMAIN}/einsatzgebiet/{o['slug']}/)" for o in ORTE] + ["",
             "## Häufige Fragen"] + [f"- **{q}** {a}" for q, a in FAQ_START] + ["",
             "## Einzelleistungen"] + [f"- [{dt['name']}]({DOMAIN}{dt['parent']}{dt['slug']}/): {dt['kurz']}" for dt in DETAILS] + ["", "## Ratgeber"] + [f"- [{a['title']}]({DOMAIN}/ratgeber/{a['slug']}/): {a['kurz']}" for a in RATGEBER] + ["",
             "## Glossar", f"Vollständig: {DOMAIN}/ratgeber/glossar/"] + [f"- **{t}:** {x}" for t, x, _ in sorted(GLOSSAR)] + ["",
             "## Weitere Seiten", f"- [Über uns]({DOMAIN}/ueber-uns/)", f"- [Referenzen]({DOMAIN}/referenzen/)", f"- [Karriere]({FIRMA['karriere']})", f"- [Instagram]({FIRMA['instagram']})", f"- [Impressum]({DOMAIN}/impressum/)", ""]
    write("llms.txt", "\n".join(lines))
    write("site.webmanifest", json.dumps({"name": "WOHLverde", "short_name": "WOHLverde", "start_url": "/", "display": "standalone", "background_color": "#003a41", "theme_color": "#003a41",
                                         "icons": [{"src": "/assets/img/favicon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/img/favicon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    page_home()
    for dt in DETAILS: page_detail(dt)
    page_referenzen()
    page_ratgeber_index()
    for a in RATGEBER: page_ratgeber(a)
    page_glossar()
    page_danke()
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
