import RoboPiLib as RPL
import setup
import time
R = 16
RPL.pinMode(R,RPL.INPUT)
readingR = RPL.digitalRead(R)
if readingR == 0:
       	x = 20
	for num in range (0,x):
		while num in x < 20:
               		RPL.servoWrite(0,1400)
                	time.sleep(0.3)
                	RPL.servoWrite(0,1500)
                	time.sleep(0.3)
