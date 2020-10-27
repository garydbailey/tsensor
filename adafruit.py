from Adafruit_IO import Client, RequestError, Feed
from configparser import ConfigParser
import os
import glob

#read in the adafruit config file
config_object = ConfigParser()
config_object.read("adafruit.config")
userinfo = config_object["USERINFO"]
user = userinfo["ADAFRUIT_IO_USERNAME"]
key = userinfo["ADAFRUIT_IO_KEY"]
ADAFRUIT_IO_USERNAME =  user.replace("'","")
ADAFRUIT_IO_KEY = key.replace("'","")

DEBUG = 1
if DEBUG == 1:
	print("User = " + ADAFRUIT_IO_USERNAME)
	print("Key = " + ADAFRUIT_IO_KEY)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


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

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
	test_feed = aio.feeds('test-feed')
except RequestError: # doesn't exist, create a new feed
	test = Feed(name='test-feed')
	test_feed = aio.create_feed(test)

temperature = (read_temp())

aio.send_data(test_feed.key, temperature)

