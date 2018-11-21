from Http import *
from XmlParser import *
import time

class ABB:
    def __init__(self,ipAddress="127.0.0.1",username="Default User",password="robotics"):
        self.ipAddress=ipAddress
        self.username=username
        self.password=password
        self.url=""
        self.data=""
    def setIP(self,ipAddress):
        self.ipAddress=ipAddress
    def getIP(self):
        return self.ipAddress
    def setUser(self,username,password):
        self.username=username
        self.password=password
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def setUrl(self,url):
        self.url="http://"+self.ipAddress+url
    def getUrl(self):
        return self.url
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data
    def getInfo(self):
        if(self.url==""):
            print("url is not set")
            return None
        hp=digestHttp(self.url,self.username,self.password)
        return hp.GET_info()
    def postInfo(self):
        if(self.data==""):
            print(" data is not set")
            return None
        if(self.url==""):
            print(" url is not set")
            return None
        hp=digestHttp(self.url,self.username,self.password)
        return hp.POST_info(self.data)

#Root Resource
def getServiceList(abb):
    abb.setUrl("/rw")
    return abb.getInfo()

#Subscription Service
def getSubscriptionActions(abb):
    abb.setUrl("/subscription?action=show")
    return abb.getInfo()

#Operations on Subscription Group
def getSubscriptionGroupActions(abb,groupId):
    abb.setUrl("/subscription/"+groupId+"?action=show")
    print(abb.getUrl())
    return abb.getInfo()

#User Service
def getUserResources(abb):
    abb.setUrl("/users")
    return abb.getInfo()

def getUserActions(abb):
    abb.setUrl("/users?action=show")
    return abb.getInfo()

#Operation on Users grants
def getUserGrants(abb):
    abb.setUrl("/users/grants")
    return abb.getInfo()

#Operations on RMMP
def getRMMPState(abb):
    abb.setUrl("/users/rmmp")
    return abb.getInfo()

def getRMMPActions(abb):
    abb.setUrl("/users/rmmp?action=show")
    return abb.getInfo()

def getPollForRMMPGrantStatus(abb):
    abb.setUrl("/users/rmmp/poll")
    return abb.getInfo()

#Operation on Remote User
def getRemoteUserActions(abb):
    abb.setUrl("/users/remoteuser?action=show")
    return abb.getInfo()

#Controller Service
def getControllerResources(abb):
    abb.setUrl("/ctrl")
    return abb.getInfo()

def getControllerActions(abb):
    abb.setUrl("/ctrl?action=show")
    return abb.getInfo()

def getControllerEnvVar(abb,envName):
    abb.setUrl("/ctrl/$"+envName)
    return abb.getInfo()

def restartOrShutdownController(abb,data):
    abb.setUrl("/ctrl")
    print(abb.getUrl())
    abb.setData(data)
    return abb.postInfo()

#Operations on Clock Resource
def getClockResource(abb):
    abb.setUrl("/ctrl/clock")
    return abb.getInfo()

def getClockActions(abb):
    abb.setUrl("/ctrl/clock?action=show")
    return abb.getInfo()

#Operation on Timezone Resource
def getTimezoneResource(abb):
    abb.setUrl("/ctrl/clock/timezone")
    return abb.getInfo()

#Operation on Identity Resource
def getIdentityResource(abb):
    abb.setUrl("/ctrl/identity")
    return abb.getInfo()

#Operation on System Resource
def getListOfInstalledSystems(abb):
    abb.setUrl("/ctrl/system")
    return abb.getInfo()

def getActionsOnSystem(abb):
    abb.setUrl("/ctrl/system?action=show")
    return abb.getInfo()

#Operations on network Resource
def getNetworkResource(abb):
    abb.setUrl("/ctrl/network")
    return abb.getInfo()

#Operation on Backup Resource
def getBackupResources(abb):
    abb.setUrl("/ctrl/backup")
    return abb.getInfo()

def getBackupActions(abb):
    abb.setUrl("/ctrl/backup?action=show")
    return abb.getInfo()

def getBackupState(abb):
    abb.setUrl("/ctrl/backup?action=backupstate")
    return abb.getInfo()

#Operations on backup system information
def getBackupSystemInformation(abb):
    return None

#Operations on Compress Resource
def getCompressResources(abb):
    abb.setUrl("/ctrl/compress")
    return abb.getInfo()

