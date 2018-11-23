from HslCommunication import SiemensS7Net
from HslCommunication import SiemensPLCS
from threading import Timer
import sys
sys.path.append('../../sql')
from SQL import *
sys.path.append('../../log')
from Log import *

class SiemensS7:
    def __init__(self,ip,s7Type):
        self.ip=ip
        self.s7Type=s7Type
        self.siemens=SiemensS7Net(self.s7Type, self.ip)
        #close connect first
        self.siemens.ConnectClose()
        self.isConnect=False
        #log
        self.LOG=Logger('aicotinlog',1)
        if self.siemens.ConnectServer().IsSuccess == False:
            print("connect fail")
            self.LOG.debug("connect fail")
            self.isConnect=False
        else:
            print("connect success")
            self.LOG.debug("connect success"+self.ip)
            self.isConnect=True

    def closeConnect(self):
        self.siemens.ConnectClose()
        
    def printReadSiemensS7(self,result):
        if result.IsSuccess:
            print(result.Content)
        else:
            print("failed   "+result.Message)
            
    def printWriteSiemensS7(self,result):
        if result.IsSuccess:
            print("success")
        else:
            print("falied  " + result.Message)
            
    #read Siemens PLC, input para ,dataType,address,dataBity
    def readSiemensS7(self,dataType,address,length=None):
        siemens = self.siemens
        #connect server
        if self.isConnect == True:
            self.LOG.debug("connect success")
            print("connect success")
            if(dataType=="byte"):
                return siemens.ReadByte(address)
            elif(dataType=="bool"):
                print("read bool")
                self.LOG.debug("read bool")
                return siemens.ReadBool(address)
            elif(dataType=="Int16"):
                self.LOG.debug("read Int16")
                return siemens.ReadInt16(address,length)
            elif(dataType=="UInt16"):
                print("read UInt16")
                return siemens.ReadUInt16(address,length)
            elif(dataType=="Int32"):                 
                return siemens.ReadInt32(address,length)
            elif(dataType=="UInt32"):
                return siemens.ReadUInt32(address,length)
            elif(dataType=="Float"):                 
                return siemens.ReadFloat(address,length)
            elif(dataType=="Int64"):                 
                return siemens.ReadInt64(address,length)
            elif(dataType=="UInt64"):
                return siemens.ReadUInt64(address,length)
            elif(dataType=="Double"):     
                return siemens.ReadDouble(address,length)  
            elif(dataType=="String"):
                return siemens.ReadString(address,length)
            else:
                return siemens.ReadByte(address,length)
        else:
            print("connec fail")
            self.LOG.debug("connec fail")
            return ''

    def readSiemensS7Bool(self,address):
        value=self.readSiemensS7("bool",address)
        if(value!=''):
            if(value.IsSuccess):
                return value.Content
            else:
                return ''
        else:
            return ''
        
    def readSiemensS7Byte(self,address):
        value=self.readSiemensS7("byte",address)
        if(value!=''):
            if(value.IsSuccess):
                return value.Content
            else:
                return ''
        else:
            return ''

    def readSiemensS7UInt16(self,address,length=None):
        if(length!=None):
            value=self.readSiemensS7("UInt16",address,length)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''
        else:
            value=self.readSiemensS7("UInt16",address)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''

    def readSiemensS7Int16(self,address,length=None):
        if(length!=None):
            value=self.readSiemensS7("Int16",address,length)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''
        else:
            value=self.readSiemensS7("Int16",address)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''
        
    def readSiemensS7Int32(self,address,length=None):
        if(length!=None):
            value=self.readSiemensS7("Int32",address,length)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''
        else:
            value=self.readSiemensS7("Int32",address)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''            
        
    def readSiemensS7UInt32(self,address,length=None):
        if(length!=None):
            value=self.readSiemensS7("UInt32",address,length)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''
        else:
            value=self.readSiemensS7("UInt32",address)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''

    def readSiemensS7Float(self,address,length=None):
        if(length!=None):
            value=self.readSiemensS7("Float",address,length)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''
        else:
            value=self.readSiemensS7("Float",address)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''            

    def readSiemensS7Int64(self,address,length=None):
        if(length!=None):
            value=self.readSiemensS7("Int64",address)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''
        else:
            value=self.readSiemensS7("Int64",address)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''           

    def readSiemensS7UInt64(self,address,length=None):
        if(length!=None):
            value=self.readSiemensS7("UInt64",address,length)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''
        else:
            value=self.readSiemensS7("UInt64",address)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return '' 

    def readSiemensS7Double(self,address,length=None):
        if(length!=None):
            value=self.readSiemensS7("Double",address,length)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''
        else:
            value=self.readSiemensS7("Double",address)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return '' 

    def readSiemensS7String(self,address,length=None):
        if(length!=None):
            value=self.readSiemensS7("String",address,length)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return ''
        else:
            value=self.readSiemensS7("String",address,1)
            if(value!=''):
                if(value.IsSuccess):
                    return value.Content
                else:
                    return ''
            else:
                return '' 
        
    def writeSiemensS7(self,dataType,address,value):
        siemens=self.siemens
        if self.isConnect == True:
            print("connect success")
            self.LOG.debug("connect success")
            if(dataType=="byte"):
                return siemens.WriteByte(address,value)
            elif(dataType=="bool"):
                print("write bool")
                return siemens.WriteBool(address,value)
            elif(dataType=="Int16"):
                return siemens.WriteInt16(address,value)
            elif(dataType=="UInt16"):
                return siemens.WriteUInt16(address,value)
            elif(dataType=="Int32"):                 
                return siemens.WriteInt32(address,value)
            elif(dataType=="UInt32"):
                return siemens.WriteUInt32(address,value)
            elif(dataType=="Float"):                 
                return siemens.WriteFloat(address,value)
            elif(dataType=="Int64"):                 
                return siemens.WriteInt64(address,value)
            elif(dataType=="UInt64"):
                return siemens.WriteUInt64(address,value)
            elif(dataType=="Double"):     
                return siemens.WriteDouble(address,value)  
            elif(dataType=="String"):
                return siemens.WriteString(address,value)
            else:
                return siemens.WriteByte(address,value)
        else:
            print("connect fail")
            self.LOG.debug("connect fail")
            return ''

    def writeSiemensS7Bool(self,address,value):
        value=self.writeSiemensS7("bool",address,value)
        if(value!=''):
            if value.IsSuccess == True:
                print("write success")
                self.LOG.debug("write success")
            else:
                print(value.Message)
                self.LOG.debug(value.Message)
        else:
            print("write fail")
            self.LOG.debug("write fail")


    def writeSiemensS7Byte(self,address,value):
        value=self.writeSiemensS7("byte",address,value)
        if(value!=''):
            if value.IsSuccess == True:
                print("write success")
                self.LOG.debug("write success")
            else:
                print(value.Message)
                self.LOG.debug(value.Message)
        else:
            print("write fail")
            self.LOG.debug("write fail")

    def writeSiemensS7Int16(self,address,value):
        value=self.writeSiemensS7("Int16",address,value)
        if(value!=''):
            if value.IsSuccess == True:
                print("write success")
                self.LOG.debug("write success")
            else:
                print(value.Message)
                self.LOG.debug(value.Message)
        else:
            print("write fail")
            self.LOG.debug("write fail")

    def writeSiemensS7UInt16(self,address,value):
        value=self.writeSiemensS7("UInt16",address,value)
        if(value!=''):
            if value.IsSuccess == True:
                print("write success")
                self.LOG.debug("write success")
            else:
                print(value.Message)
                self.LOG.debug(value.Message)
        else:
            print("write fail")
            self.LOG.debug("write fail")

    def writeSiemensS7Int32(self,address,value):
        value=self.writeSiemensS7("Int32",address,value)
        if(value!=''):
            if value.IsSuccess == True:
                print("write success")
                self.LOG.debug("write success")
            else:
                print(value.Message)
                self.LOG.debug(value.Message)
        else:
            print("write fail")
            self.LOG.debug("write fail")

    def writeSiemensS7UInt32(self,address,value):
        value=self.writeSiemensS7("UInt32",address,value)
        if(value!=''):
            if value.IsSuccess == True:
                print("write success")
                self.LOG.debug("write success")
            else:
                print(value.Message)
                self.LOG.debug(value.Message)
        else:
            print("write fail")
            self.LOG.debug("write fail")

    def writeSiemensS7Int64(self,address,value):
        value=self.writeSiemensS7("Int64",address,value)
        if(value!=''):
            if value.IsSuccess == True:
                print("write success")
                self.LOG.debug("write success")
            else:
                print(value.Message)
                self.LOG.debug(value.Message)
        else:
            print("write fail")
            self.LOG.debug("write fail")

    def writeSiemensS7UInt64(self,address,value):
        value=self.writeSiemensS7("UInt64",address,value)
        if(value!=''):
            if value.IsSuccess == True:
                print("write success")
                self.LOG.debug("write success")
            else:
                print(value.Message)
                self.LOG.debug(value.Message)
        else:
            print("write fail")
            self.LOG.debug("write fail")

    def writeSiemensS7Float(self,address,value):
        value=self.writeSiemensS7("Float",address,value)
        if(value!=''):
            if value.IsSuccess == True:
                print("write success")
                self.LOG.debug("write success")
            else:
                print(value.Message)
                self.LOG.debug(value.Message)
        else:
            print("write fail")
            self.LOG.debug("write fail")

    def writeSiemensS7Double(self,address,value):
        value=self.writeSiemensS7("Double",address,value)
        if(value!=''):
            if value.IsSuccess == True:
                print("write success")
                self.LOG.debug("write success")
            else:
                print(value.Message)
                self.LOG.debug(value.Message)
        else:
            print("write fail")
            self.LOG.debug("write fail")

    def writeSiemensS7String(self,address,value):
        value=self.writeSiemensS7("String",address,value)
        if(value!=''):
            if value.IsSuccess == True:
                print("write success")
                self.LOG.debug("write success")
            else:
                print(value.Message)
                self.LOG.debug(value.Message)
        else:
            print("write fail")
            self.LOG.debug("write fail")

