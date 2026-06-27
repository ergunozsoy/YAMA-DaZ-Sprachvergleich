# -*- coding: utf-8 -*-
"""
Einzige Inhaltsquelle für Plattform + PDFs.
Sprachvergleich Deutsch–Türkisch · DaZ · Dr. Ergun Özsoy, LMU München (ALM 260).
Didaktisches Modell: 5 Blöcke je Thema (Lernersprache-/Interlanguage-Hypothese).
"""

BLOCKNAMES = ["Kontrastiver Befund","Didaktik & DaZ-Relevanz","Interferenzanalyse",
              "Korrektur & Förderung","Interkulturalität & Mehrsprachigkeit als Ressource"]

# Strukturbaum (Reihenfolge = Navigation). status: "ready" | "draft"
MODULES = [
 {"id":"m1","name":"Modul I · Laut & Schrift","topics":[
   {"id":"alphabet","t":"Alphabet & Aussprache","s":"ready","desc":"DE: ein Buchstabe – mehrere Laute; TR: weitgehend 1:1."},
   {"id":"auslaut","t":"Auslautverhärtung","s":"ready","desc":"Finale Entstimmung – gleicher Laut, andere Schreibregel."},
   {"id":"sprossv","t":"Konsonantenhäufung & Sprossvokal","s":"ready","desc":"*Sıport: Vokaleinschub als L1-Phonotaktik."},
   {"id":"graphem","t":"Graphem-Kontraste (v/w · z/s · c/ç · ı/i)","s":"ready","desc":"Gleiche Buchstaben, andere Lautwerte."},
   {"id":"vokalh","t":"Vokalharmonie & Umlaut","s":"ready","desc":"TR-Vokalharmonie vs. DE-Umlaut als Morphemsignal."},
 ]},
 {"id":"m2","name":"Modul II · Morphologie","topics":[
   {"id":"genus","t":"Nomen: Genus & Artikel","s":"ready","desc":"der/die/das & Bestimmtheit – TR ohne Genus/Artikel."},
   {"id":"plural","t":"Nomen: Plural & Kasus","s":"ready","desc":"9 Pluralklassen vs. -lAr; 4 vs. 6 Kasus."},
   {"id":"pronomen","t":"Pronomen","s":"ready","desc":"Flexion vs. Possessivsuffix; Pro-Drop."},
   {"id":"kompar","t":"Komparation (Adjektive)","s":"ready","desc":"-er/am -sten vs. daha/en; „als“ = Ablativ."},
   {"id":"verben","t":"Verben","s":"ready","desc":"Trennbarkeit & Verbklammer vs. Suffixkette."},
   {"id":"zeit","t":"Zeitformen","s":"ready","desc":"Tempussystem & Evidentialität (-miş)."},
   {"id":"imperativ","t":"Imperativ","s":"ready","desc":"du/ihr/Sie vs. reichere TR-Höflichkeit."},
   {"id":"konjunktiv","t":"Konjunktiv","s":"ready","desc":"K I/K II vs. -se/-sa-Konditional."},
   {"id":"passiv","t":"Passiv","s":"ready","desc":"werden-Passiv vs. -Il-/-In--Suffix."},
   {"id":"praep","t":"Präpositionen vs. Kasussuffixe","s":"ready","desc":"DE-Präposition+Kasus ↔ TR-Suffix."},
   {"id":"adverb","t":"Adverbien","s":"ready","desc":"Adjektiv=Adverb; TeKaMoLo-Stellung."},
 ]},
 {"id":"m3","name":"Modul III · Syntax","topics":[
   {"id":"satzart","t":"Satzarten","s":"ready","desc":"Verbstellung vs. mi-Partikel."},
   {"id":"wortstell","t":"Wortstellung (SOV vs. V2)","s":"ready","desc":"TR verbfinal vs. DE Verbzweit/Klammer."},
   {"id":"relativ","t":"Relativsatz","s":"ready","desc":"DE-Relativpronomen vs. TR-Partizipialattribut."},
 ]},
]

# Hilfsfunktionen zum kompakten Schreiben der Blöcke ------------------------
def T(rows, head=("Kategorie","Deutsch","Türkisch")):
    h="".join(f"<th>{x}</th>" for x in head)
    body=""
    for r in rows:
        tds=f'<td>{r[0]}</td><td class="de">{r[1]}</td><td class="tr">{r[2]}</td>'
        body+=f"<tr>{tds}</tr>"
    return f"<table><tr>{h}</tr>{body}</table>"

def ITAB(rows):  # Interferenztabelle: (fehler, ziel, quelle, kategorie)
    body=""
    for f,z,q,k in rows:
        body+=(f'<tr><td><span class="err">{f}</span></td>'
               f'<td><span class="ok">{z}</span></td><td>{q}</td>'
               f'<td><span class="tag cat">{k}</span></td></tr>')
    return ('<table><tr><th>Lernerform</th><th>Zielform</th><th>Quelle (L1)</th>'
            f'<th>Kategorie</th></tr>{body}</table>')

def NOTE(s): return f'<p class="note">{s}</p>'
def P(s): return f"<p>{s}</p>"

# === DETAIL: 5 Blöcke je Thema ============================================
DETAIL = {}

DETAIL["alphabet"]=dict(
 modul="Modul I · Laut & Schrift", titel="Alphabet & Aussprache",
 lead="Das Türkische ist nahezu lautgetreu (ein Buchstabe ≈ ein Laut). Das Deutsche ist es nicht – derselbe Buchstabe kann mehrere Laute tragen. Genau diese Mehrdeutigkeit muss explizit gemacht werden.",
 blocks=[
  T([("Schrift-Laut-Bezug","ein Graphem → oft mehrere Laute","weitgehend 1 Graphem = 1 Laut"),
     ("Sonderzeichen","ä ö ü ß","ç ş ğ ı (kein ß, kein q/w/x)"),
     ("Beispiele","<span class='ex'>v</span>=[f], <span class='ex'>w</span>=[v], <span class='ex'>z</span>=[ts], <span class='ex'>ch</span>=[x]/[ç], <span class='ex'>ei</span>=[aɪ]","<span class='ex'>c</span>=[dʒ], <span class='ex'>ç</span>=[tʃ], <span class='ex'>ş</span>=[ʃ], <span class='ex'>j</span>=[ʒ]")],
    head=("Merkmal","Deutsch","Türkisch"))
  +NOTE("Kernpunkt: TR-Lernende erwarten Lautgetreue – die deutschen Sonderfälle wirken wie „Ausnahmen“ und müssen als geschlossene Liste vermittelt werden."),
  P("Aussprache <i>und</i> Lesetechnik sind betroffen: Wer ⟨v, w, z, ch, ei, eu⟩ lautgetreu liest, verliest sich systematisch. Früh im DaZ-/Alphabetisierungsprozess zu sichern."),
  ITAB([("[ˈvaːtɐ] für Vater","[ˈfaːtɐ]","⟨v⟩ im TR = [v]","Graphem-Phonem"),
        ("[zaɪt] für Zeit","[tsaɪt]","⟨z⟩ im TR = [z]","Graphem-Phonem"),
        ("[ˈwasɐ] für Wasser","[ˈvasɐ]","⟨w⟩ im TR = [v]","Graphem-Phonem")]),
  P("Laut-Buchstaben-Tabelle der Abweichungen; <b>Minimalpaare</b> (Vater/Wasser, Zeit/seit); Lautgebärden; lautes Lesen mit markierten Sonderfällen ⟨v w z s sch ch ei eu äu st sp⟩."),
  P("Die lautgetreue TR-Orthographie ist ein <b>Lesevorsprung</b> – das Prinzip „Buchstabe→Laut“ beherrschen die Lernenden bereits. Aufgabe: nur die deutschen Abweichungen ergänzen, nicht das Lesen neu lernen."),
 ])

