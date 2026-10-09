# WOHLverde | Alle Texte der Webseite an einer Stelle.
# Quellen: alte Seite wohlverde.de, Entwurf wohlverde.de/test (April 2026), Texte für Homepage (Mai 2024),
# WhatsApp-Verlauf mit Nico Sica (Juli 2026). Nichts erfunden: offene Punkte stehen in doku/offene-punkte.md.
# Regel: keine Gedankenstriche in Texten.

FIRMA = {
    "tel": "07251 3924446",
    "tel_int": "+4972513924446",
    "mail": "info@wohlverde.de",
    "instagram": "https://www.instagram.com/wohlverde/",
    "facebook": "https://www.facebook.com/hausundgartenwohl",
    "karriere": "https://wohlverde-karriere.de/",
    "google": "https://www.google.com/maps?cid=3407328301533018773",
    "sterne": "5,0",
    "rezensionen": "über 60",   # Stand 09.10.2026: 61 Rezensionen. Bei Bedarf anpassen.
    "kurz": "WOHLverde aus Forst bei Bruchsal betreut Gewerbeimmobilien, Bürogebäude, Industrieflächen, Wohnanlagen und kommunale Einrichtungen: Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst aus einer Hand, mit festangestelltem Team und ohne Subunternehmen.",
}

EINSATZORTE_ALLE = ["Forst", "Bruchsal", "Karlsruhe", "Bretten", "Hambrücken", "Ubstadt-Weiher", "Kronau", "Bad Schönborn", "Karlsdorf-Neuthard", "Graben-Neudorf", "Stutensee", "Weingarten (Baden)"]

ORTE = [
    {"slug": "bruchsal", "name": "Bruchsal", "zeile": "Direkt nebenan", "bild": "garten-hecke-sommer", "bild_alt": "WOHLverde-Mitarbeiter beim Heckenschnitt im Sommer",
     "intro": "Bruchsal liegt direkt neben unserem Standort in Forst. Für Unternehmen, Hausverwaltungen und Einrichtungen in Bruchsal sind wir deshalb besonders schnell vor Ort, ob für die regelmäßige Grünpflege, die Unterhaltsreinigung oder den Winterdienst.",
     "kurz_extra": "Unser Standort in Forst grenzt direkt an Bruchsal.",
     "text": "In Bruchsal betreuen wir Außenanlagen, Treppenhäuser, Büros und technische Abläufe. Sie bekommen feste Ansprechpartner und ein Team, das Ihr Objekt kennt.",
     "faq_weg": "Sehr schnell. Unser Standort in Forst grenzt direkt an Bruchsal, unsere Teams sind täglich in der Umgebung unterwegs. Für Notfälle stimmen wir Reaktionszeiten individuell mit Ihnen ab."},
    {"slug": "karlsruhe", "name": "Karlsruhe", "zeile": "Stadt und Umland", "bild": "reinigung-fenster", "bild_alt": "WOHLverde-Mitarbeiter bei der Glasreinigung in einem Büro",
     "intro": "Bürogebäude, Gewerbeflächen und Wohnanlagen in Karlsruhe brauchen Dienstleister, die verlässlich liefern. WOHLverde übernimmt Grünpflege, Gebäudereinigung und Hausmeisterservice mit festem Team und dokumentierten Abläufen.",
     "kurz_extra": "Karlsruhe und das nördliche Umland gehören zu unserem Kerngebiet.",
     "text": "Ob Unterhaltsreinigung im Büro, Pflege von Firmengrün oder technische Objektbetreuung: In Karlsruhe arbeiten wir mit klaren Zuständigkeiten und nachvollziehbarer Qualität.",
     "faq_weg": "Karlsruhe gehört zu unserem Kerngebiet. Die genauen Einsatzzeiten und Reaktionszeiten legen wir beim Vor-Ort-Termin gemeinsam mit Ihnen fest."},
    {"slug": "bretten", "name": "Bretten", "zeile": "Kraichgau", "bild": "garten-maeher", "bild_alt": "WOHLverde-Mitarbeiter mit Rasenmäher auf einer Grünfläche",
     "intro": "Auch in Bretten und im angrenzenden Kraichgau sind wir für Gewerbe, Hausverwaltungen und Kommunen im Einsatz. Grünpflege, Gebäudereinigung, Hausmeisterservice und Winterdienst bekommen Sie bei uns aus einer Hand.",
     "kurz_extra": "Bretten betreuen wir regelmäßig von Forst aus.",
     "text": "Für Objekte in Bretten planen wir feste Touren und feste Teams. So bleibt die Qualität gleich, und Sie wissen immer, wer bei Ihnen arbeitet.",
     "faq_weg": "Bretten betreuen wir im Rahmen fester Touren. Reaktionszeiten für dringende Fälle vereinbaren wir individuell mit Ihnen."},
    {"slug": "forst", "name": "Forst", "zeile": "Unser Standort", "bild": "marke-schild", "bild_alt": "WOHLverde-Firmenschild am Standort",
     "intro": "In Forst sind wir zu Hause: An der Kronauer Allee 1 sitzt unser Team. Für Betriebe, Wohnanlagen und Einrichtungen in Forst und den Nachbargemeinden sind wir der Dienstleister um die Ecke.",
     "kurz_extra": "Unser Firmensitz ist die Kronauer Allee 1 in Forst.",
     "text": "Kurze Wege, persönliche Ansprechpartner und ein Team, das die Gegend kennt. Genau das bekommen Sie, wenn Ihr Objekt in Forst oder direkt nebenan liegt.",
     "faq_weg": "Kürzer geht es nicht: Unser Standort ist in Forst. Bei dringenden Fällen sind wir entsprechend schnell vor Ort."},
]

ABLAUF = [
    ("Unverbindliche Anfrage", "Sie rufen an oder nutzen das Formular. Wir melden uns zeitnah und stimmen einen ersten Termin ab."),
    ("Persönliches Gespräch", "Wir analysieren Ihre Anforderungen, Abläufe und die Besonderheiten Ihrer Immobilie."),
    ("Termin und Angebot", "Vor-Ort-Termin mit Objektaufnahme. Danach erhalten Sie ein transparent kalkuliertes Angebot."),
    ("Zuverlässige Betreuung", "Nach Ihrer Freigabe starten wir mit festem Team, klaren Prozessen und definierten Zuständigkeiten."),
]

VORTEILE = [
    ("pin", "Regional und schnell vor Ort", "Kurze Wege, feste Ansprechpartner und schnelle Reaktionszeiten im Raum Bruchsal und Karlsruhe."),
    ("users", "Festes Team, volle Qualitätskontrolle", "Ausschließlich festangestellte, deutschsprachige Mitarbeitende. Keine Subunternehmen, kein Wechselpersonal."),
    ("layers", "Ganzheitliche Objektbetreuung", "Grünpflege, Gebäudereinigung und technischer Objektservice greifen ineinander. Ein Partner, ein Ansprechpartner."),
    ("doc", "Planbare Qualität im laufenden Betrieb", "Strukturiert, termintreu und dokumentiert. Leistungen sind klar definiert und dauerhaft nachvollziehbar."),
]

ZIELGRUPPEN = [
    ("Unternehmen und Gewerbe", "Bürogebäude, Gewerbeparks und Firmengelände, gepflegt im laufenden Betrieb."),
    ("Industrie", "Industrieflächen und Außenanlagen mit klaren Abläufen und Dokumentation."),
    ("Hausverwaltungen", "Wohnanlagen mit Treppenhausreinigung, Grünpflege und Hausmeisterservice."),
    ("Kommunen", "Kommunale Einrichtungen und Flächen, zuverlässig und nachvollziehbar betreut."),
]

WERTE = [
    ("Ehrlichkeit", "Wir sagen, was geht und was nicht. Klare Absprachen statt leerer Versprechen."),
    ("Verantwortung", "Wir behandeln Ihr Objekt wie unser persönliches Projekt."),
    ("Gründlichkeit", "Sauberkeit macht uns Freude. Wir arbeiten mit höchster Genauigkeit."),
    ("Wachstum", "Regelmäßige Schulungen und Weiterbildungen für das ganze Team."),
    ("Flexibilität", "Unser Service passt sich Ihrem Objekt an, nicht umgekehrt."),
    ("Deutschsprachig", "Klare Kommunikation: Jeder im Team spricht Ihre Sprache."),
    ("Innovation", "Moderne Arbeitsweisen, die fortschrittlich und umweltfreundlich sind."),
    ("Leidenschaft", "Wir machen diesen Job, weil er uns Spaß macht. Das sieht man."),
]

REFERENZEN = ["Evangelische Stadtmission Karlsruhe", "SÜDREAL", "Villa Medici", "JobService Baden GmbH", "Kurbetriebs-GmbH Bad Schönborn",
              "1463 Apartmenthaus", "PSI Software SE", "STEPHAN Exklusiv", "Topfruits Megerle", "Hintermayer"]

FAQ_START = [
    ("Welche Leistungen bietet WOHLverde an?", "WOHLverde bietet Grünpflege (Garten- und Landschaftspflege, Baumpflege), Gebäudereinigung (Unterhalts-, Treppenhaus-, Glas- und Grundreinigung), Hausmeisterservice mit Objektkontrollen und Kleinreparaturen sowie Winterdienst. Alles ist einzeln oder als Gesamtpaket aus einer Hand buchbar."),
    ("In welchen Orten ist WOHLverde tätig?", "Unser Standort ist in Forst bei Bruchsal. Wir betreuen Objekte im Raum Bruchsal, Karlsruhe, Bretten und Umgebung, zum Beispiel in Forst, Bruchsal, Karlsruhe, Bretten, Hambrücken, Ubstadt-Weiher, Kronau und Bad Schönborn."),
    ("Arbeitet WOHLverde mit Subunternehmen?", "Nein. Wir arbeiten ausschließlich mit eigenen, festangestellten und deutschsprachigen Mitarbeitenden. So behalten wir die volle Kontrolle über die Qualität."),
    ("Für wen arbeitet WOHLverde?", "Unser Schwerpunkt sind Unternehmen, Gewerbeimmobilien, Industrieflächen, Hausverwaltungen und kommunale Einrichtungen. Auf Anfrage betreuen wir auch Privatkunden."),
    ("Was kostet die Objektbetreuung bei WOHLverde?", "Das hängt von Größe, Art und gewünschtem Rhythmus ab. Nach einem unverbindlichen Vor-Ort-Termin erhalten Sie ein transparent kalkuliertes Angebot mit klar definierten Leistungen."),
    ("Wie wird WOHLverde von Kunden bewertet?", "Bei Google hat WOHLverde 5,0 von 5 Sternen bei über 60 Rezensionen (Stand Oktober 2026)."),
    ("Ist WOHLverde dasselbe Unternehmen wie H&G WOHL?", "Ja. H&G WOHL heißt jetzt WOHLverde. Team, Service und Qualitätsanspruch bleiben gleich."),
]

