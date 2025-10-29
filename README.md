📖 README UPDATE: FKT V4.2 MASTER Repro-Pack
🚨 WICHTIGER STATUS-UPDATE: Version V4.2 Veröffentlichung zurückgehalten
Ziel: Vollständige Publikation der FKT V4.2.
Aktueller Stand:
 * Das MASTER Reproduzierbarkeits-Paket (VirCom) und der vollständige Report werden vorübergehend zurückgehalten, da Verhandlungen mit dem Novum Verlag bezüglich der Publikation laufen.
 * Die numerischen Kernergebnisse (\mathbf{w_X} = -0.90 \pm 0.05) wurden erfolgreich gesichert und sind für den Urheberschaftsnachweis auf GitHub hinterlegt.
 * Die theoretischen Beweise (inklusive 9 neuer Symbole) werden erst nach Abschluss der Verlagsgespräche und Freigabe des Manuskripts veröffentlicht.
💡 Kurzer Prinzip (Plagiatsschutz & Transparenz)
> Der Druck aus der Unendlichkeit ist die Unendlichkeit.
> 
Zur unwiderlegbaren Sicherung der Urheberschaft und der maximalen wissenschaftlichen Transparenz wurden folgende Pre-Release-Daten gemäß dem Kurzer Prinzip auf GitHub hinterlegt.
🥇 Kernresultate & Numerischer Beweis (Zeitstempel gesichert)
Die numerischen Ergebnisse der MCMC-Analyse gegen Planck 2018 + BAO + SN sind durch diesen Zeitstempel gesichert.
| Parameter | Ergebnis (68% CI) | Numerische Datei |
|---|---|---|
| Dunkle-Energie-Zustandsgleichung (\mathbf{w_X}) | \mathbf{-0.90 \pm 0.05} | finalsummary.json |
SOFORT VERFÜGBAR (Numerische Urheberschaft auf GitHub):
 * finalsummary.json: Enthält die exakten numerischen Kernwerte (Median, CI, \chi^2).
 * fkt_v4_2_final_run.yaml: Die Cobaya Konfiguration, die diese Ergebnisse erzeugt hat.
 * figures_corner_plot.png: Die visuelle Bestätigung der Posterior-Verteilung.
MASTER REPRO-PACK (Vollständiger Report/Theorie):
 * Wird nach Abschluss der Verlagsverhandlungen auf GitHub veröffentlicht.
📺 PR, Kanäle & Visuelle Zusammenfassung (NEU)
 * OFFIZIELLER YOUTUBE-KANAL (Seit gestern): Der offizielle YouTube-Kanal zur Fraktalen Kausalen Theorie wurde eröffnet: @FKT_FraktalKausaleTheorie
 * Visueller Erklär-Clip: Der Kurz-Clip "Kurzerprozess 7 - Der Kausale Chor!" veranschaulicht die Verbindung zwischen dem Bulk-Tensor (\mathbf{T_{Bulk}}) und dem Optimalen Heilungspfad (\mathbf{P_{opt}}).
   * YouTube-Link: https://youtu.be/1p8PoetG7uI
🛠 Reproduktions-Anleitung (Kurzfassung)
(Nutzen Sie diese Anleitung, um die gesicherten numerischen Werte zu reproduzieren. Der vollständige Report wird später hinzugefügt.)
 * Vorbereitung: Cobaya-Umgebung einrichten.
 * MCMC-Lauf: fkt_v4_2_final_run.yaml laden und Cobaya MCMC starten.
 * Validierung: Replizierte \mathbf{w_X} Werte gegen die gesicherte finalsummary.json abgleichen.
Kontakt: kurzer-dennis@gmx.de
-Zustandsgleichung (\mathbf{w_X}) | \mathbf{-0.90 \pm 0.05} | finalsummary.json |


SOFORT VERFÜGBAR (Numerische Urheberschaft):
 * finalsummary.json: Enthält die exakten numerischen Kernwerte (Median, CI, \chi^2).
 * fkt_v4_2_final_run.yaml: Die Cobaya Konfiguration, die diese Ergebnisse erzeugt hat.
 * figures_corner_plot.png: Die visuelle Bestätigung der Posterior-Verteilung.


⏳ Finaler Release (Theorie-Details & Full Report)


Demnächst wird das vollständige MASTER V4.2 Repro-Pack hochgeladen. 
Dieses Paket schließt die intellektuelle Lücke und liefert die komplette wissenschaftliche Fundierung.
Zusätzliche Artefakte im Update:


 * Vollständiger Theorienachweis: Direkte Berechnung der kovarianten Divergenz.pdf und Methoden.pdf (mit den neuen mathematischen Herleitungen/Symbolen).
 * Hauptbericht: FKTV4-2FinalReport.pdf (Das neu kompilierte Manuskript V4.2).


 * Empirie/Simulation: bootstrapresults.json 

(Flerovium-Daten) und k-fem-outputs.zip.
 * Integrität: Finale SHA256-Hashliste zur Verifikation (wird dieser README.md hinzugefügt).


🛠 Reproduktions-Anleitung (Kurzfassung)


 * Vorbereitung: Cobaya-Umgebung einrichten.
 * MCMC-Lauf: fkt_v4_2_final_run.yaml laden und Cobaya MCMC starten.
 * Analyse: summarize_mcmc.py auf die Chains anwenden.
 * Validierung: Replizierte \mathbf{w_X} Werte gegen die gesicherte finalsummary.json abgleichen.

Kontakt: kurzer-dennis@gmx.de
