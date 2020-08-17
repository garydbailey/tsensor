# treadtemper.py

# parse the json data created by temper.py to extract the temperature

# 2020-08-06 v0.1

import json

infile = open('temper.log')
rawdata = infile.read()
data = rawdata[1:-2]
jdata = json.loads(data)

# extract the temperature

temperature = jdata['internal temperature']

print (temperature)