LEISTUNGEN = [
    {
        "name": "Grünpflege", "url": "/garten-und-landschaftspflege/", "icon": "heckenschere", "dd": "Garten- und Landschaftspflege, Baumpflege",
        "title": "Grünpflege & Landschaftspflege Bruchsal, Karlsruhe | WOHLverde",
        "desc": "Grünpflege für Gewerbe, Wohnanlagen und Kommunen im Raum Bruchsal und Karlsruhe: Rasen, Hecken, Bäume, Unkraut und Jahrespflege. Festes Team aus Forst.",
        "eyebrow": "Garten- und Landschaftspflege", "h1": "Grünpflege, die Ihr Objekt aufwertet.",
        "intro": "Strukturierte Pflege von Außenanlagen, Industrieflächen und Bürostandorten. Saisonal geplant, sauber ausgeführt und dokumentiert, im Raum Bruchsal, Karlsruhe und Bretten.",
        "teaser": "Strukturierte Pflege von Außenanlagen, Industrieflächen und Bürostandorten, von der Rasenpflege bis zum Baumschnitt.",
        "kurz": "WOHLverde übernimmt die Garten- und Landschaftspflege für Gewerbeimmobilien, Industrieflächen, Wohnanlagen und kommunale Einrichtungen im Raum Bruchsal und Karlsruhe: Rasenpflege, Hecken- und Gehölzschnitt, Baumpflege, Unkrautbeseitigung auf Grün- und Grauflächen sowie saisonale Pflege.",
        "art": "garten", "karte": "garten-hecke-sommer", "chip": "Jahrespflege nach Plan",
        "bild": "garten-pflanzen", "bild_alt": "WOHLverde-Mitarbeiterin bei Pflanzarbeiten auf einer Grünfläche",
        "bild2": "garten-graeser", "bild2_alt": "WOHLverde-Mitarbeiter beim Rückschnitt von Ziergräsern auf einem Firmengelände", "tag": "Saisonal geplant",
        "h2_leistung": "Vom Rasen bis zur <span class=\"hl\">Baumkrone</span>.",
        "leistung_text": "Ein gepflegtes Außenbild ist die Visitenkarte Ihres Unternehmens. Mit unserer Jahrespflege sieht Ihr Objekt das ganze Jahr über top aus, für Kunden, Mitarbeitende und Besucher.",
        "punkte": [
            ("Rasenpflege und Mäharbeiten", "Regelmäßiges Mähen, Kantenpflege und Pflege von Rasenflächen in einem Rhythmus, der zu Ihrem Objekt passt."),
            ("Hecken- und Gehölzschnitt", "Fachgerechter Rückschnitt von Hecken, Sträuchern, Gräsern und Gehölzen."),
            ("Baumpflege", "Baumschnitt und Baumpflege bis hin zu Fällarbeiten, sicher ausgeführt."),
            ("Unkrautbeseitigung", "Auf Grün- und Grauflächen, Pflaster und Wegen, mit umweltschonenden Methoden."),
            ("Pflanzarbeiten", "Neupflanzungen und Aufwertung von Beeten und Grünflächen."),
            ("Saisonale Pflege", "Frühjahrs- und Herbstpflege, inklusive Laubbeseitigung und Vorbereitung auf den Winter."),
        ],
        "h2_vorteil": "Ein Außenbild, auf das Sie sich verlassen können.",
        "vorteil_text": "Wir planen Pflegeeinsätze nach Jahreszeit und Objekt. Feste Teams kennen Ihre Flächen, Besonderheiten werden dokumentiert.",
        "checks": ["Feste Teams für Ihr Objekt", "Jahrespflege nach Plan", "Umweltschonende Methoden", "Kombinierbar mit Winterdienst und Hausmeisterservice"],
        "faq": [
            ("Welche Grünflächen pflegt WOHLverde?", "Außenanlagen von Bürogebäuden, Gewerbeparks und Industrieflächen, Wohnanlagen von Hausverwaltungen sowie kommunale Flächen. Auf Anfrage auch private Gärten."),
            ("Wie oft sollte eine Rasenfläche gemäht werden?", "Das hängt von Jahreszeit und Wachstum ab. In der Wachstumsphase empfehlen wir in der Regel einen wöchentlichen Rhythmus. Den passenden Plan legen wir beim Vor-Ort-Termin fest."),
            ("Wie entfernt WOHLverde Unkraut?", "Wir setzen auf effektive und umweltschonende Methoden, etwa manuelle Entfernung, Mulchen und biologisch abbaubare Mittel."),
            ("Bietet WOHLverde eine Jahrespflege an?", "Ja. Mit unserer Jahrespflege planen wir alle Arbeiten über das Jahr, von der Frühjahrspflege bis zum Winterdienst."),
        ],
    },
    {
        "name": "Gebäudereinigung", "url": "/gebaeudereinigung/", "icon": "scheibenabzieher", "dd": "Unterhalts-, Glas- und Treppenhausreinigung",
        "title": "Gebäudereinigung in Bruchsal & Karlsruhe | WOHLverde",
        "desc": "Gebäudereinigung für Büros, Industrie, Wohnanlagen und Kommunen im Raum Bruchsal und Karlsruhe: Unterhalts-, Treppenhaus- und Glasreinigung. Ohne Subunternehmen.",
        "eyebrow": "Gebäudereinigung", "h1": "Sauberkeit, auf die Sie bauen können.",
        "intro": "Planbare Unterhaltsreinigung für Bürogebäude, Industrieobjekte, Wohnanlagen und kommunale Einrichtungen. Mit festen Teams, klaren Zuständigkeiten und dokumentierten Abläufen.",
        "teaser": "Planbare Unterhaltsreinigung für Büros, Industrieobjekte und Wohnanlagen, mit festen Teams und klaren Zuständigkeiten.",
        "kurz": "WOHLverde übernimmt die Gebäudereinigung für Bürogebäude, Industrieobjekte, Wohnanlagen und kommunale Einrichtungen im Raum Bruchsal und Karlsruhe: Unterhalts- und Büroreinigung, Treppenhausreinigung, Glas- und Fensterreinigung, Grund- und Teppichreinigung. Immer mit eigenem, geschultem Personal.",
        "art": "reinigung", "karte": "reinigung-tisch", "chip": "Feste Reinigungsteams",
        "bild": "reinigung-fenster-ruecken", "bild_alt": "WOHLverde-Mitarbeiter bei der Fensterreinigung in einem Büro",
        "bild2": "reinigung-buero-wisch", "bild2_alt": "WOHLverde-Mitarbeiterin wischt den Boden in einem Büro", "tag": "Feste Teams",
        "h2_leistung": "Drinnen <span class=\"hl\">glänzt</span> es.",
        "leistung_text": "Ein sauberer Arbeitsplatz trägt zu Gesundheit und Zufriedenheit bei. Wir reinigen gründlich, diskret und so, dass Ihr Betrieb ungestört weiterläuft.",
        "punkte": [
            ("Unterhalts- und Büroreinigung", "Regelmäßige Reinigung von Büros, Sozialräumen und Sanitärbereichen nach festem Plan."),
            ("Treppenhausreinigung", "Für Wohnanlagen und Geschäftshäuser, zuverlässig im vereinbarten Rhythmus."),
            ("Glas- und Fensterreinigung", "Fenster, Glasflächen, Wintergärten, Terrassen- und Lamellendächer streifenfrei sauber."),
            ("Grundreinigung", "Intensive Reinigung bei Bedarf, zum Beispiel nach Umbauten oder vor Übergaben."),
            ("Teppichreinigung", "Professionelle Reinigung textiler Bodenbeläge."),
            ("Industriereinigung", "Reinigung von Produktions- und Industrieflächen nach Ihren Anforderungen."),
        ],
        "h2_vorteil": "Gleiches Team, gleiche Qualität. Jedes Mal.",
        "vorteil_text": "Unsere Reinigungskräfte sind bei uns festangestellt und regelmäßig geschult. Sie wissen, wer bei Ihnen arbeitet, und wir sorgen dafür, dass der Standard stimmt.",
        "checks": ["Festangestellt und geschult", "Deutschsprachige Ansprechpartner", "Reinigungsplan nach Ihrem Bedarf", "Umweltschonende Reinigungsmittel"],
        "faq": [
            ("Welche Reinigungsleistungen bietet WOHLverde?", "Unterhalts- und Büroreinigung, Treppenhausreinigung, Glas- und Fensterreinigung, Grundreinigung, Teppichreinigung und Industriereinigung."),
            ("Wie oft sollte ein Büro gereinigt werden?", "Das hängt von Nutzung und Anforderungen ab. Üblich ist eine tägliche oder wöchentliche Reinigung. Wir erstellen einen Reinigungsplan, der zu Ihrem Betrieb passt."),
            ("Kann ich einen individuellen Reinigungsplan vereinbaren?", "Ja. Wir bieten flexible Reinigungspläne, abgestimmt auf Ihre Zeiten und Abläufe."),
            ("Welche Reinigungsmittel verwendet WOHLverde?", "Wir setzen auf umweltschonende und nachhaltige Reinigungsmittel, die wirksam und zugleich schonend sind."),
        ],
    },
    {
        "name": "Hausmeisterservice", "url": "/hausmeister-service/", "icon": "schraubenzieher", "dd": "Objektkontrollen, Instandhaltung, Kleinreparaturen",
        "title": "Hausmeisterservice in Bruchsal & Karlsruhe | WOHLverde",
        "desc": "Hausmeisterservice für Gewerbe, Wohnanlagen und Kommunen im Raum Bruchsal und Karlsruhe: Objektkontrollen mit Protokoll, Kleinreparaturen, Mülltonnenservice.",
        "eyebrow": "Hausmeister- und Objektservice", "h1": "Ihr Objekt in <span style=\"color:var(--lime)\">guten Händen</span>.",
        "intro": "Wir übernehmen die technische Betreuung Ihrer Immobilie: regelmäßige Objektkontrollen, laufende Instandhaltung und klar dokumentierte Abläufe. So bleibt Ihr Objekt funktional, sicher und im Wert erhalten.",
        "teaser": "Objektkontrollen mit Dokumentation, Instandhaltung und Kleinreparaturen. Ihr Objekt bleibt funktional und sicher.",
        "kurz": "Der Hausmeisterservice von WOHLverde betreut Gewerbeimmobilien, Wohnanlagen und kommunale Einrichtungen im Raum Bruchsal und Karlsruhe: regelmäßige Objektkontrollen mit Dokumentation, Kleinreparaturen, Mülltonnenservice, Zählerstände, Regenrinnenreinigung und die Koordination externer Dienstleister.",
        "art": "werkzeug", "chip": "Objektkontrollen mit Protokoll",
        "bild": "hausmeister-runde", "bild_alt": "WOHLverde-Mitarbeiter in Warnweste bei der Objektrunde vor dem Firmenfahrzeug",
        "bild2": "hausmeister-fenster", "bild2_alt": "WOHLverde-Mitarbeiter bei Arbeiten an einem Oberlicht", "tag": "Mit Protokoll",
        "h2_leistung": "Wir kümmern uns. <span class=\"hl\">Bevor</span> es klemmt.",
        "leistung_text": "Jedes Gebäude hat eigene Anforderungen. Mit festen Teams und klaren Zuständigkeiten sorgen wir dafür, dass Technik und Abläufe reibungslos funktionieren.",
        "punkte": [
            ("Objektkontrollen mit Dokumentation", "Regelmäßige Begehungen, Mängel werden erfasst und gemeldet. Nachvollziehbar für Sie."),
            ("Instandhaltung und Kleinreparaturen", "Laufende Instandhaltung, kleinere Reparaturen und der Austausch von Leuchtmitteln aller Art."),
            ("Mülltonnenservice", "Bereitstellung und Rückstellung der Behälter, Ordnung an den Standplätzen."),
            ("Zählerstände", "Ablesen und Auswerten von Zählerständen."),
            ("Regenrinnen reinigen", "Damit Wasser abläuft, wo es soll, und keine Schäden entstehen."),
            ("Koordination von Dienstleistern", "Wir stimmen externe Gewerke ab und sind Ihr Ansprechpartner vor Ort."),
        ],
        "h2_vorteil": "Ein Ansprechpartner statt fünf Anrufe.",
        "vorteil_text": "Bei uns bekommen Sie Hausmeisterservice, Grünpflege und Reinigung aus einer Hand. Kein Koordinieren verschiedener Anbieter, sondern eine nahtlose Betreuung Ihrer Immobilie.",
        "checks": ["Schnelle Reaktionszeiten und klare Zuständigkeiten", "Unterstützung im laufenden Betriebsablauf", "Individuelle Leistungspakete", "Notfälle nach Absprache"],
        "faq": [
            ("Welche Aufgaben übernimmt der Hausmeisterservice?", "Regelmäßige Objektkontrollen mit Dokumentation, Instandhaltung und Kleinreparaturen, Austausch von Leuchtmitteln, Mülltonnenservice, Zählerstände, Regenrinnenreinigung und die Koordination externer Dienstleister."),
            ("Welche Objekte betreut der Hausmeisterservice?", "Bürogebäude, Gewerbeimmobilien, Industrieparks, Wohnanlagen und öffentliche Einrichtungen."),
            ("Bietet WOHLverde auch einen Notfallservice?", "Ja. In dringenden Fällen sind wir schnell zur Stelle. Die Erreichbarkeit für Notfälle stimmen wir mit Ihnen individuell ab."),
            ("Kann ich individuelle Leistungen vereinbaren?", "Selbstverständlich. Wir stellen das Leistungspaket passend zu Ihrer Immobilie zusammen."),
        ],
    },
    {
        "name": "Winterdienst", "url": "/winterdienst/", "icon": "rechen", "dd": "Räumen und Streuen für Gewerbe",
        "title": "Winterdienst für Gewerbe in Bruchsal & Karlsruhe | WOHLverde",
        "desc": "Winterdienst im Raum Bruchsal und Karlsruhe: Räumen und Streuen von Zufahrten, Gehwegen und Parkflächen für Gewerbe, Wohnanlagen und Kommunen.",
        "eyebrow": "Winterdienst", "h1": "Sicher durch den Winter.",
        "intro": "Räumen und Streuen für Gewerbeimmobilien, Wohnanlagen und kommunale Einrichtungen im Raum Bruchsal und Karlsruhe. Damit Mitarbeitende, Kunden und Bewohner sicher ankommen.",
        "teaser": "Räumen und Streuen für Zufahrten, Gehwege und Parkflächen. Damit alle sicher ankommen.",
        "kurz": "WOHLverde übernimmt den Winterdienst für Gewerbeimmobilien, Wohnanlagen und kommunale Einrichtungen im Raum Bruchsal und Karlsruhe: Schnee räumen und Glätte bekämpfen auf Zufahrten, Gehwegen, Eingängen und Parkflächen, gut kombinierbar mit Grünpflege und Hausmeisterservice.",
        "art": "winter", "kopf_art": "winter", "chip": "Räumen und Streuen",
        "bild": "team-fahrzeug", "bild_alt": "Das WOHLverde-Team in Winterkleidung mit Fahrzeug",
        "bild2": "team-fahrzeug", "bild2_alt": "Das WOHLverde-Team in Winterkleidung mit Fahrzeug vor einem Bürogebäude", "tag": "Aus einer Hand",
        "h2_leistung": "Wenn es glatt wird, sind <span class=\"hl\">wir</span> da.",
        "leistung_text": "Wer räumt, wann und wo? Mit uns klären Sie das einmal und richtig. Wir legen Flächen, Prioritäten und Abläufe vor der Saison gemeinsam mit Ihnen fest.",
        "punkte": [
            ("Schnee räumen", "Zufahrten, Gehwege, Eingänge und Parkflächen werden geräumt."),
            ("Streuen", "Glättebekämpfung mit Streusalz oder abgestimmten Streumitteln."),
            ("Feste Flächenpläne", "Vor der Saison legen wir gemeinsam fest, welche Flächen in welcher Reihenfolge betreut werden."),
            ("Kombination mit Grünpflege", "Ein Dienstleister für das ganze Jahr: im Sommer Grünpflege, im Winter Räumdienst."),
        ],
        "h2_vorteil": "Ein Partner für alle Jahreszeiten.",
        "vorteil_text": "Unsere Teams kennen Ihre Flächen aus der Grünpflege und dem Hausmeisterservice. Im Winter wissen sie deshalb genau, worauf es ankommt.",
        "checks": ["Abstimmung vor der Saison", "Feste Teams aus der Region", "Kombinierbar mit Grünpflege und Hausmeisterservice", "Klare Zuständigkeiten"],
        "faq": [
            ("Für welche Flächen übernimmt WOHLverde den Winterdienst?", "Für Zufahrten, Gehwege, Eingänge und Parkflächen von Gewerbeimmobilien, Wohnanlagen und kommunalen Einrichtungen."),
            ("Wann sollte ich den Winterdienst beauftragen?", "Am besten vor Beginn der Saison. Dann können wir Flächen und Abläufe in Ruhe mit Ihnen planen."),
            ("Kann ich Winterdienst und Grünpflege zusammen beauftragen?", "Ja. Viele Kunden beauftragen uns für das ganze Jahr: Grünpflege im Sommer, Winterdienst im Winter, aus einer Hand."),
        ],
    },
]

