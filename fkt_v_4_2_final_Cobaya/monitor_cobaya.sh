#!/usr/bin/env bash
# monitor_cobaya.sh
# Usage: ./monitor_cobaya.sh /path/to/output INTERVAL_SECONDS
OUTDIR=${1:-fktv42_final_run_output}
INTERVAL=${2:-120}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SUMMARIZER="${SCRIPT_DIR}/summarize_mcmc.py"

if [ ! -x "$SUMMARIZER" ]; then
  echo "Error: summarizer script not found or not executable: $SUMMARIZER"
  exit 2
fi

echo "Monitoring Cobaya output in: $OUTDIR (interval: ${INTERVAL}s)"
echo "Press Ctrl-C to stop."

while true; do
  TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
  echo "=== [$TIMESTAMP] Checking chains in $OUTDIR ==="
  python3 "$SUMMARIZER" --chains_dir "$OUTDIR" --warn_rhat 1.01 --warn_neff 10000 2>&1 | sed 's/^/   /'
  echo ""
  sleep "$INTERVAL"
done

