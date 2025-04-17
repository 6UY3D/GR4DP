#!/usr/bin/env bash
set -e

mkdir -p plots
dd if=/dev/zero of=plots/plot1.dat bs=1M count=1024
echo "Created a 1GB placeholder plot at plots/plot1.dat"
