from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

try:
    trig = GP.getPin29()
    trig.out()

    echo = GP.getPin30()
    echo.input()

    trig.low()
    print("Wait for sensor to settle")
    time.sleep(2)
    pulseStart = 0
    pulseEnd = 0
    while(1):
    isOutR = False
    init = time.clock()
	pulseStart = init
	trig.low()
	time.sleep(0.000002)
	trig.high()
	time.sleep(0.00001)
	trig.low()
	while(echo.getValue() == 0):
		pulseStart = time.clock()
		if(time.clock() - init > 0.03):
			print("out of range")
            isOutR = True
			break
	pulseEnd = time.clock()
    while(echo.getValue() == 1 && (!isOutR)):
		pulseEnd = time.clock()
    if(!isOutR):
        distance = (pulseEnd - pulseStart)*17150
	    distance = round(distance,2)
	    print("Distance: "+ str(distance))
	time.sleep(2)

finally:
    GP.cleanup()
