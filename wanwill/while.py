import RoboPiLib as RPL
import setup
import time
R = 16
RPL.pinMode(R,RPL.INPUT)
readingR = RPL.digitalRead(R)
x = 1 
if readingR == 0:
	while x < 11:
		RPL.servoWrite(7,1400)
		x = x+1
