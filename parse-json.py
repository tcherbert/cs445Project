# Example query
# https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-01

import requests
import os
import re
import time
import json

stateDict = {}
zipDatesDict = {}


zipDates = open("results.txt")


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
        state   = result["name"]
        state   = state.split(",")
        state   = state[1][1:3]
        print(result)


    break

