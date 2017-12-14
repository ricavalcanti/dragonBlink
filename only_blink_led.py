
from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

try:
    Pin29 = GP.getPin29()
    Pin29.out()
    while(1):
	Pin29.high()
	time.sleep(1)
	Pin29.low()
	time.sleep(1)

finally:
    GP.cleanup()