IMPRESSUM = """
<h2>Angaben gemäß § 5 DDG</h2>
<p>WOHLverde<br>Kronauer Allee 1<br>76694 Forst<br>Deutschland</p>
<p><strong>Vertreten durch:</strong><br>Nico Sica</p>
<h2>Kontakt</h2>
<p>Telefon: <a href="tel:+4972513924446">07251 3924446</a><br>E-Mail: <a href="mailto:info@wohlverde.de">info@wohlverde.de</a></p>
<h2>Umsatzsteuer</h2>
<p>Umsatzsteuer-Identifikationsnummer gemäß § 27 a Umsatzsteuergesetz: DE325441678</p>
<h2>Streitschlichtung</h2>
<p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Konzeption, Gestaltung und Umsetzung</h2>
<p>AO Consulting GmbH<br>Zeiloch 13<br>76646 Bruchsal<br><a href="https://ao-consult.de/" rel="noopener">ao-consult.de</a></p>
<h2>Haftung für Inhalte</h2>
<p>Als Diensteanbieter sind wir gemäß § 7 Abs. 1 DDG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 DDG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.</p>
<h2>Haftung für Links</h2>
<p>Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.</p>
<h2>Urheberrecht</h2>
<p>Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers. Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet. Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden die Urheberrechte Dritter beachtet. Insbesondere werden Inhalte Dritter als solche gekennzeichnet. Sollten Sie trotzdem auf eine Urheberrechtsverletzung aufmerksam werden, bitten wir um einen entsprechenden Hinweis. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Inhalte umgehend entfernen.</p>
<p><strong>Bildnachweis:</strong> Fotos von Iwan Artemjew für die AO Consulting GmbH sowie eigene Aufnahmen von WOHLverde.</p>
"""

