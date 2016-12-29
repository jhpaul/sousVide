import time
import RPi.GPIO as io
io.setmode(io.BCM)


power_pin = 18

io.setup(power_pin, io.OUT)
io.output(power_pin, False)

time.sleep(5)
io.output(power_pin, True)
time.sleep(5)
io.output(power_pin,False)

