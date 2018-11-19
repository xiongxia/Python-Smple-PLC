from EthernetIPDpkt import *

def testENIP():
    hostname = "192.168.31.2"

    broadcast = "192.168.255.255"

    inputsize = 1

    outputsize = 1

    EIP = EtherNetIP(hostname)

    C1 = EIP.explicit_conn(hostname)



    """    

    listOfNodes = C1.scanNetwork(broadcast,5)

    print("Found ", len(listOfNodes), " nodes")

    for node in listOfNodes:

        name = node.product_name.decode()

        sockinfo = SocketAddressInfo(node.socket_addr)

        ip = socket.inet_ntoa(struct.pack("!I",sockinfo.sin_addr))

        print(ip, " - ", name)

    """



    pkt = C1.listID()

    if pkt != None:

        print("Product name: ", pkt.product_name.decode())



    pkt = C1.listServices()

    print("ListServices:", str(pkt))

    pkt = C1.listInterfaces()
    print("ListInterfaces:",str(pkt))

    print(C1.registerSession())
    #C1.unregisterSession()



    path = C1.mkReqPath(0x1, 1, None)
    print(path)

    data = struct.pack("HB", 0x12, 0)
    print(data)

    r = C1.unconnSend(0x1, path+data, random.randint(1,4026531839))
    print(r)

    #r = C1.getAttrSingle(0x300, 1, None, struct.pack("HB", 0x12, 0))

    if 0 == r[0]:

        print("Could read 0x300")

    else:

        print("Failed to read 0x300")



    #"""

    # read input size from global system object (obj 0x84, attr 4)

    r = C1.getAttrSingle(0x2, 1, 1)
    print(r)

    if 0 == r[0]:

        print("Read CPX input size from terminal success (data: "+ str(r[1]) + ")")
        print(r[1])

        inputsize = struct.unpack_from("HB", r[1])[0]
        print(struct.unpack_from("HB", r[1]))

    else:

        print("Failed to read CPX input size")



    # read output size from global system object (obj 0x84, attr 5)

    r = C1.getAttrSingle(0x1, 1, 5)

    if 0 == r[0]:

        print("Read CPX output size from terminal sucess (data: " + str(r[1]) + ")")

        outputsize = struct.unpack_from("B", r[1])[0]
        print(struct.unpack_from("B", r[1]))
        print(outputsize)

    else:

        print("Failed to read CPX output size")

    #"""

    """

    # configure i/o

    print("Configure with {0} bytes input and {1} bytes output".format(inputsize, outputsize))

    EIP.registerAssembly(EtherNetIP.ENIP_IO_TYPE_INPUT,  inputsize, 101, C1)

    EIP.registerAssembly(EtherNetIP.ENIP_IO_TYPE_OUTPUT, outputsize, 100, C1)

    EIP.startIO()



    C1.registerSession()



    C1.setAttrSingle(CIP_OBJ_TCPIP, 1, 6, "fbxxx")



    for i in range(1,8):

        r = C1.getAttrSingle(CIP_OBJ_IDENTITY, 1, i)

        if 0 == r[0]:

            print("read ok attr (" + str(i) + ") data: " + str(r[1]))

        else:

            print("Err: " + str(r[0]))



    C1.sendFwdOpenReq(101,100,1)

    C1.produce()



    while True:

        try: 

            time.sleep(0.2)

            C1.outAssem[random.randint(0, len(C1.outAssem)-1)] = True

            C1.outAssem[random.randint(0, len(C1.outAssem)-1)] = False

        except KeyboardInterrupt:

            break

    C1.stopProduce()

    C1.sendFwdCloseReq(101,100,1)

    EIP.stopIO()

    #"""

    print("OOOOOOOOOOOOO")
    print(str(C1.getAttrAll(1,1)))

    print("pppppppppppppppppp")
    print(C1.getAttrSingle(1,1,5))
    print(C1.getAttrSingle(1,1,5))

    C1.setAttrSingle(1,1,5,bytes([1,2,3]))    
    print("XXXXXXXXXXXXXXXX")
    print(C1.getAttrSingle(1,1,7))



testENIP()
