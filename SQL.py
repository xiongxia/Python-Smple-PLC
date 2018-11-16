#coding=utf-8
import sqlite3
'''
	数据库操作类
'''

class MYSQL:
	def __init__(self, path):
		self.conn = sqlite3.connect(path)
		self.c = self.conn.cursor()
		self.c.execute("create table if not exists IMEIInfo (IMEI,serverAddr)")
		self.c.execute("create table if not exists DeviceID (ID,device)")
		self.c.execute("create table if not exists ControllerInfo (ID,name,collectionFrequency,uploadFrequency)")
		self.c.execute("create table if not exists Cmdtable (ID,name,command,parsetype,startadder,datanum,keep,quotaId,mode)")
		self.c.execute("create table if not exists Data (ID,info,value)")
		self.conn.commit()
		

	def insert(self,tablename,value):
		sql = "insert into " + tablename + " values (" 
		n = len(value) 
		
		for i in range(n) :
			sql = sql + '?'
			if i < n - 1 :
				sql = sql + ','
			else: 
				sql = sql + ')'

		#print(sql)
		self.c.execute(sql,value)
		#self.c.execute("insert into Data values(?,?,?)",value)
		self.conn.commit()

	

	def delete(self,tablename):

		sql = "delete from " + tablename
	
		self.c.execute(sql)

		self.conn.commit()
	


	def select(self,tablename):
	

		sql = "select * from " + tablename
	
		self.c.execute(sql)
	
		result = self.c.fetchall()
		#print(result)
		self.conn.commit()

		return result

	def create(self,tablename,value):
	
		sql = "create table " + tablename + "(" 
		n = len(value)
	
		for i in value :
			sql = sql + i
			n = n - 1;
			if n > 0 :
				sql = sql + ','
			else: 
				sql = sql + ')'
			
		self.c.execute(sql)

		self.conn.commit()
		
