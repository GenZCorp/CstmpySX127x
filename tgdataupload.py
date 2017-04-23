import reader as rdr
import urllib
import messagedecoder as mydecoder
import time
import basicPubSub as awsuploadhandler
channel1url = 'https://api.thingspeak.com/update?api_key=TWLSAPS8KORLDE1I'
channel2url = 'https://api.thingspeak.com/update?api_key=2T4XCPR0G1SRDCBG'

def threegupload(snumber,tstamp):
    print("In upload data")
    message = rdr.msgpktformer()
    print(bytes(message))
    parser = message.split("\n")
    for mydatastring in parser: #url lib is slow also we dont know if this runs once or until all lines read?
        datacatstring = ''
        if(len(mydatastring)>0):
            (tag,implier,loc1,loc2,sensor1data,sensor2data,sensor3data,sensor4data,sensor5data,sensor6data,sensor7data,sensor8data) = mydecoder.msgdecoder(mydatastring)
            #time.sleep(1)
            #urllib.urlopen(channel1url+'&field1='+bytes(tag)+'&field2='+bytes(implier)+'&field3='+bytes(loc1)+'&field4='+bytes(loc2))
            print("tag: "+ bytes(tag))
            #time.sleep(0.5)
            #urllib.urlopen('https://api.thingspeak.com/update?api_key=TWLSAPS8KORLDE1I&field2='+bytes(implier))
            print("implier: "+ bytes(implier))
            #time.sleep(0.5)
            #urllib.urlopen('https://api.thingspeak.com/update?api_key=TWLSAPS8KORLDE1I&field3='+bytes(loc1))
            print("loc1: "+ bytes(loc1))
            datacatstring += ('\"loc1:\" \"'+bytes(loc1)+"\"\n")
            #time.sleep(0.5)
            #urllib.urlopen('https://api.thingspeak.com/update?api_key=TWLSAPS8KORLDE1I&field4='+bytes(loc2))
            print("loc2: "+ bytes(loc2))
            datacatstring += ('\"loc2:\" \"'+bytes(loc2)+"\"\n")
            #time.sleep(0.5)
            if(sensor1data != -1):
                datacatstring += ('\"sensor1data:\" \"'+bytes(sensor1data)+"\"\n")
                print("\"sensor1data:\" "+ bytes(sensor1data))
                #time.sleep(0.5)
            if(sensor2data != -1):
                datacatstring += ('\"sensor2data:\" \"'+bytes(sensor2data)+"\"\n")
                print("sensor2data: "+ bytes(sensor2data))
                #time.sleep(0.5)
            if(sensor3data != -1):
                datacatstring += ('\"sensor3data:\" \"'+bytes(sensor3data)+"\"\n")
                print("sensor3data: "+ bytes(sensor3data))
                #time.sleep(0.5)
            if(sensor4data != -1):
                datacatstring += ('\"sensor4data:\" \"'+bytes(sensor4data)+"\"\n")
                print("sensor4data: "+ bytes(sensor4data))
                #time.sleep(0.5)
            if(sensor5data != -1):
                datacatstring += ('\"sensor5data:\" \"'+bytes(sensor5data)+"\"\n")
                print("sensor5data: "+ bytes(sensor5data))
                #time.sleep(0.5)
            if(sensor6data != -1):
                datacatstring += ('\"sensor6data:\" \"'+bytes(sensor6data)+"\"\n")
                print("sensor6data: "+ bytes(sensor6data))
                #time.sleep(0.5)
            if(sensor7data != -1):
                datacatstring += ('\"sensor7data:\" \"'+bytes(sensor7data)+"\"\n")
                print("sensor7data: "+ bytes(sensor7data))
                #time.sleep(0.5)
            if(sensor8data != -1):
                datacatstring += ('\"sensor8data:\" \"'+bytes(sensor8data)+"\"\n")
                print("sensor8data: "+ bytes(sensor8data))
                #time.sleep(0.5)
            time.sleep(0.5)
            #urllib.urlopen(channel2url+datacatstring)
            awsuploadhandler.uploadtoAWS(snumber,tstamp,datacatstring)