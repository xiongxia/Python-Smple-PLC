
class ABBCartesianValue():
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
        self.q1=0
        self.q2=0
        self.q3=0
        self.q4=0
        self.j1=0
        self.j4=0
        self.j6=0
        self.jx=0
        
    def setX(self,x):
        self.x=x
    def getX(self):
        return self.x

    def setY(self,y):
        self.y=y
    def getY(self):
        return self.y

    def setZ(self,z):
        self.z=z
    def getZ(self):
        return self.z

    def setQ1(self,q1):
        self.q1=q1
    def getQ1(self):
        return self.q1

    def setQ2(self,q2):
        self.q2=q2
    def getQ2(self):
        return self.q2

    def setQ3(self,q3):
        self.q3=q3
    def getQ3(self):
        return self.q3

    def setQ4(self,q4):
        self.q4=q4
    def getQ4(self):
        return self.q4

    def setJ1(self,j1):
        self.j1=j1
    def getJ1(self):
        return self.j1

    def setJ4(self,j4):
        self.j4=j4
    def getJ4(self):
        return self.j4

    def setJ6(self,j6):
        self.j6=j6
    def getJ6(self):
        return self.j6

    def setJX(self,jx):
        self.jx=jx
    def getJX(self):
        return self.jx

    def getValue(self):
        return str(self.x)+","+str(self.y)+","+str(self.z)\
               +","+str(self.q1)+","+str(self.q2)+","+str(self.q3)+","+str(self.q4)\
               +","+str(self.j1)+","+str(self.j4)+","+str(self.j6)+","+str(self.jx)
    
class ABBSystemInformation():
    def __init__(self):
        self.systemName=""
        self.systemRwversion=""
        self.systemSysid=""
        self.systemStarttm=""
        self.systemRwversionname=""
    def setSystemName(self,systemName):
        self.systemName=systemName
    def getSystemName(self):
        return self.systemName
    def setSystemRwversion(self,systemRwversion):
        self.systemRwversion=systemRwversion
    def getSystemRwversion(self):
        return self.systemRwversion
    def setSystemSysid(self,systemSysid):
        self.systemSysid=systemSysid
    def getSystemSysid(self):
        return self.systemSysid
    def setSystemStarttm(self,systemStarttm):
        self.systemStarttm=systemStarttm
    def getSystemStarttm(self):
        return self.systemStarttm

    def getValue(self):
        return "Name:"+self.systemName+","\
               "Rwversion:"+self.systemRwversion+","\
               "Sysid:"+self.systemSysid+","\
               "Starttm:"+self.systemStarttm

class ABBRAPIDExecutionState():
    def __init__(self):
        self.ctrlexecstate=""
        self.cycle=""
    def setCtrlexecstate(self,state):
        self.ctrlexecstate=state
    def setCycle(self,cycle):
        self.cycle=cycle
    def getValue(self):
        return self.ctrlexecstate+","+self.cycle

class ABBMotionsystemErrorState():
    def __init__(self):
        self.errState=""
        self.errCount=""
    def setErrState(self,state):
        self.errState=state
    def setErrCount(self,count):
        self.errCount=count
    def getValue(self):
        return self.errState+","+self.errCount

class ABBControllerState():
    def __init__(self):
        self.ctrlstate=""
    def setCtrlstate(self,state):
        self.ctrlstate=state
    def getValue(self):
        return self.ctrlstate

class ABBControllerOperationMode():
    def __init__(self):
        self.opmode=""
    def setOpmode(self,mode):
        self.opmode=mode
    def getValue(self):
        return self.opmode

class ABBAxisPose():
    def __init__(self):
        self.x=''
        self.y=''
        self.z=''
        self.q1=''
        self.q2=''
        self.q3=''
        self.q4=''
    def setValue(self,x,y,z,q1,q2,q3,q4):
        self.x=x
        self.y=y
        self.z=z
        self.q1=q1
        self.q2=q2
        self.q3=q3
        self.q4=q4
    def getValue(self):
        return str(self.x)+","+\
               str(self.y)+","+\
               str(self.z)+","+\
               str(self.q1)+","+\
               str(self.q2)+","+\
               str(self.q3)+","+\
               str(self.q4)
