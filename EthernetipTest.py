from Ethernetip import *

def testENIP():
    print("testENIP")
    eip=EtherNetIP('192.168.2.191')
    #eip.read_by_tag('SCADA[0-5]')
    #eip.write_by_tag('Tag[0-5]',[23,12,12,32,23,24])
    #eip.read_by_tag('Tag[0-5]')
    eip.read_by_class(1,1,1)
    #eip.write_by_class(22,1,1,0,955)

testENIP()
