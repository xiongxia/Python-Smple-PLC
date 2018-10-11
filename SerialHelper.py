#coding: utf-8
import sys
import time
import serial
import binascii
import platform
import threading
from log import Logger

if platform.system() == "Windows":
    from  serial.tools import list_ports
else:
    import glob, os, re

class SerialHelper(object):
    def __init__(self, Port="COM8", BaudRate="9600", ByteSize="8", Parity="N", Stopbits="1"):
        '''
        初始化一些参数
        '''
        self.port = Port
        self.baudrate = BaudRate
        self.bytesize = ByteSize
        self.parity = Parity
        self.stopbits = Stopbits
        self.threshold_value = 1
        self.receive_data = ""

        self._serial = None
        self._is_connected = False
        self.log = Logger(1)

    def connect(self, timeout=2):
        '''
        连接设备
        '''
        self._serial = serial.Serial()
        self._serial.port = self.port
        self._serial.baudrate = self.baudrate
        self._serial.bytesize = int(self.bytesize)
        self._serial.parity = self.parity
        self._serial.stopbits = int(self.stopbits)
        self._serial.timeout = timeout

        try:
            self._serial.open()
            if self._serial.isOpen():
                self.log.info("open success")
                self._is_connected = True
            else:
                self.log.info("open failed")
        except Exception as e:
            self.log.error("open failed")
            self._is_connected = False

    def disconnect(self):
        '''
        断开连接
        '''
        if self._serial:
            self._serial.close()

    def write(self, data, isHex=False):
        '''
        发送数据给串口设备
        '''
        self.log.info("Send:%s"%(data))
        if self._is_connected:
            if isHex:
                data = binascii.unhexlify(data).decode('iso-8859-1')
            self._serial.write(bytes(data, "utf-8"))

    def on_connected_changed(self, func):
        '''
        set serial connected status change callback
        '''
        tConnected = threading.Thread(target=self._on_connected_changed, args=(func, ))
        tConnected.setDaemon(True)
        tConnected.start()

    def _on_connected_changed(self, func):
        '''
        set serial connected status change callback
        '''
        self._is_connected_temp = False
        while True:
            if platform.system() == "Windows":
                for com in list_ports.comports():
                    if com[0] == self.port:
                        self._is_connected = True
                        break
            elif platform.system() == "Linux":
                if self.port in self.find_usb_tty():
                    self._is_connected = True

            if self._is_connected_temp != self._is_connected:
                func(self._is_connected)
            self._is_connected_temp = self._is_connected
            time.sleep(0.8)

    def on_data_received(self, func="self.myserial_on_data_received"):
        '''
        set serial data recieved callback,对接收到的数据进行func操作
        '''
        tDataReceived = threading.Thread(target=self._on_data_received, args=(func, ))
        tDataReceived.setDaemon(True)
        tDataReceived.start()
    
    def _on_data_received(self, func):
        '''
        set serial data recieved callback
        '''
        while True:
            if self._is_connected:
                try:
                    number = self._serial.inWaiting()

                    if number > 0:
                        data = self._serial.read(1000).decode(encoding="utf-8")
                        self.log.info(data)
                        func(data)
                    time.sleep(0.01)
                except Exception as e:
                    self._is_connected = False
                    self._serial = None
                    break

    def find_usb_tty(self, vendor_id=None, product_id=None):
        '''
        查找Linux下的串口设备
        '''
        tty_devs = list()
        self.log.info(glob.glob('/dev/*'))
        for dn in glob.glob('/dev/tty*') :
            try:
                vid = int(open(os.path.join(dn, "idVendor" )).read().strip(), 16)
                pid = int(open(os.path.join(dn, "idProduct")).read().strip(), 16)
                if  ((vendor_id is None) or (vid == vendor_id)) and ((product_id is None) or (pid == product_id)) :
                    dns = glob.glob(os.path.join(dn, os.path.basename(dn) + "*"))
                    for sdn in dns :
                        for fn in glob.glob(os.path.join(sdn, "*")) :
                            if  re.search(r"\/ttyUSB[0-9]+$", fn) :
                                tty_devs.append(os.path.join("/dev", os.path.basename(fn)))
            except Exception as ex:
                pass
        return tty_devs


    def hexshow(self,data):
        '''
        功 能: 将接收到的数据已hex显示
        参 数: 串口接受到的数据
        返 回: 转换后的数据
        '''
        hex_data = ''
        hLen = len(data)
        for i in range(hLen):
            hvol = ord(data[i])
            hhex = '%02x' % hvol
            hex_data += hhex+' '
        self.log.info('hexshow:', hex_data)

        return hex_data



    def hexsend(string_data=''):
        '''
        功 能: 将需要发送的字符串以hex形式发送
        参 数: 待发送的数据
        返 回: 转换后的数据
        '''
        hex_data = string_data.decode("hex")
        self.log.info(hexdata)
        return hex_data

    def LRC(self,data='110'):
        '''
        功 能: 计算LRC验证码
        参 数: 待计算的数据
        返 回: 计算结果
        '''

        c=bytes().fromhex(data)
        d=0x00
        for i in c:
            d+=i
        d=0xff-d
        d+=0x01
        self.log.info("LRC:")
        lrc="%02x"%(d)
        lrc=lrc.upper()
        self.log.info(lrc)
        return lrc

    def myserial_on_data_received(self, data):
        '''
        功 能:接收串口数据返回回调函数
        参 数: 返回数据
        返 回: 无
        '''
        self.log.info("recvice data:")
        self.log.info(data)
'''
test  串口操作
if __name__ == '__main__':
    myserial = SerialHelper(Port="com8")
    myserial.connect()
    if myserial._is_connected:
        print("open")
    else:
        print("close")

    time.sleep(1)
    myserial.write('hello')
    myserial.on_data_received()

    count = 0
    while count < 9:
        print("Count: %s"%count)
        time.sleep(1)
        count += 1
'''