#!/usr/bin/env python3
"""
Lernportal-Generator, Fassung 2 (Testszenario).

Was sich gegenüber build.py ändert:
  * CSS und JS liegen als eigene Dateien unter HTML/assets/ statt in jeder
    einzelnen Seite. Cache-Aufbrechen über ?v=<Hash>.
  * Kein Dozenten-Portal mehr.
  * Die Gliederung kommt aus kurs_konfig.json, nicht aus einer Python-Konstante.
    Der Generator kennt das Wort "Bereich" nicht mehr.
  * Startseite: einspaltige Abschnittsliste statt Kachelraster.
  * Seitenleiste: Heimatlink und Abschnittswechsler oben, Gruppen durch
    Haarlinien getrennt, aktiver Punkt mit Akzentbalken.
  * Rechte Spalte "Auf dieser Seite" mit Scroll-Mitlauf, Lesefortschrittsbalken.
  * Karteikarten, Übungen und MC-Fragen als eine Kartenkomponente.
  * Glossar als Nachschlage-Komponente mit Suche und A–Z statt als Tabelle.

Die Markdown-SSOT wird ausschließlich gelesen. Keine Quelldatei wird verändert.

Aufruf:  python3 build_v2.py
"""

import hashlib
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Das Paket 'markdown' fehlt.  pip install --break-system-packages markdown")

GEN = Path(__file__).resolve().parent
WURZEL = GEN.parent
AUS = WURZEL / "HTML"
AUS_MAT = AUS / "mat"
AUS_ASSETS = AUS / "assets"
AUS_BILD = AUS / "bilder"

KONFIG = json.loads((GEN / "kurs_konfig.json").read_text(encoding="utf-8"))
QUELLE = (GEN / KONFIG["quelle"]).resolve()

MD_ERW = ["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html", "toc"]

# Ordnername -> (kuerzel, Navigationslabel, Überschrift, Renderer)
GATTUNGEN = {k: tuple(v) for k, v in KONFIG["gattungen"].items() if not k.startswith("_")}
FLUSS = [v[0] for v in GATTUNGEN.values()]
GLOBAL = {k: v for k, v in KONFIG["global"].items() if not k.startswith("_")}
ABSCHNITTE = KONFIG["abschnitte"]
WORT = KONFIG["gliederung"]["wort_singular"]
GEWICHT_ZEIGEN = KONFIG["gliederung"].get("gewicht_zeigen", True)
UMSETZUNG = KONFIG.get("umsetzung", {})


# ------------------------------------------------------------------ Werkzeug
def slug(name: str) -> str:
    s = re.sub(r"\.md$", "", name).lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def md2html(text: str) -> str:
    return markdown.markdown(text, extensions=MD_ERW, output_format="html5")


def inline(text: str) -> str:
    """Markdown ohne umschließendes <p> – für Überschriften und Optionen."""
    html = markdown.markdown(text.strip(), extensions=["fenced_code"])
    return re.sub(r"^<p>|</p>$", "", html.strip())


def erste_h1(pfad: Path) -> str:
    for z in pfad.read_text(encoding="utf-8").splitlines():
        if z.startswith("# "):
            return z[2:].strip()
    return pfad.stem


def ohne_h1(text: str) -> str:
    raus, weg = [], False
    for z in text.splitlines():
        if not weg and z.startswith("# "):
            weg = True
            continue
        raus.append(z)
    return "\n".join(raus)


def ist_ergaenzung(pfad: Path) -> bool:
    kopf = pfad.read_text(encoding="utf-8").split("\n")[:8]
    return any("Ergänzung" in z for z in kopf)


KURZTITEL_ZEILE = re.compile(r"\*\*Kurztitel:\*\*\s*([^·|\n]+)")


def kurztitel(pfad: Path) -> str:
    """Der Name, unter dem eine Seite in der Navigation steht.

    Drei Quellen, in dieser Reihenfolge:
      1. '**Kurztitel:** …' in der Meta-Zeile der Markdown – der saubere Weg,
         weil der Name dort steht, wo auch der Inhalt steht.
      2. Ein Eintrag in kurs_konfig.json unter 'kurztitel', geschlüsselt mit
         dem Pfad ab der Bibliothek. Damit lässt sich ein fertiger Kurs
         nachrüsten, ohne eine einzige Inhaltsdatei anzufassen.
      3. Sonst die H1 der Seite.

    Der Kurztitel gilt ausschließlich für die Seitenleiste. Überschrift,
    Brotkrume, Materialliste und die Weiter-Knöpfe tragen weiter den vollen
    Titel – sonst hieße dieselbe Seite an vier Stellen unterschiedlich.
    """
    for z in pfad.read_text(encoding="utf-8").split("\n")[:8]:
        m = KURZTITEL_ZEILE.search(z)
        if m:
            return m.group(1).strip()
    schluessel = pfad.relative_to(QUELLE).as_posix()
    return KONFIG.get("kurztitel", {}).get(schluessel, "")


