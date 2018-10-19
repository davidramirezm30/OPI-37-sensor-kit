#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO
from time import sleep          # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering
GPIO.setup(7, GPIO.OUT)         # set BCM7 (pin 26) as an output (LED)
  
# The input pin which is connected with the sensor.<br /># Additional to that the pull up resistor of the input will be activated.
GPIO_PIN = 26
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
  
print "Sensor-Test [press ctrl+c to end the test]"
  
# This outputFunction will be started at signal detection
def outputFunction(null):
		print("Signal detected")
  
# The outputFunction will be started at the moment of a signal detection (raising edge).
GPIO.add_event_detect(GPIO_PIN, GPIO.RISING, callback=outputFunction, bouncetime=100) 
  
# Main program loop
try:
	while True:
		GPIO.output(7, 1)       # set port/pin value to 1/HIGH/True
		sleep(0.1)
		GPIO.output(7, 0)       # set port/pin value to 0/LOW/False
		sleep(0.1)

		GPIO.output(7, 1)       # set port/pin value to 1/HIGH/True
		sleep(0.1)
		GPIO.output(7, 0)       # set port/pin value to 0/LOW/False
		sleep(0.1)
		
		sleep(1)

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    GPIO.output(7, 0)
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print "Other error or exception occurred!"  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit 


