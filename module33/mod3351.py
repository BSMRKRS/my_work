import RoboPiLib as RPL
import setup
import time

i = 0

while i < 15:
	i += 1
	reading = RPL.analogRead(1)
	print(reading)
	if reading < 200:
		RPL.servoWrite(0,1400)
		RPL.servoWrite(1,1600)	
	else:
		RPL.servoWrite(0,1500)
		RPL.servoWrite(1,1500)
	time.sleep(0.5)
