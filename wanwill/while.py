import RoboPiLib as RPL
import setup
import time
R = 16
RPL.pinMode(R,RPL.INPUT)
readingR = RPL.digitalRead(R)
x = 1 
if readingR == 0:
	while x < 11:
		RPL.servoWrite(0,1400)
		time.sleep(0.3)
		RPL.servoWrite(0,0)
		time.sleep(0.3)
		x = x+1
		if x == 12:
			break
RPL.servoWrite(0,0)
