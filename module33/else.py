import RoboPiLib as RPL
import setup
x = 1
sensor_pin = 16
RPL.pinMode(sensor_pin ,RPL.INPUT)
while x == 1:
  reading = RPL.digitalRead(sensor_pin)
  if reading == 0:
    RPL.servoWrite(0, 1400)
  else: 
    RPL.servoWrite(0, 1600)
