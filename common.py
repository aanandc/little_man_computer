DEBUGFLAG = False

def log(stmt):
    if DEBUGFLAG:
        print(stmt)

def readfile(filename):
    f=open(filename,'r')
    lines = f.readlines()
    #Now we have all the lines , start processing
    f.close()
    return lines