def getCompressActions(abb):
    abb.setUrl("/ctrl/compress?action=show")
    return abb.getInfo()

#Operations on Diagnostics Resource
def getDiagnosticsResources(abb):
    abb.setUrl("/ctrl/diagnostics")
    return abb.getInfo()

def getDiagnosticsActions(abb):
    abb.setUrl("/ctrl/diagnostics")
    return abb.getInfo()

#Operations on CtrlSafetyResource
def getSafetyReources(abb):
    abb.setUrl("/ctrl/safety")
    return abb.getInfo()

def getSafetyActions(abb):
    abb.setUrl("/ctrl/safety?action=show")
    return abb.getInfo()

def getConfigStatus(abb):
    abb.setUrl("/ctrl/safety?resource=config-status")
    return abb.getInfo()

def getSafetyModeStatus(abb):
    abb.setUrl("/ctrl/safety?resource=safety-mode")
    return abb.getInfo()

def getSafetyConfigurations(abb):
    abb.setUrl("/ctrl/safety?resource=safety-config")
    return abb.getInfo()

def getSafetyViolationInfo(abb):
    abb.setUrl("/ctrl/safety?resource=violation-info")
    return abb.getInfo()

#Operations on options Resource

#Operations on COmpatabile Resource
def checkRobotwareCompatibility(abb,version):
    abb.setUrl("/ctrl/compatibility/"+version);
    return abb.getInfo()

#Operation on Virtual Time
def getVirtualTimeResources(abb):
    abb.setUrl("/ctrl/virtualtime")
    return abb.getInfo()

def getVirtualtime(abb):
    abb.setUrl("/ctrl/virtualtime/vttime")
    return abb.getInfo()

def getVTTimeslice(abb):
    abb.setUrl("/ctrl/virtualtime/vttimeslice")
    return abb.getInfo()

def getActionsOnVTTimeslice(abb):
    abb.setUrl("/ctrl/virtualtime/vttimeslice?action=show")
    return abb.getInfo()

def getSpeedOfVirtualTime(abb):
    abb.setUrl("/ctrl/virtualtime/vtspeed")
    return abb.getInfo()

def getActionsOnVTSpeed(abb):
    abb.setUrl("/ctrl/virtualtime/vtspeed")
    return abb.getInfo()

def getStateOfVirtualTime(abb):
    abb.setUrl("/ctrl/virtualtime/vtstate")
    return abb.getInfo()

def getActionsOnVTState(abb):
    abb.setUrl("/ctrl/virtualtime/vtstate?action=show")
    return abb.getInfo()

#File service
def getFileServiceResources(abb):
    abb.setUrl("/fileservice")
    return abb.getInfo()

#Get RobotWare services
def getRobotWareServices(abb):
    abb.setUrl("/rw")
    return abb.getInfo()

#CFG service
def getCFGResources(abb):
    abb.setUrl("/rw/cfg")
    return abb.getInfo()

#DIPC service
def getDIPCResources(abb):
    abb.setUrl("/rw/dipc")
    return abb.getInfo()

def getDIPCActions(abb):
    abb.setUrl("/rw/dipc")
    return abb.getInfo()

#Operations on DIPC Queue
def getDIPCQueue(abb):
    return None

#Elog service
def getElogResources(abb):
    abb.setUrl("/rw/elog")
    return abb.getInfo()

def getElogActions(abb):
    abb.setUrl("/rw/elog")
    return abb.getInfo()

#Operations on elog domian
def getElogMessagesInDomain(abb,domain_number):
    abb.setUrl("/rw/elog/"+domain_number+"?lang=en")
    return abb.getInfo()

#IO service
def getIOSystemResources(abb):
    abb.setUrl("/rw/iosystem")
    return abb.getInfo()

#Operations on IO Networks
def getIONetworksResources(abb):
    abb.setUrl("/rw/iosytem/networks")
    return abb.getInfo()
def getActionsOnIONetworks(abb):
    abb.setUrl("/rw/iosystem/networks?action=show")
    return abb.getInfo()

#Panel service
def getPanelResources(abb):
    abb.setUrl("/rw/panel")
    return abb.getInfo()

#Operations on Controller State Resource
def getControllerState(abb):
    abb.setUrl("/rw/panel/ctrlstate")
    return abb.getInfo()