GLEICHSTELLUNG = """
<p>Aus Gründen der besseren Lesbarkeit wird bei Personenbezeichnungen und personenbezogenen Hauptwörtern auf unserer Webseite und externen Stellenausschreibungen sowie Social Media Beiträgen die männliche Form verwendet. Entsprechende Begriffe gelten im Sinne der Gleichbehandlung grundsätzlich für alle Geschlechter.</p>
"""

DATENSCHUTZ = """
<h2>1. Datenschutz auf einen Blick</h2>
<h3>Allgemeine Hinweise</h3>
<p>Die folgenden Hinweise geben einen einfachen Überblick darüber, was mit Ihren personenbezogenen Daten passiert, wenn Sie diese Website besuchen. Personenbezogene Daten sind alle Daten, mit denen Sie persönlich identifiziert werden können.</p>
<h3>Wer ist verantwortlich für die Datenerfassung auf dieser Website?</h3>
<p>Die Datenverarbeitung auf dieser Website erfolgt durch den Websitebetreiber. Dessen Kontaktdaten finden Sie im Abschnitt „Hinweis zur verantwortlichen Stelle“.</p>
<h3>Wie erfassen wir Ihre Daten?</h3>
<p>Ihre Daten werden zum einen dadurch erhoben, dass Sie uns diese mitteilen, zum Beispiel über das Anfrageformular. Andere Daten werden beim Besuch der Website automatisch durch unsere IT-Systeme erfasst. Das sind vor allem technische Daten (z. B. Internetbrowser, Betriebssystem oder Uhrzeit des Seitenaufrufs).</p>
<h3>Wofür nutzen wir Ihre Daten?</h3>
<p>Ein Teil der Daten wird erhoben, um eine fehlerfreie Bereitstellung der Website zu gewährleisten. Die Angaben aus dem Anfrageformular nutzen wir ausschließlich, um Ihre Anfrage zu bearbeiten.</p>
<h3>Cookies und Werbemessung</h3>
<p>Ohne Ihre Einwilligung setzt diese Website keine Cookies und lädt keine Analyse- oder Werbewerkzeuge. Nur wenn Sie im Einwilligungsfenster zustimmen, nutzen wir Google Ads Conversion-Tracking (siehe Abschnitt 5). Ihre Entscheidung können Sie jederzeit über den Link „Cookie-Einstellungen“ im Seitenfuß ändern. Links zu unseren Social-Media-Profilen sind einfache Verweise; Daten werden erst übertragen, wenn Sie den Link anklicken.</p>
<h3>Welche Rechte haben Sie bezüglich Ihrer Daten?</h3>
<p>Sie haben jederzeit das Recht, unentgeltlich Auskunft über Herkunft, Empfänger und Zweck Ihrer gespeicherten personenbezogenen Daten zu erhalten. Sie haben außerdem ein Recht, die Berichtigung oder Löschung dieser Daten zu verlangen. Wenn Sie eine Einwilligung zur Datenverarbeitung erteilt haben, können Sie diese jederzeit für die Zukunft widerrufen. Außerdem haben Sie das Recht, unter bestimmten Umständen die Einschränkung der Verarbeitung Ihrer personenbezogenen Daten zu verlangen. Des Weiteren steht Ihnen ein Beschwerderecht bei der zuständigen Aufsichtsbehörde zu.</p>

<h2>2. Hosting</h2>
<p>Wir hosten die Inhalte unserer Website bei folgendem Anbieter:</p>
<p><strong>ALL-INKL.COM</strong><br>Anbieter ist die ALL-INKL.COM, Neue Medien Münnich, Inhaber René Münnich, Hauptstraße 68, 02742 Friedersdorf (nachfolgend All-Inkl).</p>
<p>Wenn Sie unsere Website besuchen, erfasst All-Inkl Server-Logfiles, die Ihr Browser automatisch übermittelt. Dies sind: Browsertyp und Browserversion, verwendetes Betriebssystem, Referrer-URL, Hostname des zugreifenden Rechners, Uhrzeit der Serveranfrage und IP-Adresse. Eine Zusammenführung dieser Daten mit anderen Datenquellen wird nicht vorgenommen.</p>
<p>Die Verwendung von All-Inkl erfolgt auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO. Wir haben ein berechtigtes Interesse an einer möglichst zuverlässigen und sicheren Darstellung unserer Website.</p>
<h3>Auftragsverarbeitung</h3>
<p>Wir haben einen Vertrag über Auftragsverarbeitung (AVV) zur Nutzung des oben genannten Dienstes geschlossen. Hierbei handelt es sich um einen datenschutzrechtlich vorgeschriebenen Vertrag, der gewährleistet, dass dieser die personenbezogenen Daten unserer Websitebesucher nur nach unseren Weisungen und unter Einhaltung der DSGVO verarbeitet.</p>

<h2>3. Allgemeine Hinweise und Pflichtinformationen</h2>
<h3>Datenschutz</h3>
<p>Die Betreiber dieser Seiten nehmen den Schutz Ihrer persönlichen Daten sehr ernst. Wir behandeln Ihre personenbezogenen Daten vertraulich und entsprechend den gesetzlichen Datenschutzvorschriften sowie dieser Datenschutzerklärung. Wir weisen darauf hin, dass die Datenübertragung im Internet (z. B. bei der Kommunikation per E-Mail) Sicherheitslücken aufweisen kann. Ein lückenloser Schutz der Daten vor dem Zugriff durch Dritte ist nicht möglich.</p>
<h3>Hinweis zur verantwortlichen Stelle</h3>
<p>Die verantwortliche Stelle für die Datenverarbeitung auf dieser Website ist:</p>
<p>WOHLverde<br>Kronauer Allee 1<br>76694 Forst<br>Deutschland<br>Telefon: 07251 3924446<br>E-Mail: info@wohlverde.de</p>
<p>Verantwortliche Stelle ist die natürliche oder juristische Person, die allein oder gemeinsam mit anderen über die Zwecke und Mittel der Verarbeitung von personenbezogenen Daten (z. B. Namen, E-Mail-Adressen o. Ä.) entscheidet.</p>
<h3>Speicherdauer</h3>
<p>Soweit innerhalb dieser Datenschutzerklärung keine speziellere Speicherdauer genannt wurde, verbleiben Ihre personenbezogenen Daten bei uns, bis der Zweck für die Datenverarbeitung entfällt. Wenn Sie ein berechtigtes Löschersuchen geltend machen oder eine Einwilligung zur Datenverarbeitung widerrufen, werden Ihre Daten gelöscht, sofern wir keine anderen rechtlich zulässigen Gründe für die Speicherung haben (z. B. steuer- oder handelsrechtliche Aufbewahrungsfristen); im letztgenannten Fall erfolgt die Löschung nach Fortfall dieser Gründe.</p>
<h3>Rechtsgrundlagen der Datenverarbeitung</h3>
<p>Sofern Sie in die Datenverarbeitung eingewilligt haben, verarbeiten wir Ihre personenbezogenen Daten auf Grundlage von Art. 6 Abs. 1 lit. a DSGVO. Sind Ihre Daten zur Vertragserfüllung oder zur Durchführung vorvertraglicher Maßnahmen erforderlich, verarbeiten wir Ihre Daten auf Grundlage des Art. 6 Abs. 1 lit. b DSGVO. Des Weiteren verarbeiten wir Ihre Daten, sofern diese zur Erfüllung einer rechtlichen Verpflichtung erforderlich sind, auf Grundlage von Art. 6 Abs. 1 lit. c DSGVO. Die Datenverarbeitung kann ferner auf Grundlage unseres berechtigten Interesses nach Art. 6 Abs. 1 lit. f DSGVO erfolgen.</p>
<h3>Widerruf Ihrer Einwilligung zur Datenverarbeitung</h3>
<p>Viele Datenverarbeitungsvorgänge sind nur mit Ihrer ausdrücklichen Einwilligung möglich. Sie können eine bereits erteilte Einwilligung jederzeit widerrufen. Die Rechtmäßigkeit der bis zum Widerruf erfolgten Datenverarbeitung bleibt vom Widerruf unberührt.</p>
<h3>Widerspruchsrecht gegen die Datenerhebung in besonderen Fällen sowie gegen Direktwerbung (Art. 21 DSGVO)</h3>
<p>WENN DIE DATENVERARBEITUNG AUF GRUNDLAGE VON ART. 6 ABS. 1 LIT. E ODER F DSGVO ERFOLGT, HABEN SIE JEDERZEIT DAS RECHT, AUS GRÜNDEN, DIE SICH AUS IHRER BESONDEREN SITUATION ERGEBEN, GEGEN DIE VERARBEITUNG IHRER PERSONENBEZOGENEN DATEN WIDERSPRUCH EINZULEGEN; DIES GILT AUCH FÜR EIN AUF DIESE BESTIMMUNGEN GESTÜTZTES PROFILING. WENN SIE WIDERSPRUCH EINLEGEN, WERDEN WIR IHRE BETROFFENEN PERSONENBEZOGENEN DATEN NICHT MEHR VERARBEITEN, ES SEI DENN, WIR KÖNNEN ZWINGENDE SCHUTZWÜRDIGE GRÜNDE FÜR DIE VERARBEITUNG NACHWEISEN, DIE IHRE INTERESSEN, RECHTE UND FREIHEITEN ÜBERWIEGEN, ODER DIE VERARBEITUNG DIENT DER GELTENDMACHUNG, AUSÜBUNG ODER VERTEIDIGUNG VON RECHTSANSPRÜCHEN (WIDERSPRUCH NACH ART. 21 ABS. 1 DSGVO).</p>
<p>WERDEN IHRE PERSONENBEZOGENEN DATEN VERARBEITET, UM DIREKTWERBUNG ZU BETREIBEN, SO HABEN SIE DAS RECHT, JEDERZEIT WIDERSPRUCH GEGEN DIE VERARBEITUNG SIE BETREFFENDER PERSONENBEZOGENER DATEN ZUM ZWECKE DERARTIGER WERBUNG EINZULEGEN (WIDERSPRUCH NACH ART. 21 ABS. 2 DSGVO).</p>
<h3>Beschwerderecht bei der zuständigen Aufsichtsbehörde</h3>
<p>Im Falle von Verstößen gegen die DSGVO steht den Betroffenen ein Beschwerderecht bei einer Aufsichtsbehörde, insbesondere in dem Mitgliedstaat ihres gewöhnlichen Aufenthalts, ihres Arbeitsplatzes oder des Orts des mutmaßlichen Verstoßes zu.</p>
<h3>Recht auf Datenübertragbarkeit</h3>
<p>Sie haben das Recht, Daten, die wir auf Grundlage Ihrer Einwilligung oder in Erfüllung eines Vertrags automatisiert verarbeiten, an sich oder an einen Dritten in einem gängigen, maschinenlesbaren Format aushändigen zu lassen.</p>
<h3>Auskunft, Berichtigung, Löschung und Einschränkung der Verarbeitung</h3>
<p>Sie haben im Rahmen der geltenden gesetzlichen Bestimmungen jederzeit das Recht auf unentgeltliche Auskunft über Ihre gespeicherten personenbezogenen Daten, deren Herkunft und Empfänger und den Zweck der Datenverarbeitung und gegebenenfalls ein Recht auf Berichtigung, Löschung oder Einschränkung der Verarbeitung dieser Daten. Hierzu sowie zu weiteren Fragen zum Thema personenbezogene Daten können Sie sich jederzeit an uns wenden.</p>
<h3>SSL- bzw. TLS-Verschlüsselung</h3>
<p>Diese Seite nutzt aus Sicherheitsgründen und zum Schutz der Übertragung vertraulicher Inhalte, wie zum Beispiel Anfragen, die Sie an uns senden, eine SSL- bzw. TLS-Verschlüsselung. Eine verschlüsselte Verbindung erkennen Sie daran, dass die Adresszeile des Browsers mit „https://“ beginnt, und an dem Schloss-Symbol in Ihrer Browserzeile.</p>

<h2>4. Datenerfassung auf dieser Website</h2>
<h3>Anfrageformular</h3>
<p>Wenn Sie uns über das Anfrageformular eine Anfrage senden, werden Ihre Angaben aus dem Formular (Unternehmen, Name, E-Mail-Adresse, Telefonnummer, Art und Ort des Objekts, gewünschte Leistungen und Ihre Nachricht) sowie die Unterseite, auf der Sie das Formular abgeschickt haben, und gegebenenfalls Kampagnenangaben aus der Adresszeile (z. B. utm_campaign) per E-Mail an uns übermittelt und zur Bearbeitung der Anfrage und für Anschlussfragen bei uns gespeichert. Auf dem Webserver werden die Formulardaten nicht gespeichert. Sie erhalten eine automatische Eingangsbestätigung an die angegebene E-Mail-Adresse. Diese Daten geben wir nicht ohne Ihre Einwilligung weiter.</p>
<p>Die Verarbeitung erfolgt auf Grundlage von Art. 6 Abs. 1 lit. b DSGVO, sofern Ihre Anfrage mit der Erfüllung eines Vertrags zusammenhängt oder zur Durchführung vorvertraglicher Maßnahmen erforderlich ist. In allen übrigen Fällen beruht die Verarbeitung auf unserem berechtigten Interesse an der effektiven Bearbeitung der an uns gerichteten Anfragen (Art. 6 Abs. 1 lit. f DSGVO) oder auf Ihrer Einwilligung (Art. 6 Abs. 1 lit. a DSGVO).</p>
<p>Die von Ihnen eingegebenen Daten verbleiben bei uns, bis Sie uns zur Löschung auffordern, Ihre Einwilligung widerrufen oder der Zweck für die Datenspeicherung entfällt (z. B. nach abgeschlossener Bearbeitung Ihrer Anfrage). Zwingende gesetzliche Bestimmungen, insbesondere Aufbewahrungsfristen, bleiben unberührt.</p>
<h3>Anfrage per E-Mail oder Telefon</h3>
<p>Wenn Sie uns per E-Mail oder Telefon kontaktieren, wird Ihre Anfrage inklusive aller daraus hervorgehenden personenbezogenen Daten (Name, Anfrage) zum Zwecke der Bearbeitung Ihres Anliegens bei uns gespeichert und verarbeitet. Diese Daten geben wir nicht ohne Ihre Einwilligung weiter. Rechtsgrundlagen und Speicherdauer entsprechen den Angaben zum Anfrageformular.</p>
<h3>Adobe Fonts</h3>
<p>Diese Website nutzt zur einheitlichen Darstellung unserer Markenschrift Web Fonts von Adobe Fonts. Anbieter ist die Adobe Systems Software Ireland Companies, 4-6 Riverwalk, Citywest Business Campus, Dublin 24, Irland (Adobe). Beim Aufruf unserer Seiten lädt Ihr Browser die Schriftarten von Servern von Adobe. Dabei wird Ihre IP-Adresse an Adobe übermittelt; eine Übertragung in die USA ist nicht ausgeschlossen. Laut Adobe werden bei der Bereitstellung der Schriften keine Cookies gesetzt und die Daten nicht zur Erstellung von Nutzerprofilen verwendet.</p>
<p>Die Nutzung erfolgt auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO. Wir haben ein berechtigtes Interesse an einer einheitlichen Darstellung unseres Markenauftritts. Adobe ist nach dem EU-US Data Privacy Framework (DPF) zertifiziert. Weitere Informationen: <a href="https://www.adobe.com/de/privacy/policies/adobe-fonts.html" rel="noopener">Datenschutzhinweise zu Adobe Fonts</a> und <a href="https://www.adobe.com/de/privacy.html" rel="noopener">Datenschutzerklärung von Adobe</a>.</p>
<p>Ist die Schrift nicht erreichbar, verwendet Ihr Browser eine lokal von unserem Server geladene Ersatzschrift (Archivo).</p>

<h2 id="google-ads">5. Google Ads und Conversion-Tracking</h2>
<p>Wir schalten Anzeigen über Google Ads. Anbieter ist die Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland (Google). Um zu messen, ob eine Anzeige zu einer Anfrage oder einem Anruf geführt hat, nutzen wir das Conversion-Tracking von Google Ads, allerdings nur, wenn Sie im Einwilligungsfenster zugestimmt haben.</p>
<p>Mit Ihrer Einwilligung lädt Ihr Browser das Skript „gtag.js“ von Google. Kommen Sie über eine Google-Anzeige auf unsere Website, wird ein Cookie gesetzt, über das Google erkennt, ob Sie anschließend eine Anfrage senden oder auf unsere Telefonnummer tippen. Wir erhalten nur zusammengefasste Zahlen und können Sie dadurch nicht persönlich identifizieren. Dabei werden unter anderem Ihre IP-Adresse, Gerätedaten und Angaben zur besuchten Seite an Google übertragen; eine Übertragung in die USA ist möglich.</p>
<p>Rechtsgrundlage ist Ihre Einwilligung (Art. 6 Abs. 1 lit. a DSGVO und § 25 Abs. 1 TDDDG). Sie können die Einwilligung jederzeit über „Cookie-Einstellungen“ im Seitenfuß widerrufen. Ihre Entscheidung speichern wir im lokalen Speicher Ihres Browsers (§ 25 Abs. 2 TDDDG). Google ist nach dem EU-US Data Privacy Framework (DPF) zertifiziert. Weitere Informationen: <a href="https://policies.google.com/privacy?hl=de" rel="noopener">Datenschutzerklärung von Google</a> und <a href="https://business.safety.google/adsservices/" rel="noopener">Hinweise zu Google-Werbediensten</a>.</p>

<h2>6. Social Media</h2>
<p>Auf dieser Website verlinken wir auf unsere Profile bei Instagram und Facebook (Anbieter: Meta Platforms Ireland Limited, Merrion Road, Dublin 4, D04 X2K5, Irland). Es handelt sich um einfache Links, nicht um eingebundene Plugins. Erst wenn Sie einen Link anklicken, werden Sie auf die Seite des jeweiligen Anbieters weitergeleitet, und es gelten dessen Datenschutzbestimmungen.</p>

<h2>7. Umgang mit Bewerberdaten</h2>
<p>Wir bieten Ihnen die Möglichkeit, sich bei uns zu bewerben (z. B. per E-Mail, postalisch oder über unsere Karriereseite). Wenn Sie uns eine Bewerbung zukommen lassen, verarbeiten wir Ihre damit verbundenen personenbezogenen Daten (z. B. Kontakt- und Kommunikationsdaten, Bewerbungsunterlagen, Notizen im Rahmen von Bewerbungsgesprächen), soweit dies zur Entscheidung über die Begründung eines Beschäftigungsverhältnisses erforderlich ist. Rechtsgrundlage hierfür ist § 26 BDSG (Anbahnung eines Beschäftigungsverhältnisses), Art. 6 Abs. 1 lit. b DSGVO (allgemeine Vertragsanbahnung) und, sofern Sie eine Einwilligung erteilt haben, Art. 6 Abs. 1 lit. a DSGVO. Ihre Daten werden innerhalb unseres Unternehmens ausschließlich an Personen weitergegeben, die an der Bearbeitung Ihrer Bewerbung beteiligt sind.</p>
<p>Sofern wir Ihnen kein Stellenangebot machen können, Sie ein Stellenangebot ablehnen oder Ihre Bewerbung zurückziehen, bewahren wir Ihre Daten auf Grundlage unserer berechtigten Interessen (Art. 6 Abs. 1 lit. f DSGVO) bis zu 6 Monate ab Beendigung des Bewerbungsverfahrens auf. Anschließend werden die Daten gelöscht. Eine längere Aufbewahrung, zum Beispiel in unserem Bewerber-Pool, erfolgt nur mit Ihrer ausdrücklichen Einwilligung (Art. 6 Abs. 1 lit. a DSGVO); die Daten werden dann spätestens zwei Jahre nach Erteilung der Einwilligung gelöscht.</p>
<p><em>Stand: Oktober 2026</em></p>
"""

