import RoboPiLib as RPL 
import setup
import time 
sensor_pin = 16
x = 1

while True:
	for x in range(1000):
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
		else:
			break
		x += 1
