from bs4 import BeautifulSoup
from ABBData import *


def xmlParserOfCartesianValue(htmlResp):
    soup=BeautifulSoup(htmlResp,"html.parser")
    
    #print(soup.find(name="span",attrs={"class":"x"}).contents[0])
    #print(soup.find(name="span",attrs={"class":"y"}).contents[0])
    #print(soup.find(name="span",attrs={"class":"z"}).contents[0])
    #print(soup.find(name="span",attrs={"class":"q1"}).contents[0])
    #print(soup.find(name="span",attrs={"class":"q2"}).contents[0])
    #print(soup.find(name="span",attrs={"class":"q3"}).contents[0])
    #print(soup.find(name="span",attrs={"class":"q4"}).contents[0])
    #print(soup.find(name="span",attrs={"class":"j1"}).contents[0])
    #print(soup.find(name="span",attrs={"class":"j4"}).contents[0])
    #print(soup.find(name="span",attrs={"class":"j6"}).contents[0])
    #print(soup.find(name="span",attrs={"class":"jx"}).contents[0])

    abbCartesianValue=ABBCartesianValue()
    abbCartesianValue.setX(soup.find(name="span",attrs={"class":"x"}).contents[0])
    #print(abbCartesianValue.getX())
    abbCartesianValue.setY(soup.find(name="span",attrs={"class":"y"}).contents[0])
    #print(abbCartesianValue.getY())
    abbCartesianValue.setZ(soup.find(name="span",attrs={"class":"z"}).contents[0])
    #print(abbCartesianValue.getZ())
    abbCartesianValue.setQ1(soup.find(name="span",attrs={"class":"q1"}).contents[0])
    #print(abbCartesianValue.getQ1())
    abbCartesianValue.setQ2(soup.find(name="span",attrs={"class":"q2"}).contents[0])
    #print(abbCartesianValue.getQ2())
    abbCartesianValue.setQ3(soup.find(name="span",attrs={"class":"q3"}).contents[0])
    #print(abbCartesianValue.getQ3())
    abbCartesianValue.setQ4(soup.find(name="span",attrs={"class":"q4"}).contents[0])
    #print(abbCartesianValue.getQ4())
    abbCartesianValue.setJ1(soup.find(name="span",attrs={"class":"j1"}).contents[0])
    #print(abbCartesianValue.getJ1())
    abbCartesianValue.setJ4(soup.find(name="span",attrs={"class":"j4"}).contents[0])
    #print(abbCartesianValue.getJ4())
    abbCartesianValue.setJ6(soup.find(name="span",attrs={"class":"j6"}).contents[0])
    #print(abbCartesianValue.getJ6())
    abbCartesianValue.setJX(soup.find(name="span",attrs={"class":"jx"}).contents[0])
    #print(abbCartesianValue.getJX())
    print(abbCartesianValue.getValue())

def xmlParserOfSystemInformation(htmlResp):
    #print(htmlResp)
    soup=BeautifulSoup(htmlResp,"html.parser")
    abbSystemInformation=ABBSystemInformation()
    abbSystemInformation.setSystemName(soup.find(name="span",attrs={"class":"name"}).contents[0])
    #print(abbSystemInformation.getSystemName())
    abbSystemInformation.setSystemRwversion(soup.find(name="span",attrs={"class":"rwversion"}).contents[0])
    #print(abbSystemInformation.getSystemRwversion())
    abbSystemInformation.setSystemSysid(soup.find(name="span",attrs={"class":"sysid"}).contents[0])
    #print(abbSystemInformation.getSystemSysid())
    abbSystemInformation.setSystemStarttm(soup.find(name="span",attrs={"class":"starttm"}).contents[0])
    #print(abbSystemInformation.getSystemStarttm())
    print(abbSystemInformation.getValue())

def xmlParserOfRAPIDExecutionState(htmlResp):
    soup=BeautifulSoup(htmlResp,"html.parser")
    abbRAPIDExecutionState=ABBRAPIDExecutionState()
    abbRAPIDExecutionState.setCtrlexecstate(soup.find(name="span",attrs={"class":"ctrlexecstate"}).contents[0])
    abbRAPIDExecutionState.setCycle(soup.find(name="span",attrs={"class":"cycle"}).contents[0])
    print(abbRAPIDExecutionState.getValue())

