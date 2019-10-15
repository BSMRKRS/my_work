import RoboPiLib as RPL
import setup
import time

i = 1
while i < 5:
	i += 1
	RPL.servoWrite(0,1400)
	RPL.servoWrite(1,1600)
	time.sleep(1)
	RPL.servoWrite(0,1500)
	time.sleep(0.5)
	RPl.servoWrite(1,1500)
	time.sleep(0.5)
	RPL.servoWrite(0,1400)
	time.sleep(1)
	RPl.servoWrite(0,1500)
	RPL.servoWrite(1,1500)
	time.sleep(1)
