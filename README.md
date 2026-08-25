# UML-Diagramme — Lehrmaterial

Kursmaterial zu den fünf UML-Diagrammtypen: Use-Case, Klasse, Aktivität, Sequenz, Zustand.
Einheitlich aufbereitet — Lerntexte, Aufgaben, gerenderte Diagramme, Dozentenskript und ein
HTML-Lernportal.

## Ordnerübersicht

| Ordner | Inhalt |
|---|---|
| **`Lerntexte/`** | Die fünf Lerntexte `7.1`–`7.5` (Markdown) mit eingebetteten SVG-Diagrammen. Das Herzstück zum Lesen und Unterrichten. |
| **`Aufgaben/`** | Aufgabensätze je Diagrammtyp: **Teil A** (Vormittag, gemeinsam) + **Teil B** (Nachmittag, Selbstlernphase), jede Aufgabe mit eingeklappter Musterlösung. |
| **`Dozentenskript/`** | Folienbezogenes Regie-Skript (`.md` + fertiges `.html`). Tag 1 = Use-Case + Klassendiagramm. |
| **`Portal/`** | Das gebaute **HTML-Lernportal** — hier starten: `Portal/HTML/index.html`. Läuft offline per Doppelklick. |
| **`Folien/`** | Die PowerPoint `UML_Diagramme.pptx` und ihr PDF-Export. |
| **`grafiken/`** | Alle gerenderten Diagramme als SVG (`uc-*`, `kls-*`, `act-*`, `seq-*`, `zus-*`); Lösungsdiagramme unter `grafiken/loesungen/`. |
| **`diagramm-quellen/`** | Die PlantUML-Quelltexte (`.wsd`) je Typ + gemeinsames `theme.puml`. Aus ihnen werden die SVGs erzeugt. |
| **`_archiv/`** | Altbestand und interne Arbeitsdateien (nicht mehr aktiv genutzt). |
| **`_backup_original/`** | Unveränderte Originalfassungen der Skripte vor der Überarbeitung. |

## Schnellzugriff

- **Unterrichten:** `Dozentenskript/Dozentenskript_Tag1_UML.html` (zweites Fenster) + `Folien/UML_Diagramme.pptx` (geteilter Bildschirm).
- **Teilnehmer, Selbstlernen:** `Portal/HTML/index.html`.
- **Nachschlagen/Bearbeiten:** die Markdown in `Lerntexte/` und `Aufgaben/`.

## Stand

| Diagrammtyp | Lerntext aufgewertet | Aufgaben | Code entfernt | Im Portal | Dozentenskript |
|---|---|---|---|---|---|
| 7.1 Use-Case | ja | ja | ja | ja | Tag 1 |
| 7.2 Klassendiagramm | ja | ja | ja | ja | Tag 1 |
| 7.3 Aktivität | ja | ja | offen | offen | offen (Tag 2) |
| 7.4 Sequenz | ja | ja | offen | offen | offen (Tag 2) |
| 7.5 Zustand | ja | ja | offen | offen | offen (Tag 3) |

## Diagramme neu bauen (bei Bedarf)

SVGs aus den Quellen rendern (Beispiel):

```bash
java -jar plantuml.jar -tsvg diagramm-quellen/UseCase/uc-01.wsd -o ../../grafiken
```

Portal neu bauen: `python3 Portal/generator/build_v2.py` (liest aus `Portal/Bibliothek/`).
Dozentenskript-HTML bauen: mit `skript_bauen.py` aus dem Kursprojekt-Template.
