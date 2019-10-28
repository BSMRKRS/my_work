import RoboPiLib as RPL
import setup
import time
x = 1
n = 1

for x in range(1000):
  x += 1
  RPL.pinMode(16,RPL.INPUT)
    if RPL.digitalRead == 0:
      RPL.servoWrite(0,1400)
      print(f'The motor has pulsed {n} times)
      time.sleep(1)
      RPL.servoWrite(0,1500)
      n += 1
    else:
      time.sleep(1)
