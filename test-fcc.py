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

#"34.23333","-86.16667"
def process():

    requestString = 'https://geo.fcc.gov/api/census/area?lat=34.23333&lon=-86.16667'
    

    r = requests.get(requestString)
    print(r.status_code)
    #Success
    if r.status_code == 200:
        print(r.text + '\n')
        



#process()