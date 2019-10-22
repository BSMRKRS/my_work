import RoboPiLib as RPL
import setup

RPL.pinMode(16,RPL.INPUT)
reading = RPL.digitalRead(16)

if reading == 0:
	RPL.servoWrite(0,1400)
else:
	RPL.servoWrite(0,1500)
