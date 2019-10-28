import RoboPiLib as RPL
import setup
sensor_pin = 16

def motor():
  RPL.servoWrote(0,1400)
  
if RPL.digitalRead(sensor_pin) == 0
  motor()
