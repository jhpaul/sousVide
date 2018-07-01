import tempRead
import switch
import time
from datetime import datetime
import logging
import json
import os
import pytz

# datetime.datetime
# datetime.timedelta
# datetime.timezone  (python 3.2+)

setTemp = 0
spikeCounter = 0
checkRate = 1 
fileDir = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename=fileDir+'tempLog.csv',level=logging.DEBUG)
#print fileDir
configFile = fileDir+'/config.json'
statusFile = fileDir+'/status.json'
historyFile = fileDir+'/history.json'

def sh(script):
    os.system("bash -c '%s'" % script)

# with open(historyFile, 'w') as f:
# 	json.dump({'power': 'OFF', 'setTemp': 0, 'temp': 0, 'datetime': str(datetime.now())}, f)

while True:
        data={}
	with open(configFile, 'r') as f:
	    config = json.load(f)

	status = {'temp' : tempRead.read_temp(), 'setTemp' : config['setTemp']}
	# print str(status)
	temp = status['temp']
	setTemp = status['setTemp']
	d_aware = datetime.now(pytz.timezone("US/Eastern"))
	if (str(config['mode']) == 'HEAT' and temp < setTemp) or (str(config['mode']) == 'COOL' and temp > setTemp):
#		print str(datetime.now())+", low, "+str(temp)
#		logging.info(str(datetime.now())+", low, "+str(temp))
		logging.info(",low,"+str(config['mode'])+","+ str(setTemp)+","+str(temp)+","+str(d_aware))
		package = {'power': 'ON', 'mode': str(config['mode']),'setTemp': setTemp, 'temp': round(temp, 2), 'datetime': str(d_aware)}
		histPackage = { str(d_aware): {'power': 'ON', 'mode': str(config['mode']),'setTemp': setTemp, 'temp': round(temp, 2), 'datetime': str(d_aware)}}
		csvPackage = 'ON,'+str(config['mode'])+','+str(setTemp)+','+str(round(temp, 2))+','+str(d_aware)+"\n"

		print str(package)
		with open(statusFile, 'w') as f:
			json.dump(package, f)
		with open(historyFile) as h:
			#print h.read()
			try:
				data = json.load(h)
				data.update(histPackage)
			except ValueError:
				data = {} 
				data.update(histPackage)
		with open(historyFile, 'w') as r:
                        json.dump(data, r)
		switch.setPower(1)
		time.sleep(checkRate)
		spikeCounter = spikeCounter + checkRate
		temp = tempRead.read_temp()
	# if temp >= (setTemp-2) and spikeCounter > 600:
	# 	switch.setPower(0)
	# 	spikeCounter = 0
	# 	print "PEAK PROTECTION, "+ str(setTemp)+", "+str(temp)+", "+str(datetime.now())
	# 	logging.info(",PEAK PROTECTION,"+ str(setTemp)+","+str(temp)+","+str(datetime.now()))
	if (str(config['mode']) == 'HEAT' and temp >= setTemp) or (str(config['mode']) == 'COOL' and temp <= setTemp):
#		print str(datetime.now())+", low, "+str(temp)
#	if temp >= setTemp:
#		print str(datetime.now())+", high, "+str(temp)
		# print "high, "+ str(setTemp)+", "+str(temp)+", "+str(datetime.now())
		logging.info(",high,"+ str(config['mode'])+","+str(setTemp)+","+str(temp)+","+str(datetime.now()))
#		logging.info(str(datetime.now())+", high, "+str(temp))
                package = {'power': 'OFF', 'mode': str(config['mode']), 'setTemp': setTemp, 'temp': round(temp, 2), 'datetime': str(d_aware)}
		histPackage = { str(d_aware): {'power': 'ON',  'mode': str(config['mode']), 'setTemp': setTemp, 'temp': round(temp, 2), 'datetime': str(d_aware)}}
		csvPackage = 'OFF,'+str(config['mode'])+','+str(setTemp)+','+str(round(temp, 2))+','+str(d_aware)+"\n"

		print str(package)
		with open(statusFile, 'w') as f:
			json.dump(package, f)
		with open(historyFile) as h:
			try:
				data = json.load(h)
				data.update(histPackage)
			except ValueError:
				data = {} 
				data.update(histPackage) 
                        data.update(histPackage)
                with open(historyFile, 'a') as h:
	                json.dump(data, h)
		# sh("echo " + str(package) + " >> history.json")

		switch.setPower(0)
		time.sleep(checkRate)
		spikeCounter = 0
		temp = tempRead.read_temp()

