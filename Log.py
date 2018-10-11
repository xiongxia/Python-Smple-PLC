#coding=utf-8
'''
	Logger

'''
import logging,os
import logging.handlers
 
class Logger:
 def __init__(self,flag,clevel = logging.DEBUG,Flevel = logging.DEBUG):
  PATH = ''
  if flag == 2:
    self.logger = logging.getLogger('service.log')
    PATH='service.log
  else:
    self.logger = logging.getLogger('aicotinlog.log')
    PATH='aicotinlog.log'
  self.logger.setLevel(logging.DEBUG)
  fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
  #设置CMD日志
  sh = logging.StreamHandler()
  sh.setFormatter(fmt)
  sh.setLevel(clevel)
  #设置文件日志
  fh = logging.FileHandler(PATH)
  fh.setFormatter(fmt)
  fh.setLevel(Flevel)
  # 添加TimedRotatingFileHandler
  # 定义一个1小时换一次log文件的handler
  # 保留3个旧log文件
  timefilehandler = logging.handlers.TimedRotatingFileHandler(PATH, when='H', interval=1, backupCount=3)
  # 设置后缀名称，跟strftime的格式一样
  timefilehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
  timefilehandler.setFormatter(fmt)
  #初始化日志文件传入0,打开日志文件传入非0值
  if(flag==0):
      #输出到控制台
      self.logger.addHandler(sh)
      #输出到日志文件
      self.logger.addHandler(fh)
      self.logger.addHandler(timefilehandler)
      
      
 def debug(self,message):
  self.logger.debug(message)
 
 def info(self,message):
  self.logger.info(message)
 
 def war(self,message):
  self.logger.warn(message)
 
 def error(self,message):
  self.logger.error(message)
 
 def cri(self,message):
  self.logger.critical(message)
 

