from Http import Http
from threading import Timer
import json
from SQL import *
from Log import *

def uploadHeart():
    #open log file
    LOG=Logger(1)
    global uploadHeartTimer
    #get upload frequency from database
    uploadHeartTimer = Timer(60, uploadHeart)
    uploadHeartTimer.start()
    #get server address from database
    deviceIdSql=MYSQL("aicotin.db")
    deviceInfo=deviceIdSql.select('DeviceID')
    #get controller info
    if(len(deviceInfo)>0):
        deviceId=deviceInfo[0][0]
        serverAddr=deviceInfo[0][1]
        url = serverAddr+'/data/heart_new'
        para = {'deviceId':deviceId,'code':'0'}
        #upload controller heart
        responseOrigin=Http.PostRequest(url,para)
        if(responseOrigin!=''):
            response=json.loads(responseOrigin)
            if(response['code']==200):
                print(deviceId+':upload heart success')
                LOG.debug(deviceId+':upload heart success')
            else:
                print(deviceId+':upload heart fail'+str(response['code']))
                LOG.debug(deviceId+':upload heart fail'+str(response['code']))
    else:
        serverAddr='http://test-collection.ycxz-china.com'
    url = serverAddr+'/data/heart_new'
    #get all deviceId of PLC from database
    plcInfo=deviceIdSql.select('Cmdtable')
    #read the PLC info
    if(len(plcInfo)>0):
        #print('ddd')
        #print(plcInfo)
        #upload PLC heart
        for item in plcInfo:
            deviceId=item[0]
            para = {'deviceId':deviceId,'code':'0'}
            responseOrigin=Http.PostRequest(url,para)
            if(responseOrigin!=''):
                #upload PLC heart
                response=json.loads(Http.PostRequest(url,para))
                if(response['code']==200):
                    print(deviceId+':upload heart success')
                    LOG.debug(deviceId+':upload heart success')
                else:
                    print(deviceId+':upload heart fail'+str(response['code']))
                    LOG.debug(deviceId+':upload heart fail'+str(response['code']))
            else:
               print(url+deviceId+':upload heart fail')
               LOG.debug(url+deviceId+':upload heart fail') 
    else:   
        print('no plc need to update heart')
        LOG.debug('no plc need to update heart')
    
def updateConfig():
    #open LOG file
    LOG=Logger(1)
    global updateConfigTimer
    #get upload frequency from database
    updateConfigTimer = Timer(60, updateConfig)
    updateConfigTimer.start()
    #get server address from database
    deviceIdSql=MYSQL("aicotin.db")
    deviceInfo=deviceIdSql.select('DeviceID')
    if(len(deviceInfo)>0):
        deviceId=deviceInfo[0][0]
        serverAddr=deviceInfo[0][1]
        url = serverAddr+'/data/deviceInfo'
        #print(url)
        #get all PLC bond to the controller
        para = {'deviceId':deviceId}
        responseOrigin=Http.PostRequest(url,para)
        if(responseOrigin!=''):
            response=json.loads(responseOrigin)
            #access cloud success
            if(response['code']==200):
                data=response['data']
                if(len(data)>0):
                    #print('has plc')
                    #delete the table before insert
                    deviceIdSql.delete('Cmdtable')
                    for item in data:
                        #print(item['deviceId'])
                        if('deviceId' in item):
                            deviceId=item['deviceId']
                        else:
                            deviceId=''
                        if('address' in item):
                            address=item['address']
                        else:
                            address=''
                        if('address' in item):
                            address=item['address']
                        else:
                            address=''
                        if('queryConfiguration' in item):
                            queryConfiguration=item['queryConfiguration']
                        else:
                            queryConfiguration=''
                        if('dataType' in item):
                            dataType=item['dataType']
                        else:
                            dataType=''
                        if('dataBits' in item):
                            dataBits=item['dataBits']
                        else:
                            dataBits=''
                        if('quotaId' in item):
                            quotaId=item['quotaId']
                        else:
                            quotaId=''
                        #insert data from cloud to database
                        plcInfo=deviceIdSql.insert('Cmdtable',(deviceId,queryConfiguration,address,dataType,dataBits,quotaId,'7','8','9'))
                    print('update configuration success')
                    LOG.debug('update configuration success')
                else:
                    print('no plc')
            else:
                print(response['code'])
        else:
            print(url+deviceId+'access cloud fail')
            LOG.debug(url+deviceId+'access cloud fail')
    else:
        serverAddr='http://test-collection.ycxz-china.com'

def uploadData():
    #open LOG file
    LOG=Logger(1)
    global uploadDataTimer
    #get the frequency from database
    uploadDataTimer = Timer(60, uploadData)
    uploadDataTimer.start()
    #get the server address from database
    deviceIdSql=MYSQL("aicotin.db")
    deviceInfo=deviceIdSql.select('DeviceID')
    if(len(deviceInfo)>0):
        deviceId=deviceInfo[0][0]
        serverAddr=deviceInfo[0][1]
    else:
        serverAddr='http://test-collection.ycxz-china.com'
    #get the data that will be uploaded
    data=deviceIdSql.select('Data')
    #print(data)
    if(len(data)>0):
        #upload all PLC data
        url = serverAddr+'/data/collect_all'
        allData=''
        for item in data:
            deviceId=item[0]
            quotaId=item[1]
            value=item[2]
            allData+='{deviceId:'+str(deviceId)+',quotaId:'+str(quotaId)+',value:'+str(value)+'}'
        para = {'collectData':'['
                +allData
                +']'}
        responseOrigin=Http.PostRequest(url,para)
        if(responseOrigin!=''):
            response=json.loads(responseOrigin)
            if((response['code']==200)&(len(response['data'])==0)):
                print('upload data success')
                LOG.debug('upload data success')
            else:
                print('upload data fail')
                LOG.debug('upload data fail')
        else:
            print(url+'access cloud fail')
            LOG.debug(url+'access cloud fail')

    
def uploadHeartTimer():
    uploadHeartTimer = Timer(1, uploadHeart)
    uploadHeartTimer.start()
    
def updateConfigTimer():
    updateConfigTimer = Timer(2, updateConfig)
    updateConfigTimer.start()

def uploadDataTimer():
    uploadDataTimer = Timer(10, uploadData)
    uploadDataTimer.start()
        


    

