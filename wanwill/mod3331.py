import RoboPiLib as RPL
import setup
import time

i = 1
while i < 10:
	i += 1
	RPL.servoWrite(0,1400)
	time.sleep(1)
	RPL.servoWrite(0,1500)
	time.sleep(1)
