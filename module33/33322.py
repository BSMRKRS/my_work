import RoboPiLib as RPL
import setup
import time
sensor_pin = 18
RPL.pinMode(sensor_pin,RPL.INPUT)
running=True

timeStart=time.time()
thing=True
thing2=True
RPL.servoWrite(0,1400)
RPL.servoWrite(1,1400)
while running:
	reading=RPL.digitalRead(sensor_pin)
	if reading==0:
		running=False
	

	tr=time.time()-timeStart +1
	t=int(tr)
	print(t)	
	



	sec=tr
	  

	if t%2==0 and thing==True:
		RPL.servoWrite(0,00)
		thing=False		
	elif t%2==0 and thing == False:
		RPL.servoWrite(0,1400)
		thing=True
	if t%3==0 and thing2==True:
		RPL.servoWrite(1,00)
		thing2=False
	elif t%3==0 and thing2==False:	
		RPL.servoWrite(1,1400)
		thing2=True
	print(thing)
	print(thing2)
	time.sleep(1)

