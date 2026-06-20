#!/usr/bin/env python3
"""
summarize_mcmc.py
Enhanced summarizer for Cobaya outputs.
Handles: .csv, .txt, .txt.gz, .csv.gz, chain*.txt, chain*.txt.gz
Automatically detects delimiter, headers, and extracts OmegaX0 and wX columns.
Usage:
  python3 summarize_mcmc.py --chains_dir /path/to/output
  python3 summarize_mcmc.py --csv mcmcflatsamples_CLEAN.csv
"""
import os
import sys
import glob
import gzip
import io
import argparse
import numpy as np
import pandas as pd
import xarray as xr
import arviz as az

COMMON_PATTERNS = ['chain*.txt','*.txt','*.csv','*.txt.gz','*.csv.gz','*.gz']
VARNAMES = ['OmegaX0','wX']

def try_read_table(filepath):
    openf = gzip.open if filepath.endswith('.gz') else open
    with openf(filepath, 'rb') as fbin:
        data = fbin.read()
    try:
        text = data.decode('utf-8')
    except Exception:
        text = data.decode('latin1', errors='ignore')
    for delim in [',','\t',None]:
        for header in [None,0]:
            try:
                if delim is None:
                    df = pd.read_table(io.StringIO(text), header=header, delim_whitespace=True)
                else:
                    df = pd.read_csv(io.StringIO(text), header=header, sep=delim)
                dfnum = df.select_dtypes(include=[np.number])
                if dfnum.shape[1] >= 2 and dfnum.dropna().shape[0] > 0:
                    return df
            except Exception:
                continue
    raise RuntimeError(f'Could not parse table: {filepath}')

def load_chains_from_dir(chains_dir):
    files = []
    for p in COMMON_PATTERNS:
        files += glob.glob(os.path.join(chains_dir, p))
    files = sorted(set(files))
    files = [f for f in files if os.path.isfile(f) and not f.endswith('.log')]
    if not files:
        raise RuntimeError(f'No chain-like files found in {chains_dir} (patterns {COMMON_PATTERNS})')
    arrays = []
    for f in files:
        try:
            df = try_read_table(f)
            dfnum = df.select_dtypes(include=[np.number])
            if dfnum.shape[1] < 2:
                dfnum = df.iloc[:, :2].apply(pd.to_numeric, errors='coerce')
            arr = dfnum.iloc[:, :2].to_numpy(dtype=float)
            arr = arr[~np.isnan(arr).any(axis=1)]
            if arr.size == 0:
                print(f"Warning: no numeric rows in {f}", file=sys.stderr)
                continue
            arrays.append(arr)
        except Exception as e:
            print(f"Warning: skipping {f} (parse error: {e})", file=sys.stderr)
    if not arrays:
        raise RuntimeError('No readable chain arrays found.')
    minlen = min(a.shape[0] for a in arrays)
    arrays = [a[:minlen, :] for a in arrays]
    stacked = np.stack(arrays, axis=0)
    return stacked

def load_single_csv(csv_file):
    df = try_read_table(csv_file)
    dfnum = df.select_dtypes(include=[np.number])
    if dfnum.shape[1] < 2:
        dfnum = df.iloc[:, :2].apply(pd.to_numeric, errors='coerce')
    arr = dfnum.iloc[:, :2].to_numpy(dtype=float)
    arr = arr[~np.isnan(arr).any(axis=1)]
    return arr

def summarize_from_chains_array(chains):
    n_chains, n_samples, n_vars = chains.shape
    if n_vars < 2:
        raise RuntimeError('Chains contain fewer than 2 numeric columns')
    ds = xr.Dataset()
    for i,name in enumerate(VARNAMES[:n_vars]):
        ds[name] = xr.DataArray(chains[:,:,i], dims=('chain','draw'))
    rhat = {name: float(az.rhat(ds[name]).values) for name in ds.data_vars}
    ess = {name: float(az.ess(ds[name]).values) for name in ds.data_vars}
    flat = chains.reshape(-1, n_vars)
    stats = {}
    for i,name in enumerate(VARNAMES[:n_vars]):
        samples = flat[:,i]
        median = float(np.median(samples))
        sigma = float(np.std(samples, ddof=1))
        ci68 = np.percentile(samples, [16,84]).tolist()
        ci95 = np.percentile(samples, [2.5,97.5]).tolist()
        stats[name] = {'median':median, 'sigma':sigma, 'ci68':ci68, 'ci95':ci95}
    return stats, rhat, ess

