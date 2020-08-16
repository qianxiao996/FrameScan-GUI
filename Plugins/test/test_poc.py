#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlparse

def vuln_info():
    info={
        'name': 'POC测试漏洞',
        'referer':'http://baidu.com',
        'author':'qianxiao996',
        'description':'''百度测试。'''

    }
    return info
def run(MainWindows,url,all):
    # all =  0=url  1=filename  2=pocmethods  3=pocname
    _url = urlparse(url)
    dip = _url.hostname
    dport = _url.port
    result = '存在'
    padload= 'payload'
    #debug信息 默认不会显示，勾选显示调试信息会输出此结果
    MainWindows.vuln_scanner_log('Debug','denbug信息')
    #返回的结果
    MainWindows.vuln_scanner_log('result', result,padload,all)
    