# auslaut + genus (aus dem Pilot, unverändert) -----------------------------
DETAIL["auslaut"]=dict(
 modul="Modul I · Laut & Schrift", titel="Auslautverhärtung",
 lead="Beide Sprachen entstimmen Plosive am Wortende – aber sie verschriften das Ergebnis unterschiedlich. Genau dort entsteht ein orthographischer Interferenzfehler.",
 blocks=[
  T([("Phonolog. Prozess","Entstimmung der Obstruenten <span class='ex'>/b d g/→[p t k]</span>","Entstimmung der Plosive <span class='ex'>/b d c g/→[p t ç k]</span>"),
     ("gesprochen","<span class='ex'>Tag</span> [taːk], <span class='ex'>Hund</span> [hʊnt], <span class='ex'>lieb</span> [liːp]","<span class='ex'>kitap</span> [kitap], <span class='ex'>renk</span> [reŋk]"),
     ("Verschriftung","<b>morphophonemisch</b>: Graphem bleibt (<span class='ex'>Tag·e</span>)","<b>oberflächenphonemisch</b>: man schreibt das Gehörte (<span class='ex'>kitap</span>, aber <span class='ex'>kitabı</span>)")],
    head=("Merkmal","Deutsch","Türkisch"))
  +NOTE("Kernpunkt: Den <i>Laut</i> kennen TR-Lernende bereits – nur die <i>Schreibkonvention</i> ist neu."),
  P("Doppelt relevant: für die <b>Rechtschreibung</b> (richtiges Endgraphem) und das <b>Leseverstehen</b> (Wortverwandtschaften: <span class='ex'>Tag–täglich–Tage</span>). Eine früh zu sichernde Rechtschreibstrategie."),
  ITAB([("Hunt","Hund","phonemische TR-Orthographie","Graphem-Phonem"),
        ("Tak","Tag","finale Entstimmung verschriftet","Graphem-Phonem"),
        ("lip","lieb","L1-Konvention auf L2 übertragen","interferenzbedingt")]),
  P("<b>Verlängerungsprobe.</b> Das Wort verlängern, bis der Auslaut stimmhaft in die nächste Silbe rückt:")
  +"<ul class='li'><li><span class='ex'>Hund → Hun<b>d</b>e</span> → <span class='ok'>d</span></li><li><span class='ex'>Tag → Ta<b>g</b>e</span> → <span class='ok'>g</span></li><li><span class='ex'>lieb → lie<b>b</b>er</span> → <span class='ok'>b</span></li></ul>"
  +P("Parallele zum TR explizit machen: <span class='ex'>kitap–kitabı</span> zeigt denselben Wechsel – nur dort wird er <i>geschrieben</i>."),
  P("Die L1 ist hier ein <b>Vorsprung</b>: Die finale Entstimmung existiert im Türkischen bereits (<span class='ex'>kitap/kitabı, renk/rengi</span>). Reframing: nicht „ein neuer Laut“, sondern „eine andere <i>Schreibregel</i> für denselben Laut“."),
 ])

DETAIL["sprossv"]=dict(
 modul="Modul I · Laut & Schrift", titel="Konsonantenhäufung & Sprossvokal",
 lead="Das Deutsche erlaubt komplexe Konsonantencluster, das Türkische meidet sie – besonders am Wortanfang. Lernende fügen einen Sprossvokal (Epenthese) ein.",
 blocks=[
  T([("Silbenstruktur","komplexe Cluster erlaubt: <span class='ex'>Strumpf, Herbst, Sprung</span>","Anfangscluster gemieden; CV-Präferenz"),
     ("Strategie bei Clustern","–","<b>Sprossvokal</b>/Epenthese: <span class='ex'>tren→tiren, spor→sıpor</span>")],
    head=("Merkmal","Deutsch","Türkisch"))
  +NOTE("Die TR-Phonotaktik ist nicht „falsch“, sondern systematisch – sie bricht Cluster durch Vokaleinschub auf."),
  P("Betrifft <b>Aussprache und Schreibung</b> gleichermaßen. Cluster-Wahrnehmung und -Produktion brauchen gezieltes Training (An- und Auslaut)."),
  ITAB([("Sıport / Sport mit Vokal","Sport","Vokaleinschub vor /sp/","Phonotaktik/Epenthese"),
        ("Kıraft","Kraft","Aufbrechen von /kr/","interferenzbedingt"),
        ("Herbst → Herbs","Herbst","Auslaut-Cluster vereinfacht","Konsonantentilgung")]),
  P("Silbensegmentierung, langsames Sprechen mit allmählicher Verdichtung, <b>Cluster-Minimalpaare</b> (Stadt/Satt), Sprech-Schreib-Kopplung."),
  P("Den Lernenden bewusst machen: Der Sprossvokal ist eine <i>Regel der L1</i>, kein Defizit. Sichtbar gemachte Kontraste (TR-Silbe vs. DE-Cluster) entlasten und erklären den eigenen „Akzent“."),
 ])

