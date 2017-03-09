import reader as rdr
import urllib
import messagedecoder as mydecoder

def threegupload():
    print("In upload data")
    message = rdr.msgpktformer()
    print(bytes(message))
    parser = message.split("\n")
    for mydatastring in parser:
        (tag,implier,loc1,loc2,sensor1data,sensor2data,sensor3data,sensor4data,sensor5data,sensor6data,sensor7data,sensor8data) = mydecoder.msgdecoder(mydatastring)
        urllib.urlopen('https://api.thingspeak.com/update?api_key=TWLSAPS8KORLDE1I&field1='+bytes(tag))
        urllib.urlopen('https://api.thingspeak.com/update?api_key=TWLSAPS8KORLDE1I&field2='+bytes(implier)
        urllib.urlopen('https://api.thingspeak.com/update?api_key=TWLSAPS8KORLDE1I&field3='+bytes(loc1))
        urllib.urlopen('https://api.thingspeak.com/update?api_key=TWLSAPS8KORLDE1I&field4='+bytes(loc2))
        if(sensor1data != -1):
            urllib.urlopen('https://api.thingspeak.com/update?api_key=2T4XCPR0G1SRDCBG&field1='+bytes(sensor1data))
        if(sensor2data != -1):
            urllib.urlopen('https://api.thingspeak.com/update?api_key=2T4XCPR0G1SRDCBG&field2='+bytes(sensor2data))
        if(sensor3data != -1):
            urllib.urlopen('https://api.thingspeak.com/update?api_key=2T4XCPR0G1SRDCBG&field3='+bytes(sensor3data))
        if(sensor4data != -1):
            urllib.urlopen('https://api.thingspeak.com/update?api_key=2T4XCPR0G1SRDCBG&field4='+bytes(sensor4data))
        if(sensor5data != -1):
            urllib.urlopen('https://api.thingspeak.com/update?api_key=2T4XCPR0G1SRDCBG&field5='+bytes(sensor5data))
        if(sensor6data != -1):
            urllib.urlopen('https://api.thingspeak.com/update?api_key=2T4XCPR0G1SRDCBG&field6='+bytes(sensor6data))
        if(sensor7data != -1):
            urllib.urlopen('https://api.thingspeak.com/update?api_key=2T4XCPR0G1SRDCBG&field7='+bytes(sensor7data))
        if(sensor8data != -1):
            urllib.urlopen('https://api.thingspeak.com/update?api_key=2T4XCPR0G1SRDCBG&field8='+bytes(sensor8data))
        