def readSiemensS7Cyclic():
    #open LOG file
    LOG=Logger('aicotinlog',1)
    LOG.debug('readSiemensS7')
    
    dataSql=MYSQL("aicotin.db")
    
    global readSiemensS7Timer
    #get sample frequency from database
    controllerInfo=dataSql.select('ControllerInfo')
    collectionFreq=controllerInfo[0][2]
    readSiemensS7Timer = Timer(10, readSiemensS7Cyclic)
    readSiemensS7Timer.start()
    
    plcInfo=dataSql.select('Cmdtable')
    #print(len(plcInfo))
    if(len(plcInfo)>0):
        dataSql.delete('Data')
        for item in plcInfo:
            if(item[1]!=''):
                LOG.debug('read plc info from table')
                deviceId=item[0]
                ipAddress=item[1]
                address=item[2]
                dataType=item[3]
                dataBits=item[4]
                quotaId=item[5]
                siemensDevice=SiemensS7(ipAddress,SiemensPLCS.S1200)
                value=siemensDevice.readSiemensS7Bool(address)
                siemensDevice.closeConnect()
                if(value !=''):
                    LOG.debug(deviceId+':read PLC success, save to database')
                    dataSql.insert('Data',(deviceId,quotaId,value))
                else:
                    LOG.debug(deviceId+':read PLC fail')
            else:
                LOG.debug('read no plc info from table')
    else:
       LOG.debug('no plc') 

