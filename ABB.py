from Http import *

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

def getServiceList(abb):
    abb.setUrl("/rw")
    return abb.getInfo()

def getSubscriptionActions(abb):
    abb.setUrl("/subscription?action=show")
    return abb.getInfo()

def getSubscriptionGroupActions(abb,groupId):
    abb.setUrl("/subscription/"+groupId+"?action=show")
    print(abb.getUrl())
    return abb.getInfo()

def getUserResources(abb):
    abb.setUrl("/users")
    return abb.getInfo()

def getUserActions(abb):
    abb.setUrl("/users?action=show")
    return abb.getInfo()

def getUserGrants(abb):
    abb.setUrl("/users/grants")
    return abb.getInfo()

def getRMMPState(abb):
    abb.setUrl("/users/rmmp")
    return abb.getInfo()

def getRMMPActions(abb):
    abb.setUrl("/users/rmmp?action=show")
    return abb.getInfo()

def getPollForRMMPGrantStatus(abb):
    abb.setUrl("/users/rmmp/poll")
    return abb.getInfo()

def getRemoteUserActions(abb):
    abb.setUrl("/users/remoteuser?action=show")
    return abb.getInfo()

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

def getClockResource(abb):
    abb.setUrl("/ctrl/clock")
    return abb.getInfo()

def getClockActions(abb):
    abb.setUrl("/ctrl/clock?action=show")
    return abb.getInfo()

def getTimezoneResource(abb):
    abb.setUrl("/ctrl/clock/timezone")
    return abb.getInfo()

def getIdentityResource(abb):
    abb.setUrl("/ctrl/identity")
    return abb.getInfo()

def getListOfInstalledSystems(abb):
    abb.setUrl("/ctrl/system")
    return abb.getInfo()

def getActionsOnSystem(abb):
    abb.setUrl("/ctrl/system?action=show")
    return abb.getInfo()

def getNetworkResource(abb):
    abb.setUrl("/ctrl/network")
    return abb.getInfo()

def getBackupResources(abb):
    abb.setUrl("/ctrl/backup")
    return abb.getInfo()

def getBackupActions(abb):
    abb.setUrl("/ctrl/backup?action=show")
    return abb.getInfo()

def getBackupState(abb):
    abb.setUrl("/ctrl/backup?action=backupstate")
    return abb.getInfo()

def getBackupSystemInformation(abb):
    return None

def getCompressResources(abb):
    abb.setUrl("/ctrl/compress")
    return abb.getInfo()

def getCompressActions(abb):
    abb.setUrl("/ctrl/compress?action=show")
    return abb.getInfo()

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

def checkRobotwareCompatibility(abb,version):
    abb.setUrl("/ctrl/compatibility/"+version);
    return abb.getInfo()

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

#RAPID services
def getRAPIDSystemResources(abb):
    abb.setUrl("/rw/rapid")
    return abb.getInfo()

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

def getRAPIDModulesAction(abb):
    abb.setUrl("/rw/rapid/modules?action=show")
    return abb.getInfo()

def getRAPIDModules(abb,task):
    abb.setUrl("/rw/rapid/modules?task="+task)
    return abb.getInfo()

def getModPossibleAll(abb):
    abb.setUrl("/rw/rapid/modules?resource=mod-possible-all")
    return abb.getInfo()

def getSpecifiedRangeOfText(abb,module,task,startRow,startColum,endRow,endColum):
    abb.setUrl("/rw/rapid/modules/"+module+"?task="+task+"&startrow="+startRow+"&startcol="+startColum+"&endrow="+endRow+"&endcol="+endColum)
    return abb.getInfo()
    
    
#####################
def test(abb,data):
    abb.setUrl("/fileservice/$home/")
    abb.setData(data)
    abb.postInfo()
    
def subscribeOnResources(abb,data):
    abb.setUrl("/subscription")
    abb.setData(data)
    abb.postInfo()

def getDiagnosticsResources(abb):
    abb.setUrl("/ctrl/diagnostics")
    return abb.postInfo()

def readABBTest():
    abb=ABB()
    abb.setIP("127.0.0.1")
    abb.setUser("Default User","robotics")

    getServiceList(abb)
    print("****************************")
    #getSubscriptionActions(abb)
    getSubscriptionGroupActions(abb,"1")
    subscribeOnResources(abb,b'resources=1&1=/rw/rapid/symbol/data/RAPID/T_ROB1/uimsg/PNum;value&1-p=2')

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
    restartOrShutdownController(abb,b'restart-mode=xstart')
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
    getSpecifiedRangeOfText(abb,"module1","T_ROB1","1","1","50","-1")
    
    

readABBTest()
