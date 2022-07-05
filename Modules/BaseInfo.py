#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ssl
from urllib.parse import urlparse

import chardet
import re
import requests
import urllib3

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_charset(res):
    if 'Content-Type' in res.headers:
        if 'charset' in res.headers['Content-Type'].lower():
            for t in re.compile(r"charset=(\w+)", re.I).findall(res.headers['Content-Type']):
                return t
        else:
            charset = chardet.detect(res.content)
            encoding = charset['encoding']
            return encoding
        
    return "utf-8"

def http_info(url):
    response = {"title": "", "body": "", "header": "", "port": "", "service": "", "protocal": ""}
    try:
        parts = urlparse(url)
        if not parts.scheme:
            return response
        response['service'] = parts.scheme
        response['protocal'] = parts.scheme
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
       
        }
        proxy = {
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080'
}
        res = requests.get(url, verify=False, timeout=5, allow_redirects=False,headers=headers)
        if 'set-cookie' in res.headers:
            response['header']="".join(res.headers['set-cookie'])
        res = requests.get(url, verify=False, timeout=5, allow_redirects=True,headers=headers)
        # findmeta=re.compile(r'<meta http-equiv=(.*?)url=(.*?)>',re.I).findall(res.text)
        # if findmeta:
        #     if len(findmeta[0])==2:
        #         # print(findmeta[0][1])
        #         metastr="".join(findmeta[0][1]).strip('"')
        #         if metastr[0:1]=="/" :
        #             res=requests.get(url+metastr,timeout=5, allow_redirects=True,headers=headers,verify=False)
        #         else:
        #             res=requests.get(url+"/"+metastr,timeout=5, allow_redirects=True,headers=headers,verify=False)
        # print(dir(res))
        charset = get_charset(res)
        #print(charset)
        res.encoding = charset
        title_data = (res.text).lower()
        # bs = BeautifulSoup(res.text, 'lxml')
        titile_re = re.search("<title>(.*)</title>",title_data)
        if titile_re:
        # for title in bs.select('title'):
            response['title'] = titile_re.group(1).replace("<title>","").replace("</title>","") # 响应title
        response['body'] = res.text # 响应body
        if response['body']:
            response['body']=response['body'].lower()
        response['header'] = response['header']+"".join(res.headers.values())
        if response['header']:
            response['header']=response['header'].lower()
        parts = urlparse(res.url)
        if not parts.scheme:
            return response
        response['service'] = parts.scheme
        response['protocal'] = parts.scheme
        if ":" in parts.netloc:
            response['port'] = int(parts.netloc.split(":")[1])
        else:
            if parts.scheme == 'https':
                response['port'] = 443
            else:
                response['port'] = 80
            #print(dir(res))

    except Exception as e:
        pass
        # print(e)
    return response

if __name__ == '__main__':
    print(http_info('http://110.93.247.208:1234'))
