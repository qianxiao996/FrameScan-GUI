#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 正方教务系统数据库任意操纵
referer: http://www.wooyun.org/bugs/wooyun-2014-079938
author: Lucifer
description: 端口211数据可操纵，泄露敏感信息。
'''
import sys
import socket
import warnings
  

from urllib.parse import urlparse

class database_control:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['正方教务系统数据库任意操纵','','']
        port = 211
        if r"http" in self.url:
            #提取host
            host = urlparse(self.url)[1]
            try:
                port = int(host.split(':')[1])
            except:
                pass
            flag = host.find(":")
            if flag != -1:
                host = host[:flag]
        else:
            if self.url.find(":") >= 0:
                host = self.url.split(":")[0]
                port = int(self.url.split(":")[1])
            else:
                host = self.url

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(6)
            s.connect((host, port))
            result[2]=  '存在'
            result[1] = host+":"+str(port)

        except:
            result[2]='未知'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = database_control(sys.argv[1])
    testVuln.run()