DETAIL["graphem"]=dict(
 modul="Modul I · Laut & Schrift", titel="Graphem-Kontraste (v/w · z/s · c/ç · ı/i)",
 lead="Viele Buchstaben existieren in beiden Alphabeten – tragen aber andere Lautwerte. Das ist eine besonders zähe, oft unbewusste Interferenzquelle.",
 blocks=[
  T([("⟨v⟩","[f] – <span class='ex'>Vater</span>","[v] – <span class='ex'>ev</span>"),
     ("⟨w⟩","[v] – <span class='ex'>Wasser</span>","existiert nicht"),
     ("⟨z⟩","[ts] – <span class='ex'>Zeit</span>","[z] – <span class='ex'>zaman</span>"),
     ("⟨c⟩ / ⟨ç⟩","[k]/[ts] (Fremdw.)","[dʒ] / [tʃ] – <span class='ex'>cam / çay</span>"),
     ("⟨ı⟩ vs ⟨i⟩","kein ⟨ı⟩; ⟨i⟩=[ɪ]/[iː]","[ɯ] vs [i] – <span class='ex'>kız / kiz</span>")],
    head=("Graphem","Deutsch","Türkisch")),
  P("Weil die Buchstaben <i>vertraut</i> aussehen, wird der falsche Lautwert oft unbemerkt übertragen – beim Lesen wie beim Schreiben."),
  ITAB([("[v]ater","[f]ater","⟨v⟩ im TR = [v]","Graphem-Phonem"),
        ("[z]eit","[ts]eit","⟨z⟩ im TR = [z]","Graphem-Phonem"),
        ("⟨w⟩ als [w]","[v]","⟨w⟩ existiert im TR nicht","Graphem-Phonem")]),
  P("Graphem-Phonem-Kontrasttabelle; <b>farbige Markierung</b> der „falschen Freunde“; Minimalpaare (Vater/Wasser, Zeit/seit); Diktat mit Fokus auf ⟨v w z⟩."),
  P("Leitidee bewusst machen: <b>Ein Buchstabe hat keinen universellen Lautwert.</b> Die TR-Werte sind nicht falsch – sie gelten nur in der L1. Sprachvergleich macht das System sichtbar."),
 ])

DETAIL["vokalh"]=dict(
 modul="Modul I · Laut & Schrift", titel="Vokalharmonie & Umlaut",
 lead="Im Türkischen richten sich Suffixvokale nach dem Stamm (Vokalharmonie). Im Deutschen signalisiert der Umlaut Morphologie (Plural, Komparativ, Diminutiv). Zwei ganz verschiedene Prinzipien.",
 blocks=[
  T([("Phänomen","<b>Umlaut</b> a→ä, o→ö, u→ü – morphologisch","<b>Vokalharmonie</b> – phonologisch"),
     ("Beispiel","<span class='ex'>Vater→Väter, alt→älter</span>","<span class='ex'>ev-ler / kitap-lar</span> (e/a; i/ı/ü/u)"),
     ("ö/ü","Phoneme vorhanden","Phoneme vorhanden (<span class='ex'>göz, gül</span>)")],
    head=("Merkmal","Deutsch","Türkisch")),
  P("Doppelter Befund: ö/ü existieren im TR – ein <b>Aussprachevorsprung</b>. Der Umlaut dagegen ist im DE ein <i>Bedeutungssignal</i> (Plural/Komparativ) und muss als solches gelernt werden."),
  ITAB([("die Mutter (Pl.)","die Mütter","Umlaut als Pluralsignal nicht erkannt","Morphologie"),
        ("alter (Komp.)","älter","Umlaut beim Komparativ fehlt","Morphologie"),
        ("Umlautpunkte weggelassen","ä/ö/ü","Diakritikum als unwichtig behandelt","Graphembestand")]),
  P("Umlaut als <b>Bedeutungsträger</b> sichtbar machen (Tochter→Töchter, lang→länger); Umlautschreibung sichern; ö/ü-Aussprache aus dem TR positiv nutzen."),
  P("Mehrsprachigkeit als Ressource doppelt: TR-ö/ü erleichtern die Aussprache; und der Kontrast „Harmonie (phonologisch) vs. Umlaut (morphologisch)“ schärft das grammatische Bewusstsein."),
 ])

DETAIL["genus"]=dict(
 modul="Modul II · Morphologie (Nomen)", titel="Genus & Artikel",
 lead="Das Deutsche markiert Genus (der/die/das) und Bestimmtheit am Artikel – das Türkische kennt weder grammatisches Genus noch Artikel. Eine der hartnäckigsten DaZ-Fehlerquellen.",
 blocks=[
  T([("Genus","3 Genera, lexikalisch fest: <span class='ex'>der Tisch, die Lampe, das Buch</span>","kein Genus – ein Wort: <span class='ex'>o</span>"),
     ("best. Artikel","<span class='ex'>der/die/das</span>","keiner; Bestimmtheit über <b>Akkusativ</b> (<span class='ex'>-i</span>) & Wortstellung"),
     ("unbest. Artikel","<span class='ex'>ein/eine/ein</span>","optional <span class='ex'>bir</span>"),
     ("Bestimmtheit am Objekt","<span class='ex'>Ich lese <b>das</b> Buch</span>","<span class='ex'>Kitab<b>ı</b> okuyorum</span> (Akk. markiert das bestimmte Objekt)")],
    head=("Kategorie","Deutsch","Türkisch"))
  +NOTE("Funktional ist Bestimmtheit in <i>beiden</i> Sprachen da – nur die Kodierung unterscheidet sich: Artikel (DE) vs. Kasus/Wortstellung (TR)."),
  P("Genus ist nicht ableitbar und muss <b>mit jedem Nomen mitgelernt</b> werden (Nomen + Artikel als Einheit). Da die L1 die Kategorie nicht besitzt, bleiben Genus-/Artikelfehler oft lange bestehen – ein <b>diagnostischer Dauerbrenner</b>."),
  ITAB([("Ich sehe Mann.","Ich sehe einen Mann.","kein obligat. Artikel in L1","Auslassung"),
        ("der Mädchen","das Mädchen","kein Genus → Zuweisung zufällig","Genuszuweisung"),
        ("ein Brot (gemeint best.)","das Brot","Bestimmtheit in L1 über Kasus","Bestimmtheit")]),
  P("<b>1. Nomen-Artikel-Kopplung</b> – Vokabeln nie ohne Artikel; Farbcode <span style='color:#1565c0'>der</span>/<span style='color:#c62828'>die</span>/<span style='color:#2e7d32'>das</span>.")
  +"<p><b>2. Genus-Heuristiken:</b></p><ul class='li'><li><span class='ex'>-ung,-heit,-keit,-schaft,-tion,-e</span> → meist <span class='ok'>die</span></li><li><span class='ex'>-chen,-lein,-ment,-um</span> → <span class='ok'>das</span></li><li>Agens auf <span class='ex'>-er</span>, Tages-/Jahreszeiten → <span class='ok'>der</span></li></ul>"
  +P("<b>3. Bestimmtheit kontrastiv</b> – TR <span class='ex'>-i</span>/<span class='ex'>bir</span> gezielt auf DE <span class='ex'>das</span>/<span class='ex'>ein</span> abbilden."),
  P("Auch ohne Artikel/Genus <b>grammatikalisiert das Türkische Bestimmtheit</b> – über das Akkusativsuffix <span class='ex'>-i</span> und die Wortstellung. Die Lernenden besitzen das <i>Konzept</i> „bestimmt vs. unbestimmt“ also bereits, nur anders kodiert. Der Artikel ist dann die deutsche <i>Bauform</i> einer längst beherrschten Funktion."),
 ])

