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
   # while(echo.getValue == 0):
    #    pulse_start = time.clock()
   # while(echo.getValue() == 1):
    #    pulse_end = time.clock()
   # pulse_duration = pulse_end - pulse_start
    while(1):
	trig.high()
	time.sleep(0.00001)
	trig.low()
	while(echo.getValue() == 0):
		pulseStart = time.time()
    	while(echo.getValue() == 1):
		pulseEnd = time.time()
	distance = (pulseEnd - pulseStart)*17150
	distance = round(distance,2)
	print("Distance: "+ str(distance))
	time.sleep(1)

finally:
    GP.cleanup()
