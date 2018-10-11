from tkinter import *           # 导入 Tkinter 库
from SQL import *
import os,sys

def helloCallBack():
   if(deviceId.get()==''):
      print('no input')
   else:
      print(deviceId.get())
   print(serverAddr.get())
   deviceIdSql=MYSQL("aicotin.db")
   deviceIdSql.insert('DeviceID',(deviceId.get(),serverAddr.get()))
   
   root.quit()

def configBeforeStart():
   global root
   root = Tk()                     # 创建窗口对象的背景色
   Label(root,text="deviceId  :").grid(row=0,column=0)
   Label(root,text="deviceKey:").grid(row=1,column=0)
   global deviceId
   deviceId=StringVar()
   global deviceKey
   deviceKey=StringVar()
   Entry(root,textvariable=deviceId).grid(row=0,column=1,padx=10,pady=5)
   Entry(root,textvariable=deviceKey).grid(row=1,column=1,padx=10,pady=5)
   global serverAddr
   serverAddr=StringVar()
   Radiobutton(root,text='test',variable=serverAddr,value='http://test-collection.ycxz-china.com').grid(row=3,column=0,padx=10,pady=5,sticky=W)
   Radiobutton(root,text='online',variable=serverAddr,value='http://online-collection.ycxz-china.com').grid(row=3,column=1,padx=10,pady=5,sticky=E)
   Button(root, text ="确定", command = helloCallBack).grid(row=4,column=0,sticky=W,padx=10,pady=5)
   Button(root,text='取消',command=root.quit).grid(row=4,column=1,sticky=E,padx=10,pady=5)
   root.mainloop()                 # 进入消息循环
