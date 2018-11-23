from Pymodbus import *
import sys
sys.path.append('../../log')
from Log import *
import time

ERRCODE=-10000

def testModbusRTUReadAndWriteCoils():
    LOG=Logger('aicotinlog',0)
    read = Modbus_rtu()
    while(1):
        #test read and write coils
        #function code 1
        #frame 01 01 00 01 00 05 AB CD
        rr=read.read_coils(1,0,32)
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read_coils ",rr.bits)
        print("1 read_coils ",rr)
        
        #function code 5
        #frame 01 05 00 03 
        rw=read.write_single_coil(1,32,1)
        if(ERRCODE==rw):
            print("error")
        else:
            print("2 write_single_coil ",rw)
        
        rr=read.read_coils(1,0,32)
        if(ERRCODE==rr):
            print("error")
        else:
            print("3 read_coils after single write ",rr.bits[31])
        print("3 read_coils after single write ",rr)
        
        #function code 15
        rw=read.write_multiple_coils(1,0,[1,0,1,1,0])
        if(ERRCODE==rw):
            print("error")
        else:
            print("4 write_multiple_coils ",rw)
        
        rr=read.read_coils(1,24,8)
        if(ERRCODE==rr):
            print("error")
        else:
            print("5 read coils after multiple write ",rr.bits)
        print("5 read coils after multiple write ",rr) 
        time.sleep(5)

def testModbusRTUReadAndWriteRegisters():
    LOG=Logger('aicotinlog',0)
    read = Modbus_rtu()
    while(1):
        #test read and write registers
        #function code 1
        #frame 01 01 00 01 00 05 AB CD
        rr=read.read_holding_register(1,0,8)
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read_registers  ",rr.registers )
        print("1 read_registers  ",rr)
        
        #function code 5
        #frame 01 05 00 03 
        rw=read.write_single_register(1,0,1)
        if(ERRCODE==rw):
            print("error")
        else:
            print("2 write_single_registers  ",rw)
        
        rr=read.read_holding_register(1,0,8)
        if(ERRCODE==rr):
            print("error")
        else:
            print("3 read_registers  after single write ",rr.registers[7])
        print("3 read_registers  after single write ",rr)
        
        #function code 15
        rw=read.write_multiple_registers(1,0,[1,0,1,1,0,1])
        if(ERRCODE==rw):
            print("error")
        else:
            print("4 write_multiple_registers  ",rw)
        
        rr=read.read_holding_register(1,0,8)
        if(ERRCODE==rr):
            print("error")
        else:
            print("5 read registers  after multiple write ",rr.registers )
        print("5 read registers  after multiple write ",rr) 
        time.sleep(5)

def testModbusRTUReadDiscreteInput():
    LOG=Logger('aicotinlog',0)
    read = Modbus_rtu()
    while(1):
        #test read and write registers
        #function code 2
        #frame 01 02 00 01 00 05 AB CD
        rr=read.read_discrete_inputs(1,0,8)
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read discrete input  ",rr.bits)
        print("1 read discrete input  ",rr)
        
        time.sleep(5)

def testModbusRTUReadInputRegister():
    LOG=Logger('aicotinlog',0)
    read = Modbus_rtu()
    while(1):
        #test read and write registers
        #function code 2
        #frame 01 02 00 01 00 05 AB CD
        rr=read.read_input_register(1,0,8)
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read input register  ",rr.registers )
        print("1 read input register  ",rr)

        time.sleep(5)
        
def testModbusTCPReadAndWriteCoils():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_tcp('127.0.0.1',502)
    except Exception as e:
        print(e)
        return
    
    if(read.isConnected==False):
        print('unconnected')
        return
    
    while(1):
        #test read and write coils
        #function code 1
        #frame 01 01 00 01 00 05 AB CD
        rr=read.read_coils(1,0,32)
        
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read_coils ",rr.bits)
        print("1 read_coils ",rr)
        
        #function code 5
        #frame 01 05 00 03 
        rw=read.write_single_coil(1,32,1)
        if(ERRCODE==rw):
            print("error")
        else:
            print("2 write_single_coil ",rw)
        
        rr=read.read_coils(1,0,32)
        if(ERRCODE==rr):
            print("error")
        else:
            print("3 read_coils after single write ",rr.bits[31])
        print("3 read_coils after single write ",rr)
        
        #function code 15
        rw=read.write_multiple_coils(1,0,[1,0,1,1,0])
        if(ERRCODE==rw):
            print("error")
        else:
            print("4 write_multiple_coils ",rw)
        
        rr=read.read_coils(1,24,8)
        if(ERRCODE==rr):
            print("error")
        else:
            print("5 read coils after multiple write ",rr.bits)
        print("5 read coils after multiple write ",rr) 
        time.sleep(5)
        
def testModbusTCPReadAndWriteRegisters():
    LOG=Logger('aicotinlog',0)
    read = Modbus_tcp()
    while(1):
        #test read and write registers
        #function code 1
        #frame 01 01 00 01 00 05 AB CD
        rr=read.read_holding_register(1,0,8)
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read_registers  ",rr.registers )
        print("1 read_registers  ",rr)
        
        #function code 5
        #frame 01 05 00 03 
        rw=read.write_single_register(1,0,1)
        if(ERRCODE==rw):
            print("error")
        else:
            print("2 write_single_registers  ",rw)
        
        rr=read.read_holding_register(1,0,8)
        if(ERRCODE==rr):
            print("error")
        else:
            print("3 read_registers  after single write ",rr.registers[7])
        print("3 read_registers  after single write ",rr)
        
        #function code 15
        rw=read.write_multiple_registers(1,0,[1,0,1,1,0,1])
        if(ERRCODE==rw):
            print("error")
        else:
            print("4 write_multiple_registers  ",rw)
        
        rr=read.read_holding_register(1,0,8)
        if(ERRCODE==rr):
            print("error")
        else:
            print("5 read registers  after multiple write ",rr.registers )
        print("5 read registers  after multiple write ",rr) 
        time.sleep(5)