def summarize_from_single(arr):
    n_samples, n_vars = arr.shape
    if n_vars < 2:
        raise RuntimeError('CSV contains fewer than 2 numeric columns')
    stats = {}
    for i,name in enumerate(VARNAMES[:n_vars]):
        samples = arr[:,i]
        median = float(np.median(samples))
        sigma = float(np.std(samples, ddof=1))
        ci68 = np.percentile(samples, [16,84]).tolist()
        ci95 = np.percentile(samples, [2.5,97.5]).tolist()
        stats[name] = {'median':median, 'sigma':sigma, 'ci68':ci68, 'ci95':ci95}
    ess = {}
    for i,name in enumerate(VARNAMES[:n_vars]):
        try:
            ess_val = float(az.ess(xr.DataArray(arr[:,i], dims=('draw',))).values)
        except Exception:
            ess_val = np.nan
        ess[name] = ess_val
    rhat = {name: np.nan for name in VARNAMES[:n_vars]}
    return stats, rhat, ess

def format_latex_row(stats, ess):
    omega = stats['OmegaX0']
    wx = stats['wX']
    neff_val = int(max(1, int(min(max(1, ess.get('OmegaX0',1)), max(1, ess.get('wX',1)))) ))
    row = f"FKT V4.2 & ${omega['median']:.2f}^{{+{omega['sigma']:.2f}}}_{{-{omega['sigma']:.2f}}}$ & ${wx['median']:.3f}^{{+{wx['sigma']:.3f}}}_{{-{wx['sigma']:.3f}}}$ & $N_{{\\\\rm eff}}\\\\gtrsim {neff_val:d}$ \\\\\\\\"
    return row

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--chains_dir', default=None)
    parser.add_argument('--csv', default='mcmcflatsamples_CLEAN.csv')
    parser.add_argument('--warn_rhat', type=float, default=1.01)
    parser.add_argument('--warn_neff', type=int, default=10000)
    args = parser.parse_args()

    try:
        if args.chains_dir:
            chains = load_chains_from_dir(args.chains_dir)
            stats, rhat, ess = summarize_from_chains_array(chains)
        else:
            arr = load_single_csv(args.csv)
            stats, rhat, ess = summarize_from_single(arr)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)

    print("Parameter summary:")
    for name in VARNAMES:
        s = stats[name]
        print(f" - {name}: median = {s['median']:.6g}, sigma = {s['sigma']:.6g}, 68% CI = [{s['ci68'][0]:.6g}, {s['ci68'][1]:.6g}], 95% CI = [{s['ci95'][0]:.6g}, {s['ci95'][1]:.6g}]")
    print("\nR-hat values (Gelman-Rubin):")
    for k,v in rhat.items():
        print(f" - {k}: {v}")
    print("\nEffective sample sizes (ESS, approx):")
    for k,v in ess.items():
        try:
            print(f" - {k}: {int(v)}")
        except Exception:
            print(f" - {k}: NaN")

    print("\nLaTeX table row:")
    print(format_latex_row(stats, ess))

    warn = False
    for k,v in rhat.items():
        if np.isfinite(v) and v > args.warn_rhat:
            print(f"WARNING: R-hat for {k} = {v:.4g} exceeds threshold {args.warn_rhat}", file=sys.stderr)
            warn = True
    for k,v in ess.items():
        if np.isfinite(v) and v < args.warn_neff:
            print(f"WARNING: ESS for {k} = {int(v)} below threshold {args.warn_neff}", file=sys.stderr)
            warn = True
    if warn:
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    main()
