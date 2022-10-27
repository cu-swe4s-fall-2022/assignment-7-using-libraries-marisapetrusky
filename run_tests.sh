#!/bin/bash

set -e
set -u
set -o

python -m unittest tests/test_data_processor.py
python -m unittest tests/test_plotter.py
