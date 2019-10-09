#is just the if.py
while x == 1:
    reading = RPL.digitalRead(sensor_pin)
    if reading == 0:
        RPL.servoWrite(1,1400)
    elif reading == 1:
        RPL.servoWrite(1,0)

