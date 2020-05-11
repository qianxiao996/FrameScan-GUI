#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: zookeeper 未授权漏洞
referer: https://www.secpulse.com/archives/61101.html
author: Lucifer
description: Zookeeper的默认开放端口是2181。Zookeeper安装部署之后默认情况下不需要任何身份验证，
            造成攻击者可以远程利用Zookeeper，通过服务器收集敏感信息或者在Zookeeper集群内进行破坏（比如：kill命令）。
            攻击者能够执行所有只允许由管理员运行的命令。。
'''
import sys
import socket
import warnings

from urllib.parse import urlparse
def run(url):
        result = ['zookeeper 未授权漏洞', '', '']
        port = 2181
        if r"http" in url:
            #提取host
            host = urlparse(url)[1]
            try:
                port = int(host.split(':')[1])
            except:
                pass
            flag = host.find(":")
            if flag != -1:
                host = host[:flag]
        else:
            if url.find(":") >= 0:
                host = url.split(":")[0]
                port = int(url.split(":")[1])
            else:
                host = url

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(6)
            s.connect((host, port))
            s.send(b'envi')
            data = s.recv(1024).decode()
            if r"Environment" in data and r"zookeeper" in data:
                result[2] = '存在'
                result[1]=host+":"+str(port)
            else:
                result[2] = '不存在'

        except:
            result[2] = '不存在'  
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])

