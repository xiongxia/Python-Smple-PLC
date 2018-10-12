from HttpAccessCloud import uploadHeartTimer
from HttpAccessCloud import updateConfigTimer
from SiemensS7 import readSiemensS7Timer
from HttpAccessCloud import uploadDataTimer
from SQL import *
from Log import *
import sys
        
if __name__ == "__main__":

    #init LOG
    LOG=Logger(0)

    #init database
    MYSQL("aicotin.db")
    
    deviceIdSql=MYSQL("aicotin.db")
	
    if len(sys.argv)>1:
        deviceIdSql.delete('DeviceID')
        LOG.debug('update DeviceId')
        deviceId=sys.argv[1]
        serverIndex= sys.argv[2]
        if serverIndex=='1':
            deviceIdSql.insert('DeviceID',(deviceId,'http://test-collection.ycxz-china.com'))
        else:
            deviceIdSql.insert('DeviceID',(deviceId,'http://online-collection.ycxz-china.com'))
        LOG.debug(deviceIdSql.select('DeviceID'))
    else:
        LOG.debug(deviceIdSql.select('DeviceID'))
                                                  
    #upload heart 
    uploadHeartTimer()
    #update configuration
    updateConfigTimer()
    #read PLC data
    readSiemensS7Timer()
    #upload data to cloud
    uploadDataTimer()
    

    

