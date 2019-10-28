import RoboPiLib as RPL
import setup
sensor_pin = 16

def motor():
  RPL.servoWrote(x,1400)
  
x = 0

if RPL.digitalRead(sensor_pin) == 0
  motor()
