import RoboPiLib as RPL
import setup
import time
R = 16 
RPL.pinMode(R,RPL.INPUT)
readingR = RPL.digitalRead(R)
def stinky(speed):
     RPL.servoWrite(0,speed)
     time.sleep(0.3)
     RPL.servoWrite(0,0)
     time.sleep(0.3)
while readingR <1: 
    stinky(1400) 
    if readingR ==1:
        import cease
