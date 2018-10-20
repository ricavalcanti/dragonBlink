from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()
state = 0
timeToEnd = 15

try:
    Pin27 = GP.getPin27()
    Pin27.out()

    Pin29 = GP.getPin29()
    Pin29.input()	

    while(1):
        Pin27.high()
        startTime  = time.clock()
        while(((time.clock() - startTime) * 100) < timeToEnd):
            pinValue = Pin29.getValue();        
            if pinValue == 1:
                Pin27.low()
                print( time.clock() - startTime)
                break
    time.sleep(5)

finally:
    GP.cleanup()
