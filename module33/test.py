import RoboPiLib as RPL
import setup
import time
sensor_pin = 17
sensor_pin1 = 18

RPL.pinMode(sensor_pin,RPL.INPUT)
RPL.pinMode(sensor_pin1,RPL.INPUT)


reading=RPL.digitalRead(sensor_pin)
reading1=RPL.digitalRead(sensor_pin1)
def puls(speed):
        RPL.servoWrite(0,speed)
        time.sleep(1)
        RPL.servoWrite(0,00)
        time.sleep(1)
       
      
