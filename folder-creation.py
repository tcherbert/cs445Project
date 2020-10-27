import os

fp = open('ZIP-COUNTY-FIPS_2010-03.csv','r')

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

    
#print(mydict)

#Work in progress...
path = os.getcwd()
for state in mydict:
    print(state)
    #state_path = path + "/" + state
    #print(state_path)
    #os.mkdir(state_path)
    #if isinstance(state,dict):
    for county, value in state:
        print(county)
        print(value)
        #county_path = state_path + "/" + county
        #print(county_path)
        #os.mkdir(county_path)


# for key in mydict:
#     print("key? is: %s",key)
