import RoboPiLib as RPL
import setup
import time
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
while time > 20:
    reading = RPL.digitalRead(sensor_pin)
    if reading == 0:
        RPL.servoWrite(1,1400)
        time.sleep(1)
        RPL.servoWrite(1,0)
        time.sleep(1)
        RPL.servoWrite(1,1400)
        time.sleep(1)
        RPL.servoWrite(1,0)
        time.sleep(1)
        RPL.servoWrite(1,1400)
        time.sleep(1)
        RPL.servoWrite(1,0)
    elif reading == 1:
        RPL.servoWrite(1,0)

