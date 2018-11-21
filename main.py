from HttpAccessCloud import *
from SiemensS7 import readSiemensS7Timer
from SQL import *
from Log import *
import sys
        
if __name__ == "__main__":

    #init LOG
    LOG=Logger('aicotinlog',0)

    #init database
    MYSQL('aicotin.db')
    
    deviceIdSql=MYSQL('aicotin.db')
	
    if len(sys.argv)>1:
        deviceIdSql.delete('IMEIInfo')
        LOG.debug('update IMEIInfo')
        IMEIValue=sys.argv[1]
        serverIndex= sys.argv[2]
        if serverIndex=='1':
            deviceIdSql.insert('IMEIInfo',(IMEIValue,'http://test-collection.ycxz-china.com'))
        else:
            deviceIdSql.insert('IMEIInfo',(IMEIValue,'http://online-collection.ycxz-china.com'))
        LOG.debug(deviceIdSql.select('IMEIInfo'))
    else:
        LOG.debug(deviceIdSql.select('IMEIInfo'))

    #getControllerInfo
    getControllerInfoTimer()
    #upload heart 
    uploadHeartTimer()
    #update configuration
    updateConfigTimer()
    #read PLC data
    readSiemensS7Timer()
    #upload data to cloud
    uploadDataTimer()
    

    

