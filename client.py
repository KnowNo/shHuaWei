#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''''
    输入文件名，并且上传
    '''
import socket
import time
import struct
import os

import time

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def schedule():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)
    e=0
    try:
        sock.connect(('127.0.0.1',8887))
        print 'connect...'
    except socket.timeout,e:
        print 'timeout',e
    except socket.error,e:
        print 'error',e
    except e:
        print 'any',e
    if not e:
        filename = '1.jpg'
        FILEINFO_SIZE = struct.calcsize('128sI')#编码格式大小
        fhead = struct.pack('128sI',filename,os.stat(filename).st_size)#按照规则进行打包
        sock.send(fhead)#发送文件基本信息数据
        fp = open(filename,'rb')
        print '111'
        while 1:        #发送文件
            print '222'
            filedata = fp.read(1024)
            if not filedata:
                print '333'
                break
            sock.send(filedata)
        
        print "sending over..."
        fp.close()

if __name__=='__main__':
    count = 0
    
    n=10
    p=0.3
    k=np.arange(0.24)
    binomial = stats.binom.pmf(k,n,p)
    #print binomial
    #plt.plot(k,binomial,'o-')
    #plt.title('Binomial: n=%i, p=%.2f'%(n,p),fontsize=15)
    #plt.show()
    
    while 1:
        #hour = time.strftime("%H")
        #interval = 3600/(binomial[hour])
        hour = 3600
        interval = 3600/hour
        time.sleep(interval)
        schedule()
        count=count+1
        print count
    