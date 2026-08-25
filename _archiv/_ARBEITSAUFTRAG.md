# Arbeitsauftrag — UML-Lehrmaterial aufwerten (gemeinsame Regeln)

Dieser Auftrag gilt für **alle** Bearbeiter. Jeder Bearbeiter ist für **genau einen** Diagrammtyp
zuständig (Use-Case, Klassen, Aktivität, Sequenz oder Zustand) und liefert dafür: (A) das
aufgewertete Lerntext-Skript und (B) einen Aufgabensatz. Der Fachinhalt bleibt erhalten — es wird
**aufgewertet, nicht umgeschrieben**.

Pfade (macOS-Sicht = was du mit Read/Write/Edit nutzt):
`/Users/segawork/Lehrmaterial/fachinformatiker/comcave-oop/07_UML-Diagramme/`
Bash-Sicht (für java/dot): `/sessions/amazing-cool-carson/mnt/07_UML-Diagramme/`

---

## 0. Zielbild

Aus je einem vorhandenen Markdown-Skript soll ein **Lerntext** werden, der
- inhaltlich mindestens so vollständig ist wie vorher (nichts fachlich Wertvolles kürzen),
- **keine Emojis** mehr enthält,
- **einheitlich gerenderte SVG-Diagramme** eingebettet hat (statt Mermaid-/PlantUML-Codeblöcken im Text),
- saubere Hinweis-Boxen, eine Notations-Referenztabelle und ein Glossar hat,
- warm und gut lesbar bleibt (kein starres Behörden-Deutsch).

Dazu ein **Aufgabensatz** pro Typ: Zwischenübungen (Vormittag) + Selbstlernaufgaben (Nachmittag),
gestaffelt leicht/mittel/schwer, jede mit eingeklappter Musterlösung als **gerendertes Lösungsdiagramm**.

---

## 1. Stil („zwischen voll und leicht")

**Beibehalten:**
- Die bestehende Kapitelstruktur, die Lernziele, die „Warum brauchen wir …?"-Motivation, alle
  Python-Codebeispiele und Erklärungen, alle Vergleichstabellen, die Zusammenfassung.
- Den freundlichen, erklärenden Ton mit Analogien.

**Ändern / ergänzen:**
- **Emojis entfernen.** Callouts mit Emoji (z. B. `> **💡 Merksatz:**`, `> **ℹ️ Hinweis:**`,
  `> **⚠️ Warnung:**`) werden zu emoji-freien Hinweis-Boxen umgeschrieben:
  ```markdown
  > **Merksatz:**
  > …

  > **Hinweis:**
  > …

  > **Warnung:**
  > …

  > **Tipp:**
  > …
  ```
  Kein Emoji im gesamten Dokument. (Prüfe am Ende mit grep.)
- **Notations-Referenztabelle:** Sorge dafür, dass es früh im Skript **eine vollständige Tabelle
  aller Notationselemente** deines Diagrammtyps gibt (Element | Bedeutung | Darstellung/Beispiel).
  Die meisten Skripte haben bereits eine „Legende"/„Notationselemente"-Sektion — vervollständige
  sie, ergänze eine Spalte mit einem gerenderten Mini-SVG des Elements, wo sinnvoll.
- **Glossar** als letzte Sektion `## Glossar` mit Tabelle `| Begriff | Kurzerklärung |` für alle
  Fachbegriffe des Skripts (deutsch + englischer Begriff, wo üblich).