DETAIL["plural"]=dict(
 modul="Modul II · Morphologie (Nomen)", titel="Plural & Kasus",
 lead="Der deutsche Plural ist unvorhersehbar (neun Klassen), der türkische denkbar einfach (ein Suffix). Bei den Kasus ist es umgekehrt: vier (DE) gegen sechs (TR), an ganz anderer Stelle markiert.",
 blocks=[
  T([("Plural","9 Klassen: <span class='ex'>-e, -er, -(e)n, -s, ∅</span> (± Umlaut), unvorhersehbar","ein Suffix <span class='ex'>-lAr</span> (Harmonie: -ler/-lar)"),
     ("Plural nach Zahl","obligatorisch: <span class='ex'>zwei Kinder</span>","kein Plural: <span class='ex'>iki çocuk</span>"),
     ("Kasus","4: Nom · Akk · Dat · Gen – am <b>Artikel</b> markiert","6: Nom ∅, Akk -i, Dat -e, Lok -de, Abl -den, Gen -in – am <b>Nomen</b>")],
    head=("Merkmal","Deutsch","Türkisch")),
  P("Plural: nicht ableitbar → mit Artikel mitlernen. Kasus: DE markiert <i>verteilt</i> (Artikel/Adjektiv), TR <i>agglutinierend</i> am Nomen. Beides braucht je eine eigene Strategie."),
  ITAB([("zwei Kind","zwei Kinder","im TR kein Plural nach Numeral","interferenzbedingt"),
        ("die Autos→die Auten","die Autos","Pluralklasse übergeneralisiert","Morphologie/systematisch"),
        ("mit das Auto","mit dem Auto","Kasus am Artikel nicht realisiert","Kasusrektion")]),
  P("Pluralklassen in Gruppen mit Artikel üben; Regel <b>„nach Zahlwort steht im DE der Plural“</b>; Kasustabellen DE (4) ↔ TR (6) nebeneinander; Wechsel Artikelflexion ↔ Suffix bewusst machen."),
  P("Das TR-System ist hochtransparent (ein Pluralsuffix, klare Kasussuffixe). Diese <b>analytische Klarheit</b> als Brücke nutzen, um die deutsche „verteilte“ Markierung am Artikel zu erklären."),
 ])

DETAIL["pronomen"]=dict(
 modul="Modul II · Morphologie", titel="Pronomen",
 lead="Beide Sprachen haben Personalpronomen – doch das Türkische drückt Besitz per Suffix aus und lässt das Subjekt weg (Pro-Drop). Das überträgt sich gern ins Deutsche.",
 blocks=[
  T([("Personalpron.","flektiert: <span class='ex'>ich / mich / mir</span>","<span class='ex'>ben / sen / o</span>"),
     ("Possessiv","eigenes Wort: <span class='ex'>mein Buch</span>","Suffix (+ optional Pron.): <span class='ex'>(benim) kitab-ım</span>"),
     ("Subjekt","obligatorisch (auch <span class='ex'>es</span>)","weglassbar – <b>Pro-Drop</b>: <span class='ex'>geliyorum</span>")],
    head=("Merkmal","Deutsch","Türkisch")),
  P("Zwei Strukturunterschiede mit hoher Fehlerlast: das obligatorische deutsche Subjekt und der Possessivartikel als eigenständiges Wort."),
  ITAB([("Komme morgen.","Ich komme morgen.","Pro-Drop der L1 übertragen","Auslassung/interferenzbedingt"),
        ("benim mein Buch","mein Buch","Possessiv-Doppelung (Suffix-Logik)","Redundanz"),
        ("Regnet.","Es regnet.","kein formales Subjekt in L1","Auslassung")]),
  P("Obligatorisches Subjekt im DE (inkl. <span class='ex'>es</span>) gezielt üben; Possessivartikel-Tabelle (mein/dein/sein …); Reflexivpronomen (mich/dich/sich)."),
  P("Pro-Drop ist ein <b>System­merkmal</b> des Türkischen, kein Flüchtigkeitsfehler. Bewusst kontrastieren: „Im Deutschen trägt das Subjekt die Personeninfo, im Türkischen das Verbsuffix.“"),
 ])

DETAIL["kompar"]=dict(
 modul="Modul II · Morphologie", titel="Komparation (Adjektive)",
 lead="Das Deutsche steigert synthetisch (Endung am Wort), das Türkische analytisch (mit Partikeln daha/en). Auch das „als“ funktioniert anders – im Türkischen über den Ablativ.",
 blocks=[
  T([("Komparativ","Endung <span class='ex'>-er</span>: schön→schöner","Partikel <span class='ex'>daha</span>: daha güzel"),
     ("Superlativ","<span class='ex'>am schönsten / der schönste</span>","Partikel <span class='ex'>en</span>: en güzel"),
     ("Vergleich „als“","<span class='ex'>größer <b>als</b> ich</span>","Ablativ <span class='ex'>-den</span>: <span class='ex'>ben<b>den</b> büyük</span>")],
    head=("Stufe","Deutsch","Türkisch")),
  P("Die synthetische deutsche Steigerung (Endung) und der Anschluss mit <span class='ex'>als</span> sind die zentralen Lernpunkte; unregelmäßige Formen (gut/besser, viel/mehr) kommen hinzu."),
  ITAB([("mehr schön","schöner","analytisch nach TR <span class='ex'>daha güzel</span>","interferenzbedingt"),
        ("größer wie ich","größer als ich","als/wie-Verwechslung","Vergleichspartikel"),
        ("am meisten schön","am schönsten","Superlativ analytisch gebildet","Morphologie")]),
  P("Muster <span class='ex'>-er … als</span> und <span class='ex'>am -sten</span> automatisieren; unregelmäßige Reihen (gut–besser–am besten); <i>als</i> nach Komparativ fest verankern."),
  P("Das TR-System (daha/en) ist analytisch-transparent. Den Kontrast „TR: extra Wort vs. DE: Endung am Adjektiv“ explizit machen – so wird die deutsche Synthese als bloß <i>andere Bauform</i> erkennbar."),
 ])

