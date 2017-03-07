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
    global i
    while(isup==0):
        print(bytes(i))
        GPIO.output(KEY,0)
        print("delay begin")
        time.sleep(5)
        print("delay end")
        if(GPIO.input(PS)):
            print("HIGH")
        else:
            print("LOW")
        GPIO.output(KEY,1)
        isup = GPIO.input(PS)
        print(bytes(isup))
        i+=1

def powerdown():
    print("3g power down")
    while(GPIO.input(PS)):
        GPIO.output(KEY,0)
        print("down delay begin")
        time.sleep(5)
        print("down delay begin")
        GPIO.output(KEY,1)



