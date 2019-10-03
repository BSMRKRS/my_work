import RoboPiLib as RPL
import setup
x = 1
sensor_pin = 0
RPL.pinMode(0,RPL.INPUT)
while x == 1:
  reading = RPL.digitalRead(0)
  if reading == 0:
    RPL.servoWrite(0, 1590)
  elif reading == 1:
    RPL.servoWrite(0, 1500)

