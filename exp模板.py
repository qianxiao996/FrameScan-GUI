#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import requests

def vuln_info():
    info={
        'name': 'POC测试漏洞',
        'referer':'http://baidu.com',
        'author':'qianxiao996',
        'description':'''exp描述信息，会显示在漏洞利用模块的信息文本编辑框'''

    }
    return info

def run(url,heads='',cookie='',cmd='whoami',lhost='',lport=8888):
    #命令执行
    if lhost=='':
        return('root')

    #反弹shell    
    if lhost!='':
        return('反弹成功！')
 