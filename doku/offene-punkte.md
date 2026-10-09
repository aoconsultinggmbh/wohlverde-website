# WOHLverde: offene Punkte vor dem Livegang

Stand: 09.10.2026, gebaut von Awan Tofik (AO Consulting) mit Claude.

## Geklärt am 09.10.2026

- Einsatzorte inklusive Nachbarorte: passt (Awan).
- Winterdienst: macht WOHLverde, Seite bleibt.
- Nennung der Referenzkunden und Zitat von Nico: freigegeben.
- Schrift: Neutronic über Adobe Fonts (AO-Abo). Eingebunden über das bestehende Kit `rma2wag` (wie auf der alten Seite), Archivo bleibt als lokaler Rückfall. Adobe Fonts darf laut Lizenz nicht selbst gehostet werden, darum ist das die einzige externe Einbindung; im Datenschutz beschrieben.
- Google Ads: Nico schaltet Anzeigen. Einwilligungsfenster und Conversion-Messung sind eingebaut, schlafen aber, bis die Kennung eingetragen ist.

## Mit Nico klären

1. **Google-Ads-Kennung**: `AW-...` und die Conversion-Labels für "Anfrage gesendet" und "Anruf" aus seinem Google-Ads-Konto. Eintragen in `website/assets/js/ao-konfiguration.js`. Danach erscheint das Einwilligungsfenster automatisch.
2. **Formular-Empfänger**: Anfragen gehen an `info@wohlverde.de`. Passt das, oder zusätzlich eine Adresse in Kopie?
3. **Winterdienst-Details**: Bereitschaftszeiten, Räumprotokoll, Streumittel für die Seite.
4. **Google-Bewertungen**: Link zum Google-Unternehmensprofil, eventuell ausgewählte Bewertungen als Text (mit Freigabe).
5. **Rechtsform**: Einzelunternehmen oder GmbH? Bei GmbH Handelsregister und Registergericht ins Impressum.
6. **Datenschutz** neu gefasst (Hosting All-Inkl, Formular, Adobe Fonts, Google Ads). Vor Livegang Nico zeigen; prüfen, ob All-Inkl wirklich der Hoster wird.

## Technisch vor dem Livegang

- [ ] Schrift in der Vorschau prüfen (Neutronic lädt, Zeilenumbrüche der großen Überschriften ok).
- [ ] Google Ads: nach Eintragen der Kennung testen (Einwilligung, Ablehnen, Conversion im Tag Assistant).
- [ ] Matomo optional: Bei Google Ads mit Einwilligung zusätzlich cookiefreies Matomo für ehrliche Besucherzahlen (siehe Skill), Datenschutz dann ergänzen.
- [ ] Karriere-Link zeigt auf `https://wohlverde-karriere.de/`.
- [ ] Domain bleibt `https://wohlverde.de` (ohne www). Alte URLs bleiben gleich, .htaccess leitet Varianten weiter.
- [ ] Testanfrage auf dem echten Server, Eingang im Postfach (nicht Spam) prüfen.
- [ ] Search Console: Property, Sitemap senden, Unternehmensprofil prüfen. Google-Ads-Kampagnen auf die passenden Unterseiten verlinken (Leistungs- und Ortsseiten sind als Zielseiten gebaut).

## Was neu ist (für das Gespräch mit Nico)

- Neues Design in den Markenfarben Petrol, Lime, Beton; große Bildwelt aus den Shootings Februar und Juni 2026.
- Fokus B2B (Gewerbe, Industrie, Hausverwaltungen, Kommunen), wie im /test-Entwurf.
- SEO: eigene Seiten je Leistung und je Ort (Bruchsal, Karlsruhe, Bretten, Forst), saubere Titel und Beschreibungen, Sitemap, strukturierte Daten (LocalBusiness, Service, FAQ, Breadcrumbs).
- GEO/AEO (Sichtbarkeit in KI-Suche wie ChatGPT, Perplexity, Google AI Overviews): "Kurz gesagt"-Absätze mit klaren Antworten, FAQ je Seite, `llms.txt`, eindeutige Firmenangaben inkl. früherem Namen H&G WOHL.
- Schnell und datensparsam: Bilder als WebP, ohne Einwilligung keine Cookies; Google Ads nur nach Zustimmung über ein eigenes, schlankes Einwilligungsfenster.
- Anfrageformular für Firmen mit Objektart und Leistungsauswahl, Eingangsbestätigung an den Kunden.
- Mobile Schnellleiste "Anrufen / Angebot anfragen".

## Anfrageformular und Messung (Stand 09.10.2026)

- Das Formular steht auf der Startseite, auf allen Leistungs- und Ortsseiten und auf der Kontaktseite (gleiches Formular, gleiches Skript). Grund: Google-Ads-Besucher landen auf einer Unterseite und sollen dort ohne weiteren Klick anfragen können.
- Jede Anfrage-Mail enthält "Gesendet von: /seite/" und, falls in der Adresse vorhanden, utm-Parameter und gclid. So sieht Nico ohne Cookies, welche Seite und welche Kampagne Anfragen bringt.
- Mit der Google-Ads-Kennung zählt zusätzlich die Conversion "Anfrage gesendet" auf jeder dieser Seiten.


## Neue Seiten (Stand 09.10.2026, abends)

- Einzelleistungen: Unterhaltsreinigung, Glas- und Fensterreinigung, Treppenhausreinigung (unter Gebäudereinigung), Baumpflege, Hecken- und Gehölzschnitt, Unkrautbeseitigung (unter Grünpflege). Inhalte nur aus dem bestehenden Leistungsumfang, keine Preise.
- Referenzen: Kundenliste (Einwilligungen im Ordner KundenLogo), Vorher/Nachher, Google-Bewertung. Für echte Fallbeispiele (Objekt, Fläche, Rhythmus, Foto) braucht es Angaben von Nico.
- Ratgeber: 3 Artikel (Unterhalts- vs. Grundreinigung, Grünpflege im Jahresverlauf, Winterdienst für Gewerbe). Rechtliche Hinweise bewusst allgemein gehalten (Bundesnaturschutzgesetz Schnittzeiten, Gemeindesatzungen beim Winterdienst). Vor Livegang kurz von Nico gegenlesen lassen.
- Danke-Seite /danke/ nach erfolgreicher Anfrage (noindex). Für Google Ads später als Conversion-Ziel nutzbar.
- Bewusst nicht gebaut: weitere Ortsseiten ohne echten Ortsbezug (Gefahr von dünnem Inhalt).
