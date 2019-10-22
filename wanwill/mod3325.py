import RoboPiLib as RPL
import setup

def readSensor(number):
	RPL.pinMode(number,RPL.INPUT)
	reading = RPL.digitalRead(number)
	return reading

if readSensor(16) == 0 and readSensor(17) == 0:
	RPL.servoWrite(0,1600)
	RPL.servoWrite(1,1400)	
elif readSensor(16) == 0:
	RPL.servoWrite(0,1400)
elif readSensor(17) == 0:
	RPL.servoWrite(1,1600)
else:
	RPL.servoWrite(0,1500)
	RPL.servoWrite(1,1500)
