#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlparse
vuln_url = []
def vuln_info():
    info={
        'vuln_name': 'SpringBoot未授权访问',  #漏洞名称
        'vuln_referer':'',  #漏洞来源
        'vuln_author':'qianxiao996',  #插件作者
        'cms_name':'SpringBoot',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''SpringBoot未授权访问''',
        'vuln_identifier':'''''',
        'vuln_class':'未授权访问',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''升级新版本''',
        'FofaQuery_type':'http', #socket、http
        'FofaQuery_link':'/adsasdasf', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule':'body="Whitelabel Error Page"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc':1, #是否有poc  1为有 0为无
        'isexp':0  #是否有exp   1为有 0为无
    }
    return info
result = {"Result":False,"Result_Info":""}
# url：url  hostname：主机地址  port：端口  scheme：服务  heads：http自定义头信息
def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    # 返回参数
    #Result返回是否存在，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
    try:
        common_dir=['/autoconfig','/beans','/env','/configprops','/dump','/health','/info','/mappings','/metrics','/shutdown','/trace','/actuator/autoconfig','/actuator/beans','/actuator/env','/actuator/configprops','/actuator/dump','/actuator/health','/actuator/info','/actuator/mappings','/actuator/metrics','/actuator/shutdown','/actuator/trace']
        for cd in common_dir:
            url_target =url+cd
            print(url_target)
            url_target=url_target.replace("://",":::").replace("//","/").replace(":::","://")
            r = requests.get(url_target, headers=heads, verify=False,timeout=3)
            if r.status_code==200:
                vuln_url.append("目标站点开启了 {} 端点的未授权访问,路径为：{}".format(cd.replace('/',''),url_target))
        if len(vuln_url)>0:
            result['Result']= True
            vuln_data  = '|'.join(vuln_url)
            result['Result_Info']= vuln_data
        else:
            result['Result_Info']= '不存在'
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')

    

