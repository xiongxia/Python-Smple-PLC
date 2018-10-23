"""
Example of using cpppo.server.enip EtherNet/IP CIP client API.

To see the Tag operations succeed, fire up:
    python -m cpppo.server.enip Tag=DINT[10]
"""
#coding:utf-8

import sys
import cpppo
from cpppo.server.enip import address, client
from Log import Logger

class EtherNetIP(object):

	host = '192.168.56.1'	# Controller IP address
	port = address[1]	# default is port 44818
	depth = 1		# Allow 1 transaction in-flight
	multiple = 0		# Don't use Multiple Service Packet
	fragment = 0		# Don't force Read/Write Tag Fragmented
	timeout = 1.0		# Any PLC I/O fails if it takes > 1s
	printing = True		# Print a summary of I/O


	def __init__(self,host= '192.168.56.1',port=address[1], depth= 1, multiple= 0, fragment= 0, timeout= 1.0,printing= True):
		self.host = host
		self.port = port
		self.depth = 1
		self.fragment = 0
		self.multiple = 0
		self.printing = True
		self.logger = Logger('aicotinlog',0)
	'''
	读取Ethernet/IP数据，通过tag
	参数：tags(标签字符串)
	返回：读取的结果
	'''
	def read_by_tag(self,tags="SCADA[0-10]"):
		tags_list = []
		tags_list.append(tags)
		with client.connector( host=self.host, port=self.port, timeout=self.timeout ) as connection:
			operations = client.parse_operations(tags_list)
			failures,transactions = connection.process(operations=operations, depth=self.depth, multiple=self.multiple,fragment=self.fragment, printing=self.printing, timeout=self.timeout )

			if failures:
				self.logger.error("EtherNetIP.read_by_tag:read error!!!!\n")
			else:
				self.logger.info("EtherNetIP.read_by_tag:read succeed\n")

				ls = [str(i) for i in transactions]
				self.logger.info("read data:"+" ".join(ls))
				return transactions
	'''
	读取Ethernet/IP数据，通过对象
	参数：Class=22,Instance=1,Attribute=1
	返回：读取的结果
	'''
	def read_by_class(self,Class=22,Instance=1,Attribute=1):
		tags_list = []
		tags = "@"+str(Class)+'/'+str(Instance)+'/'+str(Attribute)
		tags_list.append(tags)
		with client.connector( host=self.host, port=self.port, timeout=self.timeout ) as connection:
			operations = client.parse_operations(tags_list)
			failures,transactions = connection.process(operations=operations, depth=self.depth, multiple=self.multiple,fragment=self.fragment, printing=self.printing, timeout=self.timeout )
			if failures:
				self.logger.error("EtherNetIP.read_by_class:read error!!!!\n")
			else:
				self.logger.info("EtherNetIP.read_by_class:read succeed\n")
				ls = [str(i) for i in transactions]
				self.logger.info("read data:"+" ".join(ls))
				return transactions
	'''
	写入Ethernet/IP数据，通过对象
	参数：Class=22,Instance=1,Attribute=1,Index=0,values = 0
	返回：True 写入成功  False 写入失败
	'''
	def write_by_class(self,Class=22,Instance=1,Attribute=1,Index=0,values = 0):
		tags_list = []
		tags = "@"+str(Class)+'/'+str(Instance)+'/'+str(Attribute)+'['+str(Index)+']'+'='+str(values)
		tags_list.append(tags)
		#print(tags)
		tags_list.append(tags)
		with client.connector( host=self.host, port=self.port, timeout=self.timeout ) as connection:
			operations = client.parse_operations(tags_list)
			failures,transactions = connection.process(operations=operations, depth=self.depth, multiple=self.multiple,fragment=self.fragment, printing=self.printing, timeout=self.timeout )
			if failures:
				self.logger.error("EtherNetIP.write_by_class:write error!!!!\n")
				return False
			else:
				self.logger.info("EtherNetIP.write_by_class:write succeed\n")
				ls = [str(i) for i in transactions]
				self.logger.info("write data:"+" ".join(ls))
				return True

	'''
	写入Ethernet/IP数据，通过tag
	参数：tags(标签字符串) values(对应的列表值)
	返回：True 写入成功  False 写入失败
	'''
	def write_by_tag(self,tags="SCADA[0-3]",values = [1,2,3,4]):
		tags_list = []
		for i in range(len(values)):
			if i == 0:
				tags += "="
			else:
				tags += ","
			tags += str(values[i])

		tags_list.append(tags)
		with client.connector( host=self.host, port=self.port, timeout=self.timeout ) as connection:
			operations = client.parse_operations(tags_list)
			failures,transactions = connection.process(operations=operations, depth=self.depth, multiple=self.multiple,fragment=self.fragment, printing=self.printing, timeout=self.timeout )

			if failures:
				self.logger.error("EtherNetIP.write_by_tag:write error!!!!\n")
				return False
			else:
				self.logger.info("EtherNetIP.write_by_tag:write succeed\n")
				ls = [str(i) for i in transactions]
				self.logger.info("write data:"+" ".join(ls))
				return True

'''
if __name__ == "__main__":
    logging.basicConfig( **cpppo.log_cfg )
    #logging.getLogger().setLevel(logging.INFO)
    host			= '192.168.56.1'	# Controller IP address
    port			= address[1]	# default is port 44818
    depth			= 1		# Allow 1 transaction in-flight
    multiple			= 0		# Don't use Multiple Service Packet
    fragment			= False		# Don't force Read/Write Tag Fragmented
    timeout			= 1.0		# Any PLC I/O fails if it takes > 1s
    printing			= True		# Print a summary of I/O
    tags			= ["SCADA[0-10]"]
    
    with client.connector( host=host, port=port, timeout=timeout ) as connection:
        operations		= client.parse_operations( tags )
        failures,transactions	= connection.process(
            operations=operations, depth=depth, multiple=multiple,
            fragment=fragment, printing=printing, timeout=timeout )
        print(failures)
        print(transactions)
        #connection.results(operations=operations, depth=depth, multiple=multiple,fragment=fragment, printing=printing, timeout=timeout);
        req = connection.read("SCADA[1]")
        #assert connection.readable( timeout=1.0 ), "Failed to receive reply"
        #rpy = next( connection )
		##12
        for k,v in req.items():
            print(k,v)
    #client.main("-a 192.168.56.1 SCADA[1]")
    
    sys.exit( 1 if failures else 0 )
    
'''