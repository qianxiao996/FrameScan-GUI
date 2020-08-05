#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: POC测试漏洞
referer: http://baidu.com
author: qianxiao996
description: 百度测试。
'''
import sys
import json
import requests
import warnings


def run(url,heads='',cookie='',cmd='whoami',lhost='',lport=8888):
    #命令执行
    if lhost=='':
        return('root')

    #反弹shell    
    if lhost!='':
        return('反弹成功！')
 



if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run('http://baidu.com','','','whoami')
    te2stVuln = run('http://baidu.com','','','whoami','127.0.0.1',8888)