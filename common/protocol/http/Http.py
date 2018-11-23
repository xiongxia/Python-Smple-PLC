import urllib.request
import urllib.parse
import json
from threading import Timer
from urllib import error
import sys
sys.path.append('../../log')
from Log import *
from urllib import request
from http import cookiejar
from urllib import error
import urllib
import json
      

class Http:
   def PostRequest(url,para):
      #打开日志文件
      LOG=Logger('aicotinlog',1)
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

class digestHttp:
    def __init__(self,url,username,password):
        #打开日志文件
        LOG=Logger('aicotinlog',1)
        self.url=url
        self.username=username
        self.password=password
        LOG.debug("url:"+url+",username:"+username+",password:"+password)
        
    def PUT_info(self,putData):
        #打开日志文件
        LOG=Logger('aicotinlog',1)
        password_mgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None,self.url,self.username,self.password)
        digest_handler=urllib.request.HTTPDigestAuthHandler(password_mgr)
        digest_opener = urllib.request.build_opener(digest_handler)
        digest_request = urllib.request.Request(url=self.url,data=putData,method='PUT')
        #access
        try:
            digest_resp = digest_opener.open(digest_request).read().decode('utf-8')
            print(digest_resp)
            LOG.debug(digest_resp)
            return digest_resp
        except error.HTTPError as e:
            print(e)
            LOG.debug(e)
            return ''
        except error.URLError as e:
            print(e)
            LOG.debug(e)
            return ''
            
    def GET_info(self):
        #打开日志文件
        LOG=Logger('aicotinlog',1)
        password_mgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None,self.url,self.username,self.password)
        digest_handler=urllib.request.HTTPDigestAuthHandler(password_mgr)
        digest_opener = urllib.request.build_opener(digest_handler)
        digest_request = urllib.request.Request(self.url)
        #access
        try:
            digest_resp = digest_opener.open(digest_request).read().decode('utf-8')
            #print(digest_resp)
            LOG.debug(digest_resp)
            return digest_resp
        except error.HTTPError as e:
            print(e)
            LOG.debug(e)
            return ''
        except error.URLError as e:
            print(e)
            LOG.debug(e)
            return ''

    def POST_info(self,postData):
        #打开日志文件
        LOG=Logger('aicotinlog',1)
        password_mgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None,self.url,self.username,self.password)
        digest_handler=urllib.request.HTTPDigestAuthHandler(password_mgr)
        digest_opener = urllib.request.build_opener(digest_handler)
        digest_request = urllib.request.Request(url=self.url,data=postData,method='POST')
        #access
        try:
            digest_resp = digest_opener.open(digest_request).read().decode('utf-8')
            #print(digest_resp)
            LOG.debug(digest_resp)
            return digest_resp
        except error.HTTPError as e:
            print(e)
            LOG.debug(e)
            return ''
        except error.URLError as e:
            print(e)
            LOG.debug(e)
            return ''
            
    def DELETE_info(self):
        #打开日志文件
        LOG=Logger('aicotinlog',1)
        password_mgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None,self.url,self.username,self.password)
        digest_handler=urllib.request.HTTPDigestAuthHandler(password_mgr)
        digest_opener = urllib.request.build_opener(digest_handler)
        digest_request = urllib.request.Request(url=self.url,method='DELETE')
        #access
        try:
            digest_resp = digest_opener.open(digest_request).read().decode('utf-8')
            #print(digest_resp)
            LOG.debug(digest_resp)
            return digest_resp
        except error.HTTPError as e:
            print(e)
            LOG.debug(e)
            return ''
        except error.URLError as e:
            print(e)
            LOG.debug(e)
            return ''
            
    def HEAD_info(self):
        #打开日志文件
        LOG=Logger('aicotinlog',1)
        password_mgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None,self.url,self.username,self.password)
        digest_handler=urllib.request.HTTPDigestAuthHandler(password_mgr)
        digest_opener = urllib.request.build_opener(digest_handler)
        digest_request = urllib.request.Request(url=self.url)
        #access
        try:
            digest_resp = digest_opener.open(digest_request).read().decode('utf-8')
            #print(digest_resp)
            LOG.debug(digest_resp)
            digest_resp_headers = digest_opener.open(digest_request).headers
            #print(digest_resp_headers)
            LOG.debug(digest_resp_headers)
            return digest_resp_headers
        except error.HTTPError as e:
            print(e)
            LOG.debug(e)
            return ''
        except error.URLError as e:
            print(e)
            LOG.debug(e)
            return ''
            
    def HEAD_info_Content_Length(self):
        #打开日志文件
        LOG=Logger('aicotinlog',1)
        password_mgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None,self.url,self.username,self.password)
        digest_handler=urllib.request.HTTPDigestAuthHandler(password_mgr)
        digest_opener = urllib.request.build_opener(digest_handler)
        digest_request = urllib.request.Request(url=self.url)
        #access
        try:
            headers_Content_Length = digest_opener.open(digest_request).headers['Content-Length']
            #print(headers_Content_Length)
            LOG.debug(headers_Content_Length)
            return headers_Content_Length
        except error.HTTPError as e:
            print(e)
            LOG.debug(e)
            return ''
        except error.URLError as e:
            print(e)
            LOG.debug(e)
            return ''
        

def testDigestAuth():
    authInfo=AuthInfo('1','1')
    authInfo.displayAuthInfo()
    authInfoDict=authInfo.__dict__
    authInfoJson=json.dumps(authInfoDict)
    print(authInfoJson)
    
    print('digest Auth')
    print('')
    reqUrl = 'http://localhost/ctrl/backup?json=1'
    
    password_mgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None,reqUrl,'Default User','robotics')
    digest_handler=urllib.request.HTTPDigestAuthHandler(password_mgr)
    digest_opener = urllib.request.build_opener(digest_handler)
    digest_request = urllib.request.Request(reqUrl)
    #access
    try:
        digest_resp = digest_opener.open(digest_request).read().decode('utf-8')
        print(digest_resp)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)

    print('')
    print('******using cookie******')
    print('')
    
    cookie = cookiejar.CookieJar()
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
    cookie_opener = urllib.request.build_opener(cookie_handler)
    #use cookie to access
    try:
        cookie_resp = cookie_opener.open(digest_request).read().decode('utf-8')
        print(cookie_resp)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)

    print('')
    
    cookieStr = ''
    for item in cookie:
        cookieStr = cookieStr + item.name + '=' + item.value + ';'
    print(cookieStr)

def test():
    url="http://localhost/fileservice/$home/test.txt"
    DATA=b''
    hp=digestHttp(url,"Default User","robotics")
    hp.PUT_info(DATA)

    postData=b'fs-newname=newdir&fs-action=create'
    url="http://localhost/fileservice/$home/"
    hp=digestHttp(url,"Default User","robotics")
    hp.POST_info(postData)

    url="http://localhost/fileservice"
    hp=digestHttp(url,"Default User","robotics")
    hp.GET_info()


    url="http://localhost/fileservice/$home/newdir"
    hp=digestHttp(url,"Default User","robotics")
    hp.DELETE_info()

    url="http://localhost/fileservice/$home/test.txt"
    hp=digestHttp(url,"Default User","robotics")
    hp.HEAD_info()
    
    url="http://localhost/fileservice/$home/test.txt"
    hp=digestHttp(url,"Default User","robotics")
    hp.HEAD_info_Content_Length()


#testDigestAuth()
#test()