#Operations on Operation Mode Resource
def getOperationMode(abb):
    abb.setUrl("/rw/panel/opmode")
    return abb.getInfo()

#Operatons on Speed Ratio Resource
def getSpeedRatio(abb):
    abb.setUrl("/rw/panel/speedratio")
    return abb.getInfo()

#Operations on Collision Detection State
def getCollisionDetectionState(abb):
    abb.setUrl("/rw/panel/coldetstate")
    return abb.getInfo()


#RAPID services##############################################

def getRAPIDSystemResources(abb):
    abb.setUrl("/rw/rapid")
    return abb.getInfo()

#Operation on RAPID execution
def getRAPIDExecutionState(abb):
    abb.setUrl("/rw/rapid/execution")
    return abb.getInfo()

def getRAPIDExecutionActions(abb):
    abb.setUrl("/rw/rapid/execution?action=show")
    return abb.getInfo()

def startRAPIDExecution(abb,data):
    abb.setUrl("/rw/rapid/execution?action=start")
    abb.setData(data)
    return abb.postInfo()

def stopRAPIDExecution(abb,data):
    abb.setUrl("/rw/rapid/execution?action=stop")
    abb.setData(data)
    return abb.postInfo()

#Operations on RAPID modules
def getRAPIDModulesAction(abb):
    abb.setUrl("/rw/rapid/modules?action=show")
    return abb.getInfo()

def getRAPIDModules(abb,task):
    abb.setUrl("/rw/rapid/modules?task="+task)
    return abb.getInfo()

def getModPossibleAll(abb):
    abb.setUrl("/rw/rapid/modules?resource=mod-possible-all")
    return abb.getInfo()

#Operations on rapid module
def getSpecifiedRangeOfText(abb,module,task,startRow,startColum,endRow,endColum):
    abb.setUrl("/rw/rapid/modules/"+module+"?task="+task+"&startrow="+startRow+"&startcol="+startColum+"&endrow="+endRow+"&endcol="+endColum)
    return abb.getInfo()

def getRapidModuleActions(abb,module):
    abb.setUrl("/rw/rapid/modules/"+module+"?action=show")
    return abb.getInfo()

def getRAPIDModuleAttributes(abb,module,task):
    abb.setUrl("/rw/rapid/modules/"+module+"?task="+task)
    return abb.getInfo()

def getChangeCount(abb,module,task):
    abb.setUrl("/rw/rapid/modules/"+module+"?resource=change-count&task="+task)
    return abb.getInfo()

#Operations on RAPID Routine


#System service
def getSystemInformation(abb):
    abb.setUrl("/rw/system")
    return abb.getInfo()

#Robotware return codes service
def getListOfReturnCodes(abb):
    abb.setUrl("/rw/retcode")
    return abb.getInfo()

def getDescriptionOfReturnCode(abb,code):
    abb.setUrl("/rw/retcode?code="+code)
    abb.getInfo()

#Devices service
def getDevicesTreeInformation(abb):
    abb.setUrl("/rw/devices")
    return abb.getInfo()

#Motion system
def getMotionSystem(abb):
    abb.setUrl("/rw/motionsystem")
    return abb.getInfo()

def getMotionSystemAction(abb):
    abb.setUrl("/rw/motionsystem?action=show")
    return abb.getInfo()

#Operations on Error State
def getMotionsytemErrorState(abb):
    abb.setUrl("/rw/motionsystem/errorstate")
    return abb.getInfo()

#Operation on Motion Supervision
def getMotionSupervision(abb,mechunit):
    abb.setUrl("/rw/motionsystem/motionsupervision?mechunit="+mechunit)
    return abb.getInfo()

def getMotionSupervisionCollisionPredictionMode(abb):
    abb.setUrl("/rw/motionsystem/motionsupervision?action=collison-prediction-mode")
    return abb.getInfo()

#Operations on Path Supervision
def getPathSupervision(abb,mechunit):
    abb.setUrl("/rw/motionsystem/pathsupervision?mechunit="+mechunit)
    return abb.getInfo()

#Operations on Mechunits
def getMechunits(abb):
    abb.setUrl("/rw/motionsystem/mechunits")
    return abb.getInfo()

#Operation on Mechunit
def getMechunit(abb,mechunit,continueOnErr,resource):
    abb.setUrl("/rw/motionsystem/mechunits/"+mechunit+"?continue-on-err="+continueOnErr+"&resource="+resource)
    return abb.getInfo()