def nachbearbeiten(html: str) -> str:
    """Nachbehandlung des erzeugten HTML: Umsetzungsbox und Tabellenhülle."""
    ausloeser = UMSETZUNG.get("ausloeser")
    marke = UMSETZUNG.get("marke", "")
    if ausloeser:
        html = re.sub(
            r"<blockquote>\s*<p><strong>" + re.escape(ausloeser) + r"</strong>",
            f'<blockquote class="umsetzung" data-marke="{marke}"><p>',
            html,
        )
    # Breite Tabellen scrollen in ihrer eigenen Hülle, damit die Seite nie
    # waagerecht scrollt.
    html = re.sub(r"<table>(.*?)</table>",
                  r'<div class="tabellenhuelle"><table>\1</table></div>',
                  html, flags=re.S)
    return html


def klappboxen(text: str):
    """Zerlegt die <details>-Blöcke eines Markdown-Abschnitts.

    Rückgabe: (Text ohne die Klappboxen, {Titel_klein: HTML})
    """
    gefunden = {}

    def merken(m):
        titel = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        gefunden[titel.lower()] = md2html(m.group(2).strip())
        return ""

    rest = re.sub(r"<details>\s*<summary>(.*?)</summary>(.*?)</details>",
                  merken, text, flags=re.S)
    return rest, gefunden


# ------------------------------------------------------------------ Datenmodell
class Seite:
    def __init__(self, abschnitt, typ, renderer, quelle: Path):
        self.abschnitt = abschnitt          # dict oder None
        self.typ = typ                      # lt | ex | ka | ue | mu | glob
        self.renderer = renderer            # text | karten | uebung | mc | glossar
        self.quelle = quelle
        n = abschnitt["nr"] if abschnitt else 0
        self.slug = (f"a{n}_{typ}_{slug(quelle.name)}" if abschnitt
                     else f"glob_{slug(quelle.name)}")
        self.datei = f"{self.slug}.html"
        self.titel = erste_h1(quelle)
        self.nav_titel = kurztitel(quelle) or self.titel
        self.ergaenzung = ist_ergaenzung(quelle)

    @property
    def merker(self):
        return ('<span class="merker-erg" title="Ergänzung">Ergänzung</span>'
                if self.ergaenzung else "")


def pfad(ort: str, ziel: str) -> str:
    """ort: 'root' (HTML/) oder 'mat' (HTML/mat/)."""
    hoch = "" if ort == "root" else "../"
    if ziel == "index":
        return f"{hoch}index.html"
    if ziel.startswith("abschnitt:"):
        return f"{hoch}Abschnitt_{ziel.split(':')[1]}.html"
    if ziel.startswith("mat:"):
        s = ziel.split(":", 1)[1]
        return f"mat/{s}.html" if ort == "root" else f"{s}.html"
    if ziel.startswith("asset:"):
        return f"{hoch}assets/{ziel.split(':', 1)[1]}"
    return "#"


# ------------------------------------------------------------------ Assets
def assets_bauen():
    """Kopiert die Stylesheets und das Skript nach HTML/assets/ und erzeugt
    kurs.css aus der Konfiguration. Gibt den Cache-Hash zurück.

    Der Hash ist beim Ausliefern über GitHub Pages der entscheidende Punkt:
    ohne ihn sehen die Teilnehmer nach einem Push tagelang die alte Optik aus
    ihrem Browser-Cache."""
    AUS_ASSETS.mkdir(parents=True, exist_ok=True)
    d = KONFIG["design"]
    hell, dunkel = d["akzent_hell"], d["akzent_dunkel"]

    def weich(farbe, alpha):
        r, g, b = (int(farbe[i:i + 2], 16) for i in (1, 3, 5))
        return f"rgba({r},{g},{b},{alpha})"

    kurs_css = f"""/* Erzeugt aus kurs_konfig.json – nicht von Hand ändern.
   Die einzige Datei mit einer kursspezifischen Farbe. */
:root {{
  --akzent: {hell};
  --akzent-weich: {weich(hell, '.10')};
  --auf-akzent: #ffffff;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-thema="hell"]) {{
    --akzent: {dunkel};
    --akzent-weich: {weich(dunkel, '.16')};
    --auf-akzent: #0d1117;
  }}
}}
:root[data-thema="dunkel"] {{
  --akzent: {dunkel};
  --akzent-weich: {weich(dunkel, '.16')};
  --auf-akzent: #0d1117;
}}
"""
    (AUS_ASSETS / "kurs.css").write_text(kurs_css, encoding="utf-8")

    inhalt = kurs_css
    for name in ("portal.css", "komponenten.css", "portal.js"):
        text = (GEN / "assets" / name).read_text(encoding="utf-8")
        (AUS_ASSETS / name).write_text(text, encoding="utf-8")
        inhalt += text
    return hashlib.sha1(inhalt.encode("utf-8")).hexdigest()[:8]


HASH = ""

HAUS = ('<svg width="15" height="15" viewBox="0 0 16 16" fill="none" '
        'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
        'stroke-linejoin="round" aria-hidden="true">'
        '<path d="M2 6.5 8 2l6 4.5V13a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1z"/></svg>')

MENUE = ('<svg width="17" height="17" viewBox="0 0 16 16" fill="none" '
         'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
         'aria-hidden="true"><path d="M2 4h12M2 8h12M2 12h12"/></svg>')

SONNE = ('<svg class="sonne" width="16" height="16" viewBox="0 0 16 16" fill="none" '
         'stroke="currentColor" stroke-width="1.5" stroke-linecap="round" '
         'aria-hidden="true"><circle cx="8" cy="8" r="3.2"/>'
         '<path d="M8 1v1.6M8 13.4V15M1 8h1.6M13.4 8H15M3 3l1.1 1.1M11.9 11.9 13 13'
         'M13 3l-1.1 1.1M4.1 11.9 3 13"/></svg>')

