#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 正方教务系统default3.aspx爆破页面
referer: http://www.wooyun.org/bugs/WooYun-2013-21692
author: Lucifer
description: 文件default3.aspx页面可爆破。
'''
import sys
import requests
import warnings
def run(url):
        result = ['正方教务系统default3.aspx爆破页面','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        try:
            req = requests.get(url, headers=headers, timeout=6, verify=False, allow_redirects=True)
            tmpurl = str(req.url)
            tmpurl = tmpurl.lower()
            if r"default2.aspx" in tmpurl or r"default.aspx" in tmpurl:
                vulnurl = tmpurl.replace("default2.aspx","").replace("default.aspx", "")
            else:
                vulnurl = tmpurl
            vulnurl = vulnurl + "default3.aspx"
        except:
            pass
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"__VIEWSTATEGENERATOR" in req.text and r"CheckCode.aspx" not in req.text and req.status_code ==200:
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

