import RoboPiLib as RPL
import setup
sensor_pin = 16

if RPL.digitalRead(sensor_pin) == 0:
  RPL.servoWrite(0,1400)
else:
  RPL.servoWrite(0,1500)
