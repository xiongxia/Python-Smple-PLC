import sys
import struct
import time
import threading

from collections import namedtuple

import pysoem


class EtherCAT:

    BECKHOFF_VENDOR_ID = 0x0002
    EK1100_PRODUCT_CODE = 0x044c2c52
    EL3002_PRODUCT_CODE = 0x0bba3052
    EL1259_PRODUCT_CODE = 0x04eb3052

    def __init__(self):
        adapters = pysoem.find_adapters()
        self._master = pysoem.Master()
        for i, adapter in enumerate(adapters):
            #print('Adapter {}'.format(i))
            #print('  {}'.format(adapter.name))
            #print('  {}'.format(adapter.desc))
            self._master.open(adapter.name)
            if not self._master.config_init() > 0:
                #self._master.close()
                print('{} no slave found'.format(adapter.desc))
                #sys.exit(1)
            else:
                break
        print('find {} Adapter'.format(len(adapters)))
        print('{} Adapter slave found'.format(adapter.desc))
        print('use {} Adapter'.format(adapter.name))

        self._ifname = adapter.name
        self._pd_thread_stop_event = threading.Event()
        self._ch_thread_stop_event = threading.Event()
        self._actual_wkc = 0

        self._master.in_op = False
        self._master.do_check_state = False
        SlaveSet = namedtuple('SlaveSet', 'name product_code config_func')
        self._expected_slave_layout = {0: SlaveSet('EK1100', self.EK1100_PRODUCT_CODE, None),
                                       1: SlaveSet('EL3002', self.EL3002_PRODUCT_CODE, None),
                                       2: SlaveSet('EL1259', self.EL1259_PRODUCT_CODE, None)}

        for i, slave in enumerate(self._master.slaves):
        #print(slave.id)
        #print(slave.state)
            slave.config_func = self._expected_slave_layout[i].config_func
            slave.is_lost = False
        self.slave_count = i+1
        self._master.config_map()
        '''
        if self._master.state_check(pysoem.SAFEOP_STATE, 50000) != pysoem.SAFEOP_STATE:
            self._master.close()
            raise BasicExampleError('not all slaves reached SAFEOP state')
        '''
        self._master.state = pysoem.OP_STATE
        self._master.write_state()
        self.all_slaves_reached_op_state = False
        for i in range(40):
            self._master.state_check(pysoem.OP_STATE, 50000)
            if self._master.state == pysoem.OP_STATE:
                self.all_slaves_reached_op_state = True
                break
        self.check_thread = threading.Thread(target=self._check_thread)
        self.check_thread.start()
        self.proc_thread = threading.Thread(target=self._processdata_thread)
        self.proc_thread.start()
        #self._pd_thread_stop_event.set()
        #self._ch_thread_stop_event.set()
        #proc_thread.join()
        #check_thread.join()

    '''
	读取eeprom数据
	输入参数：从站节点(int)
	返回：显示对应从站0-0x10000 eeprom信息,输出到out.text文件
    '''
    def read_eeprom_of_slave(self,slave_pos):
        slave = self._master.slaves[slave_pos]
        file=open('out.txt','w+')
        for i in range(0,0x1000, 2):
            print('{:04x}:'.format(i), end='',file=file)
            print('|'.join('{:02x}'.format(x) for x in slave.eeprom_read(i)),file=file)
        file.close()
    '''
	读取eeprom数据
	输入参数：从站节点(int)，地址(int 32bit)
	返回：对应eeparm对应的32bit字节组数据
    '''
    def read_eeprom_of_slave_by_address(self,slave_pos,eep_address):
        slave = self._master.slaves[slave_pos]
        return slave.eeprom_read(eep_address)
    '''
	写eeprom数据
	输入参数：从站节点(int)，地址(int 32bit),数据（int 16bit）
	返回：true 写入成功 false 写入失败
    '''
    def write_eeprom_of_slave_by_address(self,slave_pos,eep_address,data):
        b=data.to_bytes(2, byteorder='big')
        slave = self._master.slaves[slave_pos]
        slave.eeprom_write(eep_address,b)
        if slave.eeprom_read(eep_address) == b:
            return True
        else:
            return False
    '''
	通过SDO发送数据,写对应寄存器
	输入参数：slave_pos从站节点(int)，index SDO索引(int),subindex SDO子索引,数据
	返回：true 写入成功 false 写入失败
    '''
    def write_SDO(self, slave_pos,index,subindex,data):
        self._master.in_op = True
        slave = self._master.slaves[slave_pos]
        c=data.to_bytes(2, byteorder='big')
        slave.sdo_write(index, subindex, c)
        if slave.sdo_read(index, subindex,2) == c:
            return True
        else:
            return False

    '''
	通过SDO发送数据,读取对应寄存器
	输入参数：slave_pos从站节点(int)，index SDO索引(int),subindex SDO子索引,读取数据大小
	返回：返回读取的数据
    '''
    def read_SDO(self,slave_pos,index,subindex,size):
        self._master.in_op = True
        if self.all_slaves_reached_op_state:
            return slave.sdo_read(index, subindex,size) 

        else:
            print('not all slaves reached OP state')
            return -1000


    def _processdata_thread(self):
        while not self._pd_thread_stop_event.is_set():
            self._master.send_processdata()
            self._actual_wkc = self._master.receive_processdata(10000)
            if not self._actual_wkc == self._master.expected_wkc:
                print('incorrect wkc')
            time.sleep(0.01)

    '''
	通过PDO发送数据,写对应寄存器
	输入参数：slave_pos从站节点(int)，index PDO索引(int),数据
	返回：true 写入成功 false 写入失败
    '''
    def write_PDO(self,slave_pos,index,data):
        self._master.in_op = True
        if self.all_slaves_reached_op_state:
            output_len = len(self._master.slaves[slave_pos].output)
            tmp = bytearray([0 for i in range(output_len)])
            tmp[index] = data
            self._master.slaves[slave_pos].output = bytes(tmp)
            return True
        else:
            print('not all slaves reached OP state')
            return False

        if all_slaves_reached_op_state:
            self._pdo_update_loop()

        #self._master.state = pysoem.INIT_STATE
        #self._master.write_state()
        #self._master.close()
    '''
	通过PDO发送数据,读取对应寄存器
	输入参数：slave_pos从站节点(int)
	返回：返回读取的数据
    '''
    def read_PDO(self,slave_pos):
        self._master.in_op = True
        if self.all_slaves_reached_op_state:
            input = self._master.slaves[slave_pos].input
            return input
        else:
            print('not all slaves reached OP state')
            return -1000

    @staticmethod
    def _check_slave(slave, pos):
        if slave.state == (pysoem.SAFEOP_STATE + pysoem.STATE_ERROR):
            print(
                'ERROR : slave {} is in SAFE_OP + ERROR, attempting ack.'.format(pos))
            slave.state = pysoem.SAFEOP_STATE + pysoem.STATE_ACK
            slave.write_state()
        elif slave.state == pysoem.SAFEOP_STATE:
            print(
                'WARNING : slave {} is in SAFE_OP, try change to OPERATIONAL.'.format(pos))
            slave.state = pysoem.OP_STATE
            slave.write_state()
        elif slave.state > pysoem.NONE_STATE:
            if slave.reconfig():
                slave.is_lost = False
                print('MESSAGE : slave {} reconfigured'.format(pos))
        elif not slave.is_lost:
            slave.state_check(pysoem.OP_STATE)
            if slave.state == pysoem.NONE_STATE:
                slave.is_lost = True
                print('ERROR : slave {} lost'.format(pos))
        if slave.is_lost:
            if slave.state == pysoem.NONE_STATE:
                if slave.recover():
                    slave.is_lost = False
                    print(
                        'MESSAGE : slave {} recovered'.format(pos))
            else:
                slave.is_lost = False
                print('MESSAGE : slave {} found'.format(pos))
    
    def _check_thread(self):

        while not self._ch_thread_stop_event.is_set():
            if self._master.in_op and ((self._actual_wkc < self._master.expected_wkc) or self._master.do_check_state):
                self._master.do_check_state = False
                self._master.read_state()
                for i, slave in enumerate(self._master.slaves):
                    if slave.state != pysoem.OP_STATE:
                        self._master.do_check_state = True
                        BasicExample._check_slave(slave, i)
                if not self._master.do_check_state:
                    print('OK : all slaves resumed OPERATIONAL.')
            time.sleep(0.01)
    def close(self):
        self._master.close()


if __name__ == '__main__':

    print('EtherCAT Test started')

    master = EtherCAT()
    print(master.slave_count)
    print(master.read_PDO(0))
    print(master.write_PDO(0,0,0xff))
    #time.sleep(2)
    #master.read_eeprom_of_slave(0)
    master.write_eeprom_of_slave_by_address(0,0x00e6,415)
    print(master.read_eeprom_of_slave_by_address(0,0x00e6))
    master._pd_thread_stop_event.set()
    master._ch_thread_stop_event.set()
    master.proc_thread.join()
    master.check_thread.join()
    master.close()


