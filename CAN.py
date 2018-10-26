#coding:utf-8

import can
import time
from Log import Logger

    '''
    CAN协议的实现
    '''
class CAN(object):
    def __init__(self,BaudRate=9600, interface='socketcan', channel="vcan0"):
        self.logger = Logger('aicotinlog',1)
        self.bus = can.interface.Bus(bustype=interface, channel=channel, bitrate=BaudRate)
        '''
        发送一个远程帧
        参数
		arbitration_id(int) 仲裁ID
		data(bytearray) 数据
		dlc(int) 数据长度
		Timestamp(float) 时间戳
		is_remote_frame(bool) 是否远程帧
		extended_id(bool) 是否扩展ID
		is_error_frame(bool) 是否错误帧
		is_fd(bool) 是否是FD协议
		bitrate_switch(bool) 切换高波特率
		error_state_indicator(bool) FD协议，活动状态, 
		Channel(string) 通道
        '''
    def send_one_remote(self,timeout=None,timestamp=0.0,extended_id=True,is_error_frame=False, arbitration_id=0, dlc=None, data=None,is_fd=False, bitrate_switch=False, error_state_indicator=False,channel=None):
        msg = can.Message(timestamp=timestamp, is_remote_frame=True, extended_id=extended_id,is_error_frame=is_error_frame, arbitration_id=arbitration_id, dlc=dlc, data=data,is_fd=is_fd, bitrate_switch=bitrate_switch, error_state_indicator=error_state_indicator,channel=channel)
        try:
            self.bus.send(msg,timeout=timeout)
            self.logger.info("Message sent on {}".format(self.bus.channel_info))
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            print("Message NOT sent")
            self.logger.error("Message NOT sent")
        '''
        发送一个标准帧
        '''
    def send_one_normal(self,timeout=None,timestamp=0.0,extended_id=True,is_error_frame=False, arbitration_id=0, dlc=None, data=None,is_fd=False, bitrate_switch=False, error_state_indicator=False,channel=None):
        msg = can.Message(timestamp=timestamp, is_remote_frame=False, extended_id=extended_id,is_error_frame=is_error_frame, arbitration_id=arbitration_id, dlc=dlc, data=data,is_fd=is_fd, bitrate_switch=bitrate_switch, error_state_indicator=error_state_indicator,channel=channel)
        try:
            self.bus.send(msg,timeout=timeout)
            self.logger.info("Message sent on {}".format(self.bus.channel_info))
            print("Message sent on {}".format(self.bus.channel_info))
        except can.CanError:
            self.logger.error("Message NOT sent")
            print("Message NOT sent")
        '''
        读取一个标准帧
        '''
    def read():
        self.bus.state = BusState.ACTIVE
        msg = self.bus.recv(1)
        if msg is not None:
            print(msg)
            self.logger.info("Message read %(msg.data.decode)")
            return msg.data

