import requests
import time
import os


path = os.getcwd()
path = path + "/dataset"

print(path)
for filename in os.listdir(path):
    print(filename)
    data = open(path + "/" + filename,"r")

    line = data.readline()
    line = data.readline()
    line = line.split(",")
    print(line)
    break



#pseudo code....
#iterate over dataset

#get state,county information from FCC Database. 
    #break if 429 for limiting for ipaddress switch...

#create folder structure for state / county
    #store data by years.. making sure to append new data




#"34.23333","-86.16667"
def process():

    requestString = 'https://geo.fcc.gov/api/census/area?lat=34.23333&lon=-86.16667'
    
    r = requests.get(requestString)
    print(r.status_code)
    #Success
    if r.status_code == 200:
        print(r.text + '\n')
        



#process()