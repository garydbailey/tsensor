# tread3.py
# 
# 2019-11-28
#
# 2020-01-11 Added to git project for tsensors

import os
import glob
import time
#import paho.mqtt.client as paho

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# set up paho client parameters
#broker = "localhost"
#port = 1883
#sensorname = "t001"

#def on_publish(client,userdata,result):
#	print("data published \n")
#	pass

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		return temp_c

#main routine
#client1= paho.Client("control1")
#client1.on_publish = on_publish()
#client1.connect(broker,port)

temperature = (read_temp())

# get a timestamp in string format
#ts = time.time()
#tss = str(ts)

#message = '{ sensorname: ' + sensorname + ',' + ' value: ' + str(temperature) + ', time: ' + tss + '}'
print(temperature)
#ret= client1.publish("sensors",message)



