# wohlverde-website

Neue Webseite für **WOHLverde** (früher H&G WOHL), Forst bei Bruchsal. Kunde: Nico Sica. Betreut von Awan Tofik, AO Consulting GmbH.

- Vorschau: https://wohlverde.vorschau.ao-consult.de (Zweig `main`)
- Live: https://wohlverde.de (Zweig `live`, erst nach Freigabe)

## Aufbau

| Ordner | Inhalt |
|---|---|
| `website/` | Die Seite. Nur was hier liegt, geht online. |
| `build/` | `inhalte.py` (alle Texte) und `build.py` (erzeugt die HTML-Seiten). |
| `doku/` | Offene Punkte, Bildreserve. |
| `.github/workflows/` | `vorschau.yml` (GitHub Pages) und `livegang.yml` (All-Inkl per lftp). |

## Texte ändern

1. Text in `build/inhalte.py` ändern (Seitenrahmen und Abschnitte in `build/build.py`).
2. `python3 build/build.py` ausführen. Die HTML-Dateien in `website/` werden neu geschrieben.
3. Hochladen (`main`), Vorschau prüfen.

Regel für alle Texte: keine Gedankenstriche.

## Seiten

Start, Grünpflege (`/garten-und-landschaftspflege/`), Gebäudereinigung (`/gebaeudereinigung/`), Hausmeisterservice (`/hausmeister-service/`), Winterdienst (`/winterdienst/`), Einsatzgebiet mit Bruchsal, Karlsruhe, Bretten, Forst, Über uns, Kontakt, Impressum, Datenschutz, Hinweis zur Gleichstellung, 404.

Die Adressen der alten WordPress-Seite bleiben erhalten.

## Technik

- Reines HTML, CSS, JavaScript. Einzige externe Einbindung ohne Einwilligung: Adobe Fonts (Neutronic, Kit `rma2wag`, Lizenz verbietet Selbsthosting). Archivo liegt lokal als Rückfall.
- Google Ads: `assets/js/ao-konfiguration.js` (Kennung) und `assets/js/einwilligung.js` (eigenes Einwilligungsfenster, lädt gtag erst nach Zustimmung). Ohne Kennung passiert nichts.
- Formular: `website/anfrage-senden.php` (PHP `mail()`, Honigtopf, Zeitsperre, Eingangsbestätigung). Pflichtfelder werden im Browser, in `app.js` und im PHP geprüft.
- SEO/GEO: strukturierte Daten je Seite, `sitemap.xml`, `robots.txt`, `llms.txt`.
- `.htaccess`: https ohne www, alte Adressen, Kasserver-Ausnahme, HTML ohne Zwischenspeicher.

## Vor dem Livegang zu erledigen

Siehe `doku/offene-punkte.md`.
