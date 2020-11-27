import requests
import time

headers     = {'token': 'gHlnfzHkxbaAlsIwGrxtTPEYmwgVjXpv'}
results     = open('new.results.txt','a')
counter     = 0
limit       = 1000


def process():
    print('inside process')
    r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ZIP&sortfield=name&sortorder=desc&offset=' + str(counter) + '&limit=' + str(limit), headers = headers)
    # print(r.status_code)
    #Success
    if r.status_code == 200:
        results.write(r.text + '\n')
        
        #can look at the other script to improve with other codes and such but this api is so simple you don't need it.
        #Could also get mindate easily by iterateing over the results or get it all then find it that way.
        #We then gotta make a decsion as to how we are going to manage this project in regard to start date. 
        #Either by making sure there is one zipcode for that county earlier than that or just do like we stated earlier no data for that county as of that date.. 
        



while True:
    if counter + 1000 < 30415:
        process()
        counter += 1000
    else:
        #Final run and done.
        limit = 30415 - counter
        counter = limit
        process()
        break