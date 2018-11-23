from Modbus import *
from Log import *
import time

def testModbusRTUReadAndWriteCoils():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_rtu("com7")
        while(1):
            #test read and write coils
            #function code 1
            #frame 01 01 00 01 00 05 AB CD
            rr=read.read_coils(1,0,8)
            print("1 read_coils ",rr)
            #function code 5
            #frame 01 05 00 03 
            rw=read.write_single_coil(1,0,1)
            print("2 write_single_coil ",rw)
            rr=read.read_coils(1,0,8)
            print("3 read_coils after single write ",rr)
            #function code 15
            rw=read.write_multiple_coils(1,0,[1,0,1,1,0])
            print("4 write_multiple_coils ",rw) 
            rr=read.read_coils(1,0,8)
            print("5 read coils after multiple write ",rr)           
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)

def testModbusRTUReadAndWriteRegisters():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_rtu("com7")
        while(1):
            #test read and write registers
            rr=read.read_holding_register(1,1,5)
            print("1 read_holding_register ",rr)
            rw=read.write_single_register(1,3,6)
            print("2 write_single_register",rw)
            rr=read.read_holding_register(1,1,5)
            print(rr)
            print("3 read after single write ",rr)
            rw=read.write_multiple_registers(1,3,[3,4])
            print(rw)
            rr=read.read_holding_register(1,1,5)
            print(rr)
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)

def testModbusRTUReadDiscreteInput():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_rtu("com7")
        while(1):
            #test read_discrete_inputs
            rr=read.read_discrete_inputs(1,0,0xA)
            print("1 read_discrete_inputs ",rr)
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)

def testModbusRTUReadInputRegister():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_rtu("com7")
        while(1):
            #test read_input_register
            rr=read.read_input_register(1,3,5)
            print("1 read_input_register ",rr)
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)

def testModbusTCPReadAndWriteCoils():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_tcp("127.0.0.1")
        while(1):
            #test read and write coils
            #function code 1
            #frame 01 01 00 01 00 05 AB CD
            rr=read.read_coils(1,0,8)
            print("1 read_coils ",rr)
            #function code 5
            #frame 01 05 00 03 
            rw=read.write_single_coil(1,0,1)
            print("2 write_single_coil ",rw)
            rr=read.read_coils(1,0,8)
            print("3 read_coils after single write ",rr)
            #function code 15
            rw=read.write_multiple_coils(1,0,[1,0,1,1,0])
            print("4 write_multiple_coils ",rw) 
            rr=read.read_coils(1,0,8)
            print("5 read coils after multiple write ",rr)           
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)
    except ConnectionRefusedError as e:
        print(e)
        LOG.debug(e)
        
def testModbusTCPReadAndWriteRegisters():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_tcp("127.0.0.1")
        while(1):
            #test read and write registers
            rr=read.read_holding_register(1,1,5)
            print("1 read_holding_register ",rr)
            rw=read.write_single_register(1,3,6)
            print("2 write_single_register",rw)
            rr=read.read_holding_register(1,1,5)
            print(rr)
            print("3 read after single write ",rr)
            rw=read.write_multiple_registers(1,3,[3,4])
            print("4 write_multiple_registers ",rw)
            rr=read.read_holding_register(1,1,5)
            print("5 read after multiple read", rr)
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)
    except ConnectionRefusedError as e:
        print(e)
        LOG.debug(e)

def testModbusTCPReadDiscreteInput():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_tcp("127.0.0.1")
        while(1):
            #test read_discrete_inputs
            rr=read.read_discrete_inputs(1,0,0xA)
            print("1 read_discrete_inputs ",rr)
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)
    except ConnectionRefusedError as e:
        print(e)
        LOG.debug(e)

def testModbusTCPReadInputRegister():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_tcp("127.0.0.1")
        while(1):
            #test read_input_register
            rr=read.read_input_register(1,3,5)
            print("1 read_input_register ",rr)
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)
    except ConnectionRefusedError as e:
        print(e)
        LOG.debug(e)

def testModbusASCIIReadAndWriteCoils():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_ascii("com7")
        while(1):
            #test read and write coils
            #function code 1
            #frame 01 01 00 01 00 05 AB CD
            rr=read.read_coils(1,0,8)
            print("1 read_coils ",rr)
            #function code 5
            #frame 01 05 00 03 
            rw=read.write_single_coil(1,0,1)
            print("2 write_single_coil ",rw)
            rr=read.read_coils(1,0,8)
            print("3 read_coils after single write ",rr)
            #function code 15
            rw=read.write_multiple_coils(1,0,[1,0,1,1,0])
            print("4 write_multiple_coils ",rw) 
            rr=read.read_coils(1,0,8)
            print("5 read coils after multiple write ",rr)           
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)

def testModbusASCIIReadAndWriteRegisters():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_ascii("com7")
        while(1):
            #test read and write registers
            rr=read.read_holding_register(1,0,5)
            print("1 read_holding_register ",rr)
            #rw=read.write_single_register(1,3,6)
            #print("2 write_single_register",rw)
            #rr=read.read_holding_register(1,1,5)
            #print(rr)
            #print("3 read after single write ",rr)
            #rw=read.write_multiple_registers(1,3,[3,4])
            #print(rw)
            #rr=read.read_holding_register(1,1,5)
            #print(rr)
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)

def testModbusASCIIReadDiscreteInput():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_ascii("com7")
        while(1):
            #test read_discrete_inputs
            rr=read.read_discrete_inputs(1,0,0xA)
            print("1 read_discrete_inputs ",rr)
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)

def testModbusASCIIReadInputRegister():
    LOG=Logger('aicotinlog',0)
    try:
        read = Modbus_ascii("com7")
        while(1):
            #test read_input_register
            rr=read.read_input_register(1,0,5)
            print("1 read_input_register ",rr)
            time.sleep(5)
    except serial.serialutil.SerialException as e:
        print(e)
        LOG.debug(e)
    except modbus_tk.exceptions.ModbusInvalidResponseError as e:
        print(e)
        LOG.debug(e)
    except TypeError as e:
        print(e)
        LOG.debug(e)
        
#testModbusRTUReadAndWriteCoils()
testModbusRTUReadAndWriteRegisters()
#testModbusRTUReadDiscreteInput()
#testModbusRTUReadInputRegister()
#testModbusTCPReadAndWriteCoils()
#testModbusTCPReadAndWriteRegisters()
#testModbusTCPReadDiscreteInput()
#testModbusTCPReadInputRegister()
#testModbusASCIIReadAndWriteCoils()
#testModbusASCIIReadAndWriteRegisters()
