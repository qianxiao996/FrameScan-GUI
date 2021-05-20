import time,threading,queue,importlib
from urllib.parse import urlparse

import requests
from PyQt5.QtCore import *
import eventlet

from PyQt5.QtWidgets import QTableWidgetItem


class Vuln_scanner:
    def __init__(self,Main_Windows,plugins_dir_name):
        self.Main_Windows = Main_Windows
        self.plugins_dir_name =plugins_dir_name
    def start(self):
        threadnum = int(self.Main_Windows.Ui.threadsnum.currentText())
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
            thread = threading.Thread(target=self.add_queue, args=(target,poc_data,threadnum))
            thread.setDaemon(True)  # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
            thread.start()
    def add_queue(self,target,poc_data,threadnum):
        # print(poc_data)
        portQueue = queue.Queue()  # 待检测端口队列，会在《Python常用操作》一文中更新用法
        num = 0
        if self.Main_Windows.Ui.jump_url.checkState() != Qt.Checked:
            num= len(target)
            for u in target:
                for xuanzhong_data in poc_data:
                    # print(poc_data)
                    filename =self.plugins_dir_name+'/' + xuanzhong_data['cms_name'] + '/' + xuanzhong_data['pocmethods']+'.py'
                    poc_methods = self.plugins_dir_name+'/'+ xuanzhong_data['cms_name'] + '/' + xuanzhong_data['pocmethods']
                    portQueue.put(u + '$$$' + filename + '$$$' + poc_methods+'$$$'+xuanzhong_data['vuln_name'] )
            self.Main_Windows.Ui.textEdit_log.append(
                "<p style=\"color:black\">[%s]Info:共请求%s个URL地址。</p>" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), num))
        if self.Main_Windows.Ui.jump_url.checkState() == Qt.Checked:
            self.Main_Windows.Ui.textEdit_log.append(
                "<p style=\"color:black\">[%s]Info:正在进行地址存活检测...</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
            false_url =[]
            for u in target:
                headers = {'content-type': 'application/json',
                           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
                try:
                    if u not in false_url:
                        time22 = int(self.Main_Windows.Ui.comboBox_timeout.currentText())
                        dara = requests.get(u, timeout=time22, headers=headers,verify=False)
                    else:
                        continue
                except Exception as  e:
                    false_url.append(u)
                    row = self.Main_Windows.Ui.tableWidget_vuln.rowCount()  # 获取行数
                    self.Main_Windows.Ui.tableWidget_vuln.setRowCount(row + 1)
                    urlItem = QTableWidgetItem(u)
                    resultItem = QTableWidgetItem('无法访问')
                    self.Main_Windows.Ui.tableWidget_vuln.setItem(row, 0, urlItem)
                    self.Main_Windows.Ui.tableWidget_vuln.setItem(row, 3, resultItem)
                    self.Main_Windows.Ui.textEdit_log.append(
                        "<p style=\"color:black\">[%s]Info:%s----无法访问。</p>" % (
                            (time.strftime('%H:%M:%S', time.localtime(time.time()))), u))

                    continue
                else:
                    for xuanzhong_data in poc_data:
                        # print(poc_data)
                        filename = self.plugins_dir_name+'/'+ xuanzhong_data['cmsname'] + '/' + xuanzhong_data['pocmethods'] + '.py'
                        poc_methods = self.plugins_dir_name+'/' + xuanzhong_data['cmsname'] + '/' + xuanzhong_data['pocmethods']
                        portQueue.put(u + '$$$' + filename + '$$$' + poc_methods + '$$$' + xuanzhong_data['pocname'])
                    num+= 1
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
                    all = portQueue.get().split('$$$')  # 从队列中取出 #0 url  1 filename  2 pocmethods  3 pocname
                    url = all[0]
                    filename = all[1]
                    poc_methods = all[2]
                    eventlet.monkey_patch(thread=False)
                    #超时限制
                    try:
                        timeout = int(self.Main_Windows.Ui.comboBox_timeout.currentText())
                        eventlet.monkey_patch(time=True)
                        with eventlet.Timeout(timeout,False):
                            try:
                                _url = urlparse(url)
                                hostname = _url.hostname
                                port = _url.port
                                scheme = _url.scheme
                                if port is None and scheme=='https':
                                    port=443
                                elif port is None :
                                    port=80
                                url = scheme+'://'+hostname+':'+str(port)+'/'
                                # print(url)
                                nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(poc_methods, filename).load_module()
                                result = nnnnnnnnnnnn1.do_poc(url,hostname,port,scheme)
                                # print(result)
                                if len(result) ==3 :
                                    self.Main_Windows.vuln_scanner_log(result.get("type"),  result.get("value"), result.get("payload"), all)
                                if len(result) == 4:
                                    self.Main_Windows.vuln_scanner_log(result.get("type"),  result.get("value"), result.get("payload"),all,result.get("color"))
                                else:
                                    self.Main_Windows.vuln_scanner_log(result.get("type"), result.get("value"), '', all)
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
                                (time.strftime('%H:%M:%S', time.localtime(time.time()))), url, all[3], '脚本运行超时'))
                        self.Main_Windows.Ui.pushButton_vuln_file.setEnabled(True)
                        self.Main_Windows.Ui.pushButton_vuln_start.setEnabled(True)
                        continue

            except Exception as e:
                self.Main_Windows.Ui.textEdit_log.append(
                    "<p style=\"color:red\">[%s]Error:%s脚本执行错误！<br>[Exception]:<br>%s</p>" % (
                        (time.strftime('%H:%M:%S', time.localtime(time.time()))), filename, e))
                continue