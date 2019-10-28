import RoboPiLib as RPL
import setup

def readSensor(number):
	RPL.pinMode(number,RPL.INPUT)
	reading = RPL.digitalRead(number)
	return reading

if readSensor(16) == 0 or readSensor(17) == 0:
	RPL.servoWrite(1,1400)
else:
	RPL.servoWrite(0,1500)
