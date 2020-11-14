# Example query
# https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-01

import requests
import os
import re
import time

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
        stateDict[state] = {}

    if not county in stateDict[state]:
        stateDict[state].update({county:[]})
    
    if not zipcode in stateDict[state][county]:
        stateDict[state][county].append(zipcode)

while True:
    line = zipDates.readline()
    if line == '':
        break
    mindatematch = re.search("(?<=mindate\":\")[^\"]+", line)
    maxdatematch = re.search("(?<=maxdate\":\")[^\"]+", line)
    zipmatch = re.search("(?<=id\":\"ZIP:)[^\"]+", line)
    mindate = mindatematch.group(0)
    maxdate = maxdatematch.group(0)
    zip = zipmatch.group(0)

    if zip not in zipDatesDict:
        zipDatesDict[zip] = [mindate, maxdate]

path = os.getcwd()
os.mkdir(path + "/results")
for state in stateDict.items():
    os.mkdir(path + "/results/" + state[0])
    for county in state[1].items():
        os.mkdir(path + "/results/" + state[0] + "/" + county[0])
        for zip in county[1]:
            os.mkdir(path + "/results/" + state[0] + "/" + county[0] + "/" + zip)
            # Can cause keyerror if not all zips are accounted for
            try:
                min = zipDatesDict[zip][0]
                max = zipDatesDict[zip][1]
            except:
                continue

            # GHCND dataset is for daily summaries
            #TODO: fix this. Can't do min-max. Has to be in 1 year increments
            r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:' + zip + '&startdate=' + min + '&enddate=' + max, headers = headers)
            # Dump results into files by year
            print(r.text)
            time.sleep(10)