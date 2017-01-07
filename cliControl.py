import tempRead
import switch
import time
from datetime import datetime
import logging
import json

logging.basicConfig(filename='tempLog.csv',level=logging.DEBUG)


setTemp = 0
spikeCounter = 0
checkRate = 2
configFile = 'config.json'
statusFile = 'status.json'

while True:

	with open(configFile, 'r') as f:
	    config = json.load(f)

	status = {'temp' : tempRead.read_temp(), 'setTemp' : config['setTemp']}
	# print str(status)
	temp = status['temp']
	setTemp = status['setTemp']
	if temp < setTemp:
#		print str(datetime.now())+", low, "+str(temp)
#		logging.info(str(datetime.now())+", low, "+str(temp))
		logging.info(",low,"+ str(setTemp)+","+str(temp)+","+str(datetime.now()))
		package = {'status': 'low', 'setTemp': setTemp, 'temp': round(temp, 2), 'datetime': str(datetime.now())}
		print str(package)
		with open(statusFile, 'w') as f:
			json.dump(package, f)




		switch.setPower(1)
		time.sleep(checkRate)
		spikeCounter = spikeCounter + checkRate
		temp = tempRead.read_temp()
	# if temp >= (setTemp-2) and spikeCounter > 600:
	# 	switch.setPower(0)
	# 	spikeCounter = 0
	# 	print "PEAK PROTECTION, "+ str(setTemp)+", "+str(temp)+", "+str(datetime.now())
	# 	logging.info(",PEAK PROTECTION,"+ str(setTemp)+","+str(temp)+","+str(datetime.now()))
	if temp >= setTemp:
#		print str(datetime.now())+", high, "+str(temp)
		print "high, "+ str(setTemp)+", "+str(temp)+", "+str(datetime.now())
		logging.info(",high,"+ str(setTemp)+","+str(temp)+","+str(datetime.now()))
#		logging.info(str(datetime.now())+", high, "+str(temp))
		package = {'status': 'high', 'setTemp': setTemp, 'temp': round(temp, 2), 'datetime': str(datetime.now())}
		print str(package)
		with open(statusFile, 'w') as f:
			json.dump(package, f)

		switch.setPower(0)
		time.sleep(2)
		spikeCounter = 0
		temp = tempRead.read_temp()