DETAIL["verben"]=dict(
 modul="Modul II · Morphologie", titel="Verben",
 lead="Das deutsche Verb verteilt seine Information auf Hilfsverben, Vorsilben und eine Satzklammer. Das türkische Verb bündelt alles in einer Suffixkette am Wortende. Daraus folgen typische Stellungsfehler.",
 blocks=[
  T([("Bauprinzip","analytisch: Hilfsverb + Partizip/Infinitiv","agglutinierend: <span class='ex'>gel-mi-yor-um</span> (Stamm+Neg+Tempus+Person)"),
     ("Trennbare Verben","<span class='ex'>aufstehen → ich stehe … auf</span> (Klammer)","keine trennbaren Verben"),
     ("Verbposition","V2 / Satzende (Klammer)","stets am <b>Satzende</b>")],
    head=("Merkmal","Deutsch","Türkisch")),
  P("Trennbare Verben + Verbklammer und die Hilfsverbwahl (haben/sein) sind die großen Baustellen. Das TR-Verb ist hochregelmäßig – die deutsche Verteilung wirkt dagegen „zerrissen“."),
  ITAB([("Ich aufstehe um 7.","Ich stehe um 7 auf.","keine trennbaren Verben in L1","Verbklammer/Wortstellung"),
        ("Ich habe gegangen.","Ich bin gegangen.","Hilfsverbwahl (Bewegung→sein)","Hilfsverb"),
        ("du gehst → du geht","du gehst","Kongruenzendung","systematisch")]),
  P("Trennbare Verben mit der <b>Satzklammer</b> visualisieren (steht … auf); haben/sein-Regeln (Bewegung/Zustandswechsel → sein); Konjugationsmuster sichern."),
  P("Die TR-Suffixkette ist maximal transparent – alle Information sitzt am Verb. Genau diese Erwartung erklärt die Fehler im DE. Kontrast „gebündelt (TR) vs. geklammert (DE)“ schafft Verständnis statt Frust."),
 ])

DETAIL["zeit"]=dict(
 modul="Modul II · Morphologie", titel="Zeitformen",
 lead="Die Tempora bilden nur scheinbar 1:1 aufeinander ab. Das Türkische grammatikalisiert zusätzlich Evidentialität (-miş) – eine Kategorie, die das Deutsche gar nicht hat.",
 blocks=[
  T([("Vergangenheit","Perfekt (mündl.) / Präteritum (schriftl.)","<span class='ex'>-di</span> (bezeugt) vs. <span class='ex'>-miş</span> (nicht bezeugt)"),
     ("Gegenwart","Präsens (auch futurisch)","<span class='ex'>-iyor</span> (Verlauf) / Aorist <span class='ex'>-r</span> (geniş zaman)"),
     ("Zukunft","Futur I (oft Präsens+Adverb)","<span class='ex'>-ecek</span>")],
    head=("Bereich","Deutsch","Türkisch")),
  P("Lernschwer ist nicht die Form, sondern der <b>Gebrauch</b>: Perfekt vs. Präteritum, „geniş zaman“ → Präsens, und die fehlende deutsche Evidentialität."),
  ITAB([("Ich ging gestern (mündl.)","Ich bin … gegangen","Präteritum statt mündl. Perfekt","Tempusgebrauch"),
        ("Ich gehe morgen → kein Futur","ok / Ich werde gehen","Präsens für Zukunft (wie -ecek?)","Tempus"),
        ("*er kam angeblich → -miş","er sei gekommen / soll …","Evidentialität nicht kodierbar","lexikalische Lücke")]),
  P("Perfekt als <b>mündliche</b> Vergangenheit etablieren; Tempusgebrauch funktional statt 1:1; Evidentialität (-miş) im DE lexikalisch wiedergeben (angeblich, soll, sei)."),
  P("Die TR-Evidentialität (-di/-miş) ist ein <b>Ausdrucksreichtum</b>, kein Hindernis. Sie schärft den Blick dafür, wie das Deutsche dieselbe Bedeutung mit Wörtern (statt Suffixen) leistet."),
 ])

DETAIL["imperativ"]=dict(
 modul="Modul II · Morphologie", titel="Imperativ",
 lead="Beide Sprachen befehlen und bitten – das Türkische verfügt aber über mehr Höflichkeitsstufen und sogar einen Imperativ der 3. Person. Im Deutschen sind die Formen an die Anrede gebunden.",
 blocks=[
  T([("du-Form","<span class='ex'>Komm(e)! Arbeite!</span>","<span class='ex'>gel!</span>"),
     ("ihr / höflich","<span class='ex'>Kommt!</span> · <span class='ex'>Kommen Sie!</span> (+ Pron.)","<span class='ex'>gelin / geliniz</span>"),
     ("3. Person","nur umschrieben (<span class='ex'>er soll kommen</span>)","echter Imperativ: <span class='ex'>gelsin</span>")],
    head=("Form","Deutsch","Türkisch")),
  P("Die drei deutschen Formen (du/ihr/Sie) und die Pflicht-Inversion bei <span class='ex'>Sie</span> sind zentral; die reiche TR-Höflichkeit erzeugt Wahlunsicherheit."),
  ITAB([("Komme Sie!","Kommen Sie!","Sie-Form + Pronomen + Inversion","Formenbildung"),
        ("Arbeit!","Arbeite!","obligatorisches -e nach Stamm auf -t","Morphologie"),
        ("Du komm!","Komm!","Pronomen bei du/ihr entfällt","Syntax")]),
  P("du/ihr/Sie-Formen kontrastiv; bei <span class='ex'>Sie</span>: Verb + <i>Sie</i> + Rest; -e-Regeln (atme!, arbeite!); Höflichkeit über bitte/Konjunktiv ergänzen."),
  P("Der TR-Imperativ der 3. Person (<span class='ex'>gelsin</span>) entspricht dem deutschen „er soll …“; die TR-Höflichkeitskultur lässt sich als Anlass nutzen, deutsche Höflichkeitsmittel (Sie, Konjunktiv, bitte) bewusst zu machen."),
 ])

DETAIL["konjunktiv"]=dict(
 modul="Modul II · Morphologie", titel="Konjunktiv",
 lead="Der deutsche Konjunktiv hat zwei Aufgaben: Irrealis/Höflichkeit (K II) und indirekte Rede (K I). Das Türkische deckt das Irreale mit dem Konditional -se/-sa ab – einen Modus der indirekten Rede kennt es nicht.",
 blocks=[
  T([("Irrealis","K II: <span class='ex'>käme, hätte, würde … kommen</span>","Konditional <span class='ex'>-se/-sa</span>: <span class='ex'>gelse</span>"),
     ("Höflichkeit","K II: <span class='ex'>Ich hätte gern …</span>","Optativ/Umschreibung"),
     ("Indirekte Rede","K I: <span class='ex'>er komme, er habe</span>","kein Modus – einfache Einbettung")],
    head=("Funktion","Deutsch","Türkisch")),
  P("K II (Irrealis + Höflichkeit) ist für DaZ am wichtigsten; K I (indirekte Rede) ist bildungs­sprachlich und im TR ohne direktes Äquivalent."),
  ITAB([("Wenn ich reich bin, …(irreal)","Wenn ich reich wäre, …","Irrealis nicht markiert (TR -se)","Modus"),
        ("Ich will einen Kaffee (höflich)","Ich hätte gern einen Kaffee","K II als Höflichkeit unbekannt","Pragmatik"),
        ("er sagt, er kommt","er sagt, er komme","indirekte Rede ohne K I","Modus/indirekte Rede")]),
  P("K II zuerst (würde-Form + wäre/hätte) für Irrealis und Höflichkeit; K I als bildungssprachliches Mittel der indirekten Rede; Konditionalsätze Typ II/III."),
  P("Das TR-Konditional <span class='ex'>-se/-sa</span> deckt die K-II-<i>Funktion</i> bereits ab – darauf lässt sich aufbauen. Der Konjunktiv I der indirekten Rede ist dagegen eine echte deutsche Besonderheit, die explizit eingeführt werden muss."),
 ])

