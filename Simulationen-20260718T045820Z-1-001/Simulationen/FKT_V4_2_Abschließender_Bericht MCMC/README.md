# FKT P2: Fütterer Bulk-Effekt MCMC Validierung

## Installation

1. Verzeichnisstruktur erstellen:
```bash
mkdir -p chains logs plots likelihoods
mv fkt_precision.py likelihoods/
chmod +x *.py setup.sh
```

2. Abhängigkeiten installieren:
```bash
bash setup.sh
```

## Ausführung

```bash
python3 launch_fkt_mcmc.py
```

## Erwartete Ergebnisse

- w_X = -0.90 ± 0.05
- Ω_bulk,0 = 0.73 ± 0.02

## Autor

Dennis Kurzer (FKT V4.2)
DOI: 10.5281/zenodo.17329881
