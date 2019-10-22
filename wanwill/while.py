import RoboPiLib as RPL
import setup
import time
R = 16
RPL.pinMode(R,RPL.INPUT)
readingR = RPL.digitalRead(R)
x = 0
if readingR == 0:
	while x < 10:
		RPL.servoWrite(0,1400)
		time.sleep(1)
		RPL.servoWrite(0,0)
		time.sleep(1)
		x = x + 1
