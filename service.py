#-*- coding: UTF-8 -*-

'''

	用于监控进程服务函数

'''

import os
import sys
import getopt
import time
import datetime
import codecs
import optparse
import configparser
import signal
import subprocess
import select
sys.path.append('common/log')
from Log import Logger


pid = os.getpid() 

def print_error(s):

    print('\033[31m[%d: ERROR] %s\033[31;m' % (pid, s))


def print_info(s):

    print('\033[32m[%d: INFO] %s\033[32;m' % (pid, s))


def print_warning(s):

    print('\033[33m[%d: WARNING] %s\033[33;m' % (pid, s))

'''

	函数作用：开启子进程
	参数：子进程，进程状态
	返回值：进程PID

'''

def start_child_proc(command, merged):

    try:

        if command is None:

            raise OSError("Invalid command")



        child = None

 

        if merged is True:

            # merge stdout and stderr

            child = subprocess.Popen(command,

                stderr=subprocess.STDOUT, # 表示子进程的标准错误也输出到标准输出

                stdout=subprocess.PIPE    # 表示需要创建一个新的管道

            )

        else:

            # DO NOT merge stdout and stderr

            child = subprocess.Popen(command,

                stderr=subprocess.PIPE,

                stdout=subprocess.PIPE)

 

        return child



    except subprocess.CalledProcessError:

        pass # handle errors in the called executable

    except OSError:

        pass # executable not found

 

    raise OSError("Failed to run command!")



def run_forever(command):

    log = Logger('service',0)
    log.info("start child process with command: " + ' '.join(command))
    print_info("start child process with command: " + ' '.join(command))

    merged = False

    child = start_child_proc(command, merged)


    line = ''

    errln = ''

    failover = 0


    while True:

        while child.poll() != None:

            failover = failover + 1
            log.war("child process shutdown with return code: " + str(child.returncode))
            print_warning("child process shutdown with return code: " + str(child.returncode))
            log.war("child process shutdown with return code: " + str(child.returncode))
            print_warning("restart child process again, times=%d" % failover)


            child = start_child_proc(command, merged)

 
        # read child process stdout and log it

        ch = child.stdout.read(1)

        if ch != '' and ch != '\n':
            s = str(ch, encoding = "utf-8")  
            line = line + s

        if ch == '\n':
            log.info(line)
            print_info(line)

            line = ''

 

        if merged is not True:

            # read child process stderr and log it

            ch = child.stderr.read(1)

            if ch != '' and ch != '\n':
                s = str(ch, encoding = "utf-8") 
                errln = errln + s

            if ch == '\n':

                log.error(errln)
                print_error(errln)

                errln = ''


if __name__ == "__main__":

    run_forever(["python", "./main.py"])


