import RoboPiLib as RPL 
import setup 
import time

while True:
    RPL.servoWrite(0,1400)
    RPL.servoWrite(1,1400)
    time.sleep(2)
    RPL.servoWrite(0,1500) 
    time.sleep(1) 
    RPL.servoWrite(1,1500)
