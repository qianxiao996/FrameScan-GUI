#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: POC测试漏洞
referer: http://baidu.com
author: qianxiao996
description: 百度测试。
'''
import requests
import warnings
def run(url):
    #返回一个列表，参数一为检测结果，参数二为Payload
    result = ['Payload','存在']
    return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])