#!/usr/bin/env python3
# imports
from csv import reader
import sys

# ripped from notes
for line in reader(sys.stdin):
    boro, crime = (line[13].strip(), line[7].strip())
    if not boro or not crime or boro == "BORO_NM":
        continue
    # put formatted data to stdout, so it can be sorted
    print(f"{boro},1,{crime},1")

# EOF