# ---------------- Einzelleistungen (Unterseiten der Leistungsbereiche) ----------------
# Nur Inhalte aus dem bestehenden Leistungsumfang (Texte für Homepage 2024, alte Seite, /test). Keine Preise, keine Fristen.
DETAILS = [
    {"slug": "unterhaltsreinigung", "parent": "/gebaeudereinigung/", "name": "Unterhaltsreinigung", "icon": "spruehflasche",
     "title": "Unterhaltsreinigung Bruchsal & Karlsruhe | WOHLverde",
     "desc": "Regelmäßige Unterhalts- und Büroreinigung für Unternehmen und Kommunen im Raum Bruchsal und Karlsruhe. Feste Teams, fester Plan, keine Subunternehmen.",
     "h1": "Unterhaltsreinigung für Büros und Gewerbe",
     "intro": "Saubere Büros, Sozialräume und Sanitärbereiche, jeden Tag oder jede Woche, ganz nach Ihrem Bedarf. Mit festen Teams, die Ihr Objekt kennen.",
     "kurz": "Die Unterhaltsreinigung von WOHLverde ist die regelmäßige Reinigung von Büros, Verwaltungs- und Gewerbeflächen im Raum Bruchsal und Karlsruhe. Wir reinigen nach einem festen Plan, mit eigenem, geschultem Personal und festen Ansprechpartnern.",
     "bild": "reinigung-tisch", "bild_alt": "WOHLverde-Mitarbeiterin reinigt einen Besprechungstisch", "bild2": "reinigung-buero-wisch", "bild2_alt": "WOHLverde-Mitarbeiterin wischt den Boden in einem Büro",
     "umfang": ["Büros, Besprechungsräume und Empfang", "Sozialräume und Teeküchen", "Sanitärbereiche", "Böden saugen und wischen", "Oberflächen und Kontaktflächen", "Papierkörbe und Müllentsorgung"],
     "fuer": ["Bürogebäude und Verwaltungen", "Gewerbe- und Industrieobjekte", "Kommunale Einrichtungen"],
     "faq": [("Wie oft sollte eine Unterhaltsreinigung stattfinden?", "Das hängt von Nutzung und Anforderungen ab. Üblich ist eine tägliche oder wöchentliche Reinigung. Den passenden Rhythmus legen wir beim Vor-Ort-Termin mit Ihnen fest."),
             ("Was ist der Unterschied zur Grundreinigung?", "Die Unterhaltsreinigung ist die laufende, regelmäßige Reinigung. Die Grundreinigung ist eine intensive Reinigung bei Bedarf, zum Beispiel nach Umbauten oder vor Übergaben."),
             ("Arbeitet WOHLverde mit Subunternehmen?", "Nein. Bei uns reinigen ausschließlich eigene, festangestellte und deutschsprachige Mitarbeitende.")]},
    {"slug": "glasreinigung", "parent": "/gebaeudereinigung/", "name": "Glas- und Fensterreinigung", "icon": "scheibenabzieher",
     "title": "Glas- & Fensterreinigung Bruchsal, Karlsruhe | WOHLverde",
     "desc": "Glas- und Fensterreinigung für Gewerbe, Büros und Wohnanlagen im Raum Bruchsal und Karlsruhe: Fenster, Glasflächen, Wintergärten, Terrassen- und Lamellendächer.",
     "h1": "Glas- und Fensterreinigung, streifenfrei",
     "intro": "Fenster, Glasflächen, Wintergärten, Terrassen- und Lamellendächer: Wir sorgen für klare Sicht und einen gepflegten ersten Eindruck.",
     "kurz": "WOHLverde reinigt Fenster und Glasflächen für Unternehmen, Hausverwaltungen und Kommunen im Raum Bruchsal und Karlsruhe, einmalig oder regelmäßig. Dazu gehören auch Wintergärten, Terrassen- und Lamellendächer.",
     "bild": "reinigung-fenster-ruecken", "bild_alt": "WOHLverde-Mitarbeiter reinigt ein Fenster in einem Büro", "bild2": "reinigung-fenster", "bild2_alt": "WOHLverde-Mitarbeiter mit Fensterabzieher",
     "umfang": ["Fenster innen und außen", "Glasflächen und Glastüren", "Rahmen und Fensterbänke", "Wintergärten", "Terrassendächer", "Lamellendächer"],
     "fuer": ["Bürogebäude und Geschäftshäuser", "Wohnanlagen", "Gewerbe- und Ladenflächen"],
     "faq": [("Reinigt WOHLverde Fenster innen und außen?", "Ja. Wir reinigen Fenster und Glasflächen innen und außen, inklusive Rahmen und Fensterbänken."),
             ("Kann ich die Glasreinigung regelmäßig buchen?", "Ja. Die Glasreinigung lässt sich als regelmäßige Leistung vereinbaren, auch zusammen mit der Unterhaltsreinigung."),
             ("Reinigt WOHLverde auch Terrassen- und Lamellendächer?", "Ja, ebenso Wintergärten.")]},
    {"slug": "treppenhausreinigung", "parent": "/gebaeudereinigung/", "name": "Treppenhausreinigung", "icon": "staubwedel",
     "title": "Treppenhausreinigung Bruchsal & Karlsruhe | WOHLverde",
     "desc": "Treppenhausreinigung für Wohnanlagen, Hausverwaltungen und Geschäftshäuser im Raum Bruchsal und Karlsruhe. Zuverlässig im vereinbarten Rhythmus, mit festen Teams.",
     "h1": "Treppenhausreinigung, auf die Verlass ist",
     "intro": "Für Wohnanlagen und Geschäftshäuser: saubere Treppenhäuser im vereinbarten Rhythmus, ohne Nachfragen und ohne Wechselpersonal.",
     "kurz": "WOHLverde übernimmt die Treppenhausreinigung für Hausverwaltungen, Eigentümergemeinschaften und Geschäftshäuser im Raum Bruchsal und Karlsruhe. Feste Teams reinigen im vereinbarten Rhythmus, auf Wunsch zusammen mit Hausmeisterservice und Grünpflege.",
     "bild": "reinigung-treppe-ruecken", "bild_alt": "WOHLverde-Mitarbeiterin reinigt ein Treppenhaus", "bild2": "reinigung-duo", "bild2_alt": "Zwei WOHLverde-Mitarbeitende im Treppenhaus",
     "umfang": ["Treppen und Podeste", "Geländer und Handläufe", "Eingangsbereiche", "Briefkastenanlagen und Türen", "Kellergänge auf Wunsch", "Kombinierbar mit Hausmeisterservice"],
     "fuer": ["Hausverwaltungen", "Wohnanlagen und Eigentümergemeinschaften", "Geschäftshäuser"],
     "faq": [("In welchem Rhythmus reinigt WOHLverde Treppenhäuser?", "Im Rhythmus, den Sie mit uns vereinbaren. Den Umfang legen wir beim Vor-Ort-Termin fest."),
             ("Kann ich Treppenhausreinigung und Hausmeisterservice zusammen beauftragen?", "Ja. Viele Hausverwaltungen beauftragen beides aus einer Hand, oft zusammen mit der Grünpflege."),
             ("Wer reinigt bei mir?", "Ein festes Team aus eigenen, festangestellten Mitarbeitenden. Kein Wechselpersonal, keine Subunternehmen.")]},
    {"slug": "baumpflege", "parent": "/garten-und-landschaftspflege/", "name": "Baumpflege", "icon": "heckenschere",
     "title": "Baumpflege & Baumschnitt Bruchsal, Karlsruhe | WOHLverde",
     "desc": "Baumpflege und Baumschnitt auf Firmengeländen, Wohnanlagen und kommunalen Flächen im Raum Bruchsal und Karlsruhe, bis hin zu Fällarbeiten.",
     "h1": "Baumpflege und Baumschnitt",
     "intro": "Gesunde, sichere Bäume auf Ihrem Gelände: fachgerechter Schnitt, Pflege und, wenn nötig, Fällarbeiten.",
     "kurz": "WOHLverde übernimmt Baumpflege und Baumschnitt auf Firmengeländen, Wohnanlagen und kommunalen Flächen im Raum Bruchsal und Karlsruhe, bis hin zu Fällarbeiten. Die Arbeiten sind Teil unserer Grünpflege und lassen sich mit der Jahrespflege kombinieren.",
     "bild": "baum-motorsaege", "bild_alt": "WOHLverde-Mitarbeiter mit Motorsäge an einem Baum", "bild2": "baum-schnitt", "bild2_alt": "WOHLverde-Mitarbeiter beim Baumschnitt mit Astschere",
     "umfang": ["Pflege- und Erziehungsschnitt", "Entfernen von Totholz", "Kronenpflege", "Fällarbeiten", "Abtransport des Schnittguts", "Kombinierbar mit der Jahrespflege"],
     "fuer": ["Firmengelände und Gewerbeparks", "Wohnanlagen", "Kommunale Grünflächen"],
     "faq": [("Übernimmt WOHLverde auch Baumfällungen?", "Ja. Von der Baumpflege bis zur Baumfällung, fachgerecht und sicher ausgeführt."),
             ("Wann ist der richtige Zeitpunkt für einen Baumschnitt?", "Das hängt von Baumart, Standort und Art des Schnitts ab. Je nach Lage gelten Schutzzeiten nach dem Bundesnaturschutzgesetz und teilweise kommunale Baumschutzsatzungen. Das prüfen wir vor dem Einsatz und beraten Sie beim Vor-Ort-Termin."),
             ("Kann die Baumpflege Teil der Jahrespflege sein?", "Ja. Wir planen Baumpflege, Rasen, Hecken und Winterdienst gemeinsam über das Jahr.")]},
    {"slug": "heckenschnitt", "parent": "/garten-und-landschaftspflege/", "name": "Hecken- und Gehölzschnitt", "icon": "heckenschere",
     "title": "Heckenschnitt für Gewerbe Bruchsal, Karlsruhe | WOHLverde",
     "desc": "Hecken-, Strauch- und Gehölzschnitt auf Firmengeländen, Wohnanlagen und kommunalen Flächen im Raum Bruchsal und Karlsruhe. Fachgerecht und regelmäßig.",
     "h1": "Hecken- und Gehölzschnitt",
     "intro": "Gepflegte Hecken und Sträucher sind die Visitenkarte Ihres Geländes. Wir schneiden fachgerecht und regelmäßig, damit es so bleibt.",
     "kurz": "WOHLverde schneidet Hecken, Sträucher, Gräser und Gehölze auf Firmengeländen, Wohnanlagen und kommunalen Flächen im Raum Bruchsal und Karlsruhe, als Einzelauftrag oder als Teil der Jahrespflege.",
     "bild": "garten-hecke-sommer", "bild_alt": "WOHLverde-Mitarbeiter beim Heckenschnitt", "bild2": "garten-graeser", "bild2_alt": "WOHLverde-Mitarbeiter beim Rückschnitt von Ziergräsern",
     "umfang": ["Formschnitt von Hecken", "Rückschnitt von Sträuchern", "Rückschnitt von Gräsern", "Gehölzpflege", "Abtransport des Schnittguts", "Kombinierbar mit der Jahrespflege"],
     "fuer": ["Firmengelände und Gewerbeparks", "Wohnanlagen", "Kommunale Grünflächen"],
     "faq": [("Wann dürfen Hecken geschnitten werden?", "Schonende Form- und Pflegeschnitte sind ganzjährig erlaubt. Radikale Rückschnitte sind laut Bundesnaturschutzgesetz nur außerhalb der Zeit vom 1. März bis 30. September zulässig. Wir planen die Termine entsprechend."),
             ("Wie oft sollte eine Hecke geschnitten werden?", "Das hängt von Pflanze und gewünschtem Erscheinungsbild ab. Den passenden Rhythmus legen wir in der Jahrespflege fest."),
             ("Wird das Schnittgut entsorgt?", "Ja, wir nehmen das Schnittgut mit.")]},
    {"slug": "unkrautbeseitigung", "parent": "/garten-und-landschaftspflege/", "name": "Unkrautbeseitigung", "icon": "rechen",
     "title": "Unkrautbeseitigung Bruchsal & Karlsruhe | WOHLverde",
     "desc": "Unkrautbeseitigung auf Grün- und Grauflächen, Pflaster, Wegen und Parkplätzen von Firmengeländen und Wohnanlagen im Raum Bruchsal und Karlsruhe. Umweltschonend.",
     "h1": "Unkrautbeseitigung auf Grün- und Grauflächen",
     "intro": "Pflaster, Wege, Parkplätze und Beete: Wir entfernen Unkraut umweltschonend und halten die Flächen dauerhaft gepflegt.",
     "kurz": "WOHLverde entfernt Unkraut auf Grün- und Grauflächen, also auf Beeten, Pflaster, Wegen und Parkflächen von Firmengeländen, Wohnanlagen und kommunalen Flächen im Raum Bruchsal und Karlsruhe. Wir arbeiten mit umweltschonenden Methoden.",
     "bild": "nachher-pflaster", "bild_alt": "Gepflasterter Weg auf einem Firmengelände nach der Unkrautbeseitigung", "bild2": "garten-pflanzen", "bild2_alt": "WOHLverde-Mitarbeiterin bei Arbeiten an einem Beet",
     "umfang": ["Pflaster und Wege", "Parkplätze und Einfahrten", "Beete und Pflanzflächen", "Kanten und Fugen", "Umweltschonende Methoden", "Als Einzelauftrag oder Jahrespflege"],
     "fuer": ["Firmengelände und Industrieflächen", "Wohnanlagen", "Kommunale Flächen"],
     "vn": True,
     "faq": [("Welche Methoden nutzt WOHLverde zur Unkrautbeseitigung?", "Effektive und umweltschonende Methoden, etwa manuelle Entfernung, Mulchen und biologisch abbaubare Mittel."),
             ("Was sind Grauflächen?", "Befestigte Flächen wie Pflaster, Wege, Parkplätze und Einfahrten, im Gegensatz zu Grünflächen wie Rasen und Beeten."),
             ("Reicht ein einmaliger Einsatz?", "Unkraut wächst nach. Damit die Flächen dauerhaft gepflegt bleiben, empfehlen wir einen festen Pflegeplan.")]},
]

