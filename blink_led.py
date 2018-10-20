from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

try:
    Pin27 = GP.getPin27()
    Pin27.out()

    Pin29 = GP.getPin29()
    Pin29.input()	

    while(1):
        startTime  = time.clock()
        pinValue = Pin29.getValue();        
        if pinValue == 1:
            Pin27.high()
        else:
            Pin27.low()
        print( time.clock() - startTime)
        time.sleep(5)

finally:
    GP.cleanup()