def testModbusTCPReadDiscreteInput():
    LOG=Logger('aicotinlog',0)
    read = Modbus_tcp()
    while(1):
        #test read and write registers
        #function code 2
        #frame 01 02 00 01 00 05 AB CD
        rr=read.read_discrete_inputs(1,0,8)
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read discrete input  ",rr.bits)
        print("1 read discrete input  ",rr)
        
        time.sleep(5)

def testModbusTCPReadInputRegister():
    LOG=Logger('aicotinlog',0)
    read = Modbus_tcp()
    while(1):
        #test read and write registers
        #function code 2
        #frame 01 02 00 01 00 05 AB CD
        rr=read.read_input_register(1,0,8)
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read input register  ",rr.registers )
        print("1 read input register  ",rr)

        time.sleep(5)

def testModbusASCIIReadAndWriteCoils():
    LOG=Logger('aicotinlog',0)
    read = Modbus_ascii()
    while(1):
        #test read and write coils
        #function code 1
        #frame 01 01 00 01 00 05 AB CD
        rr=read.read_coils(1,0,32)
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read_coils ",rr.bits)
        print("1 read_coils ",rr)
        
        #function code 5
        #frame 01 05 00 03 
        rw=read.write_single_coil(1,31,1)
        if(ERRCODE==rw):
            print("error")
        else:
            print("2 write_single_coil ",rw)
        
        rr=read.read_coils(1,0,32)
        if(ERRCODE==rr):
            print("error")
        else:
            print("3 read_coils after single write ",rr.bits[31])
        print("3 read_coils after single write ",rr)
        
        #function code 15
        rw=read.write_multiple_coils(1,0,[1,0,1,1,0])
        if(ERRCODE==rw):
            print("error")
        else:
            print("4 write_multiple_coils ",rw)
        
        rr=read.read_coils(1,24,8)
        if(ERRCODE==rr):
            print("error")
        else:
            print("5 read coils after multiple write ",rr.bits)
        print("5 read coils after multiple write ",rr) 
        time.sleep(5)

def testModbusASCIIReadAndWriteRegisters():
    LOG=Logger('aicotinlog',0)
    read = Modbus_ascii('com7')
    while(1):
        #test read and write registers
        #function code 1
        #frame 01 01 00 01 00 05 AB CD
        rr=read.read_holding_register(1,0,8)
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read_registers  ",rr.registers )
        print("1 read_registers  ",rr)
        
        #function code 5
        #frame 01 05 00 03 
        rw=read.write_single_register(1,0,1)
        if(ERRCODE==rw):
            print("error")
        else:
            print("2 write_single_registers  ",rw)
        
        rr=read.read_holding_register(1,0,8)
        if(ERRCODE==rr):
            print("error")
        else:
            print("3 read_registers  after single write ",rr.registers[7])
        print("3 read_registers  after single write ",rr)
        
        #function code 15
        rw=read.write_multiple_registers(1,0,[1,0,1,1,0,1])
        if(ERRCODE==rw):
            print("error")
        else:
            print("4 write_multiple_registers  ",rw)
        
        rr=read.read_holding_register(1,0,8)
        if(ERRCODE==rr):
            print("error")
        else:
            print("5 read registers  after multiple write ",rr.registers )
        print("5 read registers  after multiple write ",rr) 
        time.sleep(5)

def testModbusASCIIReadDiscreteInput():
    LOG=Logger('aicotinlog',0)
    read = Modbus_ascii('com7')
    while(1):
        #test read and write registers
        #function code 2
        #frame 01 02 00 01 00 05 AB CD
        rr=read.read_discrete_inputs(1,0,8)
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read discrete input  ",rr.bits)
        print("1 read discrete input  ",rr)
        
        time.sleep(5)

def testModbusASCIIReadInputRegister():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_ascii('com7')
    except Exception as e:
        print(e)
        return
    
    if(read.isConnected==False):
        print("unconnected")
        return
    while(1):
        #test read and write registers
        #function code 2
        #frame 01 02 00 01 00 05 AB CD
        rr=read.read_input_register(1,0,8)
        if(ERRCODE==rr):
            print('error')
        else:
            print("1 read input register  ",rr.registers )
        print("1 read input register  ",rr)

        time.sleep(5)
        
#testModbusRTUReadAndWriteCoils()
#testModbusRTUReadAndWriteRegisters()
#testModbusRTUReadDiscreteInput()
#testModbusRTUReadInputRegister()
#testModbusTCPReadAndWriteCoils()
#testModbusTCPReadAndWriteRegisters()
#testModbusTCPReadDiscreteInput()
#testModbusTCPReadInputRegister()
#testModbusASCIIReadAndWriteCoils()
#testModbusASCIIReadAndWriteRegisters()
#testModbusASCIIReadDiscreteInput()
testModbusASCIIReadInputRegister()
print("test end")
