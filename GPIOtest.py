#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep

try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(17, GPIO.IN)
        while(True):
                GPIO.output(4, GPIO.input(17))
                sleep(0.1)
finally:
        GPIO.cleanup()
