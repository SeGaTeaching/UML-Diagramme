# Dozentenskript — Tag 1: UML-Grundidee, Use-Case- und Klassendiagramme

**Die ersten beiden Diagrammtypen — live gezeichnet, Element für Element**
UML-Diagramme · Tag 1 von 3 · **Vormittag Unterricht · Nachmittag Selbstlernphase** · Folien 1–27

> **Das ist kein Vorlese-Skript.** Es ist dein roter Faden durch den Vormittag — und vor allem eine
> **Zeichen-Regie**: An jeder mit **`AKTIV`** markierten Stelle baust du das jeweilige Diagramm
> **selbst live** in einem Zeichentool auf, Baustein für Baustein, und sprichst dabei genau die
> Sätze, die unter dem Baustein stehen. Am Ende jedes Blocks steht ein **vollständiges** Diagramm
> vor der Gruppe — mit allen Sonderfällen, die üblicherweise zu Verwechslungen führen. Die Folien
> begleiten dich (Zweck, Notation, Referenz), aber das Diagramm selbst **entsteht vor den Augen der
> Gruppe**, nicht als fertiges Bild von der Folie.
>
> **Die Zeiten unten sind ein Vorschlag** für einen Vormittag mit rund dreieinhalb
> Unterrichtsstunden. Verschieb die Blockgrenzen auf deinen tatsächlichen Stundenplan — der
> **Feinschnitt** und der **Notfallweg** sagen dir, woran du das Tempo misst und was zuerst entfällt.

---

## Der Zeitschnitt

| Zeit (Vorschlag) | Teil | Folien | Dauer |
|---|---|---|---|
| 08:30–08:45 | Einstieg — Was ist UML, was kommt heute | **1** | 15 min |
| **08:45–10:15** | **Block 1 · UML-Grundidee und Use-Case-Diagramme** | **2–10** | 90 min |
| 10:15–10:30 | Pause | | 15 min |
| 10:30–10:45 | **Zwischenübung Use-Case** (Teil A, gemeinsam) | Aufgabenblatt 7.1 | 15 min |
| **10:45–12:15** | **Block 2 · Klassendiagramme** | **11–27** | 90 min |
| 12:15–12:30 | **Zwischenübung Klasse** (Teil A, gemeinsam) | Aufgabenblatt 7.2 | 15 min |
| **Nachmittag** | **Selbstlernphase** — Aufgaben Teil B zu 7.1 und 7.2, im Portal | | offen |

**Feinschnitt Block 1:**

| Zeit | Teil | Folien |
|---|---|---|
| 08:45–09:05 | 1.1 · Was ist UML, die Diagramm-Landkarte | 2–3 |
| 09:05–09:40 | 1.2 · Use-Case: Akteure, Anwendungsfälle, Systemgrenze | 4–7 |
| 09:40–10:15 | 1.3 · Beziehungen, Live-Komplettaufbau am Geldautomaten | 8–10 |

**Feinschnitt Block 2:**

| Zeit | Teil | Folien |
|---|---|---|
| 10:45–11:15 | 2.1 · Die Klasse: Live-Komplettaufbau mit zwei Klassen | 11–14 |
| 11:15–11:25 | 2.2 · Interfaces (Ergänzung, Java-Bezug) | 15, 17–19 |
| 11:25–12:05 | 2.3 · Die vier Beziehungen und ihre Pfeile, Raute-Test live | 16, 20–26 |
| 12:05–12:15 | 2.4 · Objektdiagramm und Abschluss | 27 |

> **Woran du das Tempo misst:** Bist du **10:15** am Ende von Folie 10, liegst du gut. Der
> Klassendiagramm-Block ist der dichtere — wenn etwas drängt, kürze bei den Interfaces (17–19,
> Ergänzung), **nicht** bei den Live-Aufbauten. Der Notfallweg unten sagt die Reihenfolge.

---

## Vor dem Unterricht

### 1. Vier Fenster bereitlegen

`UML_Diagramme.pptx` — die 58 Folien (heute 1–27). Dieses Dozentenskript auf dem **zweiten
Fenster** oder Monitor. Das **Portal** (`../Portal/HTML/index.html`) für Lerntext und Übungen. Und —
neu und heute zentral — ein **Zeichentool** für den Live-Aufbau, siehe unten.

### 2. Das Zeichentool: Empfehlung draw.io (diagrams.net)

Du baust die Diagramme **selbst live** auf, Element für Element. **Empfehlung: draw.io**
(`app.diagrams.net`, kostenlos, ohne Konto, läuft im Browser oder als Desktop-App).

**Warum draw.io für diese Aufgabe gewinnt:** Es hat **fertige UML-Shape-Bibliotheken** — Akteur
(Strichmännchen), Use-Case-Ellipse, Klasse mit den drei Fächern, alle Beziehungspfeile
(Vererbungsdreieck, Rauten, gestrichelte Pfeile) liegen fix und fertig in der Seitenleiste. Elemente
**rasten ein** und **verbinden sich sauber** mit den richtigen Pfeilspitzen — du zeichnest kein
krummes Dreieck von Hand, sondern ziehst das korrekte UML-Symbol auf die Fläche. Das Ergebnis ist
am Ende ein **korrektes** Diagramm, kein nur ungefähr richtiges. Export als SVG/PNG geht mit einem
Klick, falls du das Ergebnis sichern oder ins Portal stellen willst.

**Einrichtung (einmalig, dauert eine Minute):** In draw.io links in der Formenpalette ganz unten auf
„**More Shapes…**" klicken, die Kategorie **UML** aktivieren, bestätigen — danach liegen Akteur,
Use-Case-Ellipse, Klassen-Box und alle Beziehungspfeile fix in der Seitenleiste bereit.

**Alternativen, falls du sie bevorzugst:**

| | **draw.io** (empfohlen) | Excalidraw | Miro |
|---|---|---|---|
| UML-Symbole korrekt & fertig | ja, eigene UML-Bibliothek | nein, frei Hand gezeichnet | teils, per Vorlage |
| Elemente rasten/verbinden sauber | ja | nein, bewusst „unfertig" | ja |
| Stil | sauber, technisch korrekt | locker, „handgezeichnet" | neutral |
| Konto nötig | nein | nein | ja |
| Export | SVG/PNG | PNG/SVG | PNG/PDF |

**Excalidraw** (`excalidraw.com`) ist die gute Alternative, wenn du bewusst einen lockeren,
„handgezeichneten" Stil willst — der signalisiert „wir entwickeln das gerade", was manchen Gruppen
die Scheu nimmt, selbst mitzuzeichnen. Der Nachteil: Es gibt keine fertigen UML-Symbole, du
zeichnest Dreiecke und Rauten frei Hand, mit dem Risiko, dass sie nicht ganz UML-konform aussehen.
**Miro** nur, wenn du ohnehin schon damit arbeitest und deine Gruppe es kennt — für den reinen
Live-Aufbau bringt es gegenüber draw.io keinen Vorteil, aber mehr Overhead (Konto, Board anlegen).

> **Vorbereiten:** draw.io offen, ein leeres Blatt, UML-Kategorie aktiviert (siehe oben). An den mit
> **`AKTIV`** markierten Stellen baust du das jeweilige Diagramm **live, Element für Element** auf,
> statt nur die Folie zu zeigen. Zieh dir die Grundformen (Akteur, Ellipse, Rechteck-Klasse) schon
> vor Kursbeginn einmal testweise auf die Fläche, damit du im Unterricht nicht suchen musst.

### 3. Kein Code — bewusst

Der Kurs lehrt **Modellierung**, nicht Programmierung; die Codebeispiele sind aus den Lerntexten
heraus. **Aber:** Die Gruppe kommt aus Java. Übersetze UML deshalb **mündlich** nach Java, wo es
das Verständnis stützt (`-attribut` → `private`, △ → `extends`, `<<interface>>` → `implements`).
Das ist der stärkste Hebel, den du bei dieser Gruppe hast.

### 4. Die Wikipedia-Folien kennen

Mehrere Folien (3, 5, 6, 7, 10, 15) zeigen **eingebettete Wikipedia-Grafiken** mit CC-BY-SA-Quelle.
Sie sind lizenzrechtlich sauber (Attribution steht drauf), aber teils **klein oder englisch**. Zeig
sie kurz zur Orientierung — das **eigentliche** Diagramm entsteht ohnehin live in draw.io, nicht auf
der Folie. Für Nacharbeit verweise auf die deutschen, größeren Portal-SVGs.