# ---------------- Ratgeber ----------------
RATGEBER = [
    {"slug": "unterhaltsreinigung-oder-grundreinigung", "seo_title": "Unterhaltsreinigung oder Grundreinigung? | WOHLverde", "title": "Unterhaltsreinigung oder Grundreinigung: der Unterschied",
     "desc": "Was ist der Unterschied zwischen Unterhaltsreinigung und Grundreinigung, und wann braucht ein Unternehmen was? Kurz erklärt von WOHLverde aus Forst.",
     "teaser": "Zwei Begriffe, zwei Aufgaben. Wann Sie welche Reinigung brauchen.", "bild": "reinigung-tisch", "bild_alt": "Reinigung eines Besprechungstischs",
     "kurz": "Die Unterhaltsreinigung ist die regelmäßige, laufende Reinigung nach festem Plan. Die Grundreinigung ist eine intensive Reinigung bei Bedarf, zum Beispiel nach Umbauten, vor Übergaben oder wenn sich Verschmutzungen festgesetzt haben. Die meisten Unternehmen brauchen beides: die Unterhaltsreinigung als Standard und die Grundreinigung zu bestimmten Anlässen.",
     "abschnitte": [
        ("Was ist Unterhaltsreinigung?", "Die Unterhaltsreinigung hält Räume im Alltag sauber. Sie findet regelmäßig statt, je nach Nutzung täglich oder wöchentlich, und folgt einem festen Reinigungsplan. Typisch sind Büros, Besprechungsräume, Sozialräume, Teeküchen und Sanitärbereiche. Ziel ist ein gleichbleibend gepflegter Zustand."),
        ("Was ist Grundreinigung?", "Die Grundreinigung geht tiefer. Sie entfernt Verschmutzungen, die die laufende Reinigung nicht erfasst, etwa festsitzende Rückstände auf Böden. Sie wird bei Bedarf beauftragt, zum Beispiel nach Umbauten, vor der Übergabe von Räumen oder einmal im Jahr als Auffrischung."),
        ("Was braucht mein Unternehmen?", "In den meisten Fällen beides. Die Unterhaltsreinigung sorgt für den Alltag, die Grundreinigung für besondere Anlässe. Welcher Rhythmus sinnvoll ist, hängt von Fläche, Nutzung und Anforderungen ab und lässt sich am besten bei einem Termin vor Ort klären."),
        ("Wie WOHLverde das löst", "Wir übernehmen Unterhaltsreinigung und Grundreinigung aus einer Hand, mit festen Teams aus eigenen, festangestellten Mitarbeitenden. Den Reinigungsplan stimmen wir beim Vor-Ort-Termin mit Ihnen ab.")],
     "links": ["/gebaeudereinigung/unterhaltsreinigung/", "/gebaeudereinigung/"]},
    {"slug": "gruenpflege-im-jahresverlauf", "seo_title": "Grünpflege im Jahresverlauf für Firmen | WOHLverde", "title": "Grünpflege im Jahresverlauf: was auf Firmengeländen wann ansteht",
     "desc": "Welche Grünpflege-Arbeiten auf Firmengeländen im Frühjahr, Sommer, Herbst und Winter anstehen und warum ein Jahrespflegeplan Zeit und Abstimmung spart.",
     "teaser": "Frühjahr, Sommer, Herbst, Winter: der Überblick für Ihr Gelände.", "bild": "garten-hecke-sommer", "bild_alt": "Heckenschnitt im Sommer",
     "kurz": "Auf Firmengeländen verteilt sich die Grünpflege über das ganze Jahr: Im Frühjahr Rückschnitt und Vorbereitung, im Sommer Rasen, Hecken und Unkraut, im Herbst Laub und Gehölzpflege, im Winter Räum- und Streudienst. Ein Jahrespflegeplan legt alles einmal fest, statt jeden Einsatz einzeln zu beauftragen.",
     "abschnitte": [
        ("Frühjahr", "Rückschnitt von Gräsern und Stauden, Säubern der Beete, erste Rasenpflege und Unkrautbeseitigung auf Wegen und Pflaster. Jetzt wird das Gelände für die Saison vorbereitet."),
        ("Sommer", "Regelmäßiges Mähen, Kantenpflege, Formschnitt von Hecken und Unkrautbeseitigung auf Grün- und Grauflächen. In der Wachstumsphase ist ein fester Rhythmus wichtig."),
        ("Herbst", "Laubbeseitigung, Gehölzpflege und Vorbereitung auf den Winter. Größere Rückschnitte von Hecken und Gehölzen sind laut Bundesnaturschutzgesetz grundsätzlich außerhalb der Zeit vom 1. März bis 30. September vorzunehmen."),
        ("Winter", "Räum- und Streudienst für Zufahrten, Gehwege und Parkflächen. Am besten vor der Saison planen, welche Flächen in welcher Reihenfolge betreut werden."),
        ("Warum ein Jahrespflegeplan sinnvoll ist", "Mit einem Plan für das ganze Jahr entfällt die Abstimmung vor jedem Einsatz. Ein fester Partner kennt das Gelände, plant saisonal und dokumentiert die Arbeiten. WOHLverde übernimmt Grünpflege und Winterdienst aus einer Hand.")],
     "links": ["/garten-und-landschaftspflege/", "/winterdienst/"]},
    {"slug": "winterdienst-fuer-gewerbe", "seo_title": "Winterdienst für Gewerbe: Ratgeber | WOHLverde", "title": "Winterdienst für Gewerbe: worauf Unternehmen achten sollten",
     "desc": "Wer räumt, wann und wo? Worauf Unternehmen, Hausverwaltungen und Kommunen beim Winterdienst achten sollten. Ein Überblick von WOHLverde.",
     "teaser": "Wer räumt, wann und wo? Die wichtigsten Punkte vor der Saison.", "bild": "team-fahrzeug", "bild_alt": "Das WOHLverde-Team in Winterkleidung",
     "kurz": "Eigentümer und Betreiber von Gewerbeimmobilien müssen dafür sorgen, dass Zufahrten, Gehwege und Eingänge im Winter sicher begehbar sind. Die genauen Pflichten und Zeiten regelt die jeweilige Gemeinde in ihrer Satzung. Wer den Winterdienst an einen Dienstleister vergibt, sollte Flächen, Abläufe und Zuständigkeiten vor der Saison schriftlich festlegen.",
     "abschnitte": [
        ("Wer ist zuständig?", "Grundsätzlich der Eigentümer oder Betreiber des Grundstücks. Die Gemeinden regeln in ihren Satzungen, welche Flächen zu räumen sind und zu welchen Zeiten. Diese Regeln unterscheiden sich von Ort zu Ort, darum lohnt sich ein Blick in die Satzung Ihrer Gemeinde."),
        ("Was gehört dazu?", "Schnee räumen und Glätte bekämpfen auf Zufahrten, Gehwegen, Eingängen und Parkflächen. Bei Gewerbeobjekten kommen oft Lieferzonen, Notausgänge und Mitarbeiterparkplätze dazu."),
        ("Vor der Saison planen", "Legen Sie fest, welche Flächen in welcher Reihenfolge betreut werden und wer im Ernstfall Ansprechpartner ist. Ein Flächenplan verhindert Missverständnisse, wenn es schnell gehen muss."),
        ("Winterdienst aus einer Hand", "Wer im Sommer schon einen Dienstleister für Grünpflege oder Hausmeisterservice hat, kann den Winterdienst oft gleich mit vergeben. Die Teams kennen die Flächen bereits. WOHLverde übernimmt den Winterdienst im Raum Bruchsal und Karlsruhe, auf Wunsch zusammen mit Grünpflege und Hausmeisterservice.")],
     "links": ["/winterdienst/", "/hausmeister-service/"]},
]