DETAIL["passiv"]=dict(
 modul="Modul II · Morphologie", titel="Passiv",
 lead="Das deutsche Passiv ist analytisch (werden + Partizip II), das türkische synthetisch (ein Suffix am Verb). Außerdem unterscheidet das Deutsche Vorgangs- und Zustandspassiv.",
 blocks=[
  T([("Bildung","<span class='ex'>werden</span> + Partizip II: <span class='ex'>wird geschrieben</span>","Suffix <span class='ex'>-Il-/-In-</span>: <span class='ex'>yaz-ıl-ır</span>"),
     ("Zustandspassiv","<span class='ex'>sein</span> + Part. II: <span class='ex'>ist geöffnet</span>","meist über Resultativ/Adjektiv"),
     ("Agens","<span class='ex'>von</span>+Dativ / <span class='ex'>durch</span>+Akk","<span class='ex'>tarafından</span> (oft weggelassen)")],
    head=("Merkmal","Deutsch","Türkisch")),
  P("Zwei Lernpunkte: die <b>werden/sein</b>-Unterscheidung (Vorgang vs. Zustand) und die Agens-Markierung mit <span class='ex'>von/durch</span>. Das Objekt des Aktivs wird zum Subjekt im Nominativ."),
  ITAB([("Der Brief ist geschrieben (Vorgang)","… wird geschrieben","Vorgang/Zustand vermischt","Hilfsverb"),
        ("wird von durch mir","von mir","Agens-Präposition","Kasusrektion"),
        ("Der Brief schreibt.","… wird geschrieben","Passivbildung fehlt","Diathese")]),
  P("<span class='ex'>werden</span>+Partizip II sichern; Vorgangs- vs. Zustandspassiv (wird geöffnet / ist geöffnet); Agens <span class='ex'>von</span>+Dativ; Umformung Aktiv↔Passiv üben."),
  P("Das synthetische TR-Passiv (<span class='ex'>-ıl-</span> direkt am Verb) ist transparent. Der Kontrast „ein Suffix (TR) vs. Hilfsverb + Partizip (DE)“ macht die deutsche Konstruktion durchschaubar."),
 ])

DETAIL["praep"]=dict(
 modul="Modul II · Morphologie", titel="Präpositionen vs. Kasussuffixe",
 lead="Wo das Deutsche eine Präposition vor das Nomen stellt (mit Kasusrektion), hängt das Türkische ein Kasussuffix an. Lokalrelationen werden so an entgegengesetzten Enden des Wortes kodiert.",
 blocks=[
  T([("Position","<b>vor</b> dem Nomen: <span class='ex'>in dem Haus</span>","<b>Suffix</b> am Nomen: <span class='ex'>ev-de</span>"),
     ("Lokal/Direktional","Wechselpräp. an/in/auf + Akk(wohin)/Dat(wo)","Lokativ -de / Dativ -e / Ablativ -den"),
     ("Rektion","Präp. fordert festen Kasus (mit+Dat, für+Akk)","Suffix trägt die Relation selbst")],
    head=("Merkmal","Deutsch","Türkisch")),
  P("Doppelte Hürde: die <b>Wahl</b> der Präposition und ihre <b>Kasusrektion</b> – besonders bei Wechselpräpositionen (wohin? Akkusativ / wo? Dativ)."),
  ITAB([("in das Haus (Ort gemeint)","in dem Haus","wohin/wo nicht getrennt","Kasusrektion"),
        ("mit der Auto","mit dem Auto","feste Rektion (mit+Dativ)","Kasusrektion"),
        ("nach Hause → zu Hause","zu Hause (Ort)","Bedeutungs-/Rektionswahl","Präpositionswahl")]),
  P("Präpositionen in Kasusgruppen lernen (Akk-/Dativ-/Wechsel-/Genitivgruppe); Wechselpräp.: <i>wohin?→Akk</i>, <i>wo?→Dat</i>; TR-Suffix ↔ DE-Präposition gegenüberstellen."),
  P("Das TR-Kasussystem (Lokativ/Dativ/Ablativ) ist klar und konsequent. Diese Bedeutungen sind die <b>Brücke</b> zu in/auf/an/aus – die Lernenden kennen die Relationen, sie müssen sie nur „nach vorn“ (zur Präposition) umkodieren."),
 ])

DETAIL["adverb"]=dict(
 modul="Modul II · Morphologie", titel="Adverbien",
 lead="Im Deutschen ist das Adverb oft formgleich mit dem Adjektiv und unflektiert; seine Stellung folgt einer eigenen Logik (TeKaMoLo). Das Türkische bildet manche Adverbien mit -CA.",
 blocks=[
  T([("Form","oft = Adjektiv, <b>unflektiert</b>: <span class='ex'>schnell</span>","teils Suffix <span class='ex'>-CA</span> (güzel-ce), teils = Adjektiv"),
     ("Stellung","relativ frei, Tendenz <span class='ex'>Te-Ka-Mo-Lo</span>","vor dem Verb / Satzende-orientiert")],
    head=("Merkmal","Deutsch","Türkisch")),
  P("Zwei Punkte: das Adverb bleibt <b>unflektiert</b>, und die Reihung mehrerer Angaben folgt <span class='ex'>temporal–kausal–modal–lokal</span>."),
  ITAB([("Er fährt schnelle.","Er fährt schnell.","Adverb fälschlich flektiert","Morphologie"),
        ("Ich gehe ins Kino heute.","Ich gehe heute ins Kino.","Te-Ka-Mo-Lo verletzt","Wortstellung"),
        ("gut → er spielt gut (vs. guter)","gut","Adjektiv/Adverb-Abgrenzung","systematisch")]),
  P("Adverb = unflektiert sichern; <b>TeKaMoLo</b> als Stellungsfaustregel; Abgrenzung adverbialer vs. attributiver Gebrauch (er fährt schnell / das schnelle Auto)."),
  P("Der TR-Marker <span class='ex'>-CA</span> macht Adverbialität teils sichtbar; im Deutschen fehlt diese Markierung – das bewusst zu kontrastieren erklärt, warum „schnell“ unverändert bleibt."),
 ])

