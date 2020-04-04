#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: weblogic 接口泄露
referer: unknown
author: Lucifer
description: weblogic 接口泄露
'''
import sys
import warnings
import requests


class interface_disclosure_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['weblogic 接口泄露', '', '']
        headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/bea_wls_deployment_internal/DeploymentService"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False, allow_redirects=False)

            if req.status_code == 200:
                result[2] = '存在'
                result[1] = vulnurl
            else:
                result[2] = '不存在'

        except:
            result[2] = '不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = interface_disclosure_BaseVerify(sys.argv[1])
    testVuln.run()
