#coding:utf-8


import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
from SerialHelper import SerialHelper
import time
from log import Logger
class Modbus_rtu(object):
    '''
    RTU模式
    '''

    def __init__(self, Port="com8", BaudRate=9600, ByteSize=8, Parity="N", Stopbits=1):
        self.logger = Logger(1)
        try:
        #Connect to the slave
            self.master = modbus_rtu.RtuMaster(serial.Serial(Port,BaudRate,ByteSize,Parity,Stopbits,xonxoff=0))
            self.master.set_timeout(5.0)
            self.master.set_verbose(True)
            self.logger.info("connected")
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
    def read_holding_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        功能码：3 读保持寄存器
        '''
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.READ_HOLDING_REGISTERS, Start_Add, Data_len))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：1 读线圈
        '''
    def read_coils (self,Salve_Add=1,Start_Add=1,Data_len=2):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.READ_COILS, Start_Add, Data_len))
        except modbus_tk.modbus.ModbusError as exc:
            logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：2  读离散输入
        '''
    def read_discrete_inputs (self,Salve_Add=1,Start_Add=1,Data_len=2):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.READ_DISCRETE_INPUTS, Start_Add, Data_len))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：5 写单一线圈,Value为写入的值
        '''
    def write_single_coil (self,Salve_Add=1,Start_Add=1,Value=0):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.WRITE_SINGLE_COIL, Start_Add,Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：6 写单一寄存器
        '''
    def write_single_registers (self,Salve_Add=1,Start_Add=1,Value=0):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.WRITE_SINGLE_REGISTER, Start_Add, Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：15 写多个线圈 
        '''
    def write_multiple_coils (self,Salve_Add=1,Start_Add=1,Value=[1,2,3]):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.WRITE_MULTIPLE_COILS, Start_Add,Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：16 写多寄存器
        '''
    def write_multple_registers (self,Salve_Add=1,Start_Add=1,Value=[1,2]):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.WRITE_MULTIPLE_REGISTERS, Start_Add, Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())

class Modbus_tcp(object):
    '''
    TCP模式
    '''

    def __init__(self, Host="192.168.1.15"):
        self.logger = Logger(1)
        try:
        #Connect to the slave
            self.master = modbus_tcp.TcpMaster(Host)
            self.master.set_timeout(5.0)
            self.logger.info("connected")
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
    def read_holding_register (self,Start_Add=1,Data_len=2):
        '''
        功能码：3 读保持寄存器
        '''
        try:
            self.logger.info(self.master.execute(1, cst.READ_HOLDING_REGISTERS, Start_Add, Data_len))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：1 读线圈
        '''
    def read_coils (self,Start_Add=1,Data_len=2):
        try:
            self.logger.info(self.master.execute(1, cst.READ_COILS, Start_Add, Data_len))
        except modbus_tk.modbus.ModbusError as exc:
            logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：2  读离散输入
        '''
    def read_discrete_inputs (self,Start_Add=1,Data_len=2):
        try:
            self.logger.info(self.master.execute(1, cst.READ_DISCRETE_INPUTS, Start_Add, Data_len))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：5 写单一线圈,Value为写入的值
        '''
    def write_single_coil (self,Start_Add=1,Value=0):
        try:
            self.logger.info(self.master.execute(1, cst.WRITE_SINGLE_COIL, Start_Add,Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：6 写单一寄存器
        '''
    def write_single_registers (self,Salve_Add=1,Start_Add=1,Value=2):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.WRITE_SINGLE_REGISTER, Start_Add, Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：15 写多个线圈 Value=[20,21,22,23],列表写入
        '''
    def write_multiple_coils (self,Salve_Add=1,Start_Add=1,Value=[20,21,22,23]):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.WRITE_MULTIPLE_COILS, Start_Add,Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())
        '''
        功能码：16 写多寄存器, Value=[20,21,22,23],列表写入
        '''
    def write_multple_registers (self,Salve_Add=1,Start_Add=1,Value=[20,21,22,23]):
        try:
            self.logger.info(self.master.execute(Salve_Add, cst.WRITE_MULTIPLE_REGISTERS, Start_Add,Value))
        except modbus_tk.modbus.ModbusError as exc:
            self.logger.error("%s- Code=%d", exc, exc.get_exception_code())

class Modbus_ascii(object):
    '''
    ASCII模式
    '''

    def __init__(self, Port="com8", BaudRate=9600, ByteSize=8, Parity="N", Stopbits=1):
        self.logger = Logger(1)
        #Connect to the slave
        self.master = SerialHelper(Port,BaudRate,ByteSize,Parity,Stopbits)
        self.master.connect()
        time.sleep(1)
        self.logger.info("connected")

    def read_holding_register (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        功能码：3 读保持寄存器
        '''
        self.function(3,Salve_Add,Start_Add,Data_len)

    def read_coils (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        功能码：1 读线圈
        '''
        self.function(1,Salve_Add,Start_Add,Data_len)

    def read_discrete_inputs (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        功能码：2  读离散输入
        '''
        self.function(2,Salve_Add,Start_Add,Data_len)

    def write_single_coil (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        功能码：5 写单一线圈
        '''
        self.function(5,Salve_Add,Start_Add,Data_len)
    def write_single_registers (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        功能码：6 写单一寄存器
        '''
        self.function(6,Salve_Add,Start_Add,Data_len)
    def write_multiple_coils (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        功能码：15 写多个线圈 
        '''
        self.function(15,Salve_Add,Start_Add,Data_len)

    def write_multple_registers (self,Salve_Add=1,Start_Add=1,Data_len=2):
        '''
        功能码：16 写多寄存器
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

        data+="\r\n"
        #print(data)

        self.master.write(data)
        self.master.on_data_received()
        count = 0
        print("Sending")
        while count < 3:

            time.sleep(1)
            count += 1
        self.logger.info("send finish")

'''
test ASCII模式 读取台达数据
#coding:utf-8

from Modbus import Modbus_ascii
'''
read = Modbus_rtu("com8")
read.read_holding_register(4,0,2)
'''
read = Modbus_ascii("com8",9600,7,"E",1)
read.read_holding_register(1,614,8)

test RTU模式 读取传感器数据
read = Modbus_rtu("com8",9600,8,"N",1)
read.read_holding_register(4,0,2)

'''





