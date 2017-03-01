def msgdecoder(message):
    nodeid = message[0]
    changedvalues = message[1]
    gps1 = message[2]
    gps2 = message[3] 
    i = 4
    moisture = -1,ph = -1,nit = -1,pho=-1,pot = -1,disso2 = -1,bat1 = -1, bat2 = -1
    if((changedvalues)&(0x01)== 0x01):
        moisture = data[i]
        i+=1
    if((changedvalues)&(0x02)== 0x02):
        ph = data[i]
        i+=1
    if((changedvalues)&(0x04)== 0x04):
        nit = data[i]
        i+=1
    if((changedvalues)&(0x08)== 0x08):
        pho = data[i]
        i+=1
    if((changedvalues)&(0x10)== 0x10):
        pot = data[i]
        i+=1
    if((changedvalues)&(0x20)== 0x20):
        disso2 = data[i]
        i+=1
    if((changedvalues)&(0x40)== 0x40):
        bat1 = data[i]
        i+=1
    if((changedvalues)&(0x80)== 0x80):
        bat2 = data[i]
        i+=1
    return (nodeid,changedvalues,gps1,gps2,moisture,ph,nit,pho,pot,disso2,bat1,bat2)
    