DETAIL["satzart"]=dict(
 modul="Modul III · Syntax", titel="Satzarten",
 lead="Das Deutsche signalisiert den Satztyp über die Stellung des finiten Verbs, das Türkische über Partikeln und Intonation – das Verb bleibt dabei am Satzende.",
 blocks=[
  T([("Aussage","Verb an 2. Stelle (V2)","Verb am Ende"),
     ("Ja/Nein-Frage","Verb voran: <span class='ex'>Kommst du?</span>","Partikel <span class='ex'>mi</span>: <span class='ex'>Geliyor mu?</span>"),
     ("W-Frage","W-Wort + V2: <span class='ex'>Wann kommst du?</span>","Fragewort + Verb final")],
    head=("Satztyp","Deutsch","Türkisch")),
  P("Die Fragebildung ist der Knackpunkt: Deutsch verschiebt das Verb (Inversion), Türkisch hängt die Partikel <span class='ex'>mi</span> an – das Verb bleibt stehen."),
  ITAB([("Du kommst? (nur Intonation)","Kommst du?","mi-Logik: keine Inversion","Fragebildung"),
        ("Wann du kommst?","Wann kommst du?","W-Wort ohne V2","Wortstellung"),
        ("Geliyor mu → … mu am Ende","Kommst du?","Partikeltransfer","Syntax")]),
  P("Inversion bei Ja/Nein-Fragen (finites Verb voran); W-Wort + finites Verb an 2. Stelle; Intonationsfragen vom Standard abgrenzen."),
  P("Die TR-Partikel <span class='ex'>mi</span> und die deutsche Inversion erfüllen <i>dieselbe Funktion</i> (Frage markieren) mit verschiedenen Mitteln. Diese Äquivalenz explizit zu machen nimmt der Inversion das Willkürliche."),
 ])

DETAIL["wortstell"]=dict(
 modul="Modul III · Syntax", titel="Wortstellung (SOV vs. V2)",
 lead="Das Türkische ist konsequent verbfinal (SOV). Das Deutsche ist „gemischt“: Verbzweit im Hauptsatz mit Satzklammer, verbfinal im Nebensatz. Dieser Wechsel ist eine der größten syntaktischen Hürden.",
 blocks=[
  T([("Grundabfolge","S–V–O / Verbzweit (V2)","S–O–V – konsequent verbfinal"),
     ("Hauptsatz","finites Verb an 2. Stelle, Klammer: <span class='ex'>Ich habe … gekauft</span>","Verb am Ende: <span class='ex'>… aldım</span>"),
     ("Nebensatz","verbfinal: <span class='ex'>…, weil er kommt</span>","ebenfalls verbfinal (Partizip/Konverb)")],
    head=("Merkmal","Deutsch","Türkisch"))
  +NOTE("Beleg aus dem Kursmaterial: deutscher Hauptsatz <b>ÖYN</b> (Subjekt–Verb–Objekt), türkischer Satz <b>ÖNY</b> (Subjekt–Objekt–Verb)."),
  P("Lernschwer ist nicht eine einzelne Regel, sondern der <b>Wechsel</b>: V2 im Hauptsatz, Klammer, dann wieder verbfinal im Nebensatz."),
  ITAB([("Ich morgen nach Hause gehe.","Ich gehe morgen nach Hause.","SOV der L1 (Verb final)","Wortstellung/V2"),
        ("Ich habe gekauft ein Buch.","Ich habe ein Buch gekauft.","Klammer nicht geschlossen","Verbklammer"),
        ("…, weil er kommt nicht.","…, weil er nicht kommt.","Nebensatz-Verbstellung","Nebensatz")]),
  P("V2-Regel (finites Verb an 2. Stelle) markieren; <b>Satzklammer</b> visualisieren; Nebensatz = Verb ans Ende; Umstell- und Klammerübungen."),
  P("Das TR-SOV ist ein <b>einheitlicher</b> Parameter – verlässlich verbfinal. Genau diese Einheitlichkeit macht den deutschen Wechsel (V2 vs. verbfinal) erklärungsbedürftig; bewusst kontrastiert wird er lernbar."),
 ])

DETAIL["relativ"]=dict(
 modul="Modul III · Syntax", titel="Relativsatz",
 lead="Das Deutsche stellt den Relativsatz mit Relativpronomen hinter das Nomen. Das Türkische bildet stattdessen ein vorangestelltes Partizipialattribut – ganz ohne Relativpronomen.",
 blocks=[
  T([("Bauform","nachgestellter Satz + Relativpronomen","vorangestelltes <b>Partizip</b>, kein Pronomen"),
     ("Beispiel","der Mann, <span class='ex'>der</span> liest","<span class='ex'>oku-yan</span> adam (lesender Mann)"),
     ("„den ich sah“","der Mann, <span class='ex'>den</span> ich sah","<span class='ex'>gör-düğüm</span> adam")],
    head=("Merkmal","Deutsch","Türkisch")),
  P("Die deutsche Lösung verlangt <b>Relativpronomen</b> (Genus/Numerus vom Bezugswort, Kasus aus der Funktion im Relativsatz) und Verbendstellung – im TR gibt es nichts Vergleichbares."),
  ITAB([("der Frau, der ich helfe","der Frau, der ich helfe? → der","Kasus im Relativsatz","Relativpronomen-Kasus"),
        ("das Mann, der …","der Mann, der …","Genuskongruenz","Kongruenz"),
        ("Partizip statt Relativsatz / Vermeidung","der Mann, der liest","prä-nominales Muster der L1","Vermeidung/Transfer")]),
  P("Relativpronomen-Tabelle (der/die/das, dessen/deren, dem/denen); Kasus nach Funktion im Nebensatz bestimmen; Verb ans Ende; vom TR-Partizip zum deutschen Relativsatz „übersetzen“."),
  P("Das TR-Partizipialattribut (<span class='ex'>okuyan</span>, <span class='ex'>okuduğum</span>) ist das funktionale Äquivalent. Es als Ausgangspunkt zu nehmen („dieselbe Bedeutung, andere Bauform: nachgestellter Satz mit Pronomen“) nutzt vorhandene Kompetenz."),
 ])

