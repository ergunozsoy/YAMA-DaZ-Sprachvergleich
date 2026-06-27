# Sprachvergleich Deutsch ↔ Türkisch — DaZ-Lernplattform

Interaktive Lehr- und Lernplattform zur **kontrastiven Linguistik Deutsch–Türkisch**
für die **DaZ-Lehramtsausbildung** (ALM 260 · Karşılaştırmalı Dilbilgisi).
Konzept & alle Rechte: **Dr. Ergun Özsoy**, LMU München.

## Inhalt
- **19 Themen** in 3 Modulen (Laut & Schrift · Morphologie · Syntax) — je 5 Blöcke:
  Kontrastiver Befund · Didaktik & DaZ · Interferenzanalyse (n. Thomé) · Korrektur & Förderung · Interkulturalität.
- **19 Themen-Dossiers** als PDF (`themen/<id>.pdf`).
- **4 DaZ-Arbeitsblätter** mit Lösungsschlüssel (`arbeitsblaetter/`).
- **Literatur**-Seite + PDF (`literatur/literatur-de-tr.pdf`): kontrastive Grammatik, Turkologie,
  Phonetik/Graphematik, Interferenz, aktuelle DaZ-Forschung.

Theoretischer Rahmen: **Lernersprache-/Interlanguage-Hypothese** (nicht die widerlegte Kontrastivhypothese);
Fehler werden in *systematisch* vs. *interferenzbedingt* unterschieden.

## Status
| Modul | Themen | Status |
|---|---|---|
| I · Laut & Schrift | Alphabet, Auslautverhärtung, Sprossvokal, Graphem-Kontraste, Vokalharmonie/Umlaut | ✅ fertig |
| II · Morphologie | Genus/Artikel, Plural/Kasus, Pronomen, Komparation, Verben, Zeitformen, Imperativ, Konjunktiv, Passiv, Präpositionen, Adverbien | ✅ fertig |
| III · Syntax | Satzarten, Wortstellung, Relativsatz | ✅ fertig |
| Arbeitsblätter | Auslautverhärtung, Genus/Artikel, Wortstellung, Präpositionen | ✅ fertig |
| Literatur | Auswahlbibliografie (Web + PDF) | ✅ fertig |

## Aufbau / Build
Eine einzige Inhaltsquelle: **`content.py`**.
```
python3 build_index.py   # erzeugt index.html aus index.template.html + content.py
python3 gen_pdfs.py      # erzeugt themen/, arbeitsblaetter/, literatur/ (WeasyPrint)
```
`requirements.txt`: `weasyprint>=60`. Der GitHub-Action-Workflow `.github/workflows/build-pdfs.yml`
baut die PDFs bei jedem Push automatisch neu.

## Veröffentlichen (GitHub Pages)
1. Repository anlegen — empfohlener (URL-sicherer) Name: `yama-sprachvergleich-de-tr`.
2. Dateien hochladen (Inhalt dieses Ordners).
3. *Settings → Pages → Branch: main /(root)* → Speichern.
4. Seite erscheint unter `https://<user>.github.io/<repo>/`.

© Dr. Ergun Özsoy – alle Rechte vorbehalten.
