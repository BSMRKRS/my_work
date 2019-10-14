import RoboPiLib as RPL 
import setup
import time 
sensor_pin = 16

for number in range(1):
	if RPL.pinMode(sensor_pin,RPL.INPUT) == 0:
    		RPL.servoWrite(0,1400)
    		time.sleep(2)
    		RPL.servoWrite(0,1500) 
    		time.sleep(1) 
	else:
		RPL.servoWrite(0,1500) 
