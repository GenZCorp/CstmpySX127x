import Adafruit_BBIO.GPIO as GPIO
import reader as rdr
number = "+923455361619"
variable = 1
def sendtext():
    message = rdr.msgpktformer()
    smsnum=(message.__len__()/160)
    modem=serial.Serial('/dev/ttyO4',115200,timeout=5)
    modem.write("AT+CMGF=1\r".encode())
    time.sleep(1) 
    while true:
        modem.write('AT+CMGS="'+number+'"\r\n'.encode())
        time.sleep(1)
        modem.write((message[((variable*160)-160):(160*variable)]+"\r").encode())
        time.sleep(1)
        variable += 1
        if(variable == smsnum):
            break
    modem.write(ascii.ctrl('z').encode())
    time.sleep(1)
    modem.close