#encoding=utf-8

import hashlib
import os
from os import system
from threading import Timer
from Log import *

#calculate the md5 of file
def getMd5(filePath):
  md5 = None
  if os.path.isfile(filePath):
    f = open(filePath,'rb')
    md5Obj = hashlib.md5()
    md5Obj.update(f.read())
    hashCode = md5Obj.hexdigest()
    f.close()
    md5 = str(hashCode).lower()
  return md5

def update():
  #open log file
  LOG=Logger('aicotinlog',1)
  global updateTimer
  updateTimer = Timer(30, update)
  updateTimer.start()
  #get the current path
  folderPath=os.getcwd()+'/'
  folderPathBackup=os.getcwd()+'/'+'backup'+'/'
  fileName='aicotin-python'
  pyFileSuffix='.py'
  md5FileSuffix='.md5'
  soFileSuffix='.so'
  tarFileSuffix='.tar'
  #print(os.getcwd())
  md5Old=''
  md5NewInFile=''
  md5NewCalculated=''

  pyFilePath = folderPath+fileName+pyFileSuffix
  md5Old = getMd5(pyFilePath)
  #print(md5Old)

  #backup the old file
  if(os.path.exists(folderPathBackup)):
    #print(folderPathBackup+' exists')
    system('rm -rf '+folderPathBackup)
  else:
    print('create the backup folder')
  system('mkdir '+folderPathBackup)
  backupTarCommand='mv '+folderPath+fileName+tarFileSuffix+' '+folderPathBackup
  #print(backupTarCommand)
  system(backupTarCommand)

  backupPyCommand='mv '+folderPath+fileName+pyFileSuffix+' '+folderPathBackup
  #print(backupPyCommand)
  system(backupPyCommand)

  backupmd5Command='mv '+folderPath+fileName+md5FileSuffix+' '+folderPathBackup
  #print(backupmd5Command)
  system(backupmd5Command)

  backupSoCommand='mv '+folderPath+fileName+soFileSuffix+' '+folderPathBackup
  #print(backupSoCommand)
  system(backupSoCommand)

  downloadUrl='http://autocontrol-python.oss-cn-beijing.aliyuncs.com/aicotin-python.tar'
  #print(downloadUrl)
  #download the md5 file of the software and the software
  system('wget -P '+folderPath+' '+downloadUrl)
  system('tar -xvf '+folderPath+fileName+tarFileSuffix+' -C '+folderPath)
  md5NewCalculated=getMd5(pyFilePath)
  #print(md5NewCalculated)
  
  with open(folderPath+fileName+md5FileSuffix, 'r') as f:
    md5NewInFile=f.read()
    #print(md5NewInFile)

  if((md5Old!=md5NewCalculated)&(md5NewCalculated==md5NewInFile)):
      #print('need to update')
      LOG.debug('update software')
      system('reboot')
  else:
      #print('no need to update')
      LOG.debug('no need to update software')
      recoverTarCommand='mv '+folderPathBackup+fileName+tarFileSuffix+' '+folderPath
      #print(recoverTarCommand)
      system(recoverTarCommand)

      recoverPyCommand='mv '+folderPathBackup+fileName+pyFileSuffix+' '+folderPath
      #print(recoverPyCommand)
      system(recoverPyCommand)

      recovermd5Command='mv '+folderPathBackup+fileName+md5FileSuffix+' '+folderPath
      #print(recovermd5Command)
      system(recovermd5Command)

      recoverSoCommand='mv '+folderPathBackup+fileName+soFileSuffix+' '+folderPath
      #print(recoverSoCommand)
      system(recoverSoCommand)

def updateSoftwareTimer():
    updateTimer = Timer(1, update)
    updateTimer.start()

      
      

  

