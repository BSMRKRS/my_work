import RoboPiLib as RPL 
import setup
import time 
sensor_pin = 16
x = 1

for x in range(20):
	RPL.pinMode(sensor_pin,RPL.INPUT)
	if RPL.digitalRead(16) == 0:
		RPL.servoWrite(0,1400)
		time.sleep(0.5)
		RPL.servoWrite(0,1500)		
		time.sleep(0.5)
		RPL.servoWrite(0,1400)
		time.sleep(0.5)
		RPL.servoWrite(0,1500)			
		time.sleep(0.5)
		RPL.servoWrite(0,1400)
		time.sleep(0.5)
		RPL.servoWrite(0,1500)
		x += 5
	else:
		time.sleep(1)
		x += 1
