# Example query
# https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-01

import requests
import os
import re
import time
import json

headers     = {'token': 'gHlnfzHkxbaAlsIwGrxtTPEYmwgVjXpv'}
stateDict = {}
zipDatesDict = {}
zipDates = open("results.txt")
zipcodes = open("ZIP-COUNTY-FIPS_2010-03.csv")
missingZips = open("missingZips.txt", "w")






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
    
    jsonLine = json.loads(line)
    # print(jsonLine["results"])
    results = jsonLine["results"]
    for result in results:
        mindate = result["mindate"]
        maxdate = result["maxdate"]
        zipcode = result["id"]
        zipcode = zipcode[4:]
        
        if zipcode not in zipDatesDict:
            zipDatesDict[zipcode] = [mindate, maxdate]






path = os.getcwd()
try:
    os.mkdir(path + "/results")
except:
    print(path + "/results exists")


for state in stateDict.items():
    try:
        os.mkdir(path + "/results/" + state[0])
    except:
        print(path + "/results/" + state[0] + " exists")
    
    
    for county in state[1].items():
        try: 
            os.mkdir(path + "/results/" + state[0] + "/" + county[0])
        except:
            print(path + "/results/" + state[0] + "/" + county[0] + " exists")
        
        
        for zipcode in county[1]:
            try:
                os.mkdir(path + "/results/" + state[0] + "/" + county[0] + "/" + zipcode)
            except: 
                print(path + "/results/" + state[0] + "/" + county[0] + "/" + zipcode + " Exists")
            # Can cause keyerror if not all zips are accounted for
            try:
                minDate = zipDatesDict[zipcode][0]
                maxDate = zipDatesDict[zipcode][1]
            except:
                missingZips.write(zipcode + "," + county[0] + "," + state[0] + "\n")
                continue


            minYear = minDate[0:4]
            maxYear = maxDate[0:4]
            #starting a year later and just using the year -1 to get that start year for iteration sake.
            for year in range(int(minYear) + 1, int(maxYear) + 1):
                printYear = str(year)
                startDate = minDate
                startDate = startDate.replace(startDate[0:4],str(year-1))

                if int(year) == int(maxYear):
                    endDate = maxDate
                    minMonth = minDate[5:7]
                    maxMonth = maxDate[5:7]
                    
                    if int(maxMonth) > int(minMonth):
                        # We lose out on months of data with this solution.
                        # Better solution would be to make another API call and get the rest of the data but this will work for now.
                        endDate = minDate
                        endDate.replace(endDate[5:],minDate[5:])
                    else:
                        endDate = maxDate
                else:
                    endDate = minDate
                    endDate = endDate.replace(endDate[0:4],str(year))

                r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:' + zipcode + '&startdate=' + startDate + '&enddate=' + endDate, headers = headers)
                
                if not r.text == "{}":
                    w = open(path + "/results/" + state[0] + "/" + county[0] + "/" + zipcode + "/" + str(year), "w")
                    w.write(r.text)
                    w.close()

            # GHCND dataset is for daily summaries
            #TODO: fix this. Can't do min-max. Has to be in 1 year increments
            # r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:' + zip + '&startdate=' + min + '&enddate=' + max, headers = headers)
            # Dump results into files by year
            # print(r.text)
            # time.sleep(10)
            #break