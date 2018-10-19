from HslCommunication import SiemensS7Net
from HslCommunication import SiemensPLCS
from threading import Timer
from SQL import *
from Log import *

class SiemensS7:
    def printReadSiemensS7(result):
        if result.IsSuccess:
            print(result.Content)
        else:
            print("failed   "+result.Message)
    def printWriteSiemensS7(result):
        if result.IsSuccess:
            print("success")
        else:
            print("falied  " + result.Message)
    #read Siemens PLC, input para ipAddre,dataType,address,dataBity
    def readSiemensS7(ipAddress,dataType,address,dataBit):
        #open LOG file
        LOG=Logger('aicotinlog',1)
        siemens = SiemensS7Net(SiemensPLCS.S200Smart, ipAddress)
        siemens.ConnectClose()
        if siemens.ConnectServer().IsSuccess == False:
            print("connect falied")
            return ''
        else:
            LOG.debug("connect success")
            if(dataType=="byte"):
                return siemens.ReadByte(address)
            elif(dataType=="bool"):
                return siemens.ReadBool(address)
            elif(dataType=="Int16"):
                return siemens.ReadInt16(address,dataBit)
            elif(dataType=="UInt16"):
                return siemens.ReadUInt16(address,dataBit)
            elif(dataType=="Int32"):                 
                return siemens.ReadInt32(address,dataBit)
            elif(dataType=="UInt32"):
                return siemens.ReadUInt32(address,dataBit)
            elif(dataType=="Float"):                 
                return siemens.ReadFloat(address,dataBit)
            elif(dataType=="Int64"):                 
                return siemens.ReadInt64(address,dataBit)
            elif(dataType=="UInt64"):
                return siemens.ReadUInt64(address,dataBit)
            elif(dataType=="Double"):     
                return siemens.ReadDouble(address,dataBit)  
            elif(dataType=="String"):
                return siemens.ReadString(address,dataBit)
            else:
                return siemens.ReadByte(address)
    def writeSiemensS7(ipAddress,dataType,address,value):
        siemens = SiemensS7Net(SiemensPLCS.S200Smart,ipAddress)
        siemens.ConnectClose()
        if siemens.ConnectServer().IsSuccess == False:
            print("connect falied")
            return ''
        else:
            if(dataType=="byte"):
                return siemens.WrtieByte(address,value)
            elif(dataType=="bool"):
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

def readSiemensS7():
    #open LOG file
    LOG=Logger('aicotinlog',1)
    LOG.debug('readSiemensS7')
    global readSiemensS7Timer
    #get sample frequency from database
    readSiemensS7Timer = Timer(10, readSiemensS7)
    readSiemensS7Timer.start()
    #real PLC
    value=SiemensS7.readSiemensS7("192.168.31.201","Int16","M1",10)
    SiemensS7.printReadSiemensS7(value)
    value=SiemensS7.writeSiemensS7("192.168.31.201","Float","M10",9.9)
    dataSql=MYSQL("aicotin.db")
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
                value=SiemensS7.readSiemensS7(ipAddress,dataType,address,dataBits)
                #SiemensS7.printReadSiemensS7(value)          
                #insert read result into database
                if(value !=''):
                    if(value.IsSuccess==True):
                        LOG.debug(deviceId+':read PLC success, save to database')
                        dataSql.insert('Data',(deviceId,quotaId,value.Content[0]))
                    else:
                        LOG.debug(deviceId+':read PLC fail')
                else:
                    LOG.debug(deviceId+':connect PLC fail')
            else:
                LOG.debug('read no plc info from table')
    else:
       LOG.debug('no plc') 

def readSiemensS7Timer():
    readSiemensS7Timer = Timer(5, readSiemensS7)
    readSiemensS7Timer.start()
