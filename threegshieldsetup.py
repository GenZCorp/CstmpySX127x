import Adafruit_BBIO.GPIO as GPIO
import time

KEY = "P8_15" # BB GPIO 66 in
PS =  "P8_17" # BB GPIO 69 in

GPIO.setup(KEY,GPIO.OUT)
GPIO.setup(PS,GPIO.IN)
GPIO.output(KEY,1)


def powerup():
    print("3g power up")
    while(GPIO.input(PS)!=1):
        GPIO.output(KEY,0)
        time.sleep(5)
        GPIO.output(KEY,1)


def powerdown():
    print("3g power down")
    while(GPIO.input(PS)!=0):
        GPIO.output(KEY,0)
        time.sleep(5)
        GPIO.output(KEY,1)



