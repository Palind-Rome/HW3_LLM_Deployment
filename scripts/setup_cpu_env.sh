#!/usr/bin/env bash
set -euo pipefail

python -m pip install -U pip setuptools wheel

python -m pip install \
  torch==2.3.0+cpu \
  torchvision==0.18.0+cpu \
  --index-url https://download.pytorch.org/whl/cpu

python -m pip install -r requirements.txt
python -m pip install fschat --use-pep517
