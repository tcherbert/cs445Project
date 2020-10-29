import requests
import time

headers     = {'token': 'gHlnfzHkxbaAlsIwGrxtTPEYmwgVjXpv'}
error_log   = open('error-log.txt','w')
results     = open('results.txt','w')
fp          = open('ZIP-COUNTY-FIPS_2010-03.csv','r')
codes_429   = open('error-429.txt','w')
mindate     = 0


#Just skip first line -- Header Line
line = fp.readline()

mydict = {}

while True:
    line = fp.readline()
    if line == '':
        break
    row = line.split(",")

    zipcode     = row[0]
    county      = row[1]
    state       = row[2]

    if state not in mydict:
        mydict[state] = {}

    if not county in mydict[state]:
        mydict[state].update({county:[]})
    
    if not zipcode in mydict[state][county]:
        mydict[state][county].append(zipcode)


def process():
    print('inside process')
    r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ZIP&sortfield=name&sortorder=desc&offset=25&limit=200', headers = headers)
    # print(r.status_code)
    #Success
    if r.status_code == 200:
        response_dict = r.json()
        response_text = r.text
        results.write(r.text + '\n')

process()