#!/usr/bin/env python3
# imports
from csv import reader
import sys

# ripped from notes
for line in reader(sys.stdin):
    crime, date = (line[7].strip(), line[5].strip())
    if not crime or not date:
        continue
    # put formatted data to stdout, so it can be sorted
    print(f"{crime},{date}")

# EOF
