def msgpktformer():
    linenum = -1
    message = ""

    with open('wsndata.txt','r') as myfile:
        for num,line in enumerate(myfile,1):
                if '::::' in line:
                    linenum= num  
        print("linenumber from last acquire "+bytes(linenum))              
        if (linenum!= -1):
            for mynum,myline in enumerate(myfile,1):
                if mynum > (linenum+1): #+1 bcz time also takes a line slot
                    message+=myline
    print("message from last acquire:"+message)
    myfile.close()
    return message