---

## Der Einstieg um 08:30

**`▶ FOLIE` 1 — Titelfolie: UML-Diagramme**

**`SO ERKLÄRST DU ES`**

> Guten Morgen. In den nächsten Tagen lernen Sie eine Sprache — aber keine Programmier­sprache,
> sondern eine **Bildsprache**: UML, die Unified Modeling Language. Damit zeichnet man Software,
> bevor man sie baut.
>
> Sie kennen Java. Stellen Sie sich vor, Sie sollen mit drei Kollegen ein größeres System bauen.
> Bevor die erste Zeile Code entsteht, müssen sich alle einig sein: **Welche Klassen gibt es, wer
> darf was, wie hängt das zusammen?** Genau dafür ist UML da — es ist der **Bauplan vor dem Code**.
>
> Heute nehmen wir die zwei Diagramme, mit denen jede Modellierung anfängt: das **Use-Case-Diagramm**
> — die Sicht von außen, wer will was vom System — und das **Klassendiagramm** — die Sicht von
> innen, woraus das System besteht. Und ich zeichne heute alles selbst mit — Sie sehen jedes
> Diagramm wachsen, nicht fertig von der Folie fallen.

**`? FRAGEN`**

> Kurze Handzeichenfrage: Wer hat schon einmal ein UML-Diagramm gesehen — egal wo?

