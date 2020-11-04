# Example query
# https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-01

import requests
import os

headers     = {'token': 'gHlnfzHkxbaAlsIwGrxtTPEYmwgVjXpv'}
stateDict = {}
zipDatesDict = {}
zipDates = open("attempt1.results.txt")
zipcodes = open("ZIP-COUNTY-FIPS_2010-03.csv")

# Strip header
zipcodes.readline()
while True:
    line = zipcodes.readline()
    if line == '':
        break
    row = line.split(",")

    zipcode     = row[0]
    county      = row[1]
    state       = row[2]

    if state not in stateDict:
        stateDict[state] = []

    if not county in stateDict[state]:
        stateDict[state].update({county:[]})
    
    if not zipcode in stateDict[state][county]:
        stateDict[state][county].append(zipcode)

while True:
    line = zipDates.readline()
    if line == '':
        break
    mindate = re.search("(?<=mindate\":\")[^\"]+", line)
    maxdate = re.search("(?<=maxdate\":\")[^\"]+", line)
    zip = re.search("(?<=id\":\"ZIP:)[^\"]+", line)

    if zip not in zipDatesDict:
        zipDatesDict[zip] = [mindate, maxdate]

path = os.getcwd()
os.mkdir(path + "/results")
for state in stateDict:
    os.mkdir(path + "/results/" + state)
    for county in state:
        os.mkdir(path + "/results/" + state + "/" + county)
        for zip in county:
            path = os.getcwd() + "/results/" + state + "/" + county + "/" + zip
            os.mkdir(path)
            # Can cause keyerror if not all zips are accounted for
            min = zipDatesDict[zip][0]
            max = zipDatesDict[zip][1]
            # GHCND dataset is for daily summaries
            r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:' + zip + '&startdate=' + min + '&enddate=' + max, headers = headers)
            # Dump results into files by year