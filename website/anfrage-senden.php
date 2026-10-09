<?php
/* WOHLverde | Anfrageformular
   Nimmt die Anfrage entgegen, schickt sie per mail() an EMPFAENGER und eine Eingangsbestaetigung an den Absender.
   Speichert nichts. Schutz: unsichtbares Feld (website) und Zeitsperre (3 Sekunden). */

const EMPFAENGER = 'info@wohlverde.de';   // vor dem Livegang mit Nico bestaetigen
const ABSENDER   = 'info@wohlverde.de';   // echte Adresse auf derselben Domain
const FIRMA      = 'WOHLverde';

header('Content-Type: application/json; charset=utf-8');
header('X-Robots-Tag: noindex');

function antwort($ok, $code = 200, $info = '') {
    http_response_code($code);
    echo json_encode(['ok' => $ok, 'info' => $info], JSON_UNESCAPED_UNICODE);
    exit;
}
function feld($k, $max = 500) {
    $v = isset($_POST[$k]) ? (is_array($_POST[$k]) ? implode(', ', $_POST[$k]) : $_POST[$k]) : '';
    $v = trim(str_replace(["\r", "\0"], '', $v));
    return mb_substr($v, 0, $max);
}
function kopf($s) { return '=?UTF-8?B?' . base64_encode($s) . '?='; }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') antwort(false, 405, 'Nur POST');

// Roboter-Schutz
if (feld('website') !== '') antwort(true);                       // Honigtopf: still "ok" sagen
$ts = (int) feld('ts', 20);
if ($ts > 0 && (microtime(true) * 1000 - $ts) < 3000) antwort(false, 429, 'Zu schnell');

$d = [
    'Unternehmen'    => feld('firma', 200),
    'Ansprechpartner'=> feld('name', 200),
    'E-Mail'         => feld('email', 200),
    'Telefon'        => feld('telefon', 60),
    'Objekt'         => feld('objekt', 100),
    'Ort'            => feld('ort', 120),
    'Leistungen'     => feld('leistung', 300),
    'Nachricht'      => feld('nachricht', 5000),
];
$ds = feld('datenschutz', 5);

// Pflichtfelder (dritte Pruefung nach Browser und app.js)
if ($d['Ansprechpartner'] === '' || $d['Nachricht'] === '' || $ds !== 'ja') antwort(false, 422, 'Pflichtfelder fehlen');
if (!filter_var($d['E-Mail'], FILTER_VALIDATE_EMAIL)) antwort(false, 422, 'E-Mail ungueltig');
foreach (['Ansprechpartner', 'E-Mail', 'Unternehmen', 'Telefon'] as $k) {
    if (preg_match('/[\n\r]/', $d[$k])) antwort(false, 422, 'Ungueltige Eingabe');
}

// Mail an WOHLverde
$text = "Neue Anfrage über wohlverde.de\n\n";
foreach ($d as $k => $v) { if ($v !== '') $text .= str_pad($k . ':', 17) . ($k === 'Nachricht' ? "\n" . $v : $v) . "\n"; }
$text .= "\nGesendet am " . date('d.m.Y') . ' um ' . date('H:i') . " Uhr\n";

$betreff = 'Anfrage über wohlverde.de: ' . ($d['Unternehmen'] !== '' ? $d['Unternehmen'] : $d['Ansprechpartner']);
$h  = "From: " . kopf(FIRMA . ' Webseite') . " <" . ABSENDER . ">\r\n";
$h .= "Reply-To: " . kopf($d['Ansprechpartner']) . " <" . $d['E-Mail'] . ">\r\n";
$h .= "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n";
$ok = mail(EMPFAENGER, kopf($betreff), $text, $h, '-f' . ABSENDER);
if (!$ok) antwort(false, 500, 'Versand fehlgeschlagen');

// Eingangsbestaetigung an den Absender
$b  = "Guten Tag " . $d['Ansprechpartner'] . ",\n\n";
$b .= "vielen Dank für Ihre Anfrage. Sie ist bei uns angekommen. Wir melden uns in der Regel innerhalb eines Werktags bei Ihnen.\n\n";
$b .= "Ihre Angaben:\n";
foreach ($d as $k => $v) { if ($v !== '' && $k !== 'Nachricht') $b .= "  " . $k . ": " . $v . "\n"; }
$b .= "\nIhre Nachricht:\n" . $d['Nachricht'] . "\n\n";
$b .= "Freundliche Grüße\nIhr Team von WOHLverde\n\nWOHLverde | Grünpflege & Gebäudereinigung\nKronauer Allee 1, 76694 Forst\nTelefon 07251 3924446 | info@wohlverde.de | wohlverde.de\n";
$h2  = "From: " . kopf(FIRMA) . " <" . ABSENDER . ">\r\n";
$h2 .= "Reply-To: " . ABSENDER . "\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n";
@mail($d['E-Mail'], kopf('Ihre Anfrage bei WOHLverde'), $b, $h2, '-f' . ABSENDER);

antwort(true);