MOND = ('<svg class="mond" width="16" height="16" viewBox="0 0 16 16" fill="none" '
        'stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" '
        'aria-hidden="true"><path d="M13.5 9.6A6 6 0 0 1 6.4 2.5a6 6 0 1 0 7.1 7.1z"/></svg>')

# Läuft vor dem ersten Rendern: verhindert das Aufblitzen der hellen Fassung
# und schaltet die JS-abhängigen Zustände frei.
KOPF_SKRIPT = ("<script>(function(){var w=document.documentElement;w.classList.add('js');"
               "try{var t=localStorage.getItem('portal-thema');"
               "if(t==='hell'||t==='dunkel')w.setAttribute('data-thema',t);}catch(e){}})();</script>")


# ------------------------------------------------------------------ Seitenleiste
def nav_link(ort, seite, aktuell, mit_merker=True):
    adresse = pfad(ort, "mat:" + seite.slug)
    klasse = ' class="hier"' if seite.slug == aktuell else ""
    merker = seite.merker if mit_merker else ""
    # In der Leiste der Kurztitel, im Tooltip der volle – so bleibt der
    # vollständige Name erreichbar, ohne zwei Zeilen zu kosten.
    ruf = f' title="{seite.titel}"' if seite.nav_titel != seite.titel else ""
    return f'<a href="{adresse}"{klasse}{ruf}>{seite.nav_titel}{merker}</a>'


def seitenleiste(abschnitt, seiten, globale, ort, aktuell=""):
    n = abschnitt["nr"]
    t = ['<nav class="navseite" id="navseite" aria-label="Kursnavigation">']
    t.append(f'<a class="nav-heim" href="{pfad(ort, "index")}">{HAUS} Startseite</a>')

    # Abschnittswechsler oben statt einer Linkliste ganz unten. Wer zur
    # Startseite oder in einen anderen Abschnitt will, scrollt nicht mehr an
    # allem vorbei.
    if len(ABSCHNITTE) > 1:
        andere = []
        for a in ABSCHNITTE:
            if a["nr"] == n:
                continue
            erg = '<span class="merker-erg">Erg.</span>' if a.get("ergaenzung") else ""
            adresse = pfad(ort, "abschnitt:" + str(a["nr"]))
            andere.append(f'<a href="{adresse}">{WORT} {a["nr"]}: {a["titel"]}{erg}</a>')
        t.append('<details class="nav-wechsler"><summary>'
                 f'{WORT} {n}: {abschnitt["titel"]}</summary>'
                 f'<div class="nav-wechsler-liste">{"".join(andere)}</div></details>')

    ueb = seiten[n]["uebersicht"]
    hier = ' class="hier"' if ueb and ueb.slug == aktuell else ""
    adresse = pfad(ort, "abschnitt:" + str(n))
    t.append('<div class="nav-gruppe">'
             f'<div class="nav-gruppe-titel">{WORT} {n}</div>'
             f'<a href="{adresse}"{hier}>Übersicht und Lernweg</a></div>')

    # Alle Gattungsgruppen sind einklappbar. Offen ist beim ersten Besuch nur
    # die Gruppe, in der die aktuelle Seite steht – sonst wird die Leiste bei
    # fünf Gattungen länger als der Bildschirm. Die Zahl neben dem Titel sagt,
    # was in einer zugeklappten Gruppe steckt. Was der Nutzer selbst auf- oder
    # zuklappt, merkt sich portal.js.
    gruppen = []
    for _ordner, (typ, label, _ueber, _rend) in GATTUNGEN.items():
        posten = seiten[n][typ]
        if posten:
            gruppen.append((label, posten, True))
    if globale:
        gruppen.append(("Nachschlagen und Prüfen", globale, False))

    hat_treffer = any(p.slug == aktuell for _l, ps, _m in gruppen for p in ps)
    for i, (label, posten, mit_merker) in enumerate(gruppen):
        eintraege = "".join(nav_link(ort, p, aktuell, mit_merker) for p in posten)
        # Auf der Übersichtsseite steht die aktuelle Seite in keiner Gruppe.
        # Dann die erste öffnen, damit die Leiste nicht völlig zu ist.
        offen = any(p.slug == aktuell for p in posten) or (not hat_treffer and i == 0)
        t.append(
            f'<details class="nav-gruppe" data-gruppe="{slug(label)}"'
            f'{" open" if offen else ""}><summary>'
            f'<span class="nav-gruppe-titel">{label}</span>'
            f'<span class="nav-gruppe-anzahl">{len(posten)}</span></summary>'
            f'<div class="nav-gruppe-inhalt">{eintraege}</div></details>')

    t.append("</nav>")
    return "\n".join(t)


# ------------------------------------------------------------------ Rahmen
def toc_bauen(html: str) -> str:
    """Zieht h2 und h3 mit ihren IDs aus dem erzeugten Inhalt."""
    treffer = re.findall(r'<h([23])[^>]*id="([^"]+)"[^>]*>(.*?)</h\1>', html, re.S)
    if len(treffer) < 2:
        return ""
    zeilen = []
    for stufe, kennung, text in treffer:
        rein = re.sub(r"<[^>]+>", "", text).strip()
        klasse = ' class="stufe3"' if stufe == "3" else ""
        zeilen.append(f'<a href="#{kennung}"{klasse}>{rein}</a>')
    return ('<aside class="toc" aria-label="Auf dieser Seite">'
            '<div class="toc-titel">Auf dieser Seite</div>'
            + "".join(zeilen) + "</aside>")


