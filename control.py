import switch
import time

temp = 1
setTemp = 5

#while True:
def controlPower(temp, setTemp):
	if temp < setTemp:
		print "low, "+str(temp)
		switch.setPower(1)
		time.sleep(2)
		temp = tempRead.read_temp()
	if temp >= setTemp:
		print "high, "+str(temp)
		switch.setPower(0)
		time.sleep(2)
		temp = tempRead.read_temp()

#controlPower(temp,setTemp)

