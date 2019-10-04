import RoboPiLib as RPL
import setup
running = True
sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)

while running:
	reading = RPL.digitalRead(sensor_pin)
if reading == 0:
	RPL.servoWrite(0,1400)
elif reading == 1:
	RPL.servoWrite(0,00)

