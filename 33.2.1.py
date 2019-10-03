import RoboPiLib as RPL
import setup
x = 1
sensor_pin = 2
RPL.pin(2,RPL.INPUT)
while x == 1:
  reading = RPL.digitalRead(2)
  if reading == 0:
    RPL.servoWrite(0, 1590)
  elif reading == 1:
    RPL.servoWrite(0, 1500)














