import RoboPiLib as RPL
import setup
sensor_pin = 16
sensor_pin2 = 17
running = True
RPL.pinMode(sensor_pin,RPL.INPUT)
RPL.pinMode(sensor_pin2,RPL.INPUT)
while running:
        reading = RPL.digitalRead(sensor_pin)
        reading2 = RPL.digitalRead(sensor_pin2)
        if reading == 0 and reading2 == 0:
                RPL.servoWrite(0,1400)
        elif reading == 1 or reading2 == 1:
                RPL.servoWrite(0,1500)
