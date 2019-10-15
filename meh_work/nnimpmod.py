import RoboPiLib as RPL
import setup
x = 1
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
reading = RPL.digitalRead(sensor_pin)
    if reading >= 0 or 1:
        import nrunner
    elif reading < 0:
        import sleeper

