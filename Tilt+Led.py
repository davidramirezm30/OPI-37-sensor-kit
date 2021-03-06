#!/usr/bin/env python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO
from time import sleep          # this lets us have a time delay

GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)
  
# The input pin of the Sensor will be declared. Additional to that the pullup resistor will be activated.
GPIO_PIN = 7
LED = 29
GPIO.setup(GPIO_PIN, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
print "Sensor-Test [press ctrl+c to end it]"
  
# This output function will be started at signal detection
def outFunction(null):
		GPIO.output(LED, True)
  
# At the moment of detecting a Signal ( falling signal edge ) the output function will be activated.
#GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=outFunction, bouncetime=100) 
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=outFunction, bouncetime=10) 
  
try:
        while True:
			sleep(1)
			if GPIO.input(GPIO_PIN)== True:
				GPIO.output(LED,False)

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print "An error or exception occurred!"
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print "Other error or exception occurred!"  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit 
