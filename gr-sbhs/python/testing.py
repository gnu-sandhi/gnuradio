#!/usr/bin/python -tt

import serial
import time
from time import sleep

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
ser.open()


from time import sleep

import urllib
import urllib2
from sbhs import *
#from bottle import *
from scan_machines import *


new_device = Sbhs()
new_device.connect(252)
new_device.connect_device(0)


for i in range(10):
	#new_device.setHeat(10)
	#new_device.setFan(30)
	f=new_device.getTemp()
	print f
	time.sleep(3)
ser.close()
#f = 10

#@route('/temp')
#def hello():
#    return str(f)
#run(host='localhost', port=8080, debug=True)
'''
#writing to google app-engine
	data = {}
	data['temp'] = '30'#float value not int
	data['heat'] = '200'
	data['fan'] = '100'
	url_val = urllib.urlencode(data)
	print url_val
	
	url = 'http://remote-cloudlabs.appspot.com/hello'
	full_url = url + '?' + url_val
	data = urllib2.urlopen(full_url)

#reading from url
	req = urllib2.Request('http://remote-cloudlabs.appspot.com/display')
	response = urllib2.urlopen(req)
	data = response.read()
	print data

	
	time.sleep(10)

'''