# ---------------- Glossar (30 Begriffe) ----------------
# Allgemeine Fachbegriffe, sachlich erklaert. Keine Preise, keine Fristen ausser allgemein bekannten gesetzlichen Regeln.
GLOSSAR = [
    ("Bauendreinigung", "Reinigung nach Abschluss von Bau- oder Umbauarbeiten. Sie entfernt Baustaub, Farb- und Materialreste, damit Räume übergeben und genutzt werden können.", "/gebaeudereinigung/"),
    ("Baumkontrolle", "Regelmäßige Sichtprüfung von Bäumen auf Schäden, Totholz und Standsicherheit. Sie dient der Verkehrssicherheit, besonders an Wegen, Parkplätzen und Gebäuden.", "/garten-und-landschaftspflege/baumpflege/"),
    ("Baumpflege", "Alle Maßnahmen, die Bäume gesund und sicher halten: Pflege- und Erziehungsschnitt, Entfernen von Totholz, Kronenpflege und, wenn nötig, Fällarbeiten.", "/garten-und-landschaftspflege/baumpflege/"),
    ("Formschnitt", "Regelmäßiger Schnitt, der Hecken und Sträucher in einer gewünschten Form hält. Schonende Form- und Pflegeschnitte sind ganzjährig erlaubt.", "/garten-und-landschaftspflege/heckenschnitt/"),
    ("Gehölzschnitt", "Sammelbegriff für den Schnitt von Bäumen, Sträuchern und Hecken. Ziel ist eine gesunde Entwicklung, Sicherheit und ein gepflegtes Erscheinungsbild.", "/garten-und-landschaftspflege/heckenschnitt/"),
    ("Glasreinigung", "Reinigung von Fenstern, Glasflächen und Glastüren innen und außen, meist inklusive Rahmen und Fensterbänken. Dazu zählen auch Wintergärten und Glasdächer.", "/gebaeudereinigung/glasreinigung/"),
    ("Grauflächen", "Befestigte Außenflächen wie Pflaster, Wege, Parkplätze und Einfahrten. Der Begriff grenzt sie von Grünflächen wie Rasen und Beeten ab.", "/garten-und-landschaftspflege/unkrautbeseitigung/"),
    ("Grünflächen", "Bepflanzte Außenflächen wie Rasen, Beete, Hecken und Gehölzflächen. Ihre Pflege ist Teil der Grünpflege.", "/garten-und-landschaftspflege/"),
    ("Grünpflege", "Pflege aller Grünanlagen eines Objekts: Rasen, Hecken, Sträucher, Bäume, Beete sowie Unkrautbeseitigung auf Grün- und Grauflächen. Auch Garten- und Landschaftspflege genannt.", "/garten-und-landschaftspflege/"),
    ("Grundreinigung", "Intensive Reinigung bei Bedarf, die tiefer geht als die laufende Reinigung. Typische Anlässe sind Umbauten, Übergaben oder festsitzende Verschmutzungen.", "/ratgeber/unterhaltsreinigung-oder-grundreinigung/"),
    ("Hausmeisterservice", "Technische und organisatorische Betreuung einer Immobilie: Objektkontrollen, Kleinreparaturen, Mülltonnenservice, Zählerstände und die Koordination externer Dienstleister.", "/hausmeister-service/"),
    ("Heckenschnitt", "Schnitt von Hecken zur Formgebung und Pflege. Radikale Rückschnitte sind laut Bundesnaturschutzgesetz nur außerhalb der Zeit vom 1. März bis 30. September zulässig.", "/garten-und-landschaftspflege/heckenschnitt/"),
    ("Jahrespflege", "Pflegeplan für Außenanlagen über das ganze Jahr. Alle Arbeiten von der Frühjahrspflege bis zum Winterdienst werden einmal festgelegt statt einzeln beauftragt.", "/ratgeber/gruenpflege-im-jahresverlauf/"),
    ("Kronenpflege", "Schnittmaßnahmen in der Baumkrone, etwa das Entfernen von Totholz oder störenden Ästen. Sie verbessert Gesundheit und Sicherheit des Baums.", "/garten-und-landschaftspflege/baumpflege/"),
    ("Laubbeseitigung", "Entfernen von Laub von Rasen, Wegen, Parkplätzen und Dachrinnen, vor allem im Herbst. Nasses Laub auf Wegen kann zur Rutschgefahr werden.", "/garten-und-landschaftspflege/"),
    ("Leistungsverzeichnis", "Auflistung aller vereinbarten Arbeiten mit Umfang und Rhythmus. Es macht klar, was wann erledigt wird, und ist die Grundlage für ein transparentes Angebot.", "/kontakt/"),
    ("Mulchen", "Abdecken von Beeten mit organischem Material wie Rindenmulch. Es hält den Boden feucht und unterdrückt Unkraut auf natürliche Weise.", "/garten-und-landschaftspflege/unkrautbeseitigung/"),
    ("Mülltonnenservice", "Bereitstellen der Müllbehälter zur Abholung und Zurückstellen danach, oft verbunden mit Ordnung an den Standplätzen. Typische Aufgabe im Hausmeisterservice.", "/hausmeister-service/"),
    ("Objektbetreuung", "Ganzheitliche Betreuung einer Immobilie aus einer Hand, zum Beispiel Gebäudereinigung, Grünpflege, Hausmeisterservice und Winterdienst durch einen Dienstleister.", "/"),
    ("Objektkontrolle", "Regelmäßige Begehung einer Immobilie, bei der Mängel und Auffälligkeiten erfasst und gemeldet werden. Mit Protokoll ist sie für den Auftraggeber nachvollziehbar.", "/hausmeister-service/"),
    ("Pflegeschnitt", "Schonender Schnitt, der Pflanzen gesund hält, etwa durch Entfernen abgestorbener oder störender Triebe. Er ist ganzjährig erlaubt.", "/garten-und-landschaftspflege/heckenschnitt/"),
    ("Räum- und Streupflicht", "Pflicht, Gehwege und Zugänge bei Schnee und Glätte sicher begehbar zu halten. Welche Flächen und Zeiten gelten, regelt die jeweilige Gemeinde in ihrer Satzung.", "/ratgeber/winterdienst-fuer-gewerbe/"),
    ("Reinigungsintervall", "Der Rhythmus, in dem eine Reinigung stattfindet, etwa täglich, wöchentlich oder monatlich. Er richtet sich nach Nutzung und Anforderungen der Räume.", "/gebaeudereinigung/unterhaltsreinigung/"),
    ("Rückschnitt", "Stärkeres Einkürzen von Pflanzen, um sie zu verjüngen oder in Form zu bringen. Bei Hecken sind radikale Rückschnitte nur außerhalb der Brut- und Setzzeit erlaubt.", "/garten-und-landschaftspflege/heckenschnitt/"),
    ("Subunternehmen", "Firmen, die ein beauftragter Dienstleister für Teile der Arbeit einsetzt. WOHLverde arbeitet ohne Subunternehmen, ausschließlich mit eigenem Personal.", "/ueber-uns/"),
    ("Totholz", "Abgestorbene Äste in einer Baumkrone. Sie können herabfallen und werden bei der Baumpflege entfernt, besonders über Wegen und Parkplätzen.", "/garten-und-landschaftspflege/baumpflege/"),
    ("Treppenhausreinigung", "Regelmäßige Reinigung von Treppen, Podesten, Geländern und Eingangsbereichen in Wohnanlagen und Geschäftshäusern.", "/gebaeudereinigung/treppenhausreinigung/"),
    ("Unkrautbeseitigung", "Entfernen unerwünschter Pflanzen auf Grün- und Grauflächen. Umweltschonende Methoden sind etwa manuelle Entfernung und Mulchen.", "/garten-und-landschaftspflege/unkrautbeseitigung/"),
    ("Unterhaltsreinigung", "Regelmäßige, laufende Reinigung nach festem Plan, etwa von Büros, Sozialräumen und Sanitärbereichen. Sie hält Räume im Alltag sauber.", "/gebaeudereinigung/unterhaltsreinigung/"),
    ("Verkehrssicherungspflicht", "Pflicht von Eigentümern und Betreibern, Gefahren auf ihrem Grundstück für andere zu vermeiden, etwa durch Winterdienst, Baumkontrolle oder sichere Wege.", "/ratgeber/winterdienst-fuer-gewerbe/"),
    ("Winterdienst", "Räumen von Schnee und Bekämpfen von Glätte auf Zufahrten, Gehwegen, Eingängen und Parkflächen, damit alle sicher ankommen.", "/winterdienst/"),
]
