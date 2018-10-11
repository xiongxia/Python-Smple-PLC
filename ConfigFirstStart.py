import sys,time,msvcrt
def readInput(caption, default, timeout=10):
    start_time = time.time()
    sys.stdout.write('(****%d秒自动跳过****)\n%s:' % (timeout,caption))
    sys.stdout.flush()
    inputChar = ''
    while True:
        ini=msvcrt.kbhit()
        print(ini)
        try:
            if ini:
                chrInput = msvcrt.getche()
                if ord(chrInput) == 13:  # enter_key
                    print('enter')
                    break
                elif ord(chrInput) >= 32:
                    print(chrInput.decode())
                    inputChar += chrInput.decode()
                else:
                    print(chrInput.decode())
        except Exception as e:
            pass
        if len(inputChar) == 0 and time.time() - start_time > timeout:
            print ('')
            print('timeout')
            break
    print ('')  # needed to move to next line
    if len(inputChar) > 0:
        print(inputChar)
        return inputChar+''
    else:
        print('no input')
        return default
 
 
#使用方法
def configFirstStart():
    iscaiji=readInput('请输入deviceId和服务器编号(0代表线上服务器,1代表测试服务器)\n输入示例:12345678,0\n','aaa')
    print(iscaiji)