def xmlParserOfMotionsystemErrorState(htmlResp):
    soup=BeautifulSoup(htmlResp,"html.parser")
    abbErrorState=ABBMotionsystemErrorState()
    abbErrorState.setErrState(soup.find(name="span",attrs={"class":"err-state"}).contents[0])
    abbErrorState.setErrCount(soup.find(name="span",attrs={"class":"err-count"}).contents[0])
    print(abbErrorState.getValue())

def xmlParserOfControllerState(htmlResp):
    soup=BeautifulSoup(htmlResp,"html.parser")
    abbControllerState=ABBControllerState()
    abbControllerState.setCtrlstate(soup.find(name="span",attrs={"class":"ctrlstate"}).contents[0])
    print(abbControllerState.getValue())

def xmlParserOfControllerOperationMode(htmlResp):
    soup=BeautifulSoup(htmlResp,"html.parser")
    abbControllerOperationMode=ABBControllerOperationMode()
    abbControllerOperationMode.setOpmode(soup.find(name="span",attrs={"class":"opmode"}).contents[0])
    print(abbControllerOperationMode.getValue())

def xmlParserOfAxisPose(htmlResp):
    soup=BeautifulSoup(htmlResp,"html.parser")
    abbAxisPose=ABBAxisPose()
    x=soup.find(name="span",attrs={"class":"x"}).contents[0]
    y=soup.find(name="span",attrs={"class":"y"}).contents[0]
    z=soup.find(name="span",attrs={"class":"z"}).contents[0]
    q1=soup.find(name="span",attrs={"class":"q1"}).contents[0]
    q2=soup.find(name="span",attrs={"class":"q2"}).contents[0]
    q3=soup.find(name="span",attrs={"class":"q3"}).contents[0]
    q4=soup.find(name="span",attrs={"class":"q4"}).contents[0]
    abbAxisPose.setValue(x,y,z,q1,q2,q3,q4)
    print(abbAxisPose.getValue())

    
def test():
    htmlResp = """
    <?xml version="1.0" encoding="UTF-8"?><html xmlns="http://www.w3.org/1999/xhtml"><head><title>motionsystem</title><base href="http://127.0.0.1:80/rw/motionsystem/mechunits/ROB_1/"/></head><body><div class="state"> <a href="cartesian" rel="self"/> <ul> <li class="ms-mechunit-cartesian" title="cartesian"> <span class="x">286.0842</span> <span class="y">-216.5444</span> <span class="z">600.5416</span> <span class="q1">0.481397</span> <span class="q2">0.2742255</span> <span class="q3">0.8166561</span> <span class="q4">-0.1616482</span> <span class="j1">-1</span> <span class="j4">-1</span> <span class="j6">0</span> <span class="jx">0</span> </li> </ul></div></body></html>
    """
    xmlParserOfCartesianValue(htmlResp)

    htmlResp="""
    <?xml version="1.0" encoding="UTF-8"?><html xmlns="http://www.w3.org/1999/xhtml"><head><title>system</title><base href="http://127.0.0.1:80/rw/system/"/></head><body><div class="state"><a href="" rel="self"></a><ul> <li class="sys-system-li" title="system"> <span class="name">Solution1</span> <span class="rwversion">6.07.1011</span> <span class="sysid">{950DFD61-6465-4249-98B9-BDDF1E407B4F}</span> <span class="starttm">2018-10-25 T 16:56:45</span> <span class="rwversionname">6.07.01.00</span> </li> <li class="sys-options-li" title="options"> <a href="options" rel="self"></a> <ul> <li class="sys-option-li" title="0"> <span class="option">RobotWare Base</span> </li> <li class="sys-option-li" title="1"> <span class="option">English</span> </li> <li class="sys-option-li" title="2"> <span class="option">Drive System IRB 120/140/260/360/910SC/1200/1400/1520/1600/1660ID</span> </li> <li class="sys-option-li" title="3"> <span class="option">ADU-790A in position X3</span> </li> <li class="sys-option-li" title="4"> <span class="option">ADU-790A in position Y3</span> </li> <li class="sys-option-li" title="5"> <span class="option">ADU-790A in position Z3</span> </li> <li class="sys-option-li" title="6"> <span class="option">Axis Calibration</span> </li> <li class="sys-option-li" title="7"> <span class="option">IRB 120-3/0.6</span> </li> </ul> </li><li class="sys-energy-li" title="energy"> <a href="energy" rel="self"/> </li><li class="sys-license-li" title="license"> <a href="license" rel="self"/> </li></ul></div></body></html>
    """
    xmlParserOfSystemInformation(htmlResp)
#test()
