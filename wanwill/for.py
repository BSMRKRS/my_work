import RoboPiLib as RPL
import setup
import time
R = 16
RPL.pinMode(R,RPL.INPUT)
readingR = RPL.digitalRead(R)
if readingR == 0:
        loop = (1,2,3)
        for x in loop:
                RPL.servoWrite(0,1400)
                time.sleep(0.3)
                RPL.servoWrite(0,1500)
                time.sleep(0.3)
                                  
