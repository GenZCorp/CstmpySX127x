def msgpktformer():
    linenum = -1
    message = ""

    with open('wsndata.txt','r' as myfile)
        for num,line in enumerate(myfile,1):
                if '::::' in line:
                    linenum= num                
        if (linenum!= -1)
            for mynum,myline in enumerate(myfile,1):
                if mynum > linenum:
                    message+=myline
    file.close()
    return message