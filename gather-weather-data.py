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
zipDates = open("new.results.txt")
zipcodes = open("ZIP-COUNTY-FIPS_2010-03.csv")
missingZips = open("missingZips.txt", "w")
headerErrors = open("headerErrors.txt","w")



def apiCall(state,county,zipcode,year):
    print("Running request for "  + state + "/" + county + "/" + zipcode + "/" + str(year) + "\n")
    r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&locationid=ZIP:' + zipcode + '&startdate=' + startDate + '&enddate=' + endDate + "&limit=12", headers = headers)
    print("Status code: " + str(r.status_code) + " for " + state + "/" + county + "/" + zipcode + "/" + str(year) + "\n")

    if r.status_code == 200:
        if not r.text == "{}":
            w = open(path + "/results/" + state + "/" + county + "/" + zipcode + "/" + str(year), "w")
            w.write(r.text)
            w.close()
            print("Recieved Data for " + state + "/" + county + "/" + zipcode + "/" + str(year) + "\n")
        else:
            print("Recieved {} for " + state + "/" + county + "/" + zipcode + "/" + str(year) + "\n")
    #Too many requests
    elif r.status_code == 429 or r.status_code == 503:
        print("429 or 503... Sleeping...\n")
        headerErrors.write('Sleeping on:  with code: ' + str(r.status_code) + " on state: " + state + " county:" + county + " zipcode: " + str(zipcode) + " year: " + str(year) + "\n")
        #sleep 1 hours
        time.sleep(60*60*1)
        apiCall(state,county,zipcode,year)
    
    else:
        headerErrors.write("Error " + str(r.status_code) + " on state: " + state + " county:" + county + " zipcode: " + str(zipcode) + " year: " + str(year) + "\n")











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

                
                
                
                
                apiCall(state[0],county[0],zipcode,year)
                
                # print("Running request for "  + state[0] + "/" + county[0] + "/" + zipcode + "/" + str(year) + "\n")
                # r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&locationid=ZIP:' + zipcode + '&startdate=' + startDate + '&enddate=' + endDate + "&limit=12", headers = headers)
                # print("Status code: " + str(r.status_code) + " for " + state[0] + "/" + county[0] + "/" + zipcode + "/" + str(year) + "\n")

                # if r.status_code == 200:
                #     if not r.text == "{}":
                #         w = open(path + "/results/" + state[0] + "/" + county[0] + "/" + zipcode + "/" + str(year), "w")
                #         w.write(r.text)
                #         w.close()
                #         print("Recieved Data for " + state[0] + "/" + county[0] + "/" + zipcode + "/" + str(year) + "\n")
                #     else:
                #         print("Recieved {} for " + state[0] + "/" + county[0] + "/" + zipcode + "/" + str(year) + "\n")
                # #Too many requests
                # elif r.status_code == 429 or r.status_code == 503:
                #     print("429 or 503... Sleeping...\n")
                #     headerErrors.write('Sleeping on:  with code: ' + str(r.status_code) + " on state: " + state[0] + " county:" + county[0] + " zipcode: " + str(zipcode) + " year: " + str(year) + "\n")
                #     #sleep 1 hours
                #     time.sleep(60*60*1)
                
                # else:
                #     headerErrors.write("Error " + str(r.status_code) + " on state: " + state[0] + " county:" + county[0] + " zipcode: " + str(zipcode) + " year: " + str(year) + "\n")




