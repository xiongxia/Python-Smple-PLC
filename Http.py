import urllib.request
import urllib.parse
import json
from threading import Timer
from urllib import error
from Log import *
      

class Http:
   def PostRequest(url,para):
      #打开日志文件
      LOG=Logger('log.log',1)
      requestParameter = urllib.parse.urlencode(para).encode(encoding='utf-8')
      #print("%s"%requestParameter)

      #创建一个post请求
      request = urllib.request.Request(url=url,data=requestParameter)
      #响应
      try:
         #print(urllib.request.urlopen(request).read())
         #print(urllib.request.urlopen(request).read().decode('utf-8'))
         return urllib.request.urlopen(request).read().decode('ascii','ignore')
      except error.URLError as e:
         print(str(url)+str(requestParameter)+str(e))
         LOG.debug(str(url)+str(requestParameter)+str(e))
         return ''
      except error.HTTPError as e:
         print(str(url)+str(requestParameter)+str(e))         
         LOG.debug(str(url)+str(requestParameter)+str(e))
         return ''




