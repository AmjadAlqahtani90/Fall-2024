from csv import reader
from pyspark import SparkContext
from datetime import datetime

# ----- Copied from assignment pdf -----------
sc = SparkContext(appName="NYC_Crime_Analysis")
sc.setLogLevel("ERROR")

# Read input data from HDFS to create an RDD.
data = sc.textFile("hdfs://group8-1:54310/hw1-input/")

# Use csv.reader to split each line of file into a list of elements
# this will automatically split the csv data correctly.
splitdata = data.mapPartitions(lambda x: reader(x))

# use filter to select only those rows in which crime type is not blank.
filtered_data = splitdata.filter(lambda x: x[7])

# ---------- GROUP 8 CODE ---------------------------------------------------------
# Where is most of the crime happening in New York? And the total number of crimes in that location.
location_and_crime = filtered_data.map(lambda x: (x[13], 1)) # use location 13 to match BORO_NM in CSV

# Reduce by key for location count
crime_counts = location_and_crime.reduceByKey(lambda a, b: a + b)

# Find the location with the most crimes
highest_crime_location = crime_counts.takeOrdered(1, key=lambda x: -x[1])

print("The location with the most crimes: {}. number of crimes: {}".format(highest_crime_location[0][0], highest_crime_location[0][1]))

# ---------------------------------------------------------------------
# Top 3 crimes reported in the month of July

# Function to filter data for July crimes
def july(date):
    try:
        dt_date = datetime.strptime(date, "%m/%d/%Y")
        return dt_date.month == 7
    except Exception :
        return False

# Only get july crimes
july_crimes = filtered_data.filter(lambda x: july(x[5]))

# Get crime type
july_crime_type = july_crimes.map(lambda x: (x[7], 1))

# Count the number of times
july_crime_counts = july_crime_type.reduceByKey(lambda a, b: a + b)

# Find top 3
top_3_july_crimes = july_crime_counts.takeOrdered(3, key=lambda x: -x[1])

print("The top 3 crimes reported in July:")
for crime in top_3_july_crimes:
    print("{}: {} crimes".format(crime[0], crime[1]))

# ---------------------------------------------------------------------
# Number of DANGEROUS WEAPONS crimes reported in July

# Filter for 'DANGEROUS WEAPONS' crimes
dangerous_weapons_july = july_crimes.filter(lambda x: x[7] == "DANGEROUS WEAPONS")

# Count the number of crimes
dangerous_weapons_count = dangerous_weapons_july.count()

# print output
print("Number of DANGEROUS WEAPONS crimes reported in July: {}".format(dangerous_weapons_count))

# EOF
