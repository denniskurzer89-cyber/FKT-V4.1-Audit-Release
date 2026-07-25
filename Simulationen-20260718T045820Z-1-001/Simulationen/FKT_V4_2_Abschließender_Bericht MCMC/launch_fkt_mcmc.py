#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

def check_deps():
    deps = ['cobaya', 'numpy', 'scipy', 'matplotlib', 'getdist']
    missing = []
    for d in deps:
        try:
            __import__(d)
        except:
            missing.append(d)
    if missing:
        print(f"❌ Fehlend: {', '.join(missing)}")
        print(f"   pip install {' '.join(missing)}")
        return False
    print("✓ Abhängigkeiten OK")
    return True

def main():
    print("="*60)
    print("FKT P2 MCMC - RUN 2")
    print("="*60)
    
    for d in ['chains', 'logs', 'plots', 'results', 'likelihoods']:
        Path(d).mkdir(exist_ok=True)
    
    if not check_deps():
        exit(1)
    
    print("\nStarte MCMC...")
    subprocess.run(['cobaya-run', 'cobayafktbulk.yaml'])
    
    print("\n✓ FERTIG")

if __name__ == '__main__':
    main()