def rahmen(titel, inhalt, ort, leiste=None, krume="", toc=""):
    k = KONFIG["kurs"]
    v = f"?v={HASH}"
    a = lambda d: pfad(ort, f"asset:{d}") + v
    kopf = (
        f'<header class="kopf"><div class="kopf-innen">'
        f'<button class="knopf menuknopf" aria-label="Navigation anzeigen" '
        f'aria-expanded="false" aria-controls="navseite">{MENUE}</button>'
        f'<a class="marke" href="{pfad(ort, "index")}">'
        f'<span class="marke-zeichen">{k["zeichen"]}</span>'
        f'<span class="marke-name">{k["kurztitel"]}</span>'
        f'<span class="marke-zusatz">{k["name"]}</span></a>'
        f'<div class="kopf-rechts">'
        f'<button class="knopf themaschalter" aria-label="Dunkle Ansicht umschalten">'
        f'{SONNE}{MOND}</button>'
        f'</div></div></header><div class="fortschritt"></div>'
    )
    schale = "schale" if leiste else "schale schale--schlicht"
    krume_html = f'<div class="krume">{krume}</div>' if krume else ""
    return (
        '<!DOCTYPE html><html lang="de"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{titel} · {k["kurztitel"]}</title>'
        f'<link rel="stylesheet" href="{a("portal.css")}">'
        f'<link rel="stylesheet" href="{a("komponenten.css")}">'
        f'<link rel="stylesheet" href="{a("kurs.css")}">'
        f'{KOPF_SKRIPT}</head><body>'
        f'<a class="sprungmarke" href="#inhalt">Zum Inhalt springen</a>'
        f'{kopf}<div class="navschatten"></div>'
        f'<div class="{schale}">{leiste or ""}'
        f'<main class="inhalt" id="inhalt">{krume_html}{inhalt}'
        f'<footer class="fusszeile">{k["code"]} · {k["marke"]}</footer></main>'
        f'{toc}</div>'
        f'<script src="{a("portal.js")}" defer></script>'
        '<!-- Erzeugt aus der Markdown-SSOT. HTML nicht von Hand bearbeiten. -->'
        '</body></html>'
    )


def blaettern(zurueck, weiter):
    t = ['<nav class="weiterblaettern" aria-label="Blättern">']
    if zurueck:
        titel, ziel = zurueck
        t.append(f'<a class="blatt blatt--zurueck" href="{ziel}">'
                 f'<div class="blatt-marke">‹ Zurück</div>'
                 f'<div class="blatt-titel">{titel}</div></a>')
    else:
        t.append("<span></span>")
    if weiter:
        titel, ziel = weiter
        t.append(f'<a class="blatt blatt--weiter" href="{ziel}">'
                 f'<div class="blatt-marke">Weiter ›</div>'
                 f'<div class="blatt-titel">{titel}</div></a>')
    else:
        t.append("<span></span>")
    t.append("</nav>")
    return "".join(t)


# ------------------------------------------------------------------ Karteikarten
def karten_rendern(text):
    """Karteikarte: vorne die Frage, der Tipp sofort erreichbar, die Antwort
    auf Knopfdruck, die Erklärung erst danach. Ohne JavaScript ist alles
    sichtbar – die Karte funktioniert, nur ohne Aufdeck-Effekt."""
    bloecke = re.split(r"(?m)^### ", text)
    aus = []
    intro = bloecke[0].strip()
    if intro:
        aus.append(nachbearbeiten(md2html(intro)))

    karten = bloecke[1:]
    if karten:
        aus.append('<div class="kartenleiste"><span class="zaehler"></span>'
                   '<button class="knopf knopf--klein alle-aufdecken" type="button">'
                   'Alle aufdecken</button></div>')

    for i, b in enumerate(karten, 1):
        zeilen = b.splitlines()
        kopf = zeilen[0].strip()
        rest, boxen = klappboxen("\n".join(zeilen[1:]))

        # "Frage 1.1.51: Was unterscheidet ..." -> Nummer nach oben rechts
        m = re.match(r"(Frage\s+[\d.]+)\s*(?:\[(\w+)\])?\s*:\s*(.+)", kopf)
        nummer, frage = (m.group(1), m.group(3)) if m else ("", kopf)

        tipp = boxen.get("tipp", "")
        antwort = boxen.get("antwort", "")
        erklaerung = boxen.get("erklärung") or boxen.get("erklaerung", "")
        zusatz = nachbearbeiten(md2html(re.sub(r"(?m)^-{3,}\s*$", "", rest).strip()))

        fuss = []
        if tipp:
            fuss.append('<details data-rolle="tipp"><summary>Tipp</summary>'
                        f'<div class="klappinhalt">{tipp}</div></details>')
        if erklaerung:
            fuss.append('<details data-rolle="erklaerung" data-gesperrt>'
                        '<summary>Erklärung</summary>'
                        f'<div class="klappinhalt">{erklaerung}</div></details>')

        aus.append(
            f'<div class="karte-marke"><span>Karte {i} von {len(karten)}</span>'
            f'<span>{nummer}</span></div>'
            f'<article class="karte karte--frage">'
            f'<div class="karte-koerper">'
            f'<h3 class="karte-frage">{inline(frage)}</h3>{zusatz}'
            f'<button class="knopf knopf--stark karte-aufdecken" type="button">'
            f'Antwort zeigen</button>'
            f'<div class="karte-antwort">'
            f'<div class="karte-antwort-marke">Antwort</div>{antwort}</div>'
            f'</div>'
            + (f'<div class="karte-fuss">{"".join(fuss)}</div>' if fuss else "")
            + '</article>')
    return "\n".join(aus)


