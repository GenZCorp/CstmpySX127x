def msgdecoder(message):
    nodeid = -1
    changedvalues = -1
    gps1 = -1
    gps2 = -1 
    moisture = -1
    ph = -1
    nit = -1
    pho=-1
    pot = -1
    disso2 = -1
    bat1 = -1
    bat2 = -1
    if(len(message)>0): # make this read multiple packets as message will include multiple reaeived data string catenated back to back
        values = message.split(",")
        nodeid = int(values[0])
        changedvalues = int(values[1])
        gps1 = int(values[2])
        gps2 = int(values[3])
        i = 4
        if((changedvalues)&(1)== 1):
            print("moisture flag found")
            moisture = int(values[i])
            i+=1
        if((changedvalues)&(2)== 2):
            print("OHHO! flag that shouldnt be found found")
            ph = int(values[i])
            i+=1
        if((changedvalues)&(4)== 4):
            print("OHHO! flag that shouldnt be found found nit")
            nit = int(values[i])
            i+=1
        if((changedvalues)&(8)== 8):
            print("OHHO! flag that shouldnt be found found pho")
            pho = int(values[i])
            i+=1
        if((changedvalues)&(16)== 16):
            print("OHHO! flag that shouldnt be found found pot")
            pot = int(values[i])
            i+=1
        if((changedvalues)&(32)== 32):
            print("OHHO! flag that shouldnt be found found dissO2")
            disso2 = int(values[i])
            i+=1
        if((changedvalues)&(64)== 64):
            print("OHHO! bat1 flag")
            bat1 = int(values[i])
            i+=1
        if((changedvalues)&(128)== 128):
            print("OHHO! bat2 flag")
            bat2 = int(values[i])
            i+=1
    else:
        print("Message not acquired by reader")
    return (nodeid,changedvalues,gps1,gps2,moisture,ph,nit,pho,pot,disso2,bat1,bat2)


