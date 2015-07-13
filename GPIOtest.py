#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

def myHandler(channel):
	print ("howdy partner!")

try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(4, GPIO.BOTH, callback=myHandler, bouncetime=200)
	sleep(3600)

finally:
        GPIO.cleanup()
