# import requests

# response = requests.get("https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ZIP:19492&sortfield=name&sortorder=desc&token=gHlnfzHkxbaAlsIwGrxtTPEYmwgVjXpv")

# print(response.status_code)


# import urllib2
# data

# req = urllib2.Request(url, data)
# response = urllib2.urlopen(req)
# result = response.read()

import requests

headers = {'token': 'gHlnfzHkxbaAlsIwGrxtTPEYmwgVjXpv'}
#data = {'token':'gHlnfzHkxbaAlsIwGrxtTPEYmwgVjXpv'} #data = data

r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/ZIP:83501', headers = headers)
#r.text      # response as a string
##r.content   # response as a byte string
            #     gzip and deflate transfer-encodings automatically decoded 
#r.json()    # return python object from json! this is what you probably want!
print(r.status_code)