# ------------------------------------------------------------------ Übungen
def uebungen_rendern(text):
    bloecke = re.split(r"(?m)^### ", text)
    aus = []
    intro = bloecke[0].strip()
    if intro:
        aus.append(nachbearbeiten(md2html(intro)))

    for b in bloecke[1:]:
        zeilen = b.splitlines()
        kopf = zeilen[0].strip()
        rest, boxen = klappboxen("\n".join(zeilen[1:]))
        koerper = nachbearbeiten(md2html(re.sub(r"(?m)^-{3,}\s*$", "", rest).strip()))

        fuss = "".join(
            f'<details data-rolle="{slug(name)}"><summary>{name.capitalize()}</summary>'
            f'<div class="klappinhalt">{html}</div></details>'
            for name, html in boxen.items())

        aus.append(
            f'<article class="karte karte--uebung"><div class="karte-koerper">'
            f'<h3 class="uebung-titel">{inline(kopf)}</h3>{koerper}</div>'
            + (f'<div class="karte-fuss">{fuss}</div>' if fuss else "")
            + '</article>')
    return "\n".join(aus)


# ------------------------------------------------------------------ Multiple Choice
def mc_zerlegen(text):
    bloecke = re.split(r"(?m)^### ", text)
    fragen = [f for f in (mc_frage("### " + b) for b in bloecke[1:]) if f]
    return bloecke[0], fragen


def greif(text, muster):
    m = re.search(muster, text, re.S)
    return m.group(1).strip() if m else ""


def mc_frage(block):
    kopf = re.match(r"### Frage\s+([\d.]+)\s*(?:\[(\w+)\])?\s*:?\s*(.*)", block)
    if not kopf:
        return None
    vor = block.split("**Richtig:**")[0]
    optionen = dict(re.findall(r"(?m)^[-*]\s*([A-D])\)\s*(.+)$", vor))
    m = re.search(r"### Frage[^\n]*\n(.*?)\n[-*]\s*[A-D]\)", block, re.S)
    falsch = dict(re.findall(
        r"(?m)^[-*]\s*([A-D])\)\s*(.+)$",
        greif(block, r"\*\*Warum die anderen falsch sind:\*\*\s*(.+?)(?=\n\*\*Prüfungstipp|\Z)")))
    return {
        "id": kopf.group(1),
        "stufe": (kopf.group(2) or "").lower(),
        "titel": kopf.group(3).strip(),
        "frage": m.group(1).strip() if m else "",
        "optionen": optionen,
        "richtig": (re.search(r"\*\*Richtig:\*\*\s*([A-D])", block) or [None, ""])[1],
        "erklaerung": greif(block, r"\*\*Erklärung:\*\*\s*(.+?)(?=\n\*\*|\Z)"),
        "tipp": greif(block, r"\*\*Prüfungstipp:\*\*\s*(.+?)(?=\n\*\*|\Z)"),
        "falsch": falsch,
    }


def mc_rendern_frage(q):
    name = "f_" + q["id"].replace(".", "_")
    stufe = (f'<span class="mc-stufe">{q["stufe"].capitalize()}</span>'
             if q["stufe"] else "")
    optionen = "".join(
        f'<label class="mc-option"><input type="radio" name="{name}" value="{b}">'
        f'<span class="mc-buchstabe">{b}</span>'
        f'<span>{inline(q["optionen"][b])}</span>'
        f'<span class="mc-zeichen"></span></label>'
        for b in "ABCD" if b in q["optionen"])
    falsch = ""
    if q["falsch"]:
        lis = "".join(f'<li><strong>{b})</strong> {inline(t)}</li>'
                      for b, t in q["falsch"].items())
        falsch = f'<p><strong>Warum die anderen falsch sind:</strong></p><ul>{lis}</ul>'
    tipp = f'<p><strong>Prüfungstipp:</strong> {inline(q["tipp"])}</p>' if q["tipp"] else ""
    return (
        f'<article class="mc" data-richtig="{q["richtig"]}">'
        f'<div class="mc-kopf">{stufe}<span class="mc-nr">Frage {q["id"]}</span>'
        f'<span>{q["titel"]}</span></div>'
        f'<div class="mc-frage">{inline(q["frage"])}</div>{optionen}'
        f'<div class="mc-loesung"><p><strong>Erklärung:</strong> '
        f'{inline(q["erklaerung"])}</p>{falsch}{tipp}</div></article>')


def mc_rendern(text):
    intro, fragen = mc_zerlegen(text)
    aus = nachbearbeiten(md2html(intro))
    if fragen:
        aus += ('<div class="mc-leiste"><span class="punktestand"></span>'
                '<button class="knopf knopf--klein neu" type="button">'
                'Zurücksetzen</button></div>')
    return aus + "".join(mc_rendern_frage(q) for q in fragen)


