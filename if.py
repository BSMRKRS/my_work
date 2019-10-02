import RoboPiLib as RPL
imprt setup
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
reading = RPL.digitalRead(sensor_pin)
if reading == 0:
	RPL.servoWrite(1,400)
