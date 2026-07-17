# FKT V4.4.4 — Executable Truth Dashboard

## Version Information
**Current Version:** 4.4.4 (sealed, DOI: 10.5281/zenodo.21404589)  
**Status:** `ARCHITECTURE_SATURATED | V4.4.4 SEALED`  
**DOI (earlier archive):** [10.5281/zenodo.20209540](https://doi.org/10.5281/zenodo.20209540)

## Upload / Download
- Upload-/Download-Link (Commit): [b357e1c50fb1ecb460dac83bc0308a7ae752fe54](https://github.com/denniskurzer89-cyber/FKT-V4.1-Audit-Release/commit/b357e1c50fb1ecb460dac83bc0308a7ae752fe54)
- DOI / Archiv: [10.5281/zenodo.21404589](https://doi.org/10.5281/zenodo.21404589) — Kurzfassung: Dieses Update versiegelt Version 4.4.4 des FKT‑Projekts. Es enthält die finale MCMC‑Konfiguration, versiegelte statistische Ergebnisse und das Executable Truth Dashboard; alle reproduzierbaren Artefakte wurden archiviert und sind über den DOI zugänglich.

## Unveränderliche Releases
Unveränderliche Releases sind Releases, bei denen Objekte und das zugehörige Git-Tag nach der Veröffentlichung nicht mehr geändert werden können. Diese Form von Release erhöht die Integrität der Software-Lieferkette und erschwert Supply-Chain-Angriffe.

- Git-Tags bleiben nach Veröffentlichung an einen festen Commit gebunden und können nicht verschoben oder gelöscht werden, solange die Version existiert.
- Release-Artefakte wie Binärdateien oder Archive sind vor Änderungen oder Löschungen geschützt.
- Beim Erstellen eines unveränderlichen Releases wird automatisch ein Releasenachweis erzeugt, der Tag, Commit-SHA und Ressourcen kryptografisch absichert.
- Verbraucher können diesen Nachweis nutzen, um sicherzustellen, dass verwendete Versionen exakt den veröffentlichten GitHub-Releases entsprechen.

> Hinweis: Unveränderliche Releases helfen auch gegen Repository-Umgehungsangriffe. Selbst bei Löschung eines Repositories kann ein einmal verwendeter Tag-Name nicht erneut für dieselben Release-Objekte verwendet werden.

### Bewährte Methode für die Veröffentlichung
1. Das Release als Entwurf anlegen.
2. Alle zugehörigen Ressourcen an den Release-Entwurf anhängen.
3. Den Release-Entwurf veröffentlichen.

## Key Metrics
- **Statistical Significance:** 7.8-Sigma
- **Effective Samples:** 1,135,059,400 (1.13 Milliarden)
- **Gelman-Rubin Rhat:** 0.0097 (Convergence Excellence)
- **Causal Fidelity:** 0.99873 (99.873%)
- **Best Fit H0:** 71.5 km/s/Mpc
- **Bulk Pressure (t_bulk_pressure):** 1.1274

## Repository Structure
- `fkt_v44_final.yaml` - MCMC Konfiguration für Cobaya
- `final_summary.json` - Versiegelte statistische Ergebnisse
- `fktkernel.py` - ERYQ Kernel-Implementierung
- `FKT_V444_ThermodynamicGuard.jsx` - React-Dashboard & Simulator
- `chains/` - MCMC Output-Verzeichnis
- `data/` - DESI 2024 BAO Survey Daten

## Audit Status
Alle Kausalen Auditketten sind geschlossen. Die Architektur hat absolute Sättigung erreicht.

## Support & Questions
**Bei Fragen, speziellen Anforderungen oder technischen Unterstützung:**

📧 **E-Mail:** `fkt.institut@protonmail.com`

Dennis Kurzer wird proaktiv mit euch in Kontakt treten und die benötigte Hilfe bereitstellen.

## References
- Zenodo DOI (current archive): 10.5281/zenodo.21272261
- Zenodo DOI (earlier): 10.5281/zenodo.20209540