# ------------------------------------------------------------------ Glossar
VERWECHSELN = re.compile(r"\*{0,2}Nicht zu verwechseln mit .*?\.\*{0,2}(?=\s|$)")


def anfangsbuchstabe(begriff: str) -> str:
    z = unicodedata.normalize("NFD", begriff.strip()[:1].upper())[:1]
    return z if z.isalpha() else "#"


def glossar_rendern(text):
    """Aus der Markdown-Tabelle eine Nachschlage-Komponente machen.

    Bei 110 Begriffen ist das Suchfeld der eigentliche Gewinn: es macht aus
    einer Leseliste ein Nachschlagewerk."""
    zeilen = text.splitlines()
    vor, tabelle = [], []
    in_tabelle = False
    for z in zeilen:
        if z.strip().startswith("|"):
            in_tabelle = True
            tabelle.append(z.strip())
        elif in_tabelle and not z.strip():
            continue
        elif not in_tabelle:
            vor.append(z)

    eintraege = []
    for z in tabelle[2:]:                      # Kopfzeile und Trennlinie weg
        spalten = [s.strip() for s in z.strip("|").split("|")]
        if len(spalten) < 3 or not spalten[0]:
            continue
        eintraege.append(spalten[:3])
    eintraege.sort(key=lambda e: unicodedata.normalize("NFD", e[0]).lower())

    vorhanden = {anfangsbuchstabe(e[0]) for e in eintraege}
    az = "".join(
        f'<a href="#gl-{b}">{b}</a>' if b in vorhanden
        else f'<a class="leer">{b}</a>'
        for b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    aus = [nachbearbeiten(md2html("\n".join(vor).strip()))]
    aus.append(
        '<div class="glossar-kopf">'
        '<input class="suchfeld" type="search" autocomplete="off" '
        'placeholder="Begriff suchen – deutsch, englisch oder im Erklärungstext (Taste /)" '
        'aria-label="Glossar durchsuchen">'
        f'<div class="az">{az}</div>'
        '<div class="treffer"></div></div>')

    letzter = ""
    for begriff, englisch, erklaerung in eintraege:
        b = anfangsbuchstabe(begriff)
        if b != letzter:
            aus.append(f'<h2 class="buchstabe" id="gl-{b}">{b}</h2>')
            letzter = b

        warnung = ""
        m = VERWECHSELN.search(erklaerung)
        if m:
            warnung = (f'<div class="verwechseln">{inline(m.group(0))}</div>')
            erklaerung = erklaerung.replace(m.group(0), "").strip()

        en = (f'<div class="eintrag-en">{inline(englisch)}</div>'
              if englisch and englisch != begriff else "")
        aus.append(
            f'<div class="eintrag"><div class="eintrag-begriff">{inline(begriff)}</div>'
            f'{en}<div class="eintrag-text">{inline(erklaerung)}</div>{warnung}</div>')
    return "\n".join(aus)


# ------------------------------------------------------------------ Erfassung
def erfassen():
    nach_abschnitt, alle = {}, []
    for a in ABSCHNITTE:
        n = a["nr"]
        ordner = QUELLE / a["ordner"]
        eintrag = {"uebersicht": None, "quellen": None, **{t: [] for t in FLUSS}}

        for name in (f"{a['ordner'].split('_')[0]}_{n}_Uebersicht.md",
                     f"Bereich_{n}_Uebersicht.md", "Uebersicht.md"):
            if (ordner / name).exists():
                eintrag["uebersicht"] = Seite(a, "hub", "text", ordner / name)
                break
        if (ordner / "MS_Learn_Quellen.md").exists():
            eintrag["quellen"] = ordner / "MS_Learn_Quellen.md"

        for unter, (typ, _l, _u, renderer) in GATTUNGEN.items():
            d = ordner / unter
            if not d.is_dir():
                continue
            for f in sorted(d.glob("*.md")):
                p = Seite(a, typ, renderer, f)
                eintrag[typ].append(p)
                alle.append(p)
        nach_abschnitt[n] = eintrag

    globale = []
    for unter, renderer in GLOBAL.items():
        d = QUELLE / unter
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.md")):
            p = Seite(None, "glob", renderer, f)
            globale.append(p)
            alle.append(p)
    return nach_abschnitt, globale, alle


# ------------------------------------------------------------------ Seiten
def ziel(p, ort, abschnitt=None):
    if p is None:
        return None
    if p == "HUB":
        return (f"{WORT} {abschnitt['nr']}: {abschnitt['titel']}",
                pfad(ort, f"abschnitt:{abschnitt['nr']}"))
    return (p.titel, pfad(ort, f"mat:{p.slug}"))


def materialblock(eintrag, globale, ort):
    t = []
    for unter, (typ, _label, ueberschrift, _r) in GATTUNGEN.items():
        posten = eintrag[typ]
        if not posten:
            continue
        zeilen = "".join(
            f'<a class="material" href="{pfad(ort, f"mat:{p.slug}")}">'
            f'{p.titel}{p.merker}</a>' for p in posten)
        t.append(f'<div class="gattung"><div class="gattung-titel">{ueberschrift}</div>'
                 f'<div class="materialliste">{zeilen}</div></div>')
    if globale:
        zeilen = "".join(
            f'<a class="material" href="{pfad(ort, f"mat:{p.slug}")}">{p.titel}</a>'
            for p in globale)
        t.append('<div class="gattung"><div class="gattung-titel">'
                 f'Übergreifend – Nachschlagen und Prüfen</div>'
                 f'<div class="materialliste">{zeilen}</div></div>')
    if not t:
        return '<p class="hinweis">Für diesen Abschnitt liegt noch kein Material vor.</p>'
    return f'<h2 id="materialien">Materialien</h2>{"".join(t)}'


def quellenblock(p):
    if not p or not p.exists():
        return ""
    return ('<div class="quellenbox"><h2>Offizielle Quellen</h2>'
            f'{nachbearbeiten(md2html(ohne_h1(p.read_text(encoding="utf-8"))))}</div>')


def hub_rendern(a, eintrag, nach_abschnitt, globale, weiter):
    n = a["nr"]
    ueb = eintrag["uebersicht"]
    merker = '<span class="merker-erg">Ergänzung</span>' if a.get("ergaenzung") else ""
    gewicht = (f'<p><strong>Prüfungsgewicht: {a["gewicht"]}</strong> · {a["unter"]}</p>'
               if GEWICHT_ZEIGEN and a.get("gewicht") else f'<p>{a["unter"]}</p>')

    if ueb:
        text = ohne_h1(ueb.quelle.read_text(encoding="utf-8"))
        intro = f"<h1>{ueb.titel}{merker}</h1>{nachbearbeiten(md2html(text))}"
    else:
        intro = (f'<h1>{WORT} {n} – {a["titel"]}{merker}</h1>{gewicht}'
                 f'<p>Die Materialien stehen unten und in der Navigation links. '
                 f'Arbeite die Lerntexte der Reihe nach durch – sie tragen den Stoff.</p>')

    inhalt = (intro
              + materialblock(eintrag, globale, "root")
              + quellenblock(eintrag["quellen"])
              + blaettern(None, ziel(weiter, "root", a)))
    html = rahmen(
        f"{WORT} {n} – {a['titel']}", inhalt, "root",
        leiste=seitenleiste(a, nach_abschnitt, globale, "root",
                            aktuell=ueb.slug if ueb else ""),
        krume=f'<a href="index.html">Start</a><span>›</span>{WORT} {n}',
        toc=toc_bauen(inhalt))
    (AUS / f"Abschnitt_{n}.html").write_text(html, encoding="utf-8")


def inhalt_rendern(a, p, nach_abschnitt, globale, zurueck, weiter):
    text = ohne_h1(p.quelle.read_text(encoding="utf-8"))

    if p.renderer == "mc":
        koerper = f"<h1>{p.titel}{p.merker}</h1>" + mc_rendern(text)
    elif p.renderer == "karten":
        koerper = f"<h1>{p.titel}{p.merker}</h1>" + karten_rendern(text)
    elif p.renderer == "uebung":
        koerper = f"<h1>{p.titel}{p.merker}</h1>" + uebungen_rendern(text)
    elif p.renderer == "glossar":
        koerper = f"<h1>{p.titel}</h1>" + glossar_rendern(text)
    else:
        koerper = f"<h1>{p.titel}{p.merker}</h1>" + nachbearbeiten(md2html(text))

    bezug = a or ABSCHNITTE[0]
    leiste = seitenleiste(bezug, nach_abschnitt, globale, "mat", aktuell=p.slug)
    if a:
        krume = (f'<a href="../index.html">Start</a><span>›</span>'
                 f'<a href="../Abschnitt_{a["nr"]}.html">{WORT} {a["nr"]}</a>'
                 f'<span>›</span>{p.titel}')
    else:
        krume = (f'<a href="../index.html">Start</a><span>›</span>'
                 f'Übergreifend<span>›</span>{p.titel}')

    toc = "" if p.renderer in ("karten", "glossar") else toc_bauen(koerper)
    koerper += blaettern(ziel(zurueck, "mat", a), ziel(weiter, "mat", a))
    (AUS_MAT / p.datei).write_text(
        rahmen(p.titel, koerper, "mat", leiste=leiste, krume=krume, toc=toc),
        encoding="utf-8")


def index_rendern(nach_abschnitt, globale):
    k = KONFIG["kurs"]
    zeilen = []
    for a in ABSCHNITTE:
        n = a["nr"]
        anzahl = sum(len(nach_abschnitt[n][t]) for t in FLUSS)
        gattungen = [GATTUNGEN[o][1] for o in GATTUNGEN
                     if nach_abschnitt[n][GATTUNGEN[o][0]]]
        meta = (f"{anzahl} Seiten · " + ", ".join(gattungen)) if anzahl else "in Arbeit"
        gewicht = (f'<span class="abschnitt-gewicht">{a["gewicht"]}</span>'
                   if GEWICHT_ZEIGEN and a.get("gewicht") else "<span></span>")
        zeilen.append(
            f'<a class="abschnitt{" abschnitt--erg" if a.get("ergaenzung") else ""}" '
            f'href="Abschnitt_{n}.html">'
            f'<span class="abschnitt-nr">{n}</span>'
            f'<span class="abschnitt-text"><span class="abschnitt-titel">{a["titel"]}</span>'
            f'<span class="abschnitt-unter">{a["unter"]}</span>'
            f'<span class="abschnitt-meta">{meta}</span></span>'
            f'{gewicht}<span class="abschnitt-pfeil">›</span></a>')

    vorhanden = {t for a in ABSCHNITTE for t in FLUSS if nach_abschnitt[a["nr"]][t]}
    schritte = [
        ("lt", "<li><b>Verstehen</b> – die Lerntexte durcharbeiten. Sie tragen den "
               "Stoff: wer sie versteht, kann die Prüfung bestehen.</li>"),
        ("ex", "<li><b>Vertiefen</b> – Exkurse lesen, wo dich der Hintergrund "
               "interessiert.</li>"),
        ("ka", "<li><b>Abfragen</b> – Karteikarten: Frage lesen, überlegen, "
               "<i>dann erst</i> aufdecken.</li>"),
        ("ue", "<li><b>Anwenden</b> – Übungen lösen.</li>"),
        ("mu", "<li><b>Testen</b> – Selbsttest, Ziel mindestens 80 %.</li>"),
    ]
    lernweg = "".join(t for typ, t in schritte if typ in vorhanden)

    glob = ""
    if globale:
        zeilen_g = "".join(
            f'<a class="material" href="mat/{p.slug}.html">{p.titel}</a>'
            for p in globale)
        glob = (f'<h2 id="uebergreifend">Übergreifend</h2>'
                f'<div class="materialliste">{zeilen_g}</div>')

    pr = KONFIG.get("pruefung", {})
    pruefung = ""
    if pr.get("zeigen"):
        punkte = "".join(f"<li>{x}</li>" for x in pr.get("punkte", []))
        if pr.get("link_url"):
            punkte += (f'<li><a href="{pr["link_url"]}">{pr["link_text"]}</a></li>')
        pruefung = f'<h2 id="pruefung">Zur Prüfung</h2><ul>{punkte}</ul>'

    zahlwort = {1: "einen", 2: "zwei", 3: "drei", 4: "vier", 5: "fünf",
                6: "sechs", 7: "sieben"}.get(len(ABSCHNITTE), str(len(ABSCHNITTE)))

    inhalt = f"""<h1>{k["code"]} – {k["name"]}</h1>
<p>Willkommen. Dieses Lernportal ist nach {zahlwort}
{KONFIG["gliederung"]["wort_plural"].lower()} aufgebaut. Du bestimmst dein Tempo
selbst – die Navigation links zeigt, wo du bist, die Weiter-Knöpfe führen dich durch.</p>
<p class="hinweis">Dieses Portal ist so gebaut, dass du die Prüfung allein damit
bestehen kannst. Wenn dir etwas fehlt oder unverständlich ist, sag es dem Dozenten –
dann fehlt es auch anderen.</p>

<h2 id="lernweg">So arbeitest du jeden {WORT} durch</h2>
<ol class="lernweg"><li><b>Überblick</b> – die Abschnittsseite lesen, Landkarte im
Kopf.</li>{lernweg}</ol>
<p>Nicht jeder {WORT} hat jede Materialart – die Navigation zeigt dir, was da ist.</p>

<h2 id="abschnitte">{KONFIG["gliederung"]["wort_plural"]}</h2>
<div class="abschnittsliste">{"".join(zeilen)}</div>
{glob}
{pruefung}"""
    (AUS / "index.html").write_text(
        rahmen("Start", inhalt, "root"), encoding="utf-8")


def bilder_kopieren():
    anzahl = 0
    for a in ABSCHNITTE:
        q = QUELLE / a["ordner"] / "bilder"
        if not q.is_dir():
            continue
        AUS_BILD.mkdir(parents=True, exist_ok=True)
        for d in q.iterdir():
            if d.is_file():
                shutil.copy2(d, AUS_BILD / d.name)
                anzahl += 1
    return anzahl


# ------------------------------------------------------------------ Steuerung
def bauen():
    global HASH
    if not QUELLE.is_dir():
        sys.exit(f"Quelle nicht gefunden: {QUELLE}")
    if AUS.exists():
        shutil.rmtree(AUS, ignore_errors=True)
    AUS_MAT.mkdir(parents=True, exist_ok=True)

    HASH = assets_bauen()
    nach_abschnitt, globale, alle = erfassen()

    for a in ABSCHNITTE:
        e = nach_abschnitt[a["nr"]]
        inhalte = [p for typ in FLUSS for p in e[typ]]
        hub_rendern(a, e, nach_abschnitt, globale,
                    weiter=inhalte[0] if inhalte else None)
        for i, p in enumerate(inhalte):
            inhalt_rendern(a, p, nach_abschnitt, globale,
                           zurueck=inhalte[i - 1] if i > 0 else "HUB",
                           weiter=inhalte[i + 1] if i < len(inhalte) - 1 else None)

    for p in globale:
        inhalt_rendern(None, p, nach_abschnitt, globale, None, None)

    index_rendern(nach_abschnitt, globale)
    return nach_abschnitt, globale, alle, bilder_kopieren()


if __name__ == "__main__":
    nb, gl, alle, bilder = bauen()
    print(f"Fertig. {len(ABSCHNITTE)} {KONFIG['gliederung']['wort_plural']}, "
          f"{len(alle)} Inhaltsseiten ({len(gl)} übergreifend), {bilder} Bilder.")
    print(f"Assets: HTML/assets/ (Hash {HASH})")
    print(f"Ausgabe: {AUS}")
