import tempRead
import switch
import time
from datetime import datetime
import logging
logging.basicConfig(filename='tempLog.csv',level=logging.DEBUG)

temp = tempRead.read_temp()
setTemp = 131

while True:
	if temp < setTemp:
#		print str(datetime.now())+", low, "+str(temp)
#		logging.info(str(datetime.now())+", low, "+str(temp))
		logging.info(",low,"+ str(setTemp)+","+str(temp)+","+str(datetime.now()))
		print "low, "+ str(setTemp)+", "+str(temp)+", "+str(datetime.now())
		switch.setPower(1)
		time.sleep(2)
		temp = tempRead.read_temp()
	if temp >= setTemp:
#		print str(datetime.now())+", high, "+str(temp)
		print "high, "+ str(setTemp)+", "+str(temp)+", "+str(datetime.now())
		logging.info(",high,"+ str(setTemp)+","+str(temp)+","+str(datetime.now()))
#		logging.info(str(datetime.now())+", high, "+str(temp))
		switch.setPower(0)
		time.sleep(2)
		temp = tempRead.read_temp()
