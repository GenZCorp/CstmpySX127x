import Adafruit_BBIO.GPIO as GPIO
import time

KEY = "P8_07" # BB GPIO 66 in
PS =  "P8_09" # BB GPIO 69 in

GPIO.setup(KEY,GPIO.OUT)
GPIO.setup(PS,GPIO.IN)
GPIO.output(KEY,1)


def powerup():
    while(GPIO.input(PS)!=1):
        GPIO.output(KEY,0)
        time.sleep(5)
        GPIO.output(KEY,1)


def powerdown():
    while(GPIO.input(PS)!=0):
        GPIO.output(KEY,0)
        time.sleep(5)
        GPIO.output(KEY,1)



