#!/usr/bin/env python3
# imports
from csv import reader
import sys
from datetime import datetime

# sets and dictionaries
dangerousWeapons_crime = dict()
dangerousWeapons_string = "DANGEROUS WEAPONS reported per month: \n"

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# read in and "reduce" data
for line in reader(sys.stdin):
    crime = line[0]
    date_str = line[1]

    try:
        month = int(date_str.split('/')[0])  # Extract the month
        crime_month_key = month
        crime_month_display = months.get(crime_month_key, "Invalid month")
    except ValueError:
        continue  # Skip lines with invalid dates

    if crime == "DANGEROUS WEAPONS":
        if crime_month_key not in dangerousWeapons_crime:
            dangerousWeapons_crime[crime_month_key] = {"count": 1, "display": crime_month_display}
        else:
            dangerousWeapons_crime[crime_month_key]["count"] += 1




# answer question
for month_key in sorted(dangerousWeapons_crime.keys()):
    dangerousWeapons_string += f'{dangerousWeapons_crime[month_key]["display"]}: {dangerousWeapons_crime[month_key]["count"]}\n'

print(f"{dangerousWeapons_string}")
# EOF
    