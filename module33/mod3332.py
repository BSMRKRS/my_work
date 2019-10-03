import RoboPiLib as RPL
import setup
import time

def motorPulse(motor,speed,seconds):
	i = 1
	while i < 5:
		i += 1
		RPL.servoWrite(motor,speed)
		time.sleep(seconds)
		RPL.servoWrite(motor,1500)
		time.sleep(seconds)

motorPulse(0,1400,1)
motorPulse(1,1600,2)
