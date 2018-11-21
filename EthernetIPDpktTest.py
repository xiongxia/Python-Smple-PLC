from EthernetIPDpkt import *

def testENIP():
    
    hostname = "192.168.2.191"

    EIP = EtherNetIP(hostname)
    
    #显式连接
    C1 = EIP.explicit_conn(hostname)

    #input class code,instance,attribute
    r = C1.getAttrSingle(0x2, 0x1, 0x2)
    print(r)

    if 0 == r[0]:
        print(r[1])
    else:
        print("Failed to getAttrSingle")

    r = C1.getAttrSingle(0x1, 0x1, 0x5)

    if 0 == r[0]:
        print(r[1])
    else:
        print("Failed to getAttrSingle")

    r = C1.getAttrAll(0xf5, 0x1)

    if 0 == r[0]:
        print(r[1])
    else:
        print("Failed to getAttrAll")
        print(r)

    pkt = C1.listID()

    if pkt != None:
        print("ListID:",str(pkt))
        print("vendor id: ", pkt.vendor_id)
        print("device type: ", pkt.device_type)
        print("product code: ", pkt.product_code)
        print("status: ", pkt.status)
        print("Product name: ", pkt.product_name.decode())
        print("state: ", pkt.state)



    pkt = C1.listServices()

    print("ListServices:", str(pkt))

testENIP()
