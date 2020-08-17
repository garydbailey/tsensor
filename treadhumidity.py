# treadhumidity.py

# parse the json data created by temper.py to extract the humidity

# 2020-08-17 v0.1

import json

infile = open('temper.log')
rawdata = infile.read()
data = rawdata[1:-2]
jdata = json.loads(data)

# extract the humidity

humidity = jdata['internal humidity']

print (humidity)


