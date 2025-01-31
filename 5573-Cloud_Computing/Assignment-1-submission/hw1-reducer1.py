#!/usr/bin/env python3
# imports
from csv import reader
import sys

# sets and dictionaries for 
cities = set()
total_crime = dict()
unique_crimes = dict()

# read in and "reduce" data
for line in reader(sys.stdin):
    city = line[0]
    crime = line[2]
    if city not in cities:
        cities.add(city)
        total_crime[city] = 1
        unique_crimes[city] = set()
    else:
        total_crime[city] += 1
    if crime not in unique_crimes[city]:
        unique_crimes[city].add(crime)

# answer questions
highest_crime_city = max(zip(total_crime.values(), total_crime.keys()))[1]
unique_crimes_str = ', '.join(unique_crimes.get(highest_crime_city))

print(f"Most of the crimes were reported in {highest_crime_city}.")
print(f"Total number of crimes reported in {highest_crime_city} is {total_crime.get(highest_crime_city)}.")
print(f"Crime types reported in {highest_crime_city} are {unique_crimes_str}.")

# EOF
    