#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import requests
import warnings

def vuln_info():
    info={
        'name': 'POC测试漏洞',
        'referer':'http://baidu.com',
        'author':'qianxiao996',
        'description':'''expddddd'''

    }
    return info

def run(MainWindows,url,heads='',cookie='',cmd='whoami',lhost='',lport=8888):
    #命令执行
    if lhost=='':
        MainWindows.vuln_exp_log('result','root')

    #反弹shell    
    if lhost!='':
        MainWindows.vuln_exp_log('log','反弹成功','red')
 