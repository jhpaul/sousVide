import time
import RPi.GPIO as io
io.setmode(io.BCM)


power_pin = 15

io.setup(power_pin, io.OUT)
io.output(power_pin, False)


def setPower(status):
	if status == 1:
		io.output(power_pin, True)
	if status == 0: 
		io.output(power_pin, False)

