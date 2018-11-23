from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.client.sync import ModbusTcpClient as ModbusClientTCP
from pymodbus.transaction import ModbusRtuFramer
from Log import *

ERRCODE=-10000

############
############

#RTU mode

############
############
class Modbus_rtu():
    def __init__(self, Port='com7',BaudRate=9600, ByteSize=8, Parity='N', Stopbits=1):
        self.logger = Logger('aicotinlog',1)
        self.client=ModbusClient(method='rtu', port=Port, baudrate=BaudRate, bytesize=ByteSize, parity=Parity, stopbits=Stopbits,timeout=1)
        self.isConnected=self.client.connect()
        self.logger.info(self.isConnected)

    '''
    function code:1 read coils
    input:slave address, start address, data length
    default:slave address=1, start address=1, data length=2
    output:the data part in the received frame
    '''
    def read_coils (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_coils(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
    
    '''
    functionc code:2 read discrete inputs
    input:slave address, start address ,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_discrete_inputs (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_discrete_inputs(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data

    '''
    function code:3 read holding registers
    input:slave address, start address,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_holding_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_holding_registers(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data

    '''
    function code:4 read input registers
    input:slave address, start address,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_input_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_input_registers(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data

    '''
    function code:5 write single coil,Value is the input value
    input:slave address, start address, value
    default:slave address =1, start address=1,Value=0
    output:the address to write and the value
    '''
    def write_single_coil (self,Salve_Add=1,Start_Add=1,Value=0):
        data = self.client.write_coils(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
    
    '''
    function code:6,write single registers
    input:slave address, start address, value
    default:slave address=1, start address =1, value=0
    output:the start address and the function code
    '''
    def write_single_register (self,Salve_Add=1,Start_Add=1,Value=[1,1,1,1]):
        data = self.client.write_register(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
        
    '''
    function code:15, write multiple coils
    input:slave address, start address, value
    default:slave address=1, start address=1, value=[1,2,3]
    output:the start address and the data length to write
    '''
    def write_multiple_coils (self,Salve_Add=1,Start_Add=1,Value=[1,2,3]):
        data = self.client.write_coils(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
    
    '''
    function code:16, write multiple registers
    input:slave address, start address, value
    default:slave address=1, start address=1, value=[1,2]
    output:none
    '''
    def write_multiple_registers (self,Salve_Add=1,Start_Add=1,Value=[1,2]):
        data = self.client.write_registers(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data

############
############

#ASCII mode

############
############
class Modbus_ascii():
    def __init__(self, Port='com7',BaudRate=9600, ByteSize=8, Parity='N', Stopbits=1):
        self.logger = Logger('aicotinlog',1)
        self.client= ModbusClient(method='ascii', port=Port, baudrate=BaudRate, bytesize=ByteSize, parity=Parity, stopbits=Stopbits,timeout=1)
        self.isConnected=self.client.connect()
        self.logger.info(self.isConnected)
        

    '''
    function code:1 read coils
    input:slave address, start address, data length
    default:slave address=1, start address=1, data length=2
    output:the data part in the received frame
    '''
    def read_coils (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_coils(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
    
    '''
    functionc code:2 read discrete inputs
    input:slave address, start address ,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_discrete_inputs (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_discrete_inputs(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data

    '''
    function code:3 read holding registers
    input:slave address, start address,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_holding_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_holding_registers(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data

    '''
    function code:4 read input registers
    input:slave address, start address,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_input_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_input_registers(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data

    '''
    function code:5 write single coil,Value is the input value
    input:slave address, start address, value
    default:slave address =1, start address=1,Value=0
    output:the address to write and the value
    '''
    def write_single_coil (self,Salve_Add=1,Start_Add=1,Value=0):
        data = self.client.write_coils(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
    
    '''
    function code:6,write single registers
    input:slave address, start address, value
    default:slave address=1, start address =1, value=0
    output:the start address and the function code
    '''
    def write_single_register (self,Salve_Add=1,Start_Add=1,Value=[1,1,1,1]):
        data = self.client.write_register(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
        
    '''
    function code:15, write multiple coils
    input:slave address, start address, value
    default:slave address=1, start address=1, value=[1,2,3]
    output:the start address and the data length to write
    '''
    def write_multiple_coils (self,Salve_Add=1,Start_Add=1,Value=[1,2,3]):
        data = self.client.write_coils(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
    
    '''
    function code:16, write multiple registers
    input:slave address, start address, value
    default:slave address=1, start address=1, value=[1,2]
    output:none
    '''
    def write_multiple_registers (self,Salve_Add=1,Start_Add=1,Value=[1,2]):
        data = self.client.write_registers(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data


############
############

#TCP mode

############
############
class Modbus_tcp():
    def __init__(self, ip='127.0.0.1',Port=502):
        self.logger = Logger('aicotinlog',1)
        self.client=ModbusClientTCP(ip,port=Port)
        self.isConnected=self.client.connect()
        self.logger.info(self.isConnected)

    '''
    function code:1 read coils
    input:slave address, start address, data length
    default:slave address=1, start address=1, data length=2
    output:the data part in the received frame
    '''
    def read_coils (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_coils(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
    
    '''
    functionc code:2 read discrete inputs
    input:slave address, start address ,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_discrete_inputs (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_discrete_inputs(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data

    '''
    function code:3 read holding registers
    input:slave address, start address,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_holding_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_holding_registers(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data

    '''
    function code:4 read input registers
    input:slave address, start address,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_input_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        data = self.client.read_input_registers(Start_Add, Data_len,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data

    '''
    function code:5 write single coil,Value is the input value
    input:slave address, start address, value
    default:slave address =1, start address=1,Value=0
    output:the address to write and the value
    '''
    def write_single_coil (self,Salve_Add=1,Start_Add=1,Value=0):
        data = self.client.write_coils(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
    
    '''
    function code:6,write single registers
    input:slave address, start address, value
    default:slave address=1, start address =1, value=0
    output:the start address and the function code
    '''
    def write_single_register (self,Salve_Add=1,Start_Add=1,Value=[1,1,1,1]):
        data = self.client.write_register(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
        
    '''
    function code:15, write multiple coils
    input:slave address, start address, value
    default:slave address=1, start address=1, value=[1,2,3]
    output:the start address and the data length to write
    '''
    def write_multiple_coils (self,Salve_Add=1,Start_Add=1,Value=[1,2,3]):
        data = self.client.write_coils(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data
    
    '''
    function code:16, write multiple registers
    input:slave address, start address, value
    default:slave address=1, start address=1, value=[1,2]
    output:none
    '''
    def write_multiple_registers (self,Salve_Add=1,Start_Add=1,Value=[1,2]):
        data = self.client.write_registers(Start_Add, Value,unit=Salve_Add)
        self.logger.info(data)
        if(data.isError()):
            return ERRCODE
        else:
            return data

