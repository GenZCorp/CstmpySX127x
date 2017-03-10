import Adafruit_BBIO.GPIO as GPIO
import time

KEY = "P8_15" # BB GPIO 47 in
PS =  "P8_17" # BB GPIO 27 in
i = 0
GPIO.setup(KEY,GPIO.OUT)
GPIO.setup(PS,GPIO.IN)
GPIO.output(KEY,1)
isup = GPIO.input(PS)

def powerup():
    print("3g power up")
    global isup
    while(isup==0):
        print(bytes(i))
        GPIO.output(KEY,0)
        print("delay begin")
        time.sleep(5)
        print("delay end")
        GPIO.output(KEY,1)
        isup = GPIO.input(PS)

def powerdown():
    print("3g power down")
    global isup
    while(isup==1):
        GPIO.output(KEY,0)
        print("down delay begin")
        time.sleep(5)
        print("down delay end")
        GPIO.output(KEY,1)
        isup = GPIO.input(PS)