def readSiemensS7Timer():
    readSiemensS7Timer = Timer(5, readSiemensS7Cyclic)
    readSiemensS7Timer.start()



def testCase():
    siemensDevice=SiemensS7("192.168.2.5",SiemensPLCS.S1200)
    data00=siemensDevice.readSiemensS7Bool("DB1.0")
    data01=siemensDevice.readSiemensS7Bool("DB1.0.1")
    data02=siemensDevice.readSiemensS7Bool("DB1.0.2")
    data03=siemensDevice.readSiemensS7Bool("DB1.0.3")
    data04=siemensDevice.readSiemensS7Bool("DB1.0.4")
    data05=siemensDevice.readSiemensS7Bool("DB1.0.5")
    data06=siemensDevice.readSiemensS7Bool("DB1.0.6")
    data07=siemensDevice.readSiemensS7Bool("DB1.0.7")

    dataByte=siemensDevice.readSiemensS7Byte("DB1.1")
    dataUInt16=siemensDevice.readSiemensS7UInt16("DB1.0")
    dataInt16=siemensDevice.readSiemensS7Int16("DB1.0")
    dataUInt32=siemensDevice.readSiemensS7UInt32("DB1.0")
    dataInt32=siemensDevice.readSiemensS7Int32("DB1.0")
    dataUInt64=siemensDevice.readSiemensS7UInt64("DB1.0")
    dataInt64=siemensDevice.readSiemensS7Int64("DB1.0")    
    dataFloat=siemensDevice.readSiemensS7Float("DB1.0")
    dataDouble=siemensDevice.readSiemensS7Double("DB1.0")
    dataString=siemensDevice.readSiemensS7String("DB1.0",1)
    
    print(data00)
    print(data01)
    print(data02)
    print(data03)
    print(data04)
    print(data05)
    print(data06)
    print(data07)
    
    print(dataByte)
    print(dataUInt16)
    print(dataInt16)
    print(dataUInt32)
    print(dataInt32)
    print(dataUInt64)
    print(dataInt64)
    print(dataFloat)
    print(dataDouble)
    print(dataString)

    print("*****************")

    siemensDevice.writeSiemensS7Bool("DB5.0.31",True)
    data00=siemensDevice.readSiemensS7Bool("DB5.0.31")
    
    siemensDevice.writeSiemensS7Byte("DB1.0",3)
    dataByte=siemensDevice.readSiemensS7Byte("DB1.1")
    
    siemensDevice.writeSiemensS7Int16("DB3.0",33)
    dataInt16=siemensDevice.readSiemensS7Int16("DB3.0",2)
    siemensDevice.writeSiemensS7UInt16("DB3.0",6565)
    dataUInt16=siemensDevice.readSiemensS7UInt16("DB3.0")
    
    siemensDevice.writeSiemensS7Int32("DB5.0",589)
    dataInt32=siemensDevice.readSiemensS7Int32("DB5.0")
    
    siemensDevice.writeSiemensS7UInt32("DB3.0",7)
    dataUInt32=siemensDevice.readSiemensS7UInt32("DB3.0")
    
    siemensDevice.writeSiemensS7Int64("DB4.0",31)
    dataInt64=siemensDevice.readSiemensS7Int64("DB4.0") 
    dataUInt322=siemensDevice.readSiemensS7UInt32("DB4.0",2)
    
    siemensDevice.writeSiemensS7UInt64("DB4.0",34)
    dataUInt64=siemensDevice.readSiemensS7UInt64("DB4.0")

    siemensDevice.writeSiemensS7Float("DB4.0",34.09)
    dataFloat=siemensDevice.readSiemensS7Float("DB4.0",2)

    siemensDevice.writeSiemensS7Double("DB4.0",34.09)
    dataDouble=siemensDevice.readSiemensS7Double("DB4.0")

    siemensDevice.writeSiemensS7String("DB4.0",'abcdefgh')
    dataString=siemensDevice.readSiemensS7String("DB4.0",8)
    dataString1=siemensDevice.readSiemensS7String("DB4.0")

    data01=siemensDevice.readSiemensS7Bool("DB5.0.1")
    data02=siemensDevice.readSiemensS7Bool("DB5.0.2")
    data03=siemensDevice.readSiemensS7Bool("DB5.0.3")
    data04=siemensDevice.readSiemensS7Bool("DB5.0.4")
    data05=siemensDevice.readSiemensS7Bool("DB5.0.5")
    data06=siemensDevice.readSiemensS7Bool("DB5.0.6")
    data07=siemensDevice.readSiemensS7Bool("DB5.0.7")
   
    print(data00)
    print(data01)
    print(data02)
    print(data03)
    print(data04)
    print(data05)
    print(data06)
    print(data07)
    
    print(dataByte)
    print(dataUInt16)
    print(dataInt16)
    print(dataUInt32)
    print(dataInt32)
    print(dataUInt64)
    print(dataInt64)
    print(dataUInt322)
    print(dataFloat)
    print(dataDouble)
    print(dataString)
    print(dataString1)
    

    siemensDevice.closeConnect()
