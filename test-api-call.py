import requests
import time

headers     = {'token': 'gHlnfzHkxbaAlsIwGrxtTPEYmwgVjXpv'}
results     = open('results.txt','a')



def process():
    print('inside process')
    zipcode = "28801"
    startDate = "1994-08-15"
    endDate = "1995-08-15"
    requestString = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:' + zipcode + '&startdate=' + startDate + '&enddate=' + endDate
    #testRequestString = "https://www.ncdc.noaa.gov/cdo-web/api/v2/datacategories?locationid=CITY:US10001"
    testRequestString = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ZIP&sortfield=name&sortorder=desc"


    #anotherString = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:" + zipcode + "&startdate=" + startDate + "&enddate=" + endDate

    r = requests.get(testRequestString, headers = headers)
    print(r.status_code)
    #Success
    if r.status_code == 200:
        print(r.text + '\n')
        



process()