def getPhysicalJoints(abb,module):
    abb.setUrl("/rw/motionsystem/mechunits/"+module+"/pjoints")
    return abb.getInfo()

def getCartesianValue(abb,mechunit,tool,wobj,coordinate,elogAtErr):
    abb.setUrl("/rw/motionsystem/mechunits/"+mechunit+"/cartesian?tool"+tool+"&wobj"+wobj+"&coordinate="+coordinate+"&elog-at-err="+elogAtErr)
    return abb.getInfo()

def getRobtarget(abb,mechunit,tool,wobj,coordinate):
    abb.setUrl("/rw/motionsystem/mechunits/"+mechunit+"/robtarget?tool"+tool+"&wobj"+wobj+"&coordinate="+coordinate)
    return abb.getInfo()

def getJointTarget(abb,mechunit):
    abb.setUrl("/rw/motionsystem/mechunits/"+mechunit+"/jointtarget")
    return abb.getInfo()

#Operations on Axes
def getAxes(abb,mechunit):
    abb.setUrl("/rw/motionsystem/mechunits/"+mechunit+"/axes")
    return abb.getInfo()

def getAxis(abb,mechunit,axis):
    abb.setUrl("/rw/motionsystem/mechunits/"+mechunit+"/axes/"+axis)
    return abb.getInfo()

def getAxisActions(abb,mechunit,axis):
    abb.setUrl("/rw/motionsystem/mechunits/"+mechunit+"/axes/"+axis+"?action=show&json=1")
    return abb.getInfo()

def getAxisPose(abb,mechunit,axis):
    abb.setUrl("/rw/motionsystem/mechunits/"+mechunit+"/axes/"+axis+"?resource=axis-pose")
    return abb.getInfo()

#Operation on SMB Data
def getSMBData(abb,mechunit):
    abb.setUrl("/rw/motionsystem/mechunits/"+mechunit+"/smbdata")
    return abb.getInfo()

def getSMBDataActions(abb,mechunit):
    abb.setUrl("/rw/motionsystem/mechunits/"+mechunit+"/smbdata?action=show")
    return abb.getInfo()

#Operations on Motor Calib
def getMotorCalibNames(abb,mechunit):
    abb.setUrl("/rw/motionsystem/mechunits/"+mechunit+"/motorcalib")
    return abb.getInfo()

#Integrated Vision Service
def getVisionManagerResource(abb):
    abb.setUrl("/rw/vision")
    return abb.getInfo()

def getNumberOfCamerasOfIV(abb):
    abb.setUrl("/rw/vision?resource=num-of-cameras")
    return abb.getInfo()

def getIVCameraValidity(abb,cameraName):
    abb.setUrl("/rw/vision?resource=camera-validity&name="+cameraName)
    return abb.getInfo()


