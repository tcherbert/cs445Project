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

    
#print(mydict['WA'])

#Work in progress...
path = os.getcwd()

for i in mydict.keys():
    state_path = path + "/" + i
    os.mkdir(state_path)
    for j in mydict[i].keys():
        county_path = state_path + "/" + j
        os.mkdir(county_path)
        for n in mydict[i][j]:
            zip_path = county_path + "/" + n
            os.mkdir(zip_path)



for state in mydict:
    # print("\n\nHello New State")
    # print(state)
    #state_path = path + "/" + state
    #print(state_path)
    #os.mkdir(state_path)
    #if isinstance(state,dict):
    for county in state:
        pass
        # print(county)
        # print(value)
        #county_path = state_path + "/" + county
        #print(county_path)
        #os.mkdir(county_path)


# for key in mydict:
#     print("key? is: %s",key)
