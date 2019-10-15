import RoboPiLib as RPL
import setup
import time

for num in range(0,100):
	RPL.pinMode(16,RPL.INPUT)
	reading = RPL.digitalRead(16)

	if reading == 0:
		i = 0
		while i < 3:
			i += 1
			RPL.servoWrite(0,1400)
			time.sleep(0.3)
			RPL.servoWrite(0,1500)
			time.sleep(0.3)
	else:
		time.sleep(0.5)
