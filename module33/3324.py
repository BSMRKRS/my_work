import RoboPiLib as RPL
import setup

sensor_pin = 17     
value = RPL.pinMode(17,RPL.INPUT)
 
if RPL.digitalRead(17) == 0:
	RPL.servoWrite(1,1400)
else:
	RPL.servoWrite(1,1600)  
