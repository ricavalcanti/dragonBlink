from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

try:
    trig = GP.getPin29() 
    Pin27.out()

    echo = GP.getPin30() 
    Pin29.input()	

    trig.low()
    print("Wait for sensor to settle")
    time.sleep(2)
    trig.high()
    time.sleep(0.00001)
    trig.low()

    while(echo.getValue == 0):
        pulse_start = time.clock()
    while(echo.getValue() == 1):
        pulse_end = time.clock()
    pulse_duration = pulse_end - pulse_start
    print("Duration: " + str(pulse_duration))

finally:
    GP.cleanup()
