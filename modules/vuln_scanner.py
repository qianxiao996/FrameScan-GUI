import json
import time,threading,queue,importlib
from socket import *
from urllib.parse import urlparse,sys
sys.path.append('./modules')
import BaseInfo
import CyberCalculate
import requests
from PyQt5.QtCore import *
import eventlet

from PyQt5.QtWidgets import QTableWidgetItem


class Vuln_scanner:
    def __init__(self,Main_Windows,plugins_dir_name):
        self.Main_Windows = Main_Windows
        self.plugins_dir_name =plugins_dir_name
    def start(self):
        #获取是否跳过fofa检测
        
        if self.Main_Windows.Ui.jump_fofa.checkState() == Qt.Checked:
            check_fofa ="1"
        else:
            check_fofa="0"

        threadnum = int(self.Main_Windows.Ui.threadsnum.currentText())
        heads = self.Main_Windows.Ui.vuln_scanner_textEdit_heads.toPlainText()
        heads_dict  = {}
        heads = heads.split('\n')
        for head in heads:
            head = head.split(':')
            heads_dict[head[0].strip()] = head[1].strip()
        self.Main_Windows.Ui.textEdit_log.clear()
        target = []  # 存放扫描的URL
        if self.Main_Windows.url_list:
            target = self.Main_Windows.url_list
        else:
            url = self.Main_Windows.Ui.lineEdit_vuln_url.text()
            if 'http://' in url or 'https://' in url:
                target.append(url.strip())
        if not target:
            self.Main_Windows.Ui.textEdit_log.append(
                "<p style=\"color:black\">[%s]Info:未获取到URL地址。</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
            return 0
        poc_data = self.Main_Windows.get_methods() #得到选中的数据
        # print(poc_data)
        if not poc_data:
            self.Main_Windows.Ui.textEdit_log.append(
                "<p style=\"color:black\">[%s]Info:未选择插件。</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
            return 0
        else:
            self.Main_Windows.Ui.textEdit_log.append(
                "[%s]Info:共加载%s个插件。" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), len(poc_data)))
            self.Main_Windows.Ui.textEdit_log.append(
                "<p style=\"color:black\">[%s]Info:共获取到%s个URL地址。</p>" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), len(target)))
            self.Main_Windows.Ui.textEdit_log.append(
                "<p style=\"color:black\">[%s]Info:正在创建队列...</p>" % ((time.strftime('%H:%M:%S', time.localtime(time.time())))))
            thread = threading.Thread(target=self.add_queue, args=(target,poc_data,threadnum,heads,check_fofa))
            thread.setDaemon(True)  # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
            thread.start()
    def add_queue(self,target,poc_data,threadnum,heads_dict,check_fofa):
        # print(poc_data)
        portQueue = queue.Queue()  # 待检测端口队列，会在《Python常用操作》一文中更新用法
        num = 0
        if self.Main_Windows.Ui.jump_url.checkState() != Qt.Checked:
            num= len(target)
            for u in target:
                _url = urlparse(u)
                hostname = _url.hostname
                port = _url.port
                scheme = _url.scheme
                if port is None and scheme == 'https':
                    port = 443
                elif port is None:
                    port = 80
                if scheme=="http" and port == 80 or scheme=="https" and port == 443:
                    u = scheme + '://' + hostname +'/'
                else:
                    u = scheme + '://' + hostname + ':' + str(port) + '/'
                for xuanzhong_data in poc_data:
                    # print(xuanzhong_data)
                    filename =self.plugins_dir_name+'/' + xuanzhong_data['cms_name'] + '/' + xuanzhong_data['vuln_file']
                    #url  filename heads poc fofa_link  fofa  check_fofa
                    portQueue.put(u + '$$$' + filename + '$$$' + json.dumps(heads_dict)+'$$$'+xuanzhong_data['vuln_name'] +'$$$'+xuanzhong_data['FofaQuery_link'] +'$$$'+xuanzhong_data['FofaQuery']+'$$$'+check_fofa)

        if self.Main_Windows.Ui.jump_url.checkState() == Qt.Checked:
            self.Main_Windows.Ui.textEdit_log.append(
                "<p style=\"color:black\">[%s]Info:正在进行地址存活检测...</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
            false_url =[]
            for u in target:
                _url = urlparse(u)
                hostname = _url.hostname
                port = _url.port
                scheme = _url.scheme
                if port is None and scheme == 'https':
                    port = 443
                    u = scheme + '://' + hostname + '/'
                elif port is None:
                    port = 80
                    u = scheme + '://' + hostname + '/'
                else:
                    u = scheme + '://' + hostname + ':' + str(port) + '/'
                try:
                    if u not in false_url:
                        time22 = int(self.Main_Windows.Ui.comboBox_timeout.currentText())
                        result = self.port_scanner(hostname,port,time22)
                        if result:
                            for xuanzhong_data in poc_data:
                                # print(poc_data)
                                filename = self.plugins_dir_name + '/' + xuanzhong_data['cms_name'] + '/' + \
                                           xuanzhong_data['vuln_file']
                                portQueue.put(
                                    u + '$$$' + filename + '$$$' + json.dumps(heads_dict) + '$$$' + xuanzhong_data[
                                        'vuln_name'] + '$$$' + xuanzhong_data['FofaQuery_link'] + '$$$' +
                                    xuanzhong_data[
                                        'FofaQuery'] + '$$$' + check_fofa)

                            num += 1
                        else:
                            false_url.append(u)
                            self.Main_Windows.Ui.textEdit_log.append(
                                "<p style=\"color:black\">[%s]Info:%s----无法访问。</p>" % (
                                    (time.strftime('%H:%M:%S', time.localtime(time.time()))), u))

                    else:
                        continue
                except Exception as  e:
                    false_url.append(u)
                    self.Main_Windows.Ui.textEdit_log.append(
                        "<p style=\"color:black\">[%s]Info:%s----无法访问。</p>" % (
                            (time.strftime('%H:%M:%S', time.localtime(time.time()))), u))

                    continue
                    # 限制线程数小于队列大小
        self.Main_Windows.Ui.textEdit_log.append(
                "<p style=\"color:black\">[%s]Info:共获取到%s个有效URL地址。</p>" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), num))
        if threadnum > portQueue.qsize():
            threadnum = portQueue.qsize()
        # print(portQueue.qsize())
        if num==0:
            self.Main_Windows.Ui.textEdit_log.append(
                "[%s]End:扫描结束。" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
            return
        else:
            self.Main_Windows.Ui.textEdit_log.append(
                "[%s]Start:扫描开始..." % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
            self.Main_Windows.Ui.action_vuln_import.setEnabled(False)
            self.Main_Windows.Ui.pushButton_vuln_file.setEnabled(False)
            self.Main_Windows.Ui.action_vuln_start.setEnabled(False)
            self.Main_Windows.Ui.pushButton_vuln_start.setEnabled(False)
            for i in range(threadnum):
                thread = threading.Thread(target=self.vuln_scan, args=(portQueue, threadnum))
                thread.setDaemon(True)  # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
                thread.start()
    def vuln_scan(self, portQueue, threadnum):
        # print(portQueue.queue)  #输出所有队列

        while 1:
            try:
                if portQueue.empty() :  # 队列空就结束
                    time.sleep(int(self.Main_Windows.Ui.comboBox_timeout.currentText()))
                    self.Main_Windows.Ui.pushButton_vuln_file.setEnabled(True)
                    self.Main_Windows.Ui.pushButton_vuln_start.setEnabled(True)
                    return
                else:
                    # url  filename heads vuln_name fofa_link  fofa  check_fofa
                    all = portQueue.get().split('$$$')  # 从队列中取出 #0
                    url = all[0]
                    filename = all[1]
                    heads_list= json.loads(all[2])
                    heads_dict={}
                    for head in heads_list:
                        head = head.split(':')
                        heads_dict[head[0].strip()] = head[1].strip()
                    # print(heads_dict)
                    vuln_name =all[3]
                    fofa_link = all[4]
                    fofa =  all[5]
                    check_fofa = all[6]
                    timeout = int(self.Main_Windows.Ui.comboBox_timeout.currentText())
                    _url = urlparse(url)
                    hostname = _url.hostname
                    port = _url.port
                    scheme = _url.scheme
                    if port is None and scheme == 'https':
                        port = 443
                    elif port is None:
                        port = 80
                    if check_fofa=="1":
                        if fofa and fofa_link!="all":
                            fofa_url= url+'/'+fofa_link
                        if fofa and fofa_link == "all":
                            fofa_url = url
                        fofaquery = fofa.lower()
                        responce = BaseInfo.http_info(fofa_url)
                        oOperand = {"data": responce}
                        oCyberCalc = CyberCalculate.CyberCalculate(szHayStack=oOperand, szRule=fofaquery,szSplit='=')
                        blMatch = oCyberCalc.Calculate()
                        # print(fofaquery[0])
                        if blMatch:
                            # 超时限制
                            try:
                                eventlet.monkey_patch(thread=False, time=True)
                                with eventlet.Timeout(timeout, False):
                                    nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(filename[:-3], filename).load_module()
                                    result = nnnnnnnnnnnn1.do_poc(url,hostname,port,scheme,heads_dict)
                                    #存在
                                    self.scan_result_out(result,all)
                                    continue
                                self.Main_Windows.Ui.textEdit_log.append(
                                    "<p style=\"color:red\">[%s]Error:%s脚本运行超时！</p>" % (
                                        (time.strftime('%H:%M:%S', time.localtime(time.time()))), filename))
                                continue
                            except:
                                self.Main_Windows.Ui.textEdit_log.append(
                                    "<p style=\"color:red\">[%s]Error:%s----%s----%s。</p>" % (
                                        (time.strftime('%H:%M:%S', time.localtime(time.time()))), url, vuln_name, '脚本运行超时'))
                                continue
                            #进行扫描
                        else:
                            self.Main_Windows.Ui.textEdit_log.append(
                                    "<p style=\"color:black\">[%s]Info:%s----%s----%s。</p>" % (
                                        (time.strftime('%H:%M:%S', time.localtime(time.time()))), url, vuln_name, 'FoFA信息不匹配'))

                    else:
                        #超时限制
                        try:
                            eventlet.monkey_patch(thread=False,time=True)
                            with eventlet.Timeout(timeout,False):
                                try:
                                    # print(url)
                                    nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(filename[:-3], filename).load_module()
                                    result = nnnnnnnnnnnn1.do_poc(url,hostname,port,scheme,heads_dict)
                                    # print(result)
                                    self.scan_result_out(result,all)
                                    continue
                                except Exception as  e:
                                    self.Main_Windows.Ui.textEdit_log.append(
                                        "<p style=\"color:red\">[%s]Error:%s脚本执行错误！<br>[Exception]:<br>%s</p>" % (
                                            (time.strftime('%H:%M:%S', time.localtime(time.time()))), filename, e))
                                    continue
                            self.Main_Windows.Ui.textEdit_log.append(
                                "<p style=\"color:red\">[%s]Error:%s脚本运行超时！</p>" % (
                                    (time.strftime('%H:%M:%S', time.localtime(time.time()))), filename))
                        except:
                            self.Main_Windows.Ui.textEdit_log.append(
                                "<p style=\"color:red\">[%s]Error:%s----%s----%s。</p>" % (
                                    (time.strftime('%H:%M:%S', time.localtime(time.time()))), url, vuln_name, '脚本运行超时'))
                            continue
            except Exception as e:
                self.Main_Windows.Ui.textEdit_log.append(
                    "<p style=\"color:red\">[%s]Error:%s脚本执行错误！<br>[Exception]:<br>%s</p>" % (
                        (time.strftime('%H:%M:%S', time.localtime(time.time()))), filename, e))
                continue
    def scan_result_out(self,result,all):
        if result.get('Result'):
            self.Main_Windows.vuln_scanner_log("Result", True, result.get("Result_Info"), all)
        # 不存在
        else:
            self.Main_Windows.vuln_scanner_log("Result", False, result.get("Result_Info"), all)
        if result.get('Error_Info'):
            self.Main_Windows.vuln_scanner_log("Error", True, result.get("Error_Info"), all)
        if result.get('Debug_Info'):
            self.Main_Windows.vuln_scanner_log("Debug", True, result.get("Debug_Info"), all)

    def port_scanner(self,host,port,timeout):
        #返回0不存活 1存活
        try:
            tcp = socket(AF_INET, SOCK_STREAM)
            tcp.settimeout(int(timeout))  # 如果设置太小，检测不精确，设置太大，检测太慢
            # print(host,port)
            result = tcp.connect_ex((host, int(port)))  # 效率比connect高，成功时返回0，失败时返回错误码
            # print(port+"success")
            if result == 0:
                return 1
            else:
                return 0
        except:
             return 0
        finally:
            try:
                tcp.close()
            except:
                pass