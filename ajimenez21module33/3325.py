import RoboPiLib as RPL
import setup

sensor_pin = 17     
value = RPL.pinMode(17,RPL.INPUT)
 
if RPL.digitalRead(17) == 0 and RPL.digitalRead(16) == 1:
	RPL.servoWrite(1,1400)
	RPL.servoWrite(0,1500)
elif RPL.digitalRead(17) == 1 and RPL.digitalRead(16) == 0:
	RPL.servoWrite(0,1600)
	RPL.servoWrite(1,1500)
elif RPL.digitalRead(17) == 0 and RPL.digitalRead(16) == 0:
	RPL.servoWrite(0,1400)
	RPL.servoWrite(1,1600)
else:
	RPL.servoWrite(1,1500)
	RPL.servoWrite(0,1500)   
