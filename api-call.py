import requests

headers = {'token': 'gHlnfzHkxbaAlsIwGrxtTPEYmwgVjXpv'}
r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/ZIP:83501', headers = headers)
print(r.status_code)
print(r.json())