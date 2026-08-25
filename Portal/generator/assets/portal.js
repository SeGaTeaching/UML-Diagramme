/* ===========================================================================
   Lernportal – Verhalten
   ---------------------------------------------------------------------------
   Eine Datei, sieben abgeschlossene Bausteine. Jeder prüft selbst, ob es auf
   der aktuellen Seite etwas für ihn zu tun gibt.

   Regel für dieses Portal: kein fetch(), kein Modul-Import. Beides scheitert
   unter file://. Datenbestände (z. B. ein späterer Suchindex) werden als
   JS-Datei ausgeliefert, die eine globale Variable setzt – dann bleibt das
   Portal ein Ordner, den man doppelklickt.

     1  Themenumschalter (hell / dunkel)
     2  Lesefortschritt
     3  "Auf dieser Seite" mit Scroll-Mitlauf
     4  Menü-Schublade auf schmalen Fenstern
     5  Karteikarten
     6  Multiple Choice
     7  Glossar: Suche und A–Z
     8  Druck: alle Klappboxen öffnen
   =========================================================================== */

(function () {
  "use strict";

  document.documentElement.classList.add("js");

  /* ------------------------------------------------- 1 Themenumschalter */
  // Drei Zustände: keine Festlegung (Systemvorgabe), "hell", "dunkel".
  (function thema() {
    var wurzel = document.documentElement;
    var schalter = document.querySelector(".themaschalter");

    try {
      var gemerkt = localStorage.getItem("portal-thema");
      if (gemerkt === "hell" || gemerkt === "dunkel") {
        wurzel.setAttribute("data-thema", gemerkt);
      }
    } catch (e) { /* localStorage kann gesperrt sein – dann eben Systemvorgabe */ }

    if (!schalter) return;
    schalter.addEventListener("click", function () {
      var dunkelJetzt = wurzel.getAttribute("data-thema")
        ? wurzel.getAttribute("data-thema") === "dunkel"
        : window.matchMedia("(prefers-color-scheme: dark)").matches;
      var neu = dunkelJetzt ? "hell" : "dunkel";
      wurzel.setAttribute("data-thema", neu);
      try { localStorage.setItem("portal-thema", neu); } catch (e) {}
      schalter.setAttribute("aria-label",
        neu === "dunkel" ? "Zur hellen Ansicht wechseln" : "Zur dunklen Ansicht wechseln");
    });
  })();

  /* --------------------------------------------------- 2 Lesefortschritt */
  (function fortschritt() {
    var balken = document.querySelector(".fortschritt");
    if (!balken) return;

    function messen() {
      var hoehe = document.documentElement.scrollHeight - window.innerHeight;
      var anteil = hoehe > 40 ? (window.scrollY / hoehe) : 0;
      balken.style.width = Math.min(100, Math.max(0, anteil * 100)).toFixed(2) + "%";
    }
    var laeuft = false;
    window.addEventListener("scroll", function () {
      if (laeuft) return;
      laeuft = true;
      requestAnimationFrame(function () { messen(); laeuft = false; });
    }, { passive: true });
    window.addEventListener("resize", messen);
    messen();
  })();

  /* ------------------------------------ 3 "Auf dieser Seite" mit Mitlauf */
  (function inhaltsverzeichnis() {
    var toc = document.querySelector(".toc");
    if (!toc) return;
    var links = [].slice.call(toc.querySelectorAll("a[href^='#']"));
    if (!links.length) return;

    var ziele = links.map(function (a) {
      return document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)));
    });

    function hervorheben() {
      var grenze = window.scrollY + 140;
      var treffer = 0;
      for (var i = 0; i < ziele.length; i++) {
        if (ziele[i] && ziele[i].offsetTop <= grenze) treffer = i;
      }
      // Ganz unten immer den letzten Punkt markieren.
      if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 4) {
        treffer = links.length - 1;
      }
      links.forEach(function (a, i) { a.classList.toggle("hier", i === treffer); });
    }

    var laeuft = false;
    window.addEventListener("scroll", function () {
      if (laeuft) return;
      laeuft = true;
      requestAnimationFrame(function () { hervorheben(); laeuft = false; });
    }, { passive: true });
    hervorheben();
  })();

  /* ------------------------------------------------- 3b Seitenleiste-Gruppen */
  // Beim ersten Besuch ist nur die Gruppe der aktuellen Seite offen (das
  // entscheidet der Generator). Was der Nutzer danach selbst auf- oder
  // zuklappt, bleibt für alle Seiten des Portals erhalten. Die Gruppe mit der
  // aktuellen Seite wird immer geöffnet – sonst stünde man vor einer Leiste,
  // die den eigenen Standort verbirgt.
  (function navgruppen() {
    var nav = document.querySelector(".navseite");
    if (!nav) return;
    var SCHLUESSEL = "portal-nav-gruppen";
    var stand = {};
    try { stand = JSON.parse(localStorage.getItem(SCHLUESSEL) || "{}") || {}; } catch (e) {}

    var gruppen = [].slice.call(nav.querySelectorAll("details.nav-gruppe"));
    gruppen.forEach(function (g) {
      var name = g.dataset.gruppe;
      if (name && Object.prototype.hasOwnProperty.call(stand, name)) g.open = !!stand[name];
      if (g.querySelector("a.hier")) g.open = true;
    });
    // Zuhörer erst nach dem Herstellen des Anfangszustands, sonst schreibt
    // sich die Wiederherstellung selbst zurück.
    gruppen.forEach(function (g) {
      var name = g.dataset.gruppe;
      if (!name) return;
      g.addEventListener("toggle", function () {
        stand[name] = g.open;
        try { localStorage.setItem(SCHLUESSEL, JSON.stringify(stand)); } catch (e) {}
      });
    });

    // Den aktuellen Punkt in den sichtbaren Bereich der Leiste holen – ohne
    // die Seite selbst zu bewegen.
    var hier = nav.querySelector("a.hier");
    if (hier) {
      var leiste = nav.getBoundingClientRect();
      var punkt = hier.getBoundingClientRect();
      if (punkt.top < leiste.top + 8 || punkt.bottom > leiste.bottom - 8) {
        nav.scrollTop += (punkt.top - leiste.top) - nav.clientHeight / 3;
      }
    }
  })();

  /* --------------------------------------------- 4 Menü-Schublade (schmal) */
  (function schublade() {
    var knopf = document.querySelector(".menuknopf");
    var nav = document.querySelector(".navseite");
    var schatten = document.querySelector(".navschatten");
    if (!knopf || !nav) return;

    function zu() {
      nav.classList.remove("offen");
      if (schatten) schatten.classList.remove("sichtbar");
      knopf.setAttribute("aria-expanded", "false");
    }
    knopf.addEventListener("click", function () {
      var offen = nav.classList.toggle("offen");
      if (schatten) schatten.classList.toggle("sichtbar", offen);
      knopf.setAttribute("aria-expanded", offen ? "true" : "false");
    });
    if (schatten) schatten.addEventListener("click", zu);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") zu(); });
    nav.addEventListener("click", function (e) { if (e.target.tagName === "A") zu(); });
  })();

  /* ------------------------------------------------------ 5 Karteikarten */
  // Vorne die Frage. Der Tipp ist sofort erreichbar, die Erklärung erst nach
  // der Antwort – die Reihenfolge ist der eigentliche Sinn einer Karteikarte.
  (function karteikarten() {
    var karten = [].slice.call(document.querySelectorAll(".karte--frage"));
    if (!karten.length) return;

    var zaehler = document.querySelector(".kartenleiste .zaehler");
    var alleKnopf = document.querySelector(".kartenleiste .alle-aufdecken");

    function stand() {
      if (!zaehler) return;
      var auf = karten.filter(function (k) { return k.classList.contains("aufgedeckt"); }).length;
      zaehler.textContent = auf + " von " + karten.length + " aufgedeckt";
    }

    function aufdecken(karte) {
      if (karte.classList.contains("aufgedeckt")) return;
      karte.classList.add("aufgedeckt");
      karte.querySelectorAll("details[data-gesperrt]").forEach(function (d) {
        d.removeAttribute("data-gesperrt");
      });
      stand();
    }

    karten.forEach(function (karte) {
      var knopf = karte.querySelector(".karte-aufdecken");
      if (knopf) knopf.addEventListener("click", function () { aufdecken(karte); });

      // Gesperrte Klappbox bleibt zu, bis die Antwort da ist.
      karte.querySelectorAll("details").forEach(function (d) {
        d.addEventListener("click", function (e) {
          if (d.hasAttribute("data-gesperrt")) e.preventDefault();
        });
      });
    });

    if (alleKnopf) {
      alleKnopf.addEventListener("click", function () {
        var allesAuf = karten.every(function (k) { return k.classList.contains("aufgedeckt"); });
        if (allesAuf) {
          karten.forEach(function (k) {
            k.classList.remove("aufgedeckt");
            k.querySelectorAll(".karte-fuss details").forEach(function (d) {
              d.open = false;
              if (d.dataset.rolle === "erklaerung") d.setAttribute("data-gesperrt", "");
            });
          });
          alleKnopf.textContent = "Alle aufdecken";
        } else {
          karten.forEach(aufdecken);
          alleKnopf.textContent = "Alle zuklappen";
        }
        stand();
      });
    }
    stand();
  })();

  /* ---------------------------------------------------- 6 Multiple Choice */
  (function multiplechoice() {
    var fragen = [].slice.call(document.querySelectorAll(".mc"));
    if (!fragen.length) return;
    var anzeige = document.querySelector(".mc-leiste .punktestand");
    var reset = document.querySelector(".mc-leiste .neu");

    function stand() {
      if (!anzeige) return;
      var beantwortet = 0, richtig = 0;
      fragen.forEach(function (f) {
        if (!f.classList.contains("beantwortet")) return;
        beantwortet++;
        var gewaehlt = f.querySelector("input:checked");
        if (gewaehlt && gewaehlt.value === f.dataset.richtig) richtig++;
      });
      var text = beantwortet + " von " + fragen.length + " beantwortet · " + richtig + " richtig";
      if (beantwortet) {
        var quote = Math.round(richtig / beantwortet * 100);
        text += " (" + quote + " %)";
        if (beantwortet === fragen.length) {
          text += quote >= 80 ? " · Ziel erreicht" : " · Ziel sind 80 %";
        }
      }
      anzeige.textContent = text;
    }

    fragen.forEach(function (f) {
      f.querySelectorAll("input[type=radio]").forEach(function (r) {
        r.addEventListener("change", function () {
          if (f.classList.contains("beantwortet")) return;
          f.classList.add("beantwortet");
          f.querySelectorAll(".mc-option").forEach(function (o) {
            var eingabe = o.querySelector("input");
            if (eingabe.value === f.dataset.richtig) o.classList.add("richtig");
            else if (eingabe.checked) o.classList.add("falsch");
            eingabe.disabled = true;
          });
          stand();
        });
      });
    });

    if (reset) reset.addEventListener("click", function () { location.reload(); });
    stand();
  })();

  /* --------------------------------------------------- 7 Glossar: Suche */
  (function glossar() {
    var feld = document.querySelector(".suchfeld");
    if (!feld) return;
    var eintraege = [].slice.call(document.querySelectorAll(".eintrag"));
    var gruppen = [].slice.call(document.querySelectorAll(".buchstabe"));
    var treffer = document.querySelector(".treffer");
    var gesamt = eintraege.length;

    // Suchtext einmal vorbereiten statt bei jedem Tastendruck neu einsammeln.
    eintraege.forEach(function (e) {
      e.dataset.suchtext = (e.textContent || "").toLowerCase();
    });

    function filtern() {
      var q = feld.value.trim().toLowerCase();
      var sichtbar = 0;
      eintraege.forEach(function (e) {
        var passt = !q || e.dataset.suchtext.indexOf(q) !== -1;
        e.hidden = !passt;
        if (passt) sichtbar++;
      });
      // Buchstabengruppen ohne sichtbaren Eintrag ausblenden.
      gruppen.forEach(function (g) {
        var hat = false, n = g.nextElementSibling;
        while (n && !n.classList.contains("buchstabe")) {
          if (n.classList.contains("eintrag") && !n.hidden) { hat = true; break; }
          n = n.nextElementSibling;
        }
        g.hidden = !hat;
      });
      if (treffer) {
        treffer.textContent = q
          ? sichtbar + " von " + gesamt + " Begriffen"
          : gesamt + " Begriffe";
      }
    }

    feld.addEventListener("input", filtern);
    feld.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { feld.value = ""; filtern(); }
    });
    // Tastenkürzel "/" springt ins Suchfeld – Konvention aus Doku-Portalen.
    document.addEventListener("keydown", function (e) {
      if (e.key === "/" && document.activeElement !== feld) {
        e.preventDefault();
        feld.focus();
      }
    });
    filtern();
  })();

  /* ------------------------------------------------------------ 8 Druck */
  // CSS kann ein <details> nicht aufklappen. Vor dem Druck alles öffnen,
  // danach den Zustand zurücksetzen.
  (function drucken() {
    var vorher = null;
    window.addEventListener("beforeprint", function () {
      var alle = [].slice.call(document.querySelectorAll("details"));
      vorher = alle.map(function (d) { return d.open; });
      alle.forEach(function (d) { d.open = true; });
    });
    window.addEventListener("afterprint", function () {
      if (!vorher) return;
      [].slice.call(document.querySelectorAll("details")).forEach(function (d, i) {
        d.open = vorher[i];
      });
      vorher = null;
    });
  })();
})();