# === Arbeitsblätter (DaZ) ==================================================
SHEETS = [
 {"id":"ab_auslaut","t":"Auslautverhärtung","lvl":"A2–B1 / Alphabetisierung",
  "desc":"Verlängern, Fehler korrigieren, kontrastive Brücke + Lösungen.",
  "pdf":"arbeitsblaetter/ab_auslautverhaertung.pdf"},
 {"id":"ab_genus","t":"Genus, Artikel & Bestimmtheit","lvl":"A2–B1",
  "desc":"Genus-Heuristik, Artikel-Korrektur, TR↔DE-Bestimmtheit + Lösungen.",
  "pdf":"arbeitsblaetter/ab_genus-artikel.pdf"},
 {"id":"ab_wortstell","t":"Wortstellung: V2 & Satzklammer","lvl":"A2–B1",
  "desc":"Verb an 2. Stelle, Klammer schließen, Nebensatz verbfinal + Lösungen.",
  "pdf":"arbeitsblaetter/ab_wortstellung.pdf"},
 {"id":"ab_praep","t":"Präpositionen & Kasus (Wechselpräp.)","lvl":"A2–B1",
  "desc":"wohin?/wo?, Suffix↔Präposition, Rektion + Lösungen.",
  "pdf":"arbeitsblaetter/ab_praepositionen.pdf"},
]
# Verknüpfung Thema → Arbeitsblatt (für Download-Button im Themenfenster)
SHEET_FOR = {"auslaut":SHEETS[0]["pdf"],"genus":SHEETS[1]["pdf"],
             "wortstell":SHEETS[2]["pdf"],"praep":SHEETS[3]["pdf"]}

# === Literatur ============================================================
# proj=True → im Projekt vorhanden; cur=True → aktuell (2020+)
LIT = {
 "Kontrastive Grammatik & Sprachvergleich DE–TR": [
  dict(a="Balcı, Tahir", y="o. J.", t="Grundzüge der türkisch-deutschen kontrastiven Grammatik",
       q="Çukurova Üniversitesi (Substantiv, Adjektiv, Verben, Artikel, Interferenzfehler)", proj=True),
  dict(a="Balcı, Tahir", y="1998", t="Abriss der türkisch-deutschen kontrastiven Grammatik",
       q="Diyarbakır: Üniversite (Lehrbuch DaF)"),
  dict(a="Cimilli, N. / Liebe-Harkort, K.", y="1976", t="Sprachvergleich Türkisch–Deutsch",
       q="Düsseldorf: Schwann"),
  dict(a="Rehbein, Jochen", y="1995", t="Grammatik kontrastiv",
       q="Jahrbuch Deutsch als Fremdsprache 21, 265–292"),
  dict(a="Hoffmann, L. / Naumovich, O. / Selmani, L.", y="2018", t="Funktionale Grammatik und Sprachvergleich",
       q="Berlin: Erich Schmidt Verlag"),
 ],
 "Türkische Grammatik & Turkologie": [
  dict(a="Johanson, Lars / Csató, Éva Á. (Hg.)", y="1998", t="The Turkic Languages",
       q="London/New York: Routledge", proj=True),
  dict(a="Johanson, Lars", y="2002", t="Structural Factors in Turkic Language Contacts",
       q="London: Curzon / Routledge", proj=True),
  dict(a="Ersen-Rasch, Margarete I.", y="2001/2012", t="Türkische Grammatik für Anfänger und Fortgeschrittene",
       q="Ismaning: Hueber", proj=True),
  dict(a="Göksel, Aslı / Kerslake, Celia", y="2005", t="Turkish. A Comprehensive Grammar",
       q="London: Routledge"),
 ],
 "Phonetik / Graphematik / Schriftspracherwerb": [
  dict(a="Buchberger (KALiPho)", y="o. J.", t="Schriftsprachliche Interferenzen der Erstsprache Türkisch im DaZ-Erwerb",
       q="Univ. Kiel, Arbeitsberichte (Thomé-Fehlerkategorien)", proj=True),
  dict(a="Özen, Erhan", y="1985", t="Untersuchungen zu einer kontrastiven Phonetik Türkisch–Deutsch",
       q="Hamburg: Buske"),
  dict(a="Adıyaman, A. / Bayrak, A.", y="2020", t="Kontrastive Analyse der phonetischen Interferenzfehler von DaF-Studenten mit türkischer Muttersprache",
       q="Akademik Sosyal Araştırmalar Dergisi 8(104), 412–432", cur=True),
 ],
 "Interferenz, Fehleranalyse & Determination": [
  dict(a="Hansen, Björn", y="1995", t="Die deutschen Artikel und ihre Wiedergabe im Türkischen",
       q="Arbeiten zur Mehrsprachigkeit 53"),
  dict(a="Selmani, Lirim", y="2011", t="Determination im Sprachvergleich Deutsch–Türkisch–Albanisch",
       q="in: Hoffmann/Ekinci-Kocks (Hg.), Sprachdidaktik in mehrsprachigen Lerngruppen, 40–52"),
  dict(a="Grießhaber, Wilhelm", y="1999", t="Die relationierende Prozedur. Lokale Präpositionen und ihre Verwendung durch türkische Deutschlerner",
       q="Münster: Waxmann"),
  dict(a="Uslu, Zeki", y="o. J.", t="Almanca ve Türkçe Önermelerde Nedensellik İşlevi",
       q="Doktora-Arbeit (Kausalität DE–TR)", proj=True),
 ],
 "DaZ, Mehrsprachigkeit & Didaktik (aktuell)": [
  dict(a="Koch, Nikolas / Riehl, Claudia Maria", y="2024", t="Migrationslinguistik. Eine Einführung",
       q="Tübingen: Narr Francke Attempto", cur=True),
  dict(a="Tan, Nimet", y="2023", t="Mehrsprachigkeit und Nachhaltigkeitsaspekte in der Deutschlehrkräfteausbildung",
       q="(dt./türk.); sowie: Sprachvergleiche mittels KI in der Hochschullehre", cur=True),
  dict(a="Selmani, Lirim", y="2024", t="Das Passiv im Deutschen und Albanischen. Formenbildung und Funktion",
       q="Deutsche Sprache 2/2024, 139–170", cur=True),
  dict(a="Ekinci-Kocks, Y. / Hoffmann, L. u. a. (Hg.)", y="2013", t="Migration – Mehrsprachigkeit – Bildung",
       q="Tübingen: Stauffenburg"),
 ],
}
LIT_INTRO = ("Auswahlbibliografie zum Sprachvergleich Deutsch–Türkisch und zur DaZ-Didaktik. "
  "Mit ● markierte Titel liegen als Referenzmaterial im Projekt vor; mit ✦ markierte sind "
  "aktuelle Arbeiten (2020+). Die Liste dient als Referenz – Konzept und Inhalt der Plattform "
  "stammen von Dr. Ergun Özsoy.")

def app_json():
    return {"modules":MODULES,"detail":DETAIL,"sheets":SHEETS,
            "sheetFor":SHEET_FOR,"blocknames":BLOCKNAMES,"lit":LIT,"litIntro":LIT_INTRO}
