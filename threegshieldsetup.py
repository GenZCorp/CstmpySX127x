import Adafruit_BBIO.GPIO as GPIO
import time

KEY = "P8_15" # BB GPIO 66 in
PS =  "P8_17" # BB GPIO 69 in
i = 0
GPIO.setup(KEY,GPIO.OUT)
GPIO.setup(PS,GPIO.IN)
GPIO.output(KEY,1)


def powerup():
    print("3g power up")
    global i
    while(GPIO.input(PS)!=1):
        print(bytes(i))
        GPIO.output(KEY,0)
        print("delay begin")
        time.sleep(5)
        print("delay end")
        GPIO.output(KEY,1)
        print(bytes(GPIO.input(PS)))
        i+=1

def powerdown():
    print("3g power down")
    while(GPIO.input(PS)!=0):
        GPIO.output(KEY,0)
        print("down delay begin")
        time.sleep(5)
        print("down delay begin")
        GPIO.output(KEY,1)



