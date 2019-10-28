import RoboPiLib as RPL
import setup
While True:
  while RPL.analogRead(8) < 500:
    RPL.servoWrite(0,1400)
    RPL.servoWrite(1,1400)
  else:
    RPL.servoWrite(0,1450)
    RPL.servoWrite(1,1450)
