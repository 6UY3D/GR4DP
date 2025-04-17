#!/usr/bin/env bash
set -e

echo "Stopping GR4DP node..."
pkill -f "python -m gr4dp.main run" || true