##################################test#################################
def readABBTest():
    abb=ABB()
    abb.setIP("127.0.0.1")
    abb.setUser("Default User","robotics")

    #getServiceList(abb)
    #print("****************************")
    #getSubscriptionActions(abb)
    #getSubscriptionGroupActions(abb,"1")
    #subscribeOnResources(abb,b'resources=1&1=/rw/rapid/symbol/data/RAPID/T_ROB1/uimsg/PNum;value&1-p=2')

    #getUserResources(abb)
    #getUserActions(abb)
    #getUserGrants(abb)
    #getRMMPState(abb)
    #getRMMPActions(abb)
    #getPollForRMMPGrantStatus(abb)
    #getRemoteUserActions(abb)
    #getControllerResources(abb)
    #getControllerActions(abb)
    #getControllerEnvVar(abb,"TEMP")
    #getControllerEnvVar(abb,"HOME")
    #getControllerEnvVar(abb,"BACKUP")
    #restartOrShutdownController(abb,b'restart-mode=xstart')
    #getClockResource(abb)
    #getClockActions(abb)
    #getTimezoneResource(abb)
    #getIdentityResource(abb)
    #getListOfInstalledSystems(abb)
    #getActionsOnSystem(abb)
    #getNetworkResource(abb)
    #getBackupResources(abb)
    #getBackupActions(abb)
    #getBackupState(abb)
    #getCompressResources(abb)
    #getCompressActions(abb)
    #getDiagnosticsResources(abb)
    #getSafetyReources(abb)
    #getSafetyActions(abb)
    #getConfigStatus(abb)
    #getSafetyModeStatus(abb)
    #getSafetyConfigurations(abb)
    #checkRobotwareCompatibility(abb,"6.07.01")
    #getVirtualTimeResources(abb)
    #getVirtualtime(abb)
    #getVTTimeslice(abb)
    #getActionsOnVTTimeslice(abb)
    #getSpeedOfVirtualTime(abb)
    #getActionsOnVTSpeed(abb)
    #getStateOfVirtualTime(abb)
    #getActionsOnVTState(abb)

    #getRAPIDSystemResources(abb)
    #getRAPIDExecutionState(abb)
    #getRAPIDExecutionActions(abb)
    #stopRAPIDExecution(abb,b'stopmode=stop&usetsp=normal')
    #startRAPIDExecution(abb,b'regain=clear&execmode=continue&cycle=forever&condition=none&stopatbp=disabled&alltaskbytsp=false')
    #getRAPIDModulesAction(abb)
    #getRAPIDModules(abb,"T_ROB1")
    #getModPossibleAll(abb)
    #getSpecifiedRangeOfText(abb,"module1","T_ROB1","1","1","50","-1")
    #getRapidModuleActions(abb,"module1")
    #getRAPIDModuleAttributes(abb,"module1","T_ROB1")
    #getChangeCount(abb,"module1","T_ROB1")
    #getMotionSystem(abb)
    #getMotionSystemAction(abb)
    #getMechunits(abb)
    #getMechunit(abb,"ROB_1","1","tool")
    #getPhysicalJoints(abb,"ROB_1")
    #getRobtarget(abb,"ROB_1","tool0","wobj1","Base")
    #getAxes(abb,"ROB_1")
    #getAxis(abb,"ROB_1","1")
    #getAxis(abb,"ROB_1","2")
    #getAxis(abb,"ROB_1","3")
    #getAxis(abb,"ROB_1","4")
    #getAxis(abb,"ROB_1","5")
    #getAxis(abb,"ROB_1","6")
    #getAxisActions(abb,"ROB_1","1")
    #getSMBData(abb,"ROB_1")
    #getSMBDataActions(abb,"ROB_1")
    #getMotorCalibNames(abb,"ROB_1")
    #getVisionManagerResource(abb)
    #getNumberOfCamerasOfIV(abb)
    #getIVCameraValidity(abb,"camera1")

    #read system information
    resp=getSystemInformation(abb)
    if(resp!=""):
        xmlParserOfSystemInformation(resp)

    #controller state
    resp=getControllerState(abb)
    if(resp!=''):
        xmlParserOfControllerState(resp)

    #controller operation mode
    resp=getOperationMode(abb)
    if(resp!=''):
        xmlParserOfControllerOperationMode(resp)

    #get Elog Message the controller
    print(getElogMessagesInDomain(abb,"0"))

    #diagnostics

    #get RAPID Excecution state
    resp=getRAPIDExecutionState(abb)
    if(resp!=""):
        xmlParserOfRAPIDExecutionState(resp)

    #get Error state
    resp=getMotionsytemErrorState(abb)
    if(resp!=""):
        xmlParserOfMotionsystemErrorState(resp)

    #get Axis position
    resp=getAxisPose(abb,"ROB_1","1")
    if(resp!=""):
        xmlParserOfAxisPose(resp)
    resp=getAxisPose(abb,"ROB_1","2")
    if(resp!=""):
        xmlParserOfAxisPose(resp)
    resp=getAxisPose(abb,"ROB_1","3")
    if(resp!=""):
        xmlParserOfAxisPose(resp)
    resp=getAxisPose(abb,"ROB_1","4")
    if(resp!=""):
        xmlParserOfAxisPose(resp)
    resp=getAxisPose(abb,"ROB_1","5")
    if(resp!=""):
        xmlParserOfAxisPose(resp)
    resp=getAxisPose(abb,"ROB_1","6")
    if(resp!=""):
        xmlParserOfAxisPose(resp)

    #read the coordination of current point
    count=0
    while count<5:
        resp=getCartesianValue(abb,"ROB_1","too10","wobj0","Base","0")
        if(resp!=''):
            xmlParserOfCartesianValue(resp)
        count=count+1
        time.sleep(1)        
    
    

readABBTest()
