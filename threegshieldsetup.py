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
        print("delay begin")
        time.sleep(0.0833)
        print("delay end")
        GPIO.output(KEY,1)
        print(bytes(GPIO.input(PS)))


def powerdown():
    print("3g power down")
    while(GPIO.input(PS)!=0):
        GPIO.output(KEY,0)
        print("down delay begin")
        time.sleep(0.0833)
        print("down delay begin")
        GPIO.output(KEY,1)



