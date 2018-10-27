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
    for i in range(15):
        pulseStart = 0
        pulseEnd = 0
            isOutR = False
            init = time.clock()	
        trig.high()
        time.sleep(0.00001)
        trig.low()
        while(echo.getValue() == 0):
            pulseStart = time.clock()
            if(pulseStart - init > 0.3):
                print("out of range")
                        isOutR = True
                break
        pulseEnd = time.clock()
            while(echo.getValue() == 1):
            pulseEnd = time.clock()
            if(not isOutR):
                distance = (pulseEnd - pulseStart)*17150
                distance = round(distance,2)
            if(distance < 20 and distance >3) :
                    print("Distance: "+ str(distance))
                    distances.append(distance)
            else:
                i = i-1
        time.sleep(2)
    print("Terminado")
    
finally:
    GP.cleanup()