**Das ist Kalibrierung, keine Kontrolle.** Melden sich viele, kannst du beim Use-Case Tempo machen
und mehr fragen als erklären. Melden sich wenige, nimm die Folien 4 und 11 (die zwei „Zweck"-Folien)
besonders sorgfältig.

**`DU MUSST WISSEN`**

**Halte den Einstieg bei fünfzehn Minuten.** Der Stoff selbst ist heute dankbar — der Einstieg muss
nur die eine Idee setzen: *UML ist kein einzelnes Bild, sondern mehrere Sichten auf dasselbe System.*
Diese Idee kommt auf Folie 3 als Bild wieder.

---

# Block 1 · UML-Grundidee und Use-Case-Diagramme

**90 Minuten · 08:45–10:15 · Folien 2–10**

**`DER FADEN`**

Der Block hängt an vier Fragen, von der allgemeinsten zur konkretesten:

1. **Warum überhaupt Bilder statt Text?** → was UML ist, die zwei Kategorien *(2–3)*
2. **Wer will was vom System?** → Akteur, Anwendungsfall, Systemgrenze *(4–7)*
3. **Wie hängen Anwendungsfälle zusammen?** → include, extend, Generalisierung *(8–9)*
4. **Wie sieht das fertig aus?** → hier bauen wir das komplette Diagramm live *(10)*

**Der Schnitt bei Folie 4 gehört ausgesprochen:** Bis 3 geht es um UML allgemein, ab 4 beginnt der
erste konkrete Diagrammtyp.

---

## Teil 1.1 · Was ist UML, und die Diagramm-Landkarte

**20 Minuten · 08:45–09:05 · Folien 2–3**

**`▶ FOLIE` 2 — Einführung in UML**

**`ÜBERGANG`**

> Fangen wir mit der Frage an, die jeder im Kopf hat: Warum zeichnen, wenn man auch programmieren
> kann? Weil natürliche Sprache **mehrdeutig** ist und Code **zu detailliert**, um den Überblick zu
> behalten. UML liegt genau dazwischen.

**`SO ERKLÄRST DU ES`**

> UML ist eine **standardisierte, grafische Sprache** zur Modellierung von Softwaresystemen —
> standardisiert heißt: weltweit gleich, jeder Entwickler liest dieselben Symbole gleich. Sie dient
> drei Dingen: **Visualisieren** (das System sichtbar machen), **Spezifizieren** (festlegen, was
> gebaut wird) und **Dokumentieren** (festhalten, was gebaut wurde).
>
> Wichtig — und das nimmt Druck raus: **UML ist keine Programmiersprache.** Aus einem UML-Diagramm
> läuft nichts. Es ist der Plan, nach dem Sie hinterher in Java bauen.

**`DU MUSST WISSEN`**

**Der Vergleich, der immer zieht:** UML ist für Software, was der Bauplan für den Hausbau ist —
niemand mauert ohne Grundriss. Diesen Vergleich brauchst du gleich auf Folie 3 wieder, halt ihn
also bereit.

**`▶ FOLIE` 3 — Übersicht: die UML-Diagramm-Hierarchie**

**`ÜBERGANG`**

> Und jetzt die Landkarte. UML ist nicht ein Diagramm, sondern eine ganze Familie — und die zerfällt
> in zwei Hälften.

**`SO ERKLÄRST DU ES`**

> Zwei große Gruppen. **Strukturdiagramme** beschreiben den **Aufbau** — die „Substantive" des
> Systems: Klassen, Objekte, Komponenten. Die Frage dahinter: *Woraus besteht das System?* Das
> wichtigste ist das **Klassendiagramm** — unser zweites Thema heute.
>
> **Verhaltensdiagramme** beschreiben die **Abläufe** — die „Verben": Aktionen, Interaktionen,
> Zustände. Die Frage: *Was passiert zur Laufzeit?* Dazu gehören Use-Case, Aktivität, Sequenz und
> Zustand — die anderen vier Themen der Woche.
>
> Merken Sie sich für heute nur die Zweiteilung und wo wir stehen: **Use-Case ist Verhalten,
> Klassendiagramm ist Struktur.** Wir fangen mit dem Verhalten an, weil man ein System zuerst von
> außen betrachtet, bevor man hineinschaut.

**`DU MUSST WISSEN`**

**Die abgebildete Grafik ist die Wikipedia-Übersicht — englisch und dicht.** Zeig sie als Landkarte,
aber lies sie **nicht** Kästchen für Kästchen vor. Es genügt: zwei Gruppen, und wir behandeln fünf
der Typen. Wer die vollständige Aufzählung will, findet sie in Lerntext 7.1, Abschnitt 1.

---

## Teil 1.2 · Use-Case: Akteure, Anwendungsfälle, Systemgrenze

**35 Minuten · 09:05–09:40 · Folien 4–7**

**`▶ FOLIE` 4 — Use-Case-Diagramm (Anwendungsfalldiagramm)**

**`ÜBERGANG`**

> Das erste konkrete Diagramm — und das zugänglichste. Es beantwortet eine einzige Frage: **Wer
> will was vom System?** Nicht wie, nicht in welcher Reihenfolge — nur *wer* und *was*.

**`SO ERKLÄRST DU ES`**

> Drei Bausteine, mehr braucht es zunächst nicht:
>
> **Der Akteur** — das Strichmännchen. Eine **Rolle**, die mit dem System arbeitet: Kunde,
> Bibliothekar. Wichtig: eine Rolle, kein einzelner Mensch, und er steht **außerhalb** des Systems.
>
> **Der Anwendungsfall** — die Ellipse. Ein **Ziel**, das der Akteur erreichen will: „Geld abheben",
> „Buch ausleihen". Immer aus Nutzersicht, immer ein abgeschlossener Nutzen.
>
> **Die Systemgrenze** — der Kasten drumherum. Alles innerhalb ist das System, die Akteure stehen
> außen. Diese Grenze zu ziehen ist die eigentliche Denkarbeit: Sie sagt, was *wir* bauen und was
> *Umwelt* ist.

**`AKTIV`**

Ein erster, kurzer Live-Antippser in draw.io — noch nicht das ganze Diagramm, nur die drei
Bausteine einmal in Aktion sehen:

1. **Rechteck aus der UML-Palette ziehen, oben beschriften: „Pizza-Bestell-App".** Sag: „Alles in
   diesem Kasten ist unser System, alles außerhalb ist die Umwelt."
2. **Akteur-Symbol (Strichmännchen) links außerhalb des Rechtecks platzieren, beschriften: „Gast".**
   Sag: „Der Gast steht bewusst außen — er ist nicht Teil des Systems, er benutzt es nur."
3. **Eine Use-Case-Ellipse in den Kasten ziehen, beschriften: „Pizza bestellen".** Verbindungslinie
   vom Gast zur Ellipse ziehen (die Palette rastet automatisch am Rand ein). Sag: „Diese Linie heißt
   Assoziation — sie sagt nur: der Gast kann das."

**Das ist erst der Auftakt.** Das vollständige Diagramm mit allen Anwendungsfällen und Beziehungen
bauen wir gemeinsam auf Folie 10 — heb dir dafür eine frische, leere Fläche auf.

**`? FRAGEN`**

> Ist „Zahlungsart auswählen" ein eigener Anwendungsfall?

Erwartete Falle: viele sagen ja. **Antwort:** nein — das ist ein *Schritt* auf dem Weg zum Ziel
„Pizza bestellen", kein eigenständiges Ziel. **Das ist der wichtigste Test des Themas:** Hat die
Ellipse für den Akteur einen abgeschlossenen Nutzen? Zahlungsart auswählen allein bringt ihm nichts.
Wir kommen auf diese Falle beim Komplettaufbau (Folie 10) noch einmal ganz konkret zurück.

**`▶ FOLIE` 5 — Beispiel: Akteur und Anwendungsfälle**

**`ÜBERGANG`**

> Genau das, was wir eben gezeichnet haben, hier als sauberes Beispiel.

**`SO ERKLÄRST DU ES`**

> Ein Akteur, mehrere Anwendungsfälle, jede Verbindung eine einfache Linie — die **Assoziation**,
> sie sagt nur „dieser Akteur nutzt diesen Anwendungsfall". Mehr Notation ist hier nicht im Spiel.
>
> Achten Sie auf die **Benennung**: Anwendungsfälle heißen **Verb + Objekt** — „Buch ausleihen",
> nicht „Ausleihe". Ein Substantiv als Ellipsentitel ist fast immer ein Zeichen, dass da in
> Wahrheit ein Datending steht, kein Nutzerziel.

**`DU MUSST WISSEN`**

**Die Grafik ist ein Wikipedia-SVG** (Attribution auf der Folie). Inhaltlich brauchbar; wenn du ein
deutsches, größeres Beispiel willst, öffne stattdessen `uc-03.svg` im Portal (Bibliotheks­system).

**`▶ FOLIE` 6 — Komplexeres Beispiel**

**`ÜBERGANG`**

> Und so sieht es aus, wenn ein reales System mit mehreren Akteuren dazukommt. Nicht auswendig
> lernen — nur den Blick üben.

**`SO ERKLÄRST DU ES`**

> Zwei Beobachtungen genügen. Erstens: Es gibt **mehrere Akteure**, und nicht jeder darf alles —
> man sieht sofort, welche Rolle welche Anwendungsfälle nutzt. Zweitens: Das Diagramm bleibt trotz
> vieler Ellipsen lesbar, **weil keine Abläufe drinstehen**. In dem Moment, wo Sie Pfeile mit „dann,
> dann, dann" bräuchten, ist es das falsche Diagramm — dafür kommen Aktivität und Sequenz.

**`▶ FOLIE` 7 — Generalisierung von Akteuren und Anwendungsfällen**

**`ÜBERGANG`**

> Ein erstes Beziehungsmittel, und es ist genau das, was Sie aus Java als Vererbung kennen — nur
> hier für Rollen und Ziele.

**`SO ERKLÄRST DU ES`**

> **Generalisierung von Akteuren:** Ein „Premium-Kunde" ist ein besonderer „Kunde" — er kann alles,
> was ein Kunde kann, und mehr. Derselbe Dreieckspfeil wie bei der Vererbung, Spitze zum
> Allgemeineren.
>
> **Generalisierung von Anwendungsfällen:** „Mit Karte zahlen" und „Mit Bargeld zahlen" sind
> Spezialfälle von „Bezahlen". Der Spezialfall erbt die Bedeutung des allgemeinen und verfeinert sie.
>
> Für die Java-Gruppe: **Das ist `extends` auf der Ebene der Anforderungen.** Dieselbe Idee, die Sie
> beim Klassendiagramm gleich wiedersehen — dort mit demselben Pfeil.

**`DU MUSST WISSEN`**

**Wichtig — ein Akteur muss kein Mensch sein.** Neben „Premium-Kunde" gehört hierher auch der
zweite große Sonderfall des Themas: Ein Akteur kann ein **externes System** sein (ein
Bezahlsystem, das der Automat anruft) oder ein **Zeitgeber** (eine nächtliche Stapelverarbeitung).
Erkennungsmerkmal ist immer dasselbe: **außerhalb der Systemgrenze, will etwas vom System.** Wir
setzen genau so einen Systemakteur gleich beim Komplettaufbau ein — halt diesen Gedanken bereit.

**Hier endet der leichte Teil des Blocks.** Ab Folie 8 kommen include und extend — die einzige echte
Stolperstelle des Use-Case-Themas. Der Satz für den Übergang: *„Jetzt die zwei Pfeile, die
regelmäßig verwechselt werden — und die Prüfung fragt genau die Verwechslung ab."*

---

## Teil 1.3 · Beziehungen und der komplette Live-Aufbau

**35 Minuten · 09:40–10:15 · Folien 8–10**

**`▶ FOLIE` 8 — Include- und Extend-Beziehung**

**`ÜBERGANG`**

> Zwei gestrichelte Pfeile, die fast gleich aussehen und Gegenteiliges bedeuten. Wenn heute im
> Use-Case-Teil eine Prüfungsfrage lauert, dann hier.

**`SO ERKLÄRST DU ES`**

> **`<<include>>` — der Pflichtbaustein.** „Geld abheben" schließt **immer** „PIN prüfen" ein. Man
> lagert den Schritt aus, weil ihn **mehrere** Anwendungsfälle brauchen — einmal modelliert, überall
> genutzt. Der Pfeil geht **vom Basisfall zum eingebundenen** Fall: „Geld abheben" `..>` „PIN prüfen".
>
> **`<<extend>>` — die Kür.** „Ticket kaufen" wird **manchmal** um „Rabattcode einlösen" erweitert —
> nur unter einer Bedingung. Der Pfeil geht **von der Erweiterung zum Basisfall**, also **umgekehrt**:
> „Rabattcode einlösen" `..>` „Ticket kaufen". Das ist der zweite Stolperstein — die Richtung.

**`AKTIV`**

Zeichne beide isoliert nebeneinander in draw.io, damit die Richtung sich einprägt, **bevor** wir sie
gleich im Gesamtbild wiederverwenden:

1. **Zwei Ellipsen „Geld abheben" und „PIN prüfen" nebeneinander.** Gestrichelter Pfeil (aus der
   UML-Palette, Include-Vorlage) von „Geld abheben" zu „PIN prüfen", beschriftet `«include»`. Sag:
   „Pflicht — der Pfeil folgt dem Ablauf: erst abheben, das schließt PIN prüfen zwingend ein."
2. **Darunter zwei Ellipsen „Rabattcode einlösen" und „Ticket kaufen".** Gestrichelter Pfeil von
   „Rabattcode einlösen" zu „Ticket kaufen", beschriftet `«extend»`. Sag: „Kür — und der Pfeil zeigt
   **gegen** den gewohnten Ablauf, nämlich auf den, der erweitert wird."

Lass die beiden Zeichnungen **nebeneinander stehen bleiben** — der Vergleich ist die Lektion.

**`? FRAGEN`**

> „Kunde bewerten" beim Onlineshop: Der Verkauf funktioniert auch ohne. Include oder extend?

**Antwort: extend** — es passiert nur manchmal, der Verkauf braucht es nicht. **Die Prüffrage laut
mitsprechen lassen:** *Passiert es immer? → include. Nur manchmal? → extend.*

**`DU MUSST WISSEN`**

**Das ist die eine Folie, die sitzen muss.** Wenn die Gruppe hier wackelt, nimm dir zwei Minuten
mehr — der Rest des Use-Case-Themas ist dagegen selbsterklärend. Merksatz zum Mitgeben:
**include = eingebaut (immer), extend = erweitert (manchmal).**

**`▶ FOLIE` 9 — Extend mit Extension Point**

**`ÜBERGANG`**

> Eine Verfeinerung von extend — kurz halten, es ist Zusatzwissen.

**`SO ERKLÄRST DU ES`**

> Der **Extension Point** sagt, **an welcher Stelle** und **unter welcher Bedingung** die Erweiterung
> einhakt — zum Beispiel „nach der Betragseingabe, falls die Karte aus dem Ausland stammt". Praktisch
> ist es die Feinschrift zu Folie 8: *wann genau* die Kür greift.

**`DU MUSST WISSEN`**

**Kürzbar (Notfallweg, Rang 2).** Für die Prüfung genügt der Unterschied include/extend von Folie 8.
Wenn du kürzt, ein Satz: *„Man kann bei extend zusätzlich angeben, an welcher Stelle und unter
welcher Bedingung erweitert wird — das heißt Extension Point."*

**`▶ FOLIE` 10 — Vollständiges Beispiel**

**`ÜBERGANG`**

> Jetzt alles zusammen — und diesmal zeichnen wir es komplett neu, von einer leeren Fläche bis zum
> fertigen Diagramm. Jedes Element, das wir heute Vormittag einzeln besprochen haben, kommt jetzt an
> seinen Platz.

**`SO ERKLÄRST DU ES`**

> Bevor wir zeichnen, einmal die **Lesereihenfolge**, die zugleich die **Zeichenreihenfolge** ist:
> Erst die **Systemgrenze** — was gehört dazu? Dann die **Akteure** außen — wer ist beteiligt? Dann
> die **Anwendungsfälle** innen — welche Ziele? Dann die **Assoziationen** — wer darf was? Zuletzt
> die **gestrichelten Pfeile** — was ist Pflicht (include), was Kür (extend)?

**`AKTIV`**

**Der komplette Live-Aufbau — neue, leere Fläche in draw.io.** Baue jetzt das gesamte
Geldautomat-Diagramm Baustein für Baustein auf. Sprich bei jedem Schritt genau den Satz dazu, der
Sonderfälle unterwegs ausdrücklich mit:

1. **Systemgrenze zeichnen** — ein großes Rechteck, oben „Geldautomat". Sag: „Alles in diesem Kasten
   ist unser System, alles außerhalb ist Umwelt — das legen wir immer zuerst fest."
2. **Ersten Akteur setzen** — Strichmännchen links außerhalb, „Kunde". Sag: „Unser primärer Akteur —
   ein Mensch, der ein eigenes Ziel verfolgt."
3. **Zweiten Akteur setzen — bewusst kein Mensch** — ein zweites Strichmännchen rechts außerhalb,
   „Banksystem". Sag: „Akteure müssen keine Menschen sein. Das Banksystem ist ein externes System,
   das unser Automat kontaktiert — auch das ist ein Akteur, weil es außerhalb steht und mit unserem
   System kommuniziert. Das nennt man einen sekundären Akteur."
4. **Ersten Anwendungsfall in die Systemgrenze ziehen** — Ellipse „Geld abheben", Linie zum Kunden.
   Sag: „Ein abgeschlossenes Ziel des Kunden."
5. **Zwei weitere Anwendungsfälle ergänzen** — Ellipsen „Kontostand abfragen" und „PIN ändern",
   jeweils mit Linie zum Kunden. Frag die Gruppe: „Was will der Kunde noch von diesem Automaten?" —
   und ergänze, was kommt.
6. **Bewusster Fehlversuch, sofort korrigiert** — kurz eine vierte Ellipse „PIN eingeben" andeuten,
   dann **durchstreichen** oder wieder löschen. Sag: „Fast reingerutscht — aber das ist kein eigenes
   Ziel, nur ein Schritt auf dem Weg zu ‚Geld abheben'. Der Test: Hat es für den Kunden allein einen
   abgeschlossenen Nutzen? Nein — also keine eigene Ellipse."
7. **Den gemeinsamen Teilschritt auslagern** — neue Ellipse „Authentifizieren" in die Systemgrenze,
   **unterhalb** der drei bisherigen. Sag: „Das ist der Schritt, den wir eben nicht extra gezeichnet
   haben, sondern jetzt sauber als eigenen Anwendungsfall modellieren."
8. **Drei Include-Pfeile ziehen** — gestrichelte `«include»`-Pfeile von „Geld abheben", „Kontostand
   abfragen" und „PIN ändern" jeweils zu „Authentifizieren". Sag: „Alle drei brauchen ihn **immer**
   — deshalb dreimal include, einmal modelliert."
9. **Das Banksystem anbinden** — Linie vom Akteur „Banksystem" zu „Authentifizieren". Sag: „Die
   PIN-Prüfung selbst läuft nicht im Automaten, sondern wird beim Banksystem angefragt — deshalb
   auch hier eine Assoziation, diesmal von einem System-Akteur."
10. **Die optionale Erweiterung ergänzen** — neue Ellipse „Bargeld in Fremdwährung ausgeben".
    Gestrichelter `«extend»`-Pfeil **von** dieser Ellipse **zu** „Geld abheben". Sag: „Nur bei
    ausländischen Karten kommt das dazu — deshalb extend, und der Pfeil zeigt bewusst **gegen** den
    Ablauf, auf den Basisfall, den er erweitert."
11. **Einmal komplett vorlesen** — mit dem Finger über das fertige Bild fahren: Systemgrenze, zwei
    Akteure (einer davon kein Mensch), fünf Anwendungsfälle, drei Include-Pfeile, ein Extend-Pfeil.
    Sag: „Das ist ein vollständiges Use-Case-Diagramm — und genauso, in dieser Reihenfolge, gehen
    Sie in der Übung gleich selbst vor."

**`DU MUSST WISSEN`**

**Diese eine Zeichnung trägt den ganzen Block.** Lass sie nach dem Zeichnen sichtbar stehen — auch
während der Pause und der Zwischenübung, sie ist die Referenz, auf die sich die Gruppe beim eigenen
Zeichnen bezieht. **Zwei Sonderfälle sind absichtlich eingebaut** und sollten explizit benannt
bleiben: der Akteur, der kein Mensch ist (Banksystem), und der Fehlversuch, der zeigt, warum
„PIN eingeben" kein Use Case ist.

**Hier endet Block 1.** Bist du vor 10:15 fertig, ist das gut — der Klassendiagramm-Block ist der
dichtere. Der Satz für die Pause und die Übung: *„Nach der Pause zeichnen Sie zuerst selbst ein
Use-Case-Diagramm — dann drehen wir das System um und schauen hinein: das Klassendiagramm."*

Die **Zwischenübung Use-Case** (Aufgabenblatt 7.1, Teil A) macht ihr gemeinsam: eine Aufgabe an der
Tafel/in draw.io vorführen, eine die Gruppe selbst, Musterlösung aus dem Portal aufdecken.

---

# Block 2 · Klassendiagramme

**90 Minuten · 10:45–12:15 · Folien 11–27**

**`DER FADEN`**

Der Block dreht das System um: von der Außensicht zur Innensicht. Vier Fragen:

1. **Woraus besteht eine Klasse, und wie hängen zwei Klassen zusammen?** → Live-Komplettaufbau
   *(11–14)*
2. **Welche Beziehungen gibt es im Überblick?** → die Pfeil-Übersicht, Interfaces *(15–19)*
3. **Was bedeutet jede Beziehung genau?** → Vererbung, Aggregation, Komposition live mit
   Raute-Test *(13, 20–26)*
4. **Wie sieht das zur Laufzeit aus?** → das Objektdiagramm *(27)*

**Der wichtigste Satz des Blocks fällt gleich bei Folie 11 und noch einmal am Ende:** Ein
Klassendiagramm lässt sich **Zeile für Zeile nach Java übersetzen** — und weil die Gruppe Java kann,
ist das dein stärkster Hebel.

---

## Teil 2.1 · Die Klasse — kompletter Live-Aufbau mit zwei Klassen

**30 Minuten · 10:45–11:15 · Folien 11–14**

**`▶ FOLIE` 11 — Klassendiagramm (Struktur)**

**`ÜBERGANG`**

> Wir haben von außen geschaut: wer will was. Jetzt schauen wir hinein: **woraus** bauen wir das
> System? Das Klassendiagramm ist das wichtigste Diagramm der objektorientierten Programmierung —
> und Ihrem Java-Alltag am nächsten.

**`SO ERKLÄRST DU ES`**

> Das Klassendiagramm zeigt die **Bausteine** eines Systems und wie sie zusammenhängen: **Klassen**,
> ihre **Attribute** (was ein Objekt weiß), ihre **Methoden** (was ein Objekt kann) und die
> **Beziehungen** zwischen ihnen.
>
> Und der Satz, den Sie den ganzen Block über hören werden: **Ein Klassendiagramm ist Java in
> Kurzschrift.** Was hier als Kästchen steht, wird bei Ihnen zur `class`; jedes Attribut zu einem
> Feld, jede Methode zu einer Methode. Wer das Diagramm liest, hat die Klasse schon geschrieben.

**`▶ FOLIE` 12 — Aufbau und Syntax einer Klasse**

**`ÜBERGANG`**

> Ab jetzt zeichnen wir wieder komplett selbst, von einer leeren Fläche an — und diesmal bauen wir
> gleich zwei Klassen mit einer vollständigen Beziehung dazwischen. Das ist der wichtigste
> Live-Aufbau des Klassendiagramm-Blocks.

**`SO ERKLÄRST DU ES`**

> Eine Klasse ist ein Rechteck mit **drei Fächern** übereinander — Name, Attribute, Methoden — und
> davor bei Attributen und Methoden ein **Sichtbarkeitszeichen**:
>
> | Zeichen | Bedeutung | Java |
> |---|---|---|
> | `+` | öffentlich | `public` |
> | `-` | privat | `private` |
> | `#` | geschützt | `protected` |
>
> Die Faustregel, die die meisten Fehler verhindert: **Attribute privat, Methoden öffentlich** —
> die Daten werden gekapselt, der Zugriff läuft über Methoden. Das ist genau das
> „private Feld, public Getter", das Sie schon schreiben.

**`AKTIV`**

**Der komplette Live-Aufbau — neue, leere Fläche in draw.io.** Baue zwei Klassen mit einer
vollständigen Beziehung samt Multiplizität auf, Fach für Fach:

1. **Leeres Klassen-Rechteck aus der UML-Palette ziehen** — noch ohne Beschriftung, nur die drei
   leeren Fächer sichtbar. Sag: „Das ist der leere Steckbrief — jede Klasse fängt bei mir mit diesem
   Kasten an."
2. **Oberstes Fach beschriften: „Konto"** — fett, Singular. Sag: „Der Name steht immer oben,
   groß geschrieben, in der Einzahl — nicht ‚Konten'."
3. **Erstes Attribut ins mittlere Fach: `-kontonummer: String`.** Sag: „Minus heißt privat — von
   außen nicht direkt sichtbar. In Java wäre das `private String kontonummer;`."
4. **Zweites Attribut ergänzen: `-kontostand: double`.** Sag: „Auch privat — der Kontostand ist
   sensibel, den lassen wir niemanden direkt verändern."
5. **Erste Methode ins untere Fach: `+einzahlen(betrag: double): void`.** Sag: „Plus heißt
   öffentlich — von außen aufrufbar. In Java: `public void einzahlen(double betrag) { }`."
6. **Zweite Methode ergänzen: `+getKontostand(): double`.** Sag: „Ein Getter — er macht den privaten
   Kontostand kontrolliert von außen zugänglich. Genau das Prinzip: privat schützen, über eine
   öffentliche Methode freigeben."
7. **Zweite, leere Klasse daneben ziehen, beschriften: „Kunde", ein Attribut `-name: String`.**
   Sag: „Zweite Klasse, gleiches Schema — Name oben, Attribut privat darunter."
8. **Verbindungslinie zwischen „Kunde" und „Konto" ziehen** — einfache Assoziationslinie. Sag:
   „Diese Linie sagt: Ein Kunde kennt sein Konto — mehr noch nicht."
9. **Multiplizität an beide Enden schreiben: `1` bei Kunde, `1..*` bei Konto.** Sag: „Jetzt wird es
   präzise: Ein Konto gehört zu **genau einem** Kunden — die `1` beim Kunden. Ein Kunde hat
   **mindestens ein** Konto, vielleicht mehrere — die `1..*` beim Konto. Gelesen wird über Kreuz:
   die Zahl steht bei der Klasse, von der aus man zählt."
10. **Kurz zurücktreten und komplett vorlesen** — mit dem Finger über das fertige Bild: zwei
    Klassen, je drei Fächer, Sichtbarkeiten, eine Beziehung mit Multiplizität an beiden Enden. Sag:
    „Das ist ein vollständiges kleines Klassendiagramm — Steckbrief, Steckbrief, Beziehung dazwischen."

Dann frag: *„Wie sähe die Klasse Konto als Java-Code aus?"* — und lass die Gruppe `private double
kontostand;`, `public void einzahlen(double betrag)` und `private Konto konto;` (für die
Beziehung, als Attribut in `Kunde`) zurufen. **Dieser Übersetzungsmoment ist Gold bei dieser Gruppe.**

**`DU MUSST WISSEN`**

**Lass dieses Diagramm stehen — es ist die Referenz für den ganzen Block.** Auf Folie 14
(Multiplizität formal) und Folie 20 (gerichtete Assoziation) greifst du genau darauf zurück, statt
neu zu zeichnen: „Erinnern Sie sich an die `1` und die `1..*` zwischen Kunde und Konto von eben —
genau das war schon eine Multiplizität, genau die Linie schon eine Assoziation."

**`▶ FOLIE` 13 — Vererbung: „Auto erbt von Fahrzeug"**

**`ÜBERGANG`**

> Die erste Beziehung, und die kennen Sie schon: Vererbung. In UML hat sie ein unverwechselbares
> Symbol. Ein kurzer, eigener Aufbau dafür.

**`SO ERKLÄRST DU ES`**

> **Der Dreieckspfeil** mit der Spitze zur **allgemeineren** Klasse: `Auto ──▷ Fahrzeug`. Gelesen:
> „Auto **ist ein** Fahrzeug." Das Auto erbt alle Attribute und Methoden von Fahrzeug und ergänzt
> eigene.
>
> Für Sie: **Das ist `class Auto extends Fahrzeug`.** Die leere Dreiecksspitze steht immer beim
> **Elternteil** — der Merksatz: *Die Spitze zeigt auf den, von dem geerbt wird.*

**`AKTIV`**

Kurzer, eigener Live-Aufbau — neue Fläche, oder rechts neben dem Kunde/Konto-Diagramm:

1. **Klasse „Fahrzeug" zeichnen**, ein Attribut `-geschwindigkeit: double`, eine Methode
   `+beschleunigen(): void`. Sag: „Die allgemeine Basisklasse — das, was jedes Fahrzeug kann."
2. **Klasse „Auto" darunter zeichnen**, ein eigenes Attribut `-anzahlTueren: int`. Sag: „Das Auto
   bekommt zusätzlich etwas Eigenes, das nicht jedes Fahrzeug hat."
3. **Vererbungspfeil aus der UML-Palette (leeres Dreieck) von „Auto" zu „Fahrzeug" ziehen.** Sag:
   „Die Spitze zeigt nach oben, zum Elternteil. Auto erbt jetzt Geschwindigkeit und Beschleunigen
   automatisch dazu."
4. **Den ist-ein-Test laut anwenden.** Sag: „Ist ein Auto ein Fahrzeug? Ja — Vererbung passt. Wäre
   die Frage ‚Ist ein Motor ein Auto?', wäre die Antwort nein — der Motor ist ein *Teil*, das ist
   eine andere Beziehung, die kommt gleich."

**`DU MUSST WISSEN`**

**Der ist-ein-Test ist das wichtigste Werkzeug gegen den häufigsten Anfängerfehler:** Vererbung zu
verwenden, wo eine Teil-Beziehung gemeint ist. Halt den Satz „Ist ein Motor ein Auto?" bereit — du
brauchst ihn bei Folie 23 wieder, wenn die Aggregation drankommt.

**`▶ FOLIE` 14 — Multiplizität / Kardinalität**

**`ÜBERGANG`**

> Wir haben die Multiplizität eben am Kunde-Konto-Diagramm schon benutzt — jetzt machen wir die
> Regel dahinter explizit.

**`SO ERKLÄRST DU ES`**

> Die **Multiplizität** steht an den **Enden** einer Beziehung und gibt an, wie viele Objekte
> beteiligt sein dürfen — als `untere..obere` Schranke:
>
> | Angabe | Bedeutung |
> |---|---|
> | `1` | genau eins |
> | `0..1` | keins oder eins (optional) |
> | `*` oder `0..*` | beliebig viele |
> | `1..*` | mindestens eins |
>
> Der Stern steht für die **obere** Schranke „beliebig viele". Gelesen wird **über Kreuz**: „Ein
> Kunde hat `1..*` Konten; ein Konto gehört zu genau `1` Kunden" — genau das Diagramm, das gerade
> neben uns steht.

**`? FRAGEN`**

> Ein Auto und seine Räder — welche Multiplizität schreiben Sie an die beiden Enden?

Erwarte: Auto `1` — Rad `4` (oder `1..*`, je nach Modell). **Der Punkt:** Multiplizität zwingt zum
Nachdenken über den Sonderfall — darf es null sein? beliebig viele? Genau das prüft die Klausur.

**`DU MUSST WISSEN`**

**Die abgebildete Tabelle ist vollständig — nutze sie als Referenz**, aber lass die Gruppe die drei
wichtigsten (`1`, `0..*`, `1..*`) am eigenen Kunde-Konto-Diagramm nachvollziehen, statt alle Zeilen
vorzulesen. Die Portal-Referenz `kls-ref-multiplizitaet.svg` zeigt es zusätzlich grafisch.

---

## Teil 2.2 · Die Beziehungen im Überblick — und Interfaces

**10 Minuten · 11:15–11:25 · Folien 15, 17–19**

**`▶ FOLIE` 15 — Ein vollständiges Klassendiagramm**

**`ÜBERGANG`**

> Bevor wir die restlichen Beziehungen einzeln durchgehen, einmal das große Bild: So sieht ein
> fertiges Klassendiagramm mit mehreren Klassen aus.

**`SO ERKLÄRST DU ES`**

> Lesen Sie es wie eine Landkarte: erst die **Kästen** (welche Klassen gibt es?), dann die **Linien**
> dazwischen (wie hängen sie zusammen?). Noch müssen Sie nicht jede Linienart deuten können — das
> kommt gleich. Der Punkt ist: **Ein Klassendiagramm ist selten eine Klasse, meist ein Netz.**

**`DU MUSST WISSEN`**

**Wikipedia-Grafik, englisch/klein.** Für ein deutsches, sauberes Gesamtbeispiel öffne im Portal das
Banksystem-Diagramm (`kls-14.svg` / `kls-16.svg` im Lerntext 7.2) — das greift die Beispiele auf,
die die Gruppe schon aus dem Use-Case-Teil kennt.

**`▶ FOLIE` 17 — Interfaces**

**`ÜBERGANG`**

> Ein kurzer Ausflug, der Ihnen als Java-Leuten leichtfällt: das Interface. Es ist eine Sonderform
> der Klasse.

**`SO ERKLÄRST DU ES`**

> Ein **Interface** ist ein **Vertrag**: Es legt fest, **was** eine Klasse können muss, aber nicht,
> **wie**. Nur Methodensignaturen, keine Umsetzung. Eine Klasse kann **mehrere** Interfaces erfüllen
> — anders als bei der Vererbung, wo es in Java nur eine Elternklasse gibt.

**`DU MUSST WISSEN`**

**Das ist Ergänzungsstoff — nicht in den fünf Kern-Lerntexten, aber auf den Folien.** Halt es kurz;
die Gruppe kennt Interfaces aus Java. Der UML-Teil ist nur die **Schreibweise**, und die kommt auf
Folie 19.

**`▶ FOLIE` 18 — Interfaces in Java**

**`SO ERKLÄRST DU ES`**

> Kurz der Java-Bezug, den Sie schon haben: `interface Zahlbar { void zahlen(); }` und
> `class Rechnung implements Zahlbar`. **Wichtig für gleich:** In UML wird `implements` nicht zum
> Vererbungspfeil, sondern zu einem **gestrichelten** Dreieckspfeil — der **Realisierung**.

**`DU MUSST WISSEN`**

**Kürzbar (Notfallweg, Rang 1).** Wenn die Zeit im Block drängt, fasse 17–19 in einem Satz zusammen:
*„Interface = Vertrag; in UML `<<interface>>` überm Namen und ein gestrichelter Dreieckspfeil für
`implements`."* — und geh weiter zu den Beziehungen, die prüfungsrelevanter sind.

**`▶ FOLIE` 19 — Interface-Darstellung in UML**

**`SO ERKLÄRST DU ES`**

> Zwei Schreibweisen: Entweder ein Klassenkasten mit **`<<interface>>`** über dem Namen und einer
> gestrichelten Realisierungslinie von der umsetzenden Klasse — oder die **„Lollipop"-Notation**:
> ein kleiner Kreis am Faden, der das angebotene Interface markiert. Die erste Form sehen Sie
> häufiger.

**`DU MUSST WISSEN`**

**Der Übergang zurück zum Kern:** *„So viel zum Vertrag. Jetzt die vier Beziehungen, die Sie am
häufigsten brauchen — und die die Prüfung liebt."*

---

## Teil 2.3 · Die vier Beziehungen im Detail — mit dem Raute-Test live

**40 Minuten · 11:25–12:05 · Folien 16, 20–26**

**`▶ FOLIE` 16 — Übersicht: alle Beziehungspfeile**

**`ÜBERGANG`**

> Der „Pfeil-Zoo" — alle Beziehungsarten nebeneinander. Diese eine Folie ist die Nachschlagekarte
> für den Rest des Blocks.

**`SO ERKLÄRST DU ES`**

> Sieben Linienarten, und jede sagt etwas anderes:
>
> | Beziehung | Linie/Pfeil | Frage |
> |---|---|---|
> | **Assoziation** | einfache Linie | kennt-ein? |
> | **Gerichtete Assoziation** | Linie mit offener Pfeilspitze | kennt-ein, nur in eine Richtung |
> | **Vererbung** | leerer Dreieckspfeil △ | ist-ein? |
> | **Realisierung** | gestrichelter Dreieckspfeil | erfüllt-Vertrag (Interface) |
> | **Abhängigkeit** | gestrichelte Linie, offene Spitze | benutzt-kurz? |
> | **Aggregation** | leere Raute ◇ | hat-ein (locker) |
> | **Komposition** | gefüllte Raute ◆ | besteht-aus (fest) |

**`AKTIV`**

Zeichne den „Pfeil-Zoo" **einmal live** untereinander — je zwei Kästchen aus der UML-Palette,
dazwischen die jeweilige Linie, rechts das Stichwort. Das dauert drei Minuten und ist die Referenz,
auf die du die nächsten Folien alle beziehst: *„Erinnern Sie sich an die gestrichelte Linie von
eben — das war die Abhängigkeit."*

**`DU MUSST WISSEN`**

**Die zwei Rauten sind die Prüfungsfalle des ganzen Themas** — leer gegen gefüllt. Sag es hier schon
an: *„Merken Sie sich die zwei Rauten, dazu kommen wir gleich mit einem Test, der sie
auseinanderhält."* Das ist der Raute-Test von Folie 25.

**`▶ FOLIE` 20 — Gerichtete Assoziation**

**`ÜBERGANG`**

> Die einfachste dauerhafte Beziehung — und ihre gerichtete Variante. Wir haben sie eben schon
> gezeichnet, ohne den Namen zu nennen.

**`SO ERKLÄRST DU ES`**

> Eine **Assoziation** ist eine **dauerhafte** Verbindung: Ein Objekt kennt ein anderes über die
> Zeit — genau wie „Kunde kennt Konto" von vorhin.
>
> **Gerichtet** heißt: Die Kenntnis geht nur in **eine** Richtung — eine offene Pfeilspitze zeigt,
> wer wen kennt. Der Kunde kennt sein Konto; das Konto muss seinen Kunden nicht zwingend kennen.
>
> Für Sie: **Das ist ein Attribut.** `class Kunde { private Konto konto; }` — die gerichtete
> Assoziation ist genau dieses Feld, das Sie am Anfang des Blocks schon mündlich benannt haben.

**`▶ FOLIE` 21 — Abhängigkeit (Dependency)**

**`ÜBERGANG`**

> Und jetzt der schwächere Verwandte, der ständig mit der Assoziation verwechselt wird.

**`SO ERKLÄRST DU ES`**

> Eine **Abhängigkeit** ist **kurzfristig**: Ein Objekt benutzt ein anderes nur **vorübergehend** —
> als Methodenparameter, als lokale Variable, für einen Moment. „Benutzt-ein" statt „kennt-ein".
> Gestrichelte Linie mit offener Spitze.
>
> Der Unterschied in einem Bild: **Die Assoziation ist eine Ehe (dauerhaft, als Attribut
> gespeichert), die Abhängigkeit ein Taxi (kurz genutzt, dann weg).** In Java: Attribut gegen
> Parameter — `void bezahlen(Kreditkarte k)` hängt von `Kreditkarte` ab, speichert sie aber nicht.

**`? FRAGEN`**

> Ein Drucker, der ein Dokument druckt — Assoziation oder Abhängigkeit?

**Antwort: Abhängigkeit** — der Drucker *benutzt* das Dokument im Moment des Druckens, *besitzt* es
nicht. Kommt „nur für einen Aufruf" vor → gestrichelt.

**`DU MUSST WISSEN`**

**Die Leitfrage, die beide trennt:** *Speichert das Objekt das andere als Attribut?* Ja →
Assoziation (durchgezogen). Nur kurz benutzt → Abhängigkeit (gestrichelt). Wenn die Gruppe hier
„Assoziation gegen Abhängigkeit" sicher trennt, kannst du bei Aggregation/Komposition Tempo machen —
die bauen auf demselben Denken auf.

**`▶ FOLIE` 22 — Beispiel kombiniert**

**`SO ERKLÄRST DU ES`**

> Beides an einem Bild: Der **Kunde** hat eine **gerichtete Assoziation** zum **Warenkorb** — er
> besitzt ihn über den ganzen Einkauf. Und der Kunde hat eine **Abhängigkeit** zur **Kreditkarte** —
> die braucht er nur im Moment des Bezahlens.

**`▶ FOLIE` 23 — Aggregation**

**`ÜBERGANG`**

> Jetzt die zwei Teil-Ganzes-Beziehungen — und hier sitzt die berühmteste Verwechslung von UML.
> Zuerst die lockere Form, wieder als eigener kurzer Live-Aufbau.

**`SO ERKLÄRST DU ES`**

> Die **Aggregation** ist eine **lockere** „Teil-von"-Beziehung: Ein Objekt ist Teil eines Ganzen,
> **kann aber unabhängig davon existieren**. Symbol: die **leere Raute** ◇ — und sie sitzt immer
> **beim Ganzen**.
>
> „Ein **Spieler** ist Teil eines **Teams** — aber der Spieler existiert auch ohne das Team weiter."
> Löst sich das Team auf, sind die Spieler nicht verschwunden.

**`AKTIV`**

Eigener kurzer Live-Aufbau — neue Fläche, für den direkten Vergleich mit Komposition gleich
reserviert genug Platz darunter:

1. **Klasse „Team" zeichnen**, ein Attribut `-name: String`. Sag: „Das Ganze."
2. **Klasse „Spieler" daneben zeichnen**, ein Attribut `-rueckennummer: int`. Sag: „Das Teil."
3. **Linie zwischen beiden ziehen, am Ende bei „Team" die leere Raute aus der UML-Palette setzen.**
   Sag: „Die Raute sitzt beim Ganzen, nie beim Teil — sie zeigt, wer wen ‚hat'."
4. **Den Raute-Test laut anwenden.** Sag: „Löse ich das Team auf — existiert der Spieler noch?
   Ja. Deshalb die leere Raute."

**`▶ FOLIE` 24 — Beispiel Aggregation**

**`SO ERKLÄRST DU ES`**

> Ein zweites Beispiel zum Festigen: **Bibliothek ◇— Buch** — das Buch existiert auch, wenn die
> Bibliothek schließt. Gemeinsames Muster mit Team/Spieler: **Das Teil hat ein Eigenleben.**

**`▶ FOLIE` 25 — Komposition**

**`ÜBERGANG`**

> Und jetzt die starke Form — direkt unter die Aggregation gezeichnet, damit der Unterschied auf
> einen Blick sichtbar wird.

**`SO ERKLÄRST DU ES`**

> Die **Komposition** ist eine **starke** „Besteht-aus"-Beziehung: Das Teil ist **fester Bestandteil**
> des Ganzen und **stirbt mit ihm**. Symbol: die **gefüllte Raute** ◆, wieder beim Ganzen.
>
> „Ein **Raum** ist Teil eines **Hauses** — wird das Haus abgerissen, verschwinden die Räume mit."
> Der Raum hat kein Eigenleben außerhalb des Hauses.

**`AKTIV`**

Direkt **unter** das Team/Spieler-Diagramm von Folie 23 zeichnen, gleiches Schema:

1. **Klasse „Haus" zeichnen**, ein Attribut `-adresse: String`. Sag: „Wieder das Ganze — direkt
   unter Team, damit wir gleich vergleichen können."
2. **Klasse „Raum" daneben zeichnen**, ein Attribut `-quadratmeter: double`. Sag: „Wieder das Teil."
3. **Linie ziehen, am Ende bei „Haus" die gefüllte Raute aus der UML-Palette setzen.** Sag: „Optisch
   fast identisch mit eben — nur diesmal ist die Raute ausgefüllt."
4. **Beide Diagramme nebeneinander zeigen und den Raute-Test aussprechen:**

> **Der Raute-Test:** Zerstöre das Ganze. Lebt das Teil weiter? **Ja → leere Raute** (Aggregation).
> **Nein → gefüllte Raute** (Komposition).

Sag: *„Team weg, Spieler da — leere Raute. Haus weg, Räume weg — gefüllte Raute."* **Dieser eine
Test beantwortet jede Prüfungsfrage zum Thema.**

**`? FRAGEN`**

> Eine Bestellung und ihre Bestellpositionen — leere oder gefüllte Raute?

**Antwort: gefüllt (Komposition)** — löscht man die Bestellung, sind die Positionen sinnlos und
verschwinden. Wende den Test laut an.

**`▶ FOLIE` 26 — Beispiel Komposition**

**`SO ERKLÄRST DU ES`**

> Zum Festigen: **Haus ◆— Raum** und **Bestellung ◆— Bestellposition**. Gemeinsames Muster: **Das
> Teil gehört zu genau einem Ganzen und teilt dessen Lebensdauer.** Damit haben Sie alle vier
> Beziehungen live gesehen: Vererbung (ist-ein), Assoziation (kennt-ein), Aggregation (hat-ein
> locker), Komposition (besteht-aus fest).

**`DU MUSST WISSEN`**

**Hier ist der inhaltliche Höhepunkt des Tages erreicht.** Wenn du die vier Beziehungen mit ihren
Tests (ist-ein, kennt-ein, Raute-Test) live gezeichnet und sicher rübergebracht hast, ist das
Tageslernziel erfüllt. Der Rest ist Zugabe.

---

## Teil 2.4 · Objektdiagramm und Abschluss

**10 Minuten · 12:05–12:15 · Folie 27**

**`▶ FOLIE` 27 — Objektdiagramm**

**`ÜBERGANG`**

> Ein letztes, kurzes Diagramm — die Momentaufnahme zum Klassendiagramm.

**`SO ERKLÄRST DU ES`**

> Das **Klassendiagramm** zeigt die **Bauform** — die Klasse `Kunde`, allgemein. Das
> **Objektdiagramm** zeigt einen **konkreten Augenblick**: `max : Kunde` mit seinen zwei konkreten
> Konten. Objektnamen werden **unterstrichen** und mit Doppelpunkt geschrieben: `max : Kunde`.
>
> Wozu? Es macht Multiplizitäten **anfassbar**: Wo das Klassendiagramm „ein Kunde hat `1..*` Konten"
> sagt, zeigt das Objektdiagramm den konkreten Max mit genau zwei Konten. **Es ist der Schnappschuss
> zur Bauzeichnung.**

**`AKTIV`**

Optionaler Mini-Aufbau, wenn die Zeit reicht — direkt neben dem Kunde/Konto-Klassendiagramm vom
Anfang des Blocks:

1. **Rechteck zeichnen, Titel unterstrichen: „max : Kunde".** Sag: „Kein Klassenname mehr — ein
   konkreter Name, gefolgt von der Klasse, aus der er stammt."
2. **Zwei weitere Rechtecke daneben: „sparkonto1 : Konto" und „girokonto1 : Konto", je eine Linie
   zu „max : Kunde".** Sag: „Genau zwei Konten — das ist die Multiplizität `1..*` von vorhin, jetzt
   an einem konkreten Beispiel gezeigt statt nur als Regel."

**`DU MUSST WISSEN`**

**Kürzbar (Notfallweg, Rang 3), aber schade drum** — es ist ein Zwei-Minuten-Diagramm und schließt
den Block rund ab. Merksatz: **Klasse = Bauplan, Objekt = ein gebautes Haus.**

**Der Tagesabschluss, ohne Folie:**

> Ich fasse den Tag in zwei Sätzen zusammen. **Erstens: Man schaut ein System zuerst von außen an —
> wer will was (Use-Case) — und dann von innen — woraus besteht es (Klassen).** **Zweitens: Ein
> Klassendiagramm ist Java in Kurzschrift** — drei Fächer, Sichtbarkeiten, und vier Beziehungen, die
> Sie mit drei Fragen auseinanderhalten: ist-ein, kennt-ein, und der Raute-Test.
>
> Heute Nachmittag üben Sie beides selbst — die Aufgaben liegen im Portal, jede mit Musterlösung.
> Morgen drehen wir vom Aufbau zum Ablauf: **wie sich das System zur Laufzeit verhält.**

Die **Zwischenübung Klasse** (Aufgabenblatt 7.2, Teil A) direkt im Anschluss: eine Klasse mit
Attributen/Methoden gemeinsam zeichnen, dann eine Beziehungsaufgabe, Musterlösung aus dem Portal.

---

## Der Nachmittag: Selbstlernphase

**Heute arbeitet die Gruppe selbstständig.** Der Nachmittag vertieft die zwei Diagrammtypen des
Vormittags — jede Aufgabe hat eine eingeklappte Musterlösung, die Teilnehmer prüfen sich selbst.

| Datei | Wofür |
|---|---|
| `../Portal/HTML/index.html` | das **Lernportal** — Lerntexte 7.1 und 7.2 zum Nachlesen, Übungen im selben Layout |
| Aufgabenblatt 7.1, **Teil B** (8–12 Aufgaben) | Use-Case selbstständig modellieren, gestaffelt leicht→schwer |
| Aufgabenblatt 7.2, **Teil B** (8–12 Aufgaben) | Klassendiagramme selbstständig modellieren, bis zu mehreren Klassen mit allen Beziehungen |

**Sag der Gruppe, wie sie üben soll:** erst selbst zeichnen (Papier oder draw.io), **dann erst** die
Musterlösung aufdecken. Das Aufdecken vor dem eigenen Versuch ist der häufigste Lernfehler. Wer
draw.io noch nicht kennt: kurzer Hinweis auf die UML-Palette (siehe „Vor dem Unterricht") reicht,
die Bedienung ist selbsterklärend.

**Wer schnell fertig ist:** die letzten beiden Aufgaben in Teil B sind bewusst anspruchsvoller
(mehrere Akteure mit include/extend; mehrere Klassen mit allen vier Beziehungen und Multiplizitäten).

---

## Wenn eine Frage kommt, die du nicht sofort beantworten willst

> „Gute Frage — was denken die anderen?" — und dann zurück zum Diagramm.

> „Das ist eine Vertiefung, die über den heutigen Stoff hinausgeht. **Wer von Ihnen hat damit
> schon gearbeitet?**"

**Die sieben Fragen, die mit hoher Wahrscheinlichkeit kommen, mit Antwort:**

**„Ist ein Akteur immer ein Mensch?"** — Nein, und das ist wichtig zu sagen. Ein Akteur ist eine
**Rolle**, die mit dem System interagiert — das kann auch ein **Fremdsystem** (das Banksystem, das
der Automat aufruft — genau der Akteur aus unserem Live-Aufbau) oder ein **Zeitgeber** (eine
nächtliche Abrechnung) sein. Man erkennt ihn daran, dass er **außerhalb** des Systems steht und
etwas von ihm will. *(Folie 4/7, live gezeichnet auf Folie 10.)*

**„Wann include, wann extend?"** — Passiert der Teilschritt **immer**, ist es `include`; passiert
er **nur unter einer Bedingung**, ist es `extend`. Eselsbrücke: **include = Pflichtbaustein,
extend = Sonderfall.** *(Folie 8/9, live gezeichnet auf Folie 10.)*

**„Was ist der Unterschied zwischen Assoziation und Abhängigkeit?"** — Die **Assoziation** ist
**dauerhaft** (ein Objekt hält das andere als Attribut — der Kunde *hat* sein Konto). Die
**Abhängigkeit** ist **kurzfristig** (ein Objekt benutzt ein anderes nur vorübergehend, etwa als
Methodenparameter — „benutzt-ein"). In Java: Attribut gegen lokale Variable. *(Folie 20/21.)*

**„Aggregation oder Komposition — brauche ich das im echten Java-Code überhaupt?"** — Ehrliche
Antwort: **im Code kaum sichtbar**, beides ist am Ende ein Attribut. Der Unterschied ist die
**Lebensdauer** und wird beim Modellieren entschieden. Für die Modellierung (und die Prüfung) zählt
der **Raute-Test**. *(Folie 23–26, live gezeichnet.)*

**„Interface oder abstrakte Klasse?"** — Die Java-Gruppe kennt das. Kurz: Ein **Interface** ist ein
reiner **Vertrag** (nur Methodensignaturen, keine Umsetzung, eine Klasse kann **mehrere**
implementieren). In UML steht `<<interface>>` über dem Klassennamen, die Umsetzung ist ein
**gestrichelter** Dreieckspfeil (**Realisierung**). *(Folie 17–19.)*

**„Wir schreiben doch gar keinen Code — warum dann so genau?"** — Weil UML die **Sprache vor dem
Code** ist: Ein Klassendiagramm lässt sich Zeile für Zeile nach Java übersetzen (`-attribut` →
`private`, Dreieckspfeil → `extends`, `<<interface>>` → `implements`). **Wer das Diagramm sauber
liest, schreibt hinterher die Klassen fehlerfrei.** Die knappe UML→Java-Tabelle steht am Ende von
Lerntext 7.2.

**„Wozu ein Objektdiagramm, wenn es das Klassendiagramm gibt?"** — Das Klassendiagramm zeigt die
**Bauform** (die Klasse *Kunde*), das Objektdiagramm eine **Momentaufnahme** konkreter Objekte
(*Max Mustermann : Kunde* mit seinen zwei konkreten Konten). Es ist der Beweis, dass eine
Multiplizität stimmt. *(Folie 27.)*

---

## Notfallweg, wenn die Zeit knapp wird

**Der Klassendiagramm-Block ist der dichtere.** Wenn es drängt, kürze in dieser Reihenfolge:

| Rang | Folien | Was entfällt | Was der Verzicht kostet |
|---|---|---|---|
| 1 | **17–19** | Interfaces | Ergänzung, nicht in den Kern-Lerntexten. Ein Satz: „Interface = Vertrag, in UML `<<interface>>` + gestrichelter Dreieckspfeil" |
| 2 | **9** | Extension Point | Ein Satz genügt — der Unterschied include/extend (Folie 8) reicht |
| 3 | **27** | Objektdiagramm / dessen Live-Aufbau | Merksatz mündlich: „Klasse = Bauplan, Objekt = ein gebautes Haus" |
| 4 | **6** | Komplexes Use-Case-Beispiel | Zeigen, nicht besprechen — Folie 5 trägt die Notation schon |
| 5 | **15** | Wikipedia-Gesamtbeispiel | Durch das deutsche Portal-SVG ersetzen oder überspringen |

**Was auf keinen Fall entfällt — die Live-Aufbauten, die den Tag tragen:** **4/10** (der komplette
Use-Case-Aufbau am Geldautomaten, inklusive der beiden Sonderfälle), **12** (der komplette
Klassen-Aufbau mit zwei Klassen, Sichtbarkeiten und Multiplizität), **13** (Vererbung und der
ist-ein-Test) sowie **23/25** (Aggregation und Komposition mit dem Raute-Test). Wenn du nur diese
vier Live-Aufbauten schaffst, hat die Gruppe den kompletten Kern des Tages selbst wachsen sehen.

**Wenn Block 2 nicht mehr durchläuft:** Streich 17–19 und den Live-Aufbau von 27. **Kürze nicht bei
23/25** — der Unterschied der beiden Rauten ist die häufigste Prüfungsfrage des Klassendiagramms.

---

## Blick auf morgen

**Tag 2 — Aktivitäts- und Sequenzdiagramme.** Der Blickwechsel von der **Struktur** zum
**Verhalten**: Heute ging es darum, *woraus* ein System besteht; morgen darum, *wie* es abläuft.

> **Der rote Faden für morgen:** Das **Aktivitätsdiagramm** zeigt einen Prozess als Fluss (wie ein
> Flussdiagramm — Entscheidungen, Schleifen, Parallelität). Das **Sequenzdiagramm** zeigt, **wer
> wann mit wem spricht** (der zeitliche Nachrichtenaustausch zwischen Objekten). Beide werden wieder
> live in draw.io aufgebaut, genau wie heute — nur mit neuen Symbolen aus derselben UML-Palette.

**Ein Satz zum Mitgeben am Ende von heute:** *„Sie können jetzt ein System von außen (Use-Case) und
von innen (Klassen) beschreiben. Morgen bringen wir es in Bewegung."*
