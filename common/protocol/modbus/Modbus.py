#coding:utf-8


import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
from modbus_tk import modbus_tcp
import sys
sys.path.append('../serial')
from SerialHelper import SerialHelper
import time
sys.path.append('../../log')
from Log import Logger
class Modbus_rtu(object):
    '''
    RTU mode data part is returned
    '''

    def __init__(self, Port="com8", BaudRate=9600, ByteSize=8, Parity="N", Stopbits=1):
        self.logger = Logger('aicotinlog',1)
        try:
        #Connect to the slave
            self.master = modbus_rtu.RtuMaster(serial.Serial(Port,BaudRate,ByteSize,Parity,Stopbits,xonxoff=0))
            self.master.set_timeout(5.0)
            self.master.set_verbose(True)
            self.logger.info("connected")
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())

    '''
    function code:1 read coils
    input:slave address, start address, data length
    default:slave address=1, start address=1, data length=2
    output:the data part in the received frame
    '''
    def read_coils (self,Salve_Add=1,Start_Add=1,Data_len=2):
        try:
            data = self.master.execute(Salve_Add, cst.READ_COILS, Start_Add, Data_len)
            self.logger.info(data)
            return data
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000
    
    '''
    functionc code:2 read discrete inputs
    input:slave address, start address ,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_discrete_inputs (self,Salve_Add=1,Start_Add=1,Data_len=2):
        try:
            data = self.master.execute(Salve_Add, cst.READ_DISCRETE_INPUTS, Start_Add, Data_len)
            self.logger.info(data)
            return data 
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000

    '''
    function code:3 read holding registers
    input:slave address, start address,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_holding_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        try:
            data = self.master.execute(Salve_Add, cst.READ_HOLDING_REGISTERS, Start_Add, Data_len)
            self.logger.info(data)
            return data
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000

    '''
    function code:4 read input registers
    input:slave address, start address,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_input_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        try:
            data = self.master.execute(Salve_Add, cst.READ_INPUT_REGISTERS, Start_Add, Data_len)
            self.logger.info(data)
            return data
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000

    '''
    function code:5 write single coil,Value is the input value
    input:slave address, start address, value
    default:slave address =1, start address=1,Value=0
    output:the start address and the data part
    '''
    def write_single_coil (self,Salve_Add=1,Start_Add=1,Value=0):
        try:
            data = self.master.execute(Salve_Add, cst.WRITE_SINGLE_COIL, Start_Add,output_value=Value)
            self.logger.info(data)
            return data
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000
    
    '''
    function code:6,write single registers
    input:slave address, start address, value
    default:slave address=1, start address =1, value=0
    output:the start address and the function code
    '''
    def write_single_register (self,Salve_Add=1,Start_Add=1,Value=0):
        try:
            data = self.master.execute(Salve_Add, cst.WRITE_SINGLE_REGISTER, Start_Add, output_value=Value)
            self.logger.info(data)
            return data
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000
        
    '''
    function code:15, write multiple coils
    input:slave address, start address, value
    default:slave address=1, start address=1, value=[1,2,3]
    output:none
    '''
    def write_multiple_coils (self,Salve_Add=1,Start_Add=1,Value=[1,2,3]):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.WRITE_MULTIPLE_COILS, Start_Add,output_value=Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000
    
    '''
    function code:16, write multiple registers
    input:slave address, start address, value
    default:slave address=1, start address=1, value=[1,2]
    output:none
    '''
    def write_multiple_registers (self,Salve_Add=1,Start_Add=1,Value=[1,2]):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.WRITE_MULTIPLE_REGISTERS, Start_Add, output_value=Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000

class Modbus_tcp(object):
    '''
    TCPmode
    '''

    def __init__(self, Host="192.168.1.15"):
        self.logger = Logger('aicotinlog',1)
        try:
        #Connect to the slave
            self.master = modbus_tcp.TcpMaster(Host)
            self.master.set_timeout(5.0)
            self.logger.info("connected")
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000
    '''
    function code:1 read coils
    input:slave address, start address, data length
    default:slave address=1, start address=1, data length=2
    output:the data part in the received frame
    '''
    def read_coils (self,Salve_Add=1,Start_Add=1,Data_len=2):
        try:
            data = self.master.execute(Salve_Add, cst.READ_COILS, Start_Add, Data_len)
            self.logger.info(data)
            return data
        except modbus_tk.modbus.ModbusError as exc:
            logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000
    
    '''
    functionc code:2 read discrete inputs
    input:slave address, start address ,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_discrete_inputs (self,Salve_Add=1,Start_Add=1,Data_len=2):
        try:
            data = self.master.execute(Salve_Add, cst.READ_DISCRETE_INPUTS, Start_Add, Data_len)
            self.logger.info(data)
            return data 
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000

    '''
    function code:3 read holding registers
    input:slave address, start address,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_holding_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        try:
            data = self.master.execute(Salve_Add, cst.READ_HOLDING_REGISTERS, Start_Add, Data_len)
            self.logger.info(data)
            return data
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000

    '''
    function code:4 read input registers
    input:slave address, start address,data length
    default:slave address=1, start address=1,data length=2
    output:the data part in the received frame
    '''
    def read_input_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        try:
            data = self.master.execute(Salve_Add, cst.READ_INPUT_REGISTERS, Start_Add, Data_len)
            self.logger.info(data)
            return data
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000

    '''
    function code:5 write single coil,Value is the input value
    input:slave address, start address, value
    default:slave address =1, start address=1,Value=0
    output:the start address and the function code
    '''
    def write_single_coil (self,Salve_Add=1,Start_Add=1,Value=0):
        try:
            data = self.master.execute(Salve_Add, cst.WRITE_SINGLE_COIL, Start_Add,output_value=Value)
            self.logger.info(data)
            return data
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000
    
    '''
    function code:6,write single registers
    input:slave address, start address, value
    default:slave address=1, start address =1, value=0
    output:the start address and the function code
    '''
    def write_single_register (self,Salve_Add=1,Start_Add=1,Value=0):
        try:
            data = self.master.execute(Salve_Add, cst.WRITE_SINGLE_REGISTER, Start_Add, output_value=Value)
            self.logger.info(data)
            return data
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000
        
    '''
    function code:15, write multiple coils
    input:slave address, start address, value
    default:slave address=1, start address=1, value=[1,2,3]
    output:the start address and the function code
    '''
    def write_multiple_coils (self,Salve_Add=1,Start_Add=1,Value=[1,2,3]):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.WRITE_MULTIPLE_COILS, Start_Add,output_value=Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000
    
    '''
    function code:16, write multiple registers
    input:slave address, start address, value
    default:slave address=1, start address=1, value=[1,2]
    output:the start address and the function code
    '''
    def write_multiple_registers (self,Salve_Add=1,Start_Add=1,Value=[1,2]):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.WRITE_MULTIPLE_REGISTERS, Start_Add, output_value=Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
            return -10000

class Modbus_ascii(object):
    '''
    ASCII mode
    '''

    def __init__(self, Port="com7", BaudRate=9600, ByteSize=8, Parity="N", Stopbits=1):
        self.logger = Logger('aicotinlog',1)
        #Connect to the slave
        self.master = SerialHelper(Port,BaudRate,ByteSize,Parity,Stopbits)
        self.master.connect()
        time.sleep(1)
        self.logger.info("connected")

    def read_holding_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        function code:3, read holding register
        '''
        print(self.function(3,Salve_Add,Start_Add,Data_len))
        return self.master.receive_data

    def read_coils (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        function code:1, read coils
        '''
        self.function(1,Salve_Add,Start_Add,Data_len)
        print(self.master.receive_data)
        return self.master.receive_data

    def read_discrete_inputs (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        function code:2, read discrete inputs
        '''
        self.function(2,Salve_Add,Start_Add,Data_len)
        return self.master.receive_data
    def write_single_coil (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        function code:5, write single coils
        '''
        self.function(5,Salve_Add,Start_Add,Data_len)
    def write_single_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        function code:6, write single register
        '''
        self.function(6,Salve_Add,Start_Add,Data_len)
    def write_multiple_coils (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        function code:15, write multiple coils
        '''
        self.function(15,Salve_Add,Start_Add,Data_len)

    def write_multiple_registers (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        function code:16, write multiple registers
        '''
        self.function(16,Salve_Add,Start_Add,Data_len)

    def function(self,code=1,Salve_Add=1,Start_Add=1,Data_len=2):

        data = ":"
        if Salve_Add < 10:
            s='0'+str(Salve_Add)
        else:
            s=str(Salve_Add)
        if code < 10:
            s+='0'+str(code)
        else:
            s+=str(code)

        if Start_Add < 10:
            s+='000'+str(Salve_Add)
        elif Start_Add < 100:
            s+='00'+str(Start_Add)
        elif Start_Add < 1000:
            s+='0'+str(Start_Add)
        else:
            s+=str(Start_Add)

        if Data_len < 10:
            s+='000'+str(Data_len)
        elif Data_len < 100:
            s+='00'+str(Data_len)
        elif Data_len < 1000:
            s+='0'+str(Data_len)
        else:
            s+=str(Data_len)
        data+=s

        temp=self.master.LRC(s)
        data+=temp
        print(temp)

        data+="\r\n"
        print(data)

        self.master.write(data)
        self.master.on_data_received()
        count = 0
        print("Sending")
        while count < 3:

            time.sleep(1)
            count += 1
        print("send finish")
        self.logger.info("send finish")

'''
test ASCII模式 读取台达数据
#coding:utf-8

from Modbus import Modbus_ascii

read = Modbus_rtu("com8")
read.read_holding_register(4,0,2)

read = Modbus_ascii("com8",9600,7,"E",1)
read.read_holding_register(1,614,8)

test RTU模式 读取传感器数据
read = Modbus_rtu("com8",9600,8,"N",1)
read.read_holding_register(4,0,2)

'''





