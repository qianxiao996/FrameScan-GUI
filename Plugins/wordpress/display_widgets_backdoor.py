#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: wordpress display-widgets插件后门漏洞
referer: http://www.nsfocus.com.cn/upload/contents/2017/09/20170915174457_73771.pdf
author: Lucifer
description: wordpress display-widgets Version 2.6.1——Version 2.6.3.1 geolocation.php存在后门。
'''
import sys
import requests
import warnings
def run(url):
        result = ['wordpress display-widgets插件后门漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/wp-content/plugins/display-widgets/geolocation.php"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False, allow_redirects=False)
            if req.status_code == 200:
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
    
