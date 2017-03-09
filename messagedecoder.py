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
        nodeid = int(message[0])
        changedvalues = int(message[1])
        gps1 = int(message[2])
        gps2 = int(message[3])
        i = 4
        if((changedvalues)&(1)== 1):
            print("moisture flag found")
            moisture = int(data[i])
            i+=1
        if((changedvalues)&(2)== 2):
            print("OHHO! flag that shouldnt be found found")
            ph = int(data[i])
            i+=1
        if((changedvalues)&(4)== 4):
            nit = int(data[i])
            i+=1
        if((changedvalues)&(8)== 8):
            pho = int(data[i])
            i+=1
        if((changedvalues)&(16)== 16):
            pot = int(data[i])
            i+=1
        if((changedvalues)&(32)== 32):
            disso2 = int(data[i])
            i+=1
        if((changedvalues)&(64)== 64):
            bat1 = int(data[i])
            i+=1
        if((changedvalues)&(128)== 128):
            bat2 = int(data[i])
            i+=1
    else:
        print("Message not acquired by reader")
    return (nodeid,changedvalues,gps1,gps2,moisture,ph,nit,pho,pot,disso2,bat1,bat2)
