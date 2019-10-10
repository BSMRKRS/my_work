<<<<<<< HEAD
<<<<<<< Updated upstream
import RoboPiLib as RPL
import setup
import time
from multiprocessing import Process 
x = RPL.servoWrite(0,1400) 
y = RPL.servoWrite(1,1400) 
 
def wheel_1(): 
	while True:
		RPL.servoWrite(0,1400) 
		time.sleep(2)
		RPL.servoWrite(0,1500)
		time.sleep(2)	
def wheel_2():
	while True:
		RPL.servoWrite(1,1400) 
		time.sleep(3)
		RPL.servoWrite(1,1500)
		time.sleep(3) 

if True:
	Process(target=wheel_1).start()
	Process(target=wheel_2).start()
=======
=======
>>>>>>> master
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
    time.sleep(1) 
    RPL.servoWrite(0,1400)
    time.sleep(2)
    RPL.servoWrite(1,1400)
    RPL.servoWrite(0,1500)
    time.sleep(2) 
    RPL.servoWrite(0,1400)
    time.sleep(1) 
    RPL.servoWrite(1,1500) 
    time.sleep(1) 
    RPL.servoWrite(0,1500)
    time.sleep(2)
    

<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> master
