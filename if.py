





import RoboPiLib as RPL
import setup
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
reading = RPL.digitalRead(sensor_pin)
print reading
if reading == 0:
    RPL.servoWrite(1,1400)
elif reading == 1:
    RPL.servoWrite(1,0) 
    








