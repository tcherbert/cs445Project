import requests

headers     = {'token': 'gHlnfzHkxbaAlsIwGrxtTPEYmwgVjXpv'}
error_log   = open('error-log.txt','w')
results     = open('results.txt','w')
fp          = open('ZIP-COUNTY-FIPS_2010-03.csv','r')
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


#State
for i in mydict.keys():
    #County
    for j in mydict[i].keys():
        #Zip
        for n in mydict[i][j]:
            r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/ZIP:' + n, headers = headers)
            # print(r.status_code)
            #Success
            if r.status_code == 200:
                response_dict = r.json()
                response_text = r.text
                #print(len(r.text))
                if len(r.text) > 2:
                    #print(response_dict['mindate'])
                    results.write(response_text + '\n')
                else:
                    error_log.write('Error in processing Zip: ' + n + ' with length 2 or less\n')
            #Not Found.. or possible another code..
            else:
                error_log.write('Error in processing Zip: ' + n + ' with code: ' + r.status_code + '\n')
            # if r.status_code == 404:
