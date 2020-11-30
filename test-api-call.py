import requests
import time

headers     = {'token': 'pAnnanLcCpjkYqirJaZRBjRQkNKMilFk'}
results     = open('results.txt','a')



def process():
    # print('inside process')
    # zipcode = "28801"
    # startDate = "1994-08-15"
    # endDate = "1995-08-15"
    zipcode = "36006"
    startDate = "1960-01-01"
    endDate = "1960-02-01"
    #requestString = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:' + zipcode + '&startdate=' + startDate + '&enddate=' + endDate
    #testRequestString = "https://www.ncdc.noaa.gov/cdo-web/api/v2/datacategories?locationid=CITY:US10001"
    anotherString = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOM&locationid=ZIP:" + zipcode + "&startdate=" + startDate + "&enddate=" + endDate
    #testRequestString = "https://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes/DP10"

    r = requests.get(anotherString, headers = headers)
    print(r.status_code)
    #Success
    if r.status_code == 200:
        print(r.text + '\n')
        



process()