- **Diagramme:** Jeder Mermaid-Block und jeder PlantUML-Codeblock, der ein *fachliches Diagramm*
  zeigt, wird durch ein **eingebettetes gerendertes SVG** ersetzt (siehe Abschnitt 2). Der
  PlantUML-/Mermaid-Quelltext verschwindet aus dem Lerntext (er gehört nicht in den Fließtext des
  Schülers). **Ausnahme:** Wenn ein Codeblock bewusst die *Notation zum Selberschreiben* lehrt
  (z. B. „so schreibt man PlantUML"), darf er als Codeblock bleiben — im Zweifel: Diagramm = Bild,
  Syntaxlehre = Codeblock. Python-Code bleibt immer als Codeblock.
- **„Was passiert hier?"**-Erklärungen nach komplexen Diagrammen/Code sind erwünscht, aber nicht
  erzwingen.

**Nicht** das Template-Korsett erzwingen: keine Meta-Zeile im `> **Bereich:** …`-Format nötig,
keine `<details>` im Lerntext nötig (die kommen in die Aufgaben). Es ist ein Lehr-Skript, kein
Portal-SSOT.

---

## 2. Diagramm-Workflow (verbindlich, damit alles gleich aussieht)

Alle Diagramme werden mit **PlantUML** gerendert, mit gemeinsamem Theme.

- PlantUML-Jar: `/tmp/plantuml.jar`  · Graphviz `dot` ist installiert.
- Theme: `/sessions/amazing-cool-carson/mnt/07_UML-Diagramme/PlantUMLs/theme.puml`
- **Jede** `.wsd`-Quelle beginnt mit:
  ```
  @startuml
  !include /sessions/amazing-cool-carson/mnt/07_UML-Diagramme/PlantUMLs/theme.puml
  … Diagramm …
  @enduml
  ```
- Rendern (Bash):
  ```
  cd /sessions/amazing-cool-carson/mnt/07_UML-Diagramme
  java -jar /tmp/plantuml.jar -tsvg PlantUMLs/<Ordner>/<name>.wsd -o /sessions/amazing-cool-carson/mnt/07_UML-Diagramme/images
  ```
  (Das SVG landet dann in `images/<name>.svg`.)
- **Prüfe jedes Rendering**: Die Datei muss existieren und `>0` Byte sein; bei `dot`-Fehlern
  erscheint eine Fehlerbox im SVG — dann Syntax korrigieren und neu rendern.

**Quellen je Typ:**
- Aktivität: vorhandene `.wsd` in `PlantUMLs/Aktivitaet/` — Theme-Include ergänzen, neu rendern.
- Sequenz: vorhandene `.wsd` in `PlantUMLs/Sequenz/` + die 8 PlantUML-Blöcke im Skript.
- Zustand: vorhandene `.wsd` in `PlantUMLs/Zustand/` + die 14 PlantUML-Blöcke im Skript.
- Use-Case: **neu** aus den Mermaid-Blöcken übersetzen → `PlantUMLs/UseCase/uc-*.wsd`.
- Klassen: **neu** aus den Mermaid-Blöcken übersetzen → `PlantUMLs/Klassen/kls-*.wsd`.

**Einbetten im Markdown** mit relativem Pfad und aussagekräftigem Alt-Text:
```markdown
![Use-Case-Diagramm Bibliothekssystem](images/uc-05.svg)
```

**Deutsche Umlaute** in `.wsd` sind ok (UTF-8). Bezeichner mit Umlaut/Leerzeichen immer quoten:
`usecase "Buch zurückgeben" as UC2`.

---

## 3. Aufgabensatz je Typ

Eigene Datei unter `Exercises/`, Name: `Aufgaben_7.X_<Typ>.md`.

Struktur:
```markdown
# Aufgaben — <Diagrammtyp>

Kurzer Einleitungssatz + Hinweis auf das zugehörige Skript.

## Teil A — Zwischenübungen (Vormittag)
### Aufgabe A1 [leicht]: <Titel>
<Aufgabenstellung: was modelliert werden soll, nicht wie>

<details><summary>Musterlösung</summary>

![Lösung A1](../images/loesungen/<name>.svg)

<pre><code>… PlantUML-Quelle der Lösung (zum Nachvollziehen) …</code></pre>

Kurze Erläuterung: warum so, worauf achten.

</details>

---
```
- **Teil A: 3–5 Aufgaben** (leicht→mittel), zum sofort Üben nach der Erklärung.
- **Teil B — Selbstlernphase (Nachmittag): 8–12 Aufgaben**, gestaffelt leicht/mittel/schwer,
  die letzten 1–2 anspruchsvoll (Transfer, kombiniert mehrere Konzepte).
- **Jede** Aufgabe hat eine **Musterlösung in `<details>`** mit **gerendertem Lösungs-SVG**
  (in `images/loesungen/`) **und** der PlantUML-Quelle als `<pre><code>…</code></pre>`
  (nicht als ```-Fence, weil das in Klappboxen unzuverlässig rendert).
- Zielgruppe: **UML-Erstlernende.** Aufgaben konkret, alltagsnah (Automat, Bibliothek, Online-Shop,
  Smart Home, Ampel, Aufzug …), klar abgegrenzt. Keine Aufgabe ohne eindeutig modellierbare Lösung.
- Alle Lösungs-Diagramme mit dem gemeinsamen Theme rendern (Abschnitt 2).

---

## 4. Ausgabe-Orte (Zusammenfassung)

| Was | Wohin |
|---|---|
| Aufgewertetes Skript | dieselbe Datei überschreiben (`7.X_….md`) |
| Diagramm-Quellen | `PlantUMLs/<Typ>/*.wsd` (mit Theme-Include) |
| Gerenderte Diagramme | `images/*.svg` |
| Lösungs-Diagramme | `images/loesungen/*.svg` |
| Aufgabensatz | `Exercises/Aufgaben_7.X_<Typ>.md` |

## 5. Selbstprüfung vor Abschluss
- [ ] `grep -oE '💡|ℹ️|⚠️|✅|📝|🎯|🔑|✏️|📌|🚀|❗|✔️' <skript>` liefert nichts.
- [ ] Jedes eingebettete SVG existiert und öffnet (Bytegröße > 0, keine Fehlerbox).
- [ ] Kein Mermaid-/PlantUML-Diagrammblock mehr im Lerntext-Fließtext (Python-Code bleibt).
- [ ] Notations-Referenztabelle + Glossar vorhanden.
- [ ] Aufgabensatz: Teil A (3–5) + Teil B (8–12), jede mit Musterlösung + Lösungs-SVG.
- [ ] Inhalt vollständig erhalten (mit Backup in `_backup_original/` vergleichen, wenn unsicher).

Melde am Ende knapp zurück: Anzahl gerenderte Diagramme, Anzahl Aufgaben (A/B), was du am Inhalt
verändert hast, und offene Punkte.
