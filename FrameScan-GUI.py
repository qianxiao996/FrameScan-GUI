#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base64
import configparser
import datetime
import importlib
import json
import os
import platform
import socket
import sys
import traceback

import socks
import qdarkstyle
from qdarkstyle import LightPalette
from qt_material import apply_stylesheet

sys.path.append('./Modules')
sys.path.append('./Gui')

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import csv, re, requests, time, sqlite3
from Gui.main import Ui_MainWindow
from Gui.Vuln_Plugins import Ui_Form_Vuln
from Gui.Vuln_Info import Ui_From_Vuln_Info
from Gui.Vuln_Edit import Ui_Form_Vuln_Edit
from Gui.Proxy import Ui_Proxy
from Gui.Server import Ui_Server
import pyperclip
import frozen_dir
from Modules.Vuln_Scanner import Vuln_Scanner
from Modules.Vuln_Exp import Vuln_Exp
from Modules.PythonHighlighter import PythonHighlighter

import logging
import webbrowser

SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)
DB_NAME = './Conf/DB.db'
version = '1.4.1'
vuln_plugins_dir = './Plugins/Vuln_Plugins/'
exp_plugins_dir = './Plugins/Exp_Plugins/'
log_file_dir = './Logs/'
config_file_dir = './Conf/config.ini'
vuln_plugins_template = './Plugins/Plugins_Template/Plugins_漏洞插件模板.py'
update_time = '2022/07/05'
requests.packages.urllib3.disable_warnings()
sysstr = platform.system()

if (sysstr == "Windows"):
    houzhui = '.pyd'
elif (sysstr == "Linux"):
    houzhui = '.so'
plugins_ext = ['.py', '.pyc']
plugins_ext.append(houzhui)


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):  # 主窗口
    def __init__(self, parent=None):
        sys.excepthook = self.HandleException
        super(MainWindows, self).__init__(parent)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) #去掉标题栏
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.setWindowTitle('FrameScan-GUI  by qianxiao996 v' + version + ' ' + update_time)
        self.setWindowIcon(QtGui.QIcon('Conf/main.ico'))

        self.Ui.action_proxy.triggered.connect(self.proxy_setting)  # 查看插件

        self.__Logger = self.__BuildLogger()
        # 存放poc插件
        self.poc_cms_name_dict = {}
        # 存放exp插件
        self.exp_cms_name_dict = {}

        self.vuln_url_list = []

        # 初始化加载插件
        self.load_config()
        self.load_vuln_plugins()
        self.load_exp_plugins()
        # self.load_options_menu()
        self.load_server()

        # 漏洞扫描
        self.Ui.pushButton_vuln_file.clicked.connect(
            lambda: self.vuln_import_file(self.Ui.lineEdit_vuln_url, self.Ui.textEdit_log, 'vuln_scanner'))  # 导入地址
        self.Ui.pushButton_vuln_start.clicked.connect(self.vuln_Start)  # 开始扫描
        self.Ui.pushButton_vuln_stop.clicked.connect(self.vuln_Stop)  # 停止扫描
        self.Ui.pushButton_vuln_expstart.clicked.connect(self.vuln_exp)  # 一键利用
        self.Ui.pushButton_vuln_all.clicked.connect(self.vuln_all)  # 全选
        self.Ui.pushButton_vuln_noall.clicked.connect(self.vuln_noall)  # 反选

        # 插件管理（漏洞）
        self.Ui.action_vuln_reload.triggered.connect(self.vuln_reload_Plugins)  # 重新加载插件
        self.Ui.action_vuln_reload_update.triggered.connect(self.vuln_reload_update)  # 插件网络检查更新
        self.Ui.action_vuln_update.triggered.connect(self.Show_Server_Widget)  # 插件更新设置
        self.Ui.action_vuln_showplubins.triggered.connect(self.vuln_ShowPlugins)  # 查看插件

        # 选项
        self.Ui.action_about_.triggered.connect(self.about)
        self.Ui.action_update_.triggered.connect(self.version_update)
        self.Ui.action_fankui_.triggered.connect(self.ideas)  # 意见反馈
        self.Ui.action_default.triggered.connect(lambda: self.change_pifu("默认风格"))  # 明亮皮肤
        self.Ui.action_mingliang.triggered.connect(lambda: self.change_pifu("明亮风格"))  # 明亮皮肤
        self.Ui.action_anhei.triggered.connect(lambda: self.change_pifu("暗黑风格"))  # 暗黑皮肤

        # 漏洞利用
        self.Ui.vuln_exp_button_cmd.clicked.connect(lambda: self.exp_send('cmd'))
        self.Ui.vuln_exp_button_shell.clicked.connect(lambda: self.exp_send('shell'))
        self.Ui.vuln_exp_button_uploadfile.clicked.connect(lambda: self.exp_send('uploadfile'))
        self.Ui.vuln_type.activated[str].connect(self.change_exp_list)
        self.Ui.vuln_name.activated[str].connect(self.change_exp_name_change)
        self.Ui.vuln_exp_comboBox_shell.activated[str].connect(self.change_exp_combox)
        self.Ui.vuln_exp_button_getfile.clicked.connect(
            lambda: self.import_file(self.Ui.vuln_exp_textEdit_shell, '', self.Ui.vuln_exp_lineEdit_filename))  # 导入地址

        #
        # 漏洞扫描右键菜单
        self.Ui.tableWidget_vuln.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Ui.tableWidget_vuln.customContextMenuRequested.connect(
            self.createtableWidget_vulnMenu)  # 将菜单的信号链接到自定义菜单槽函数
        # self.Ui.tableWidget_vuln.customContextMenuRequested['QPoint'].connect(self.createtableWidget_vulnMenu)

        # 重定向输出
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)

    def normalOutputWritten(self, text):
        out_log_ui_obj.append(text)

    def proxy_setting(self):
        self.Proxy_WChild = Ui_Proxy()
        self.proxy_dialog = QtWidgets.QDialog()
        self.Proxy_WChild.setupUi(self.proxy_dialog)
        if int(self.Proxy_enable):
            self.Proxy_WChild.radioButton_proxy_enable.setChecked(True)
        else:
            self.Proxy_WChild.radioButton_proxy_disabled.setChecked(True)
        proxy_index = self.Proxy_WChild.comboBox_proxy_type.findText(self.Proxy_type, QtCore.Qt.MatchFixedString)
        if proxy_index >= 0:
            self.Proxy_WChild.comboBox_proxy_type.setCurrentIndex(proxy_index)
            if self.Proxy_type == "SOCKS4" or self.Proxy_type == "SOCKS5":
                self.Proxy_WChild.lineEdit_proxy_username.setDisabled(False)
                self.Proxy_WChild.lineEdit_proxy_passwd.setDisabled(False)
            else:
                self.Proxy_WChild.lineEdit_proxy_username.setDisabled(True)
                self.Proxy_WChild.lineEdit_proxy_passwd.setDisabled(True)
        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "未找到%s代理类型！" % self.Proxy_type)
        self.Proxy_WChild.lineEdit_proxy_ip.setText(self.Proxy_ip)
        self.Proxy_WChild.lineEdit_proxy_port.setText(str(self.Proxy_port))
        self.Proxy_WChild.lineEdit_proxy_username.setText(self.Proxy_username)
        self.Proxy_WChild.lineEdit_proxy_passwd.setText(self.Proxy_password)
        self.proxy_dialog.setWindowIcon(QtGui.QIcon('Conf/main.png'))
        self.proxy_dialog.show()
        self.Proxy_WChild.pushButton_proxy_save.clicked.connect(self.proxy_save)
        self.Proxy_WChild.comboBox_proxy_type.activated[str].connect(self.change_Proxy_combox_type)

    def change_Proxy_combox_type(self):
        proxy_type = self.Proxy_WChild.comboBox_proxy_type.currentText()
        if proxy_type == "SOCKS4" or proxy_type == "SOCKS5":
            self.Proxy_WChild.lineEdit_proxy_username.setDisabled(False)
            self.Proxy_WChild.lineEdit_proxy_passwd.setDisabled(False)
        else:
            self.Proxy_WChild.lineEdit_proxy_username.setDisabled(True)
            self.Proxy_WChild.lineEdit_proxy_passwd.setDisabled(True)

    def proxy_save(self):
        try:
            self.Proxy_type = self.Proxy_WChild.comboBox_proxy_type.currentText()
            self.Proxy_ip = self.Proxy_WChild.lineEdit_proxy_ip.text()
            self.Proxy_port = int(self.Proxy_WChild.lineEdit_proxy_port.text())
            self.Proxy_username = self.Proxy_WChild.lineEdit_proxy_username.text()
            self.Proxy_password = self.Proxy_WChild.lineEdit_proxy_passwd.text()

            if self.Proxy_WChild.radioButton_proxy_enable.isChecked():
                self.Proxy_enable = '1'
                config_setup.set("Proxy", "proxy_enable", '1')
                self.set_Proxy()
            else:
                self.Proxy_enable = '0'
                config_setup.set("Proxy", "proxy_enable", '0')
            config_setup.set("Proxy", "proxy_type", self.Proxy_type)
            config_setup.set("Proxy", "proxy_ip", self.Proxy_ip)
            config_setup.set("Proxy", "proxy_port", str(self.Proxy_port))
            config_setup.set("Proxy", "proxy_username", self.Proxy_username)
            config_setup.set("Proxy", "proxy_password", self.Proxy_password)
            self.proxy_dialog.close()
        except Exception as e:
            # print(str(e))
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "代理设置错误！请检查。")

    def load_proxy(self):
        try:
            self.Proxy_type = ''
            self.Proxy_ip = ''
            self.Proxy_port = 0
            self.Proxy_enable = ''
            self.Proxy_username = ''
            self.Proxy_password = ''
            for key, value in config_setup.items('Proxy'):
                if value == config_setup.get('Proxy', 'Proxy_enable'):
                    self.Proxy_enable = value
                elif value == config_setup.get('Proxy', 'Proxy_type'):
                    self.Proxy_type = value
                elif value == config_setup.get('Proxy', 'Proxy_ip'):
                    self.Proxy_ip = value
                elif value == config_setup.get('Proxy', 'Proxy_port'):
                    self.Proxy_port = int(value)
                elif value == config_setup.get('Proxy', 'Proxy_username'):
                    self.Proxy_username = value
                elif value == config_setup.get('Proxy', 'Proxy_password'):
                    self.Proxy_password = value
            # print(Proxy_username,Proxy_password)
        except:
            box = QtWidgets.QMessageBox()
            box.information(self, "提示", "代理设置错误！请检查。")
        if int(self.Proxy_enable) and self.Proxy_type and self.Proxy_ip and self.Proxy_port:
            self.set_Proxy()

    def set_Proxy(self):
        box = QtWidgets.QMessageBox()
        if self.Proxy_type == "HTTP":
            socks.set_default_proxy(socks.HTTP, self.Proxy_ip, self.Proxy_port)
            socket.socket = socks.socksocket
            box.information(self, "提示",
                            "代理已被设置：\n代理类型：" + self.Proxy_type + "\n代理IP:" + self.Proxy_ip + "\n代理端口:" + str(
                                self.Proxy_port))
        elif self.Proxy_type == "SOCKS4":
            if self.Proxy_username and self.Proxy_password:
                socks.set_default_proxy(socks.SOCKS4, self.Proxy_ip, self.Proxy_port, self.Proxy_username,
                                        self.Proxy_password)
                box.information(self, "提示",
                                "代理已被设置：\n代理类型：" + self.Proxy_type + "\n代理IP:" + self.Proxy_ip + "\n代理端口:" + str(
                                    self.Proxy_port) + "\n用户名:" + self.Proxy_username + "\n密码:" + self.Proxy_password)

            else:
                socks.set_default_proxy(socks.SOCKS4, self.Proxy_ip, self.Proxy_port)
                box.information(self, "提示",
                                "代理已被设置：\n代理类型：" + self.Proxy_type + "\n代理IP:" + self.Proxy_ip + "\n代理端口:" + str(
                                    self.Proxy_port))
            socket.socket = socks.socksocket
        elif self.Proxy_type == "SOCKS5":
            if self.Proxy_username and self.Proxy_password:
                socks.set_default_proxy(socks.SOCKS5, self.Proxy_ip, self.Proxy_port, self.Proxy_username,
                                        self.Proxy_password)
                box.information(self, "提示",
                                "代理已被设置：\n代理类型：" + self.Proxy_type + "\n代理IP:" + self.Proxy_ip + "\n代理端口:" + str(
                                    self.Proxy_port) + "\n用户名:" + self.Proxy_username + "\n密码:" + self.Proxy_password)
            else:
                socks.set_default_proxy(socks.SOCKS5, self.Proxy_ip, self.Proxy_port)
                box.information(self, "提示",
                                "代理已被设置：\n代理类型：" + self.Proxy_type + "\n代理IP:" + self.Proxy_ip + "\n代理端口:" + str(
                                    self.Proxy_port))
            socket.socket = socks.socksocket

    ## @detail 创建logger类
    def __BuildLogger(self):
        logger = logging.getLogger(__file__)
        logger.setLevel(logging.DEBUG)
        # 建立一个filehandler来把日志记录在文件里，级别为debug以上
        fh = logging.FileHandler(log_file_dir + "FrameScan.log")
        fh.setLevel(logging.DEBUG)
        # 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 设置日志格式
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(lineno)s %(message)s",
                                      datefmt="%Y-%m-%d %H:%M:%S")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # 将相应的handler添加在logger对象中
        logger.addHandler(ch)
        logger.addHandler(fh)
        # 开始打日志
        # logger.debug("debug message")
        # logger.info("info message")
        # logger.warning("warn message")
        # logger.error("error message")
        # logger.critical("critical message")
        return logger

    def replace_text(self):
        type = self.Ui.encode_replace_type.currentText()
        source_text = self.Ui.encode_tihuan_Source.text()
        result_text = self.Ui.encode_tihuan_Result.text()
        if type == "Source":
            data = self.Ui.encode_Source_text.toPlainText()
            text = data.replace(source_text, result_text)
            self.Ui.encode_Source_text.setText(str(text))
        elif type == "Result":
            data = self.Ui.encode_Result_text.toPlainText()
            text = data.replace(source_text, result_text)
            self.Ui.encode_Result_text.setText(str(text))
        else:
            pass

    def Copy_text(self, data):
        # 访问剪切板，存入值
        pyperclip.copy(data)
        # wincld.OpenClipboard()
        # wincld.EmptyClipboard()
        # wincld.SetClipboardData(win32con.CF_UNICODETEXT, data)
        # wincld.CloseClipboard()

    def change_exp_combox(self):
        exp_name_text = self.Ui.vuln_exp_comboBox_shell.currentText()
        if exp_name_text:
            f = open(exp_plugins_dir + '/' + exp_name_text, 'r', encoding='utf-8')
            data = f.read()
            f.close()
            self.Ui.vuln_exp_textEdit_shell.setPlainText(data)
            self.Ui.vuln_exp_lineEdit_filename.setText(exp_name_text)
        else:
            pass

    def load_config(self):
        global config_setup
        global plugins_version
        # 实例化configParser对象
        config_setup = configparser.ConfigParser()
        # -read读取ini文件
        config_setup.read(config_file_dir, encoding='utf-8')
        plugins_version = config_setup.get('Plugins', 'version')
        # print(plugins_version)
        if 'Skin' not in config_setup:  # 如果分组type不存在则插入type分组
            config_setup.add_section('Skin')
            config_setup.set("Skin", "default", '明亮风格')
            qss_Setup = '明亮风格'
        else:
            qss_Setup = config_setup.get('Skin', 'default')
        self.change_pifu(qss_Setup)

    def load_server(self):
        global Server_address
        global Server_user
        global Server_passwd
        Server_address = config_setup.get('Server', 'server')
        Server_user = config_setup.get('Server', 'user')
        Server_passwd = config_setup.get('Server', 'passwd')

    def change_pifu(self, q):
        config_setup.set("Skin", "default", q)
        if q == "默认风格":
            app.setStyleSheet('')
            # apply_stylesheet(app, theme='dark_teal.xml')
        elif q == "明亮风格":
            app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
        elif q == "暗黑风格":
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        #
        # print(i[1].menu().actions()[4].text())
        othersmenubar = self.menuBar()  # 获取窗体的菜单栏
        for i in othersmenubar.actions():
            # print(i.text())
            if i.text() == "选项":
                # sub_action = i()
                for j in i.menu().actions():
                    # 输出为关于软件、检查更新、意见反馈、皮肤风格
                    if j.text() == "皮肤风格":
                        for k in j.menu().actions():
                            if k.text() == q:
                                k.setChecked(True)
                            else:
                                k.setChecked(False)
                        return

    def createtableWidget_vulnMenu(self):
        '''''
                创建右键菜单
        '''
        # 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        self.Ui.tableWidget_vuln.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Ui.tableWidget_vuln.customContextMenuRequested.connect(self.showContextMenu)
        # 创建QMenu
        self.contextMenu = QtWidgets.QMenu(self)
        self.open = self.contextMenu.addAction(u'打开')
        self.daochu = self.contextMenu.addAction(u'导出')
        self.second = self.contextMenu.addMenu(u'复制')
        self.copy_url = self.second.addAction(u'网页地址')
        self.copy_vuln_name = self.second.addAction(u'漏洞名称')
        self.copy_path = self.second.addAction(u'插件路径')
        self.copy_payload = self.second.addAction(u'返回信息')
        self.copy_all = self.second.addAction(u'全部')
        self.delete_textEdit = self.contextMenu.addAction(u'删除')
        self.clear_textEdit = self.contextMenu.addAction(u'清空')

        # 将动作与处理函数相关联
        # 这里为了简单，将所有action与同一个处理函数相关联，
        # 当然也可以将他们分别与不同函数关联，实现不同的功能
        self.open.triggered.connect(self.open_url)
        self.daochu.triggered.connect(lambda: self.export_file(self.Ui.tableWidget_vuln, self.Ui.textEdit_log))
        self.copy_url.triggered.connect(lambda: self.Copy_tableWidget(self.Ui.tableWidget_vuln, 0))
        self.copy_vuln_name.triggered.connect(lambda: self.Copy_tableWidget(self.Ui.tableWidget_vuln, 1))
        self.copy_path.triggered.connect(lambda: self.Copy_tableWidget(self.Ui.tableWidget_vuln, 2))
        self.copy_payload.triggered.connect(lambda: self.Copy_tableWidget(self.Ui.tableWidget_vuln, 4))
        self.copy_all.triggered.connect(lambda: self.Copy_tableWidget(self.Ui.tableWidget_vuln, 'all'))
        self.clear_textEdit.triggered.connect(lambda: self.Clear_tableWidget(self.Ui.tableWidget_vuln))
        self.delete_textEdit.triggered.connect(lambda: self.Delete_tableWidget(self.Ui.tableWidget_vuln))

    # 右键点击时调用的函数，移动鼠标位置
    def showContextMenu(self, pos):
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu.move(QtGui.QCursor.pos())
        self.contextMenu.show()

    def createtableWidget_portscan_vulnMenu(self):
        '''''
                创建右键菜单
        '''
        # 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        self.Ui.portscan_result.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Ui.portscan_result.customContextMenuRequested.connect(self.showContextMenu)
        # 创建QMenu
        self.contextMenu = QtWidgets.QMenu(self)
        self.open_address = self.contextMenu.addAction(u'打开地址')
        self.daochu_portscan = self.contextMenu.addAction(u'导出数据')
        self.copy_portscan = self.contextMenu.addMenu(u'复制内容')
        self.copy_portscan_url = self.copy_portscan.addAction(u'URL')
        self.copy_portscan_ip = self.copy_portscan.addAction(u'IP')
        self.copy_portscan_port = self.copy_portscan.addAction(u'端口')
        self.copy_portscan_title = self.copy_portscan.addAction(u'Title')
        self.copy_portscan_banner = self.copy_portscan.addAction(u'Banner')
        self.copy_portscan_all = self.copy_portscan.addAction(u'全部')
        self.delete_portscan_textEdit = self.contextMenu.addAction(u'删除此条')
        self.clear_portscan_textEdit = self.contextMenu.addAction(u'清空数据')

        # 将动作与处理函数相关联
        # 这里为了简单，将所有action与同一个处理函数相关联，
        # 当然也可以将他们分别与不同函数关联，实现不同的功能
        self.open_address.triggered.connect(lambda: self.open_domain_url('port_url'))
        self.daochu_portscan.triggered.connect(lambda: self.export_file(self.Ui.portscan_result, self.Ui.portscan_logs))
        self.copy_portscan_url.triggered.connect(lambda: self.Copy_portscan_url_tableWidget())
        self.copy_portscan_ip.triggered.connect(lambda: self.Copy_tableWidget(self.Ui.portscan_result, 0))
        self.copy_portscan_port.triggered.connect(lambda: self.Copy_tableWidget(self.Ui.portscan_result, 1))
        self.copy_portscan_title.triggered.connect(lambda: self.Copy_tableWidget(self.Ui.portscan_result, 4))
        self.copy_portscan_banner.triggered.connect(lambda: self.Copy_tableWidget(self.Ui.portscan_result, 5))
        self.copy_portscan_all.triggered.connect(lambda: self.Copy_tableWidget(self.Ui.portscan_result, 'all'))
        self.delete_portscan_textEdit.triggered.connect(lambda: self.Delete_tableWidget(self.Ui.portscan_result))
        self.clear_portscan_textEdit.triggered.connect(lambda: self.Clear_tableWidget(self.Ui.portscan_result))

    def Copy_tableWidget(self, copy_obj, weizhi):
        try:
            data = ''
            if weizhi == 'all':
                # data = self.Ui.tableWidget_vuln.selectedItems()
                for i in copy_obj.selectedItems():
                    data += str(i.text()) + '  '
            else:
                data = copy_obj.selectedItems()[weizhi].text()
            # print(data)
            # 访问剪切板，存入值
            pyperclip.copy(data)
            self.Ui.statusBar.showMessage("复制成功!", 5000)
            # wincld.OpenClipboard()
            # wincld.EmptyClipboard()
            # wincld.SetClipboardData(win32con.CF_UNICODETEXT, data)
            # wincld.CloseClipboard()
        except:
            self.Ui.textEdit_log.append(
                "<a  style=\"color:red\">[%s]Error:请选择一个结果！</a>" % (
                    time.strftime('%H:%M:%S', time.localtime(time.time()))))

    def open_url(self):
        try:
            url = self.Ui.tableWidget_vuln.selectedItems()[0].text()
            webbrowser.open(url)
        except:
            self.Ui.textEdit_log.append(
                "<a  style=\"color:red\">[%s]Error:请选择一个结果！</a>" % (
                    time.strftime('%H:%M:%S', time.localtime(time.time()))))

    def Clear_tableWidget(self, table_obj):
        for i in range(0, table_obj.rowCount()):  # 循环行
            table_obj.removeRow(0)

    def Delete_tableWidget(self, table_obj):
        table_obj.removeRow(table_obj.currentRow())  # 删除选中的行

    # 得到选中的方法
    def get_methods(self):
        all_data = []
        item = QtWidgets.QTreeWidgetItemIterator(self.Ui.treeWidget_Plugins)
        # 该类的value()即为QTreeWidgetItem
        while item.value():
            if not item.value().parent():  # 判断有没有父节点
                pass
            else:  # 输出所有子节点
                if item.value().checkState(0) == QtCore.Qt.Checked:
                    # print(item.value().text(0))
                    for cms in self.poc_cms_name_dict:
                        for poc in self.poc_cms_name_dict[cms]:
                            # print(item.value().parent().text(0),item.value().text(0))
                            if poc['vuln_name'] == item.value().text(0) and poc[
                                'cms_name'] == item.value().parent().text(0):
                                all_data.append(poc)
            item = item.__iadd__(1)
        # print(all_data)
        # 返回所有选中的数据
        return all_data

    # 开始扫描
    def vuln_Start(self):
        try:
            timeout = int(self.Ui.comboBox_timeout.currentText())
        except:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "超时获取失败！")
            return
        jump_url = self.Ui.jump_url.isChecked()
        jump_fofa = self.Ui.jump_fofa.isChecked()
        threadnum = int(self.Ui.threadsnum.currentText())
        heads = self.Ui.vuln_scanner_textEdit_heads.toPlainText()
        target = []
        url = self.Ui.lineEdit_vuln_url.text()
        if "https://" in url.lower() or 'http://' in url.lower():
            target.append(url.strip())
        else:
            if self.vuln_url_list:
                target = self.vuln_url_list
            else:
                self.Ui.textEdit_log.append(
                    '[%s] %s' % (time.strftime('%H:%M:%S', time.localtime(time.time())), "未获取到URL"))
                return
        # print(target)
        poc_data = self.get_methods()  # 得到选中的数据
        self.vuln_scan_obj = Vuln_Scanner(vuln_plugins_dir, self.__Logger, timeout, jump_url, jump_fofa, threadnum,
                                          heads, target, poc_data)
        self.vuln_scan_obj._data.connect(self.update_vulnscanner_data)  # 线程发过来的信号挂接到槽函数update_sum
        self.vuln_scan_obj._log.connect(self.update_vulnscanner_log)  # 线程发过来的信号挂接到槽函数update_sum
        self.Ui.pushButton_vuln_file.setEnabled(False)
        self.Ui.pushButton_vuln_start.setEnabled(False)
        self.Ui.pushButton_vuln_stop.setEnabled(True)
        self.Ui.textEdit_log.clear()
        self.vuln_scan_obj.start()  # 线程启动

    def update_vulnscanner_log(self, log):
        self.Ui.textEdit_log.append('[%s] %s' % (time.strftime('%H:%M:%S', time.localtime(time.time())), log))
        if "停止扫描" in log or "扫描结束" in log:
            self.Ui.pushButton_vuln_file.setEnabled(True)
            self.Ui.pushButton_vuln_start.setEnabled(True)
            self.Ui.pushButton_vuln_stop.setEnabled(False)

    def update_vulnscanner_data(self, data):
        # print(type,text)
        if data.get('Error_Info'):
            self.Ui.textEdit_log.append(
                "<p style=\"color:red\">[%s]Error:<br>Filename:%s<br>Error-Info:%s。</a>" % (
                    time.strftime('%H:%M:%S'), data.get('poc_file'), data.get('Error_Info')))
        if data.get('Debug_Info') and self.Ui.vuln_scanner_debug.isChecked():
            self.Ui.textEdit_log.append(
                "<p style=\"color:blue\">[%s]Debug:<br>Filename:%s<br>Debug-Info:%s。</a>" % (
                    time.strftime('%H:%M:%S'), data.get('poc_file'), data.get('Debug_Info')))
        if data.get('Result'):
            url = data.get('url')
            filename = data.get('poc_file')
            poc_name = data.get('poc_name')
            cms_name = data.get('cms_name')
            self.Ui.textEdit_log.append(
                "<p style=\"color:green\">[%s] Result:%s----%s----%s。</a>" % (
                    (time.strftime('%H:%M:%S', time.localtime(time.time()))), url, (cms_name + "|" + poc_name), "存在"))
            self.Ui.tableWidget_vuln.setSortingEnabled(False)

            row = self.Ui.tableWidget_vuln.rowCount()  # 获取行数
            self.Ui.tableWidget_vuln.setRowCount(row + 1)
            urlItem = QTableWidgetItem(url)
            nameItem = QTableWidgetItem(str(cms_name + "|" + poc_name))
            payloadItem = QTableWidgetItem(data.get('Result_Info'))
            resultItem = QTableWidgetItem("存在")
            filenameItem = QTableWidgetItem(filename)
            self.Ui.tableWidget_vuln.setItem(row, 0, urlItem)
            self.Ui.tableWidget_vuln.setItem(row, 1, nameItem)
            self.Ui.tableWidget_vuln.setItem(row, 3, resultItem)
            self.Ui.tableWidget_vuln.setItem(row, 2, filenameItem)
            self.Ui.tableWidget_vuln.setItem(row, 4, payloadItem)
            self.Ui.tableWidget_vuln.setSortingEnabled(True)

        elif not data.get('Result'):
            if data.get('Result_Info'):
                self.Ui.textEdit_log.append(
                    "<p style=\"color:black\">[%s] Result:%s----%s----%s----%s。</a>" % (
                        time.strftime('%H:%M:%S'), data.get('url'), data.get('cms_name') + "|" + data.get('poc_name'),
                        "不存在", data.get('Result_Info')))
            else:
                self.Ui.textEdit_log.append(
                    "<p style=\"color:black\">[%s] Result:%s----%s----%s。</a>" % (
                        time.strftime('%H:%M:%S'), data.get('url'), data.get('cms_name') + "|" + data.get('poc_name'),
                        "不存在"))

    def vuln_Stop(self):
        self.Ui.textEdit_log.append(
            "<p style=\"color:black\">[%s]Info:发出停止信号，请等待...</a>" % (
                (time.strftime('%H:%M:%S', time.localtime(time.time())))))
        self.vuln_scan_obj.vuln_portQueue.queue.clear()
        # 初始化加载vuln插件

    def load_vuln_plugins(self):
        if not os.path.isfile(DB_NAME):
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "数据文件不存在，正在重新加载数据库！")
            self.vuln_reload_Plugins()
            return 0
        # 加载漏洞扫描模块
        try:
            # 列出所有数据
            sql_poc = "SELECT cms_name,vuln_name,vuln_file,FofaQuery_type,FofaQuery_link,FofaQuery_rule from vuln_poc where ispoc !=''"
            poc_dict = self.sql_search(sql_poc, 'dict')
            # print(values)
        except Exception as e:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "数据文件错误：\n%s" % e)
            return 0
        # 将查询的值组合为字典包含列表的形式
        self.poc_cms_name_dict = {}
        for cms in poc_dict:
            self.poc_cms_name_dict[cms['cms_name']] = []
        # print(cms_name)
        for cms in poc_dict:
            poc_cms_sing = {}
            poc_cms_sing['cms_name'] = cms['cms_name']
            poc_cms_sing['vuln_name'] = cms['vuln_name']
            poc_cms_sing['vuln_file'] = cms['vuln_file']
            poc_cms_sing['FofaQuery_type'] = cms['FofaQuery_type']
            poc_cms_sing['FofaQuery_link'] = cms['FofaQuery_link']
            poc_cms_sing['FofaQuery_rule'] = cms['FofaQuery_rule']
            self.poc_cms_name_dict[cms['cms_name']].append(poc_cms_sing)
        for cms in self.poc_cms_name_dict:
            # 设置root为self.treeWidget_Plugins的子树，故root是根节点
            root = QTreeWidgetItem(self.Ui.treeWidget_Plugins)
            root.setText(0, cms)  # 设置根节点的名称
            # root.setCheckState(0, QtCore.Qt.Unchecked)  # 开启复选框
            root.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)

            # print(cms_name[cms])
            for cms_single in self.poc_cms_name_dict[cms]:
                # 为root节点设置子结点
                child1 = QTreeWidgetItem(root)
                child1.setText(0, cms_single['vuln_name'])
                child1.setCheckState(0, QtCore.Qt.Unchecked)
        # self.Ui.treeWidget_Plugins.itemChanged.connect(self.handleChanged)
        self.Ui.treeWidget_Plugins.doubleClicked.connect(self.Show_Plugins_info)
        self.Ui.textEdit_log.append(
            "<p style=\"color:green\">[%s]Success:插件加载完成，共%s个。</a>" % (
                time.strftime('%H:%M:%S', time.localtime(time.time())), len(poc_dict)))

    # 初始化加载exp插件
    def load_exp_plugins(self):
        try:
            # print(self.poc_dict)
            sql_exp = "SELECT cms_name,vuln_name,vuln_file,vuln_description,FofaQuery_type,FofaQuery_link,FofaQuery_rule from vuln_poc where isexp !='' and isexp ='1'"
            exp_dict = self.sql_search(sql_exp, 'dict')

            # 将查询的值组合为字典包含列表的形式
            self.exp_cms_name_dict = {}
            for cms in exp_dict:
                self.exp_cms_name_dict[cms['cms_name']] = []
            # print(exp_cms_name_dict)
            for exp_cms in exp_dict:
                # print(cms['cmsname'] )
                # if cms['cmsname'] in cms_name.keys():
                exp_cms_sing = {}
                exp_cms_sing['cms_name'] = exp_cms['cms_name']
                exp_cms_sing['vuln_name'] = exp_cms['vuln_name']
                exp_cms_sing['vuln_file'] = exp_cms['vuln_file']
                exp_cms_sing['vuln_description'] = exp_cms['vuln_description']
                self.exp_cms_name_dict[exp_cms['cms_name']].append(exp_cms_sing)
            # print(exp_cms_name_dict)
            self.Ui.vuln_name.clear()
            self.Ui.vuln_type.clear()
            for cms in self.exp_cms_name_dict:
                self.Ui.vuln_type.addItem(cms)
            for exp_methods in list(self.exp_cms_name_dict.values())[0]:
                # print(exp_methods)
                self.Ui.vuln_name.addItem(exp_methods['vuln_name'])
                self.Ui.vuln_exp_textEdit_info.setText("漏洞信息会显示在这里！")
            # 加载本地shell文件
            for root, dirs, files in os.walk(exp_plugins_dir):
                for file in files:
                    if file[0] != ".":
                        self.Ui.vuln_exp_comboBox_shell.addItem(file)
            self.change_exp_combox()
        except Exception as e:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "数据文件错误：\n%s" % e)
            # self.vuln_reload_Plugins()

    # 初始化加载note插件
    def Show_Plugins_info(self):
        poc_name = self.Ui.treeWidget_Plugins.currentItem().text(0)
        # 列出所有数据
        sql = "SELECT *  from vuln_poc where vuln_name='%s'" % poc_name
        values = self.sql_search(sql, 'dict')
        # print(values)
        try:
            self.dialog.close()
        except Exception as e:
            pass
        if len(values) != 0:
            self.WChild_info = Ui_From_Vuln_Info()
            self.dialog = QtWidgets.QDialog(self)

            self.WChild_info.setupUi(self.dialog)
            self.dialog.setWindowIcon(QtGui.QIcon('Conf/main.png'))
            self.dialog.show()
            # print(values)
            self.WChild_info.vuln_name.setText(values[0]['vuln_name'])
            self.WChild_info.cms_name.setText(values[0]['cms_name'])
            if values[0]['isexp']:
                self.WChild_info.vuln_exp.setText("True")
            else:
                self.WChild_info.vuln_exp.setText("暂无")
            if values[0]['ispoc']:
                self.WChild_info.vuln_poc.setText("True")
            else:
                self.WChild_info.vuln_poc.setText("暂无")

            self.WChild_info.vuln_file.setText(vuln_plugins_dir + values[0]['cms_name'] + '/' + values[0]['vuln_file'])
            self.WChild_info.vuln_url.setText(
                '<a href="' + values[0]['vuln_referer'] + '">' + values[0]['vuln_referer'] + '</a>')
            self.WChild_info.vuln_miaoshu.setText(values[0]['vuln_description'])
            self.WChild_info.vuln_solution.setText(values[0]['vuln_solution'])
            self.WChild_info.vuln_identifier.setText(values[0]['vuln_identifier'])
            return 0
        else:
            return

    # 导入文件列表
    def vuln_import_file(self, lineEdit_vuln_obj, textEdit_log_obj, type):
        self.vuln_url_list = []
        self.domain_url_list = []
        url_list = []
        filename = self.file_open(r"Text Files (*.txt);;All files(*.*)")
        try:
            if os.path.isfile(filename):
                textEdit_log_obj.append(
                    "<a  style=\"color:black\">[%s]Info:正在从文件中读取URL...</a>" % (
                        time.strftime('%H:%M:%S', time.localtime(time.time()))))
                f = open(filename, 'r', encoding='utf-8')
                for line in f.readlines():
                    if "https://" in line.lower() or 'http://' in line.lower():
                        url_list.append(line.strip())
                    else:
                        url_list.append('http://' + line.strip())

                textEdit_log_obj.append(
                    "<a  style=\"color:black\">[%s]Info:读取完成，共加载%s条。</a>" % (
                        (time.strftime('%H:%M:%S', time.localtime(time.time()))), len(url_list)))
            lineEdit_vuln_obj.setText(filename)
            if type == 'vuln_scanner':
                self.vuln_url_list = url_list
            if type == 'domain_scanner':
                self.domain_url_list = url_list

        except Exception as e:
            textEdit_log_obj.append(
                "<a  style=\"color:red\">[%s]Error:文件打开失败，请使用UTF-8编码</a>" % (
                    time.strftime('%H:%M:%S', time.localtime(time.time()))))
            pass

    #
    # # 导入文件列表
    def import_file(self, path_obj, type='', filename_obj=''):
        filename = self.file_open(r"All files(*.*)")
        try:
            data = ''
            if os.path.isfile(filename):
                f = open(filename, 'r', encoding='utf-8')
                data = f.read()
                f.close()
                if data:
                    if type == "PlainText":
                        path_obj.setPlainText(data)
                    else:
                        path_obj.setText(data)
                    if filename_obj:
                        filename = os.path.basename(filename)
                        filename_obj.setText(filename)
        except Exception as e:
            # print(str(e))
            box = QtWidgets.QMessageBox()
            box.warning(self, "错误", "文件打开失败，请确实编码是否是utf-8")

    # 导出扫描结果
    def export_file(self, table_obj, log_obj):
        data = []
        comdata = []
        if table_obj.rowCount() > 0:
            for lll in range(0, table_obj.columnCount()):  # 循环列
                data.append(table_obj.horizontalHeaderItem(lll).text())  # 空格分隔
            comdata.append(list(data))
            data = []
            for i in range(0, table_obj.rowCount()):  # 循环行
                for j in range(0, table_obj.columnCount()):  # 循环列
                    if table_obj.item(i, j) != None:  # 有数据
                        data.append(table_obj.item(i, j).text())  # 空格分隔
                comdata.append(list(data))
                data = []
            if len(comdata) > 0:
                path = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '.csv').replace(' ', '-').replace('-',
                                                                                                                 '').replace(
                    ':', '')
                # print(path)
                file_name = self.file_save(path)
                if file_name != "":
                    with open(file_name, 'w', encoding='utf-8', newline="") as f:
                        writer = csv.writer(f)
                        for row in comdata:
                            writer.writerow(row)
                    f.close()
                    box = QtWidgets.QMessageBox()
                    box.information(self, "Success", "导出成功！\n文件位置：" + file_name)
                    # self.Ui.statusBar.showMessage("Success", "导出成功！\n文件位置：" + file_name, 5000)
                else:
                    # box2= QtWidgets.QMessageBox()
                    # box2.warning(self, "Error", "保存失败！文件名错误！" )
                    pass
            else:
                try:
                    box = QtWidgets.QMessageBox()
                    box.warning(self, "提示", "表格无结果！")
                    if log_obj != '':
                        log_obj.append(
                            "[%s]Faile:没有结果！" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
                except:
                    pass

    def vuln_reload_update(self):
        box = QtWidgets.QMessageBox()
        try:
            ua = {
                "Authorization": "Basic %s" % (base64.b64encode((Server_user + ":" + Server_passwd).encode())).decode()}
            req = requests.get(Server_address + 'update.json', headers=ua, timeout=5, verify=False)
            if req.status_code == 200:
                dic_data = json.loads(req.text)
                if int(plugins_version.replace('.', '')) < int(dic_data.get('version').replace('.', '')):
                    reply = QMessageBox.question(self, '插件更新',
                                                 "当前插件版本：v%s\n最新插件版本：v%s\n更新日志:\n%s\n检测到插件库已更新，是否立即更新?" % (
                                                     plugins_version, dic_data.get('version'),
                                                     dic_data.get('description')),
                                                 QMessageBox.Yes | QMessageBox.No,
                                                 QMessageBox.Yes)
                    if reply == QMessageBox.Yes:
                        box.warning(self, "提示", "插件不会删除原有的插件，若完整更新，请手动删除插件目录！")
                        sysstr = platform.system()
                        if (sysstr == "Windows"):
                            houzhui = '.pyd'
                        elif (sysstr == "Linux"):
                            houzhui = '.so'
                        else:
                            houzhui = '.pyc'
                        for cms in dic_data.get('data'):
                            cms_path = vuln_plugins_dir + '/' + cms
                            # 判断结果
                            if not os.path.exists(cms_path):
                                # 如果不存在则创建目录 # 创建目录操作函数
                                os.makedirs(cms_path)
                            for poc in dic_data.get('data').get(cms):

                                req = requests.get(Server_address + cms + '/' + poc + houzhui, headers=ua, timeout=5,
                                                   verify=False)
                                if req.status_code == 200:
                                    f = open(vuln_plugins_dir + '/' + cms + '/' + poc + houzhui, 'wb')
                                    f.write(req.content)
                                    f.close()
                                    # print(poc+houzhui)
                                else:
                                    req = requests.get(Server_address + cms + '/' + poc + '.pyc', headers=ua, timeout=5,
                                                       verify=False)
                                    if req.status_code == 200:
                                        f = open(vuln_plugins_dir + '/' + cms + '/' + poc + '.pyc', 'wb')
                                        f.write(req.content)
                                        f.close()
                                        # print(poc+'.py')
                                    else:
                                        req = requests.get(Server_address + cms + '/' + poc + '.py', headers=ua,
                                                           timeout=5,
                                                           verify=False)
                                        if req.status_code == 200:
                                            f = open(vuln_plugins_dir + '/' + cms + '/' + poc + '.py', 'wb')
                                            f.write(req.content)
                                            f.close()
                                        else:
                                            box.warning(self, "警告", '插件%s丢失!' % (cms + '|' + poc))

                        config_setup.set("Plugins", "version", dic_data.get('version'))
                        box.information(self, "插件更新", "插件更新完成,当前版本：v" + dic_data.get('version'))
                        self.vuln_reload_Plugins()
                else:
                    box.information(self, "插件更新",
                                    "当前插件版本：v%s\n最新插件版本：v%s\n已是最新版本" % (plugins_version, dic_data.get('version')))
            elif req.status_code == 404:
                box.warning(self, "提示", "服务器json文件丢失，请检查！")
            else:
                box.warning(self, "提示", "服务器连接失败，请检查！")
        except Exception as  e:
            box.warning(self, "提示", str(e))

    def Show_Server_Widget(self):
        self.form_server = QtWidgets.QWidget()
        self.Server_widget = Ui_Server()
        self.Server_widget.setupUi(self.form_server)
        self.form_server.setWindowIcon(QtGui.QIcon('Conf/main.png'))
        self.Server_widget.lineEdit_server.setText(config_setup.get('Server', 'server'))
        self.Server_widget.lineEdit_user.setText(config_setup.get('Server', 'user'))
        self.Server_widget.lineEdit_passwd.setText(config_setup.get('Server', 'passwd'))
        self.form_server.show()
        self.Server_widget.pushButton_ceshi.clicked.connect(self.Server_ceshi)
        self.Server_widget.pushButton_save.clicked.connect(self.Server_save)

    def Server_ceshi(self):
        box = QtWidgets.QMessageBox()
        try:
            server = self.Server_widget.lineEdit_server.text()
            user = self.Server_widget.lineEdit_user.text()
            passwd = self.Server_widget.lineEdit_passwd.text()
            ua = {"Authorization": "Basic %s" % (base64.b64encode((user + ":" + passwd).encode())).decode()}
            req = requests.get(server, headers=ua, timeout=5, verify=False)
            if req.status_code == 200:
                box.information(self, "提示", "连接成功！")
            else:
                box.warning(self, "提示", "连接失败！")
        except Exception as  e:
            box.warning(self, "提示", str(e))

    def Server_save(self):
        server = self.Server_widget.lineEdit_server.text()
        user = self.Server_widget.lineEdit_user.text()
        passwd = self.Server_widget.lineEdit_passwd.text()
        config_setup.set("Server", "server", server)
        config_setup.set("Server", "user", user)
        config_setup.set("Server", "passwd", passwd)
        box = QtWidgets.QMessageBox()
        box.information(self, "提示", "保存成功！")
        self.form_server.close()

    # 显示插件
    def vuln_ShowPlugins(self):
        # self.form2 = QtWidgets.QWidget()
        # self.vuln_widget = Ui_Form_Vuln()
        # self.vuln_widget.setupUi(self.form2)
        # self.form2.setStyleSheet(qss_style)
        # self.form2.setWindowIcon(QtGui.QIcon('Conf/main.png'))
        # self.form2.show()

        self.vuln_widget = Ui_Form_Vuln()
        self.vuln_dialog = QtWidgets.QDialog(self)
        self.vuln_widget.setupUi(self.vuln_dialog)
        self.vuln_dialog.setWindowIcon(QtGui.QIcon('./logo.ico'))
        self.vuln_dialog.show()

        self.vuln_update_table_data()
        self.vuln_widget.pushButton_show_Plugins_add.clicked.connect(self.vuln_plugins_add)
        self.vuln_widget.pushButton_show_Plugins_delete.clicked.connect(self.vuln_plugins_delete)
        self.vuln_widget.pushButton_show_Plugins_edit.clicked.connect(self.vuln_plugins_edit)
        self.vuln_widget.pushButton_show_Plugins_reload.clicked.connect(self.vuln_update_table_data)

        self.vuln_widget.show_Plugins_comboBox_cms_name.currentIndexChanged.connect(
            self.show_plugins_go)  # comboBox事件选中触发刷新
        self.vuln_widget.show_Plugins_comboBox_vuln_class.currentIndexChanged.connect(
            self.show_plugins_go)  # comboBox事件选中触发刷新

    def vuln_plugins_add(self):
        sql = 'SELECT distinct cms_name from vuln_poc'
        cms_name_data = self.sql_search(sql)
        self.form3_vuln_edit = QtWidgets.QWidget()
        self.widget_vuln_edit = Ui_Form_Vuln_Edit()
        self.widget_vuln_edit.setupUi(self.form3_vuln_edit)
        self.form3_vuln_edit.setWindowIcon(QtGui.QIcon('Conf/main.ico'))
        self.form3_vuln_edit.show()
        for cms_name in cms_name_data:
            self.widget_vuln_edit.comboBox_vuln_cms.addItem(cms_name[0])
        self.highlighter = PythonHighlighter(self.widget_vuln_edit.vuln_exp_textEdit_shell.document())
        f = open(vuln_plugins_template, 'r', encoding='utf-8')
        data = f.read()
        f.close()
        self.widget_vuln_edit.vuln_exp_textEdit_shell.setText(data)
        # 插件保存
        self.widget_vuln_edit.pushButton_vuln_save.clicked.connect(self.vuln_plugins_save)

    def vuln_plugins_delete(self):
        obj = self.vuln_widget.show_Plugins.selectedItems()
        id = obj[0].text()

        filename = vuln_plugins_dir + obj[1].text() + '/' + obj[7].text()
        sql = "DELETE FROM vuln_poc WHERE id=" + id
        result_flag = self.sql_search(sql, 'delete')
        if result_flag:
            box = QtWidgets.QMessageBox()
            self.vuln_update_table_data()
            reply = QMessageBox.question(window, '插件删除', "数据库已删除，是否删除本地文件", QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                try:
                    remove_file = ''
                    if os.path.isfile(filename + '.py'):
                        os.remove(filename + '.py')
                        remove_file = filename + '.py'
                    if os.path.isfile(filename + houzhui):
                        os.remove(filename + houzhui)
                        remove_file += "\n" + filename + '.py'
                    box.information(self, "Success", remove_file + "\n文件删除成功！")
                    self.vuln_reload_Plugins()
                except Exception as e:
                    pass
            else:
                pass

    # 刷新显示的数据
    def vuln_update_table_data(self):
        self.vuln_widget.show_Plugins_comboBox_cms_name.clear()
        self.vuln_widget.show_Plugins_comboBox_vuln_class.clear()
        sql = "SELECT * from vuln_poc"
        values = self.sql_search(sql, 'dict')
        i = 0
        self.vuln_widget.show_Plugins.setRowCount(len(values))
        sql2 = "SELECT distinct cms_name from vuln_poc"
        sql_vuln_class = "SELECT distinct vuln_class from vuln_poc where vuln_class!='' and vuln_class not null"
        cms_name_data = self.sql_search(sql2)
        vuln_class_data = self.sql_search(sql_vuln_class)
        # 添加查询列表
        self.vuln_widget.show_Plugins_comboBox_cms_name.addItem("ALL")
        self.vuln_widget.show_Plugins_comboBox_vuln_class.addItem("ALL")
        for cms_name in cms_name_data:
            self.vuln_widget.show_Plugins_comboBox_cms_name.addItem(cms_name[0])
        for vuln_class in vuln_class_data:
            self.vuln_widget.show_Plugins_comboBox_vuln_class.addItem(vuln_class[0])
        # print(cms_name[0])
        self.vuln_widget.show_Plugins.setSortingEnabled(False)

        for single in values:
            # print(single)
            id = QTableWidgetItem(str(single['id']))
            cms_name = QTableWidgetItem(str(single['cms_name']))
            vuln_name = QTableWidgetItem(str(single['vuln_name']))
            vuln_class = QTableWidgetItem(str(single['vuln_class']))
            vuln_identifier = QTableWidgetItem(str(single['vuln_identifier']))
            vuln_referer = QTableWidgetItem(str(single['vuln_referer']))
            vuln_description = QTableWidgetItem(str(single['vuln_description']))
            vuln_file = QTableWidgetItem(str(single['vuln_file']))
            vuln_author = QTableWidgetItem(str(single['vuln_author']))
            vuln_solution = QTableWidgetItem(str(single['vuln_solution']))
            self.vuln_widget.show_Plugins.setItem(i, 0, id)
            self.vuln_widget.show_Plugins.setItem(i, 1, cms_name)
            self.vuln_widget.show_Plugins.setItem(i, 2, vuln_name)
            self.vuln_widget.show_Plugins.setItem(i, 3, vuln_class)
            self.vuln_widget.show_Plugins.setItem(i, 4, vuln_identifier)
            self.vuln_widget.show_Plugins.setItem(i, 5, vuln_referer)
            self.vuln_widget.show_Plugins.setItem(i, 6, vuln_description)
            self.vuln_widget.show_Plugins.setItem(i, 7, vuln_file)
            self.vuln_widget.show_Plugins.setItem(i, 8, vuln_author)
            self.vuln_widget.show_Plugins.setItem(i, 9, vuln_solution)
            i = i + 1
        self.vuln_widget.show_Plugins.setVisible(False)
        self.vuln_widget.show_Plugins.resizeColumnToContents(0)
        self.vuln_widget.show_Plugins.resizeColumnToContents(1)
        self.vuln_widget.show_Plugins.resizeColumnToContents(2)
        self.vuln_widget.show_Plugins.resizeColumnToContents(3)
        self.vuln_widget.show_Plugins.resizeColumnToContents(4)
        self.vuln_widget.show_Plugins.resizeColumnToContents(8)

        # self.vuln_widget.show_Plugins.resizeColumnsToContents()
        self.vuln_widget.show_Plugins.setVisible(True)
        self.vuln_widget.show_Plugins.setSortingEnabled(True)

    def vuln_plugins_edit(self):
        try:
            id = self.vuln_widget.show_Plugins.selectedItems()[0].text()
        except:
            box = QtWidgets.QMessageBox()
            box.information(self, "Error", "请选择一个插件！")
            return
        if id:
            sql = 'SELECT distinct * from vuln_poc where id=' + id
            cms_name_data = self.sql_search(sql, 'dict')
            plugins = vuln_plugins_dir + cms_name_data[0]['cms_name'] + '/' + cms_name_data[0]['vuln_file'] + '.py'
            if os.path.splitext(plugins)[-1] != '.py':
                box = QtWidgets.QMessageBox()
                box.information(self, "Error", "此插件非py脚本格式！")
                return
            f = open(plugins, 'r', encoding='utf-8')
            data = f.read()
            f.close()
            self.form3_vuln_edit = QtWidgets.QWidget()
            self.widget_vuln_edit = Ui_Form_Vuln_Edit()
            self.widget_vuln_edit.setupUi(self.form3_vuln_edit)
            self.form3_vuln_edit.setWindowIcon(QtGui.QIcon('Conf/main.png'))
            self.form3_vuln_edit.show()
            self.widget_vuln_edit.comboBox_vuln_cms.addItem(cms_name_data[0]['cms_name'])
            self.highlighter = PythonHighlighter(self.widget_vuln_edit.vuln_exp_textEdit_shell.document())
            self.widget_vuln_edit.vuln_exp_textEdit_shell.setText(data)
            self.widget_vuln_edit.label_vuln_id.setText(id)
            self.widget_vuln_edit.lineEdit_vuln_file.setText(cms_name_data[0]['vuln_file'])
            # 插件保存
            self.widget_vuln_edit.pushButton_vuln_save.clicked.connect(self.vuln_plugins_save)
        else:
            box = QtWidgets.QMessageBox()
            box.information(self, "Error", "请选择一个插件！")

    def vuln_plugins_save(self):  # 需要插入数据库一条保存的数据
        try:
            cms_name = self.widget_vuln_edit.comboBox_vuln_cms.currentText()
            fine_name = self.widget_vuln_edit.lineEdit_vuln_file.text()
            if fine_name:
                plugins_text = self.widget_vuln_edit.vuln_exp_textEdit_shell.toPlainText()
                if not os.path.exists(vuln_plugins_dir + '/' + cms_name):
                    os.makedirs(vuln_plugins_dir + '/' + cms_name)
                else:
                    if fine_name[:8] != "Plugins_":
                        fine_name = 'Plugins_' + fine_name
                    if not fine_name.endswith('.py'):
                        fine_name = fine_name + '.py'
                    plugins_filename = vuln_plugins_dir + '/' + cms_name + '/' + fine_name
                    f = open(plugins_filename, 'w', encoding='utf-8')
                    f.write(plugins_text)
                    f.close()
                    nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(plugins_filename[:-3],
                                                                         plugins_filename).load_module()
                    vuln_info = nnnnnnnnnnnn1.vuln_info()
                    if vuln_info.get('vuln_class'):
                        vuln_class = vuln_info.get('vuln_class')
                    else:
                        vuln_class = '未分类'
                    if vuln_info.get('FofaQuery_link'):
                        FofaQuery_link = (vuln_info.get('FofaQuery_link'))
                    else:
                        FofaQuery_link = ''
                    if vuln_info.get('FofaQuery_rule'):
                        FofaQuery_rule = vuln_info.get('FofaQuery_rule')
                    else:
                        FofaQuery_rule = ''
                    insert_sql = 'insert into vuln_poc  (id,cms_name,vuln_file,vuln_name,vuln_author,vuln_referer,vuln_description,vuln_identifier,vuln_solution,ispoc,isexp,vuln_class,FofaQuery_link,FofaQuery_rule) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                    conn = sqlite3.connect(DB_NAME)
                    # 创建一个游标 curson
                    cursor = conn.cursor()
                    id_sql = "select id from vuln_poc  order by id desc limit 1"
                    cursor.execute(id_sql)
                    id_values = cursor.fetchall()
                    # print(id_values[0][0])
                    # 将数据插入到表中
                    cursor.execute(insert_sql, (
                        str(int(id_values[0][0]) + 1), cms_name, fine_name[:-3], vuln_info['vuln_name'],
                        vuln_info['vuln_author'],
                        vuln_info['vuln_referer'], vuln_info['vuln_description'],
                        vuln_info['vuln_identifier'], vuln_info['vuln_solution'], vuln_info['ispoc'],
                        vuln_info['isexp'], vuln_class, FofaQuery_link, FofaQuery_rule))
                    conn.commit()  # 提交
                    cursor.close()
                    conn.close()
                    self.vuln_update_table_data()
                    box = QtWidgets.QMessageBox()
                    box.information(self, "Error", "保存成功！")
                    self.form3_vuln_edit.close()
            else:
                box = QtWidgets.QMessageBox()
                box.information(self, "Error", "请输入插件名称！")
        except Exception as e:
            box = QtWidgets.QMessageBox()
            box.information(self, "Error", "保存失败\n！" + str(e))

    # 单击列表刷新显示控件
    def show_plugins_go(self):
        self.vuln_widget.show_Plugins.clearContents()
        cms_name = self.vuln_widget.show_Plugins_comboBox_cms_name.currentText()  # 获取文本
        vuln_class = self.vuln_widget.show_Plugins_comboBox_vuln_class.currentText()  # 获取文本
        if cms_name == "ALL" and vuln_class == "ALL":
            sql = "SELECT * from vuln_poc "
        elif cms_name == "ALL" and vuln_class != "ALL":
            sql = "SELECT * from vuln_poc where vuln_class='%s'" % (vuln_class)
        elif cms_name != "ALL" and vuln_class == "ALL":
            sql = "SELECT * from vuln_poc where cms_name = '%s'" % (cms_name)
        else:
            sql = "SELECT * from vuln_poc where cms_name = '%s' and vuln_class='%s'" % (cms_name, vuln_class)
        cms_data = self.sql_search(sql, 'dict')
        i = 0
        self.vuln_widget.show_Plugins.setRowCount(len(cms_data))
        self.vuln_widget.show_Plugins.setSortingEnabled(False)
        for single in cms_data:
            id = QTableWidgetItem(str(single['id']))
            cms_name = QTableWidgetItem(str(single['cms_name']))
            vuln_name = QTableWidgetItem(str(single['vuln_name']))
            vuln_class = QTableWidgetItem(str(single['vuln_class']))
            vuln_identifier = QTableWidgetItem(str(single['vuln_identifier']))
            vuln_referer = QTableWidgetItem(str(single['vuln_referer']))
            vuln_description = QTableWidgetItem(str(single['vuln_description']))
            vuln_file = QTableWidgetItem(str(single['vuln_file']))
            vuln_author = QTableWidgetItem(str(single['vuln_author']))
            vuln_solution = QTableWidgetItem(str(single['vuln_solution']))
            self.vuln_widget.show_Plugins.setItem(i, 0, id)
            self.vuln_widget.show_Plugins.setItem(i, 1, cms_name)
            self.vuln_widget.show_Plugins.setItem(i, 2, vuln_name)
            self.vuln_widget.show_Plugins.setItem(i, 3, vuln_class)
            self.vuln_widget.show_Plugins.setItem(i, 4, vuln_identifier)
            self.vuln_widget.show_Plugins.setItem(i, 5, vuln_referer)
            self.vuln_widget.show_Plugins.setItem(i, 6, vuln_description)
            self.vuln_widget.show_Plugins.setItem(i, 7, vuln_file)
            self.vuln_widget.show_Plugins.setItem(i, 8, vuln_author)
            self.vuln_widget.show_Plugins.setItem(i, 9, vuln_solution)
            i = i + 1
        self.vuln_widget.show_Plugins.setSortingEnabled(True)

    # 重新加载插件
    def vuln_reload_Plugins(self):
        self.Ui.treeWidget_Plugins.clear()
        self.Ui.textEdit_log.setText("[%s]Start:正在重新加载插件..." % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
        # 连接数据库。如果数据库不存在的话，将会自动创建一个 数据库
        conn = sqlite3.connect(DB_NAME)
        # 创建一个游标 curson
        cursor = conn.cursor()
        # 删除数据库，重新建立
        if os.path.isfile(DB_NAME):
            try:
                sql = 'drop table if exists vuln_poc;'
                cursor.execute(sql)
                self.Ui.textEdit_log.append(
                    "<a  style=\"color:green\">[%s]Success:删除数据表成功！</a>" % (
                        time.strftime('%H:%M:%S', time.localtime(time.time()))))
            except Exception as e:
                self.Ui.textEdit_log.append(
                    "<a  style=\"color:red\">[%s]Error:数据表vuln_poc删除失败！<br>[Exception]:<br>%s</a>" % (
                        (time.strftime('%H:%M:%S', time.localtime(time.time()))), e))
                return 0
        else:
            self.Ui.textEdit_log.append(
                "<a  style=\"color:black\">[%s]Info:数据库文件不存在，尝试创建数据库！</a>" % (
                    time.strftime('%H:%M:%S', time.localtime(time.time()))))
        try:

            # 执行一条语句,创建 user表 如不存在创建
            sql = 'CREATE TABLE `vuln_poc`  (`id` int(255) NULL DEFAULT NULL,`cms_name` varchar(255),`vuln_file` varchar(255),`vuln_name` varchar(255),`vuln_author` varchar(255),`vuln_referer` varchar(255),`vuln_description` varchar(255),`vuln_identifier` varchar(255),`vuln_solution` varchar(255),`ispoc` int(255) NULL DEFAULT NULL,`isexp` int(255) NULL DEFAULT NULL,`vuln_class` varchar(255),`FofaQuery_type` varchar(255),`FofaQuery_link` varchar(255),`FofaQuery_rule` varchar(255))'
            # sql = 'create table IF NOT EXISTS vuln_poc ("id" integer PRIMARY KEY AUTOINCREMENT,"cms_name" varchar(30),"vuln_file" varchar(50),"vuln_name" varchar(30),"vuln_author" varchar(50),"vuln_referer" varchar(50),"vuln_description" varchar(200),"vuln_identifier" varchar(100),"vuln_solution" varchar(500),  "ispoc" integer(1),"isexp" integer(1))'
            cursor.execute(sql)
            self.Ui.textEdit_log.append(
                "<a  style=\"color:green\">[%s]Success:创建数据表完成！</a>" % (
                    time.strftime('%H:%M:%S', time.localtime(time.time()))))
        except Exception as e:
            self.Ui.textEdit_log.append(
                "<a  style=\"color:red\">[%s]Error:数据表创建失败！<br>[Exception]:<br>%s</a>" % (
                    time.strftime('%H:%M:%S', time.localtime(time.time())), e))
            return 0
        try:
            id = 1
            all_plugins = self.get_dir_file(vuln_plugins_dir)
            # print(all_plugins)
            go_load_plugins = []  # 存放已经加载的模块

            for poc in all_plugins:
                try:
                    if os.path.splitext(poc['poc_file_name'])[-1] in plugins_ext:
                        if os.path.splitext(poc['poc_file_name'])[-1] == '.py':
                            nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(
                                os.path.splitext(poc['poc_file_name'])[0],
                                poc['poc_file_path']).load_module()
                        elif os.path.splitext(poc['poc_file_name'])[-1] in ['.pyc', '.pyd', '.so']:
                            if os.path.splitext(poc['poc_file_name'])[0] in go_load_plugins:
                                continue
                            module_spec = importlib.util.spec_from_file_location(
                                os.path.splitext(poc['poc_file_name'])[0], poc['poc_file_path'])
                            nnnnnnnnnnnn1 = importlib.util.module_from_spec(module_spec)
                            module_spec.loader.exec_module(nnnnnnnnnnnn1)
                        vuln_info = nnnnnnnnnnnn1.vuln_info()
                        if vuln_info.get('vuln_class'):
                            vuln_class = vuln_info.get('vuln_class')
                        else:
                            vuln_class = '未分类'
                        if vuln_info.get('FofaQuery_type'):
                            FofaQuery_type = vuln_info.get('FofaQuery_type')
                        else:
                            FofaQuery_type = 'http'
                        if vuln_info.get('FofaQuery_link'):
                            FofaQuery_link = (vuln_info.get('FofaQuery_link'))
                        else:
                            FofaQuery_link = '/'

                        if vuln_info.get('FofaQuery_rule'):
                            FofaQuery_rule = vuln_info.get('FofaQuery_rule')
                        else:
                            FofaQuery_rule = ''
                        insert_sql = 'insert into vuln_poc  (id,cms_name,vuln_file,vuln_name,vuln_author,vuln_referer,vuln_description,vuln_identifier,vuln_solution,ispoc,isexp,vuln_class,FofaQuery_type,FofaQuery_link,FofaQuery_rule) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

                        # 将数据插入到表中
                        cursor.execute(insert_sql, (
                            id, poc['cms_name'], os.path.splitext(poc['poc_file_name'])[0], vuln_info['vuln_name'],
                            vuln_info['vuln_author'],
                            vuln_info['vuln_referer'], vuln_info['vuln_description'],
                            vuln_info['vuln_identifier'], vuln_info['vuln_solution'], vuln_info['ispoc'],
                            vuln_info['isexp'], vuln_class, FofaQuery_type, FofaQuery_link, FofaQuery_rule))
                        id = id + 1
                        go_load_plugins.append(os.path.splitext(poc['poc_file_name'])[0])
                except Exception as  e:
                    print(str(e))
                    self.Ui.textEdit_log.append(
                        "<a  style=\"color:red\">[%s]Error:%s脚本执行错误！<br>[Exception]:<br>%s</a>" % (
                            (time.strftime('%H:%M:%S', time.localtime(time.time()))), poc['poc_file_name'], e))
                    continue
                conn.commit()  # 提交
            # print(result)
            cursor.execute("select count(ispoc) from vuln_poc where ispoc =1")
            poc_num = cursor.fetchall()
            cursor.execute("select count(isexp) from vuln_poc where isexp =1")
            exp_num = cursor.fetchall()
            conn.close()
            self.Ui.textEdit_log.append(
                "<a  style=\"color:green\">[%s]Success:共写入%s个POC</a>" % (
                    (time.strftime('%H:%M:%S', time.localtime(time.time()))), poc_num[0][0]))
            self.Ui.textEdit_log.append(
                "<a  style=\"color:green\">[%s]Success:共写入%s个EXP</a>" % (
                    (time.strftime('%H:%M:%S', time.localtime(time.time()))), exp_num[0][0]))

            self.load_vuln_plugins()  # 调用加载插件
            self.load_exp_plugins()
            box = QtWidgets.QMessageBox()
            box.information(self, "漏洞插件", "数据更新完成！\nPOC数量：%s\nEXP数量：%s" % (poc_num[0][0], exp_num[0][0]))
            # reboot = sys.executable
            # os.execl(reboot, reboot, *sys.argv)

        except Exception as e:
            self.Ui.textEdit_log.append(
                "<a  style=\"color:red\">[%s]Error:数据写入失败！\n[Exception]:\n%s</a>" % (
                    (time.strftime('%H:%M:%S', time.localtime(time.time()))), e))
            return 0

    def vuln_exp(self):
        if self.Ui.tableWidget_vuln.selectedItems():
            url = self.Ui.tableWidget_vuln.selectedItems()[0].text()
            poc_value = self.Ui.tableWidget_vuln.selectedItems()[1].text().split('|')
            sql = "select * from vuln_poc where cms_name='%s' and vuln_name='%s'  and isexp='1'" % (
                poc_value[0], poc_value[1])
            exp_data = self.sql_search(sql, 'dict')
            # print(exp_data)
            if len(exp_data):
                # 根据文本查找索引设置选中
                cms_index = self.Ui.vuln_type.findText(exp_data[0]['cms_name'], QtCore.Qt.MatchFixedString)
                if cms_index >= 0:
                    # print(2)
                    self.Ui.vuln_type.setCurrentIndex(cms_index)
                    self.change_exp_list(exp_data[0]['cms_name'])
                    exp_index = self.Ui.vuln_name.findText(exp_data[0]['vuln_name'], QtCore.Qt.MatchFixedString)
                    if cms_index >= 0:
                        self.Ui.vuln_name.setCurrentIndex(exp_index)
                        self.change_exp_name_change()
                    else:
                        box = QtWidgets.QMessageBox()
                        box.warning(self, "提示", "该漏洞暂时没有利用工具！")
                else:
                    box = QtWidgets.QMessageBox()
                    box.warning(self, "提示", "该漏洞暂时没有利用工具！")

                self.Ui.tabWidget.setCurrentIndex(1)
                self.Ui.vuln_lineEdit_url.setText(url)

            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "该漏洞暂时没有利用工具！")
        else:
            self.Ui.textEdit_log.append(
                "<a  style=\"color:red\">[%s]Error:请选择一个结果！</a>" % (
                    time.strftime('%H:%M:%S', time.localtime(time.time()))))

    def exp_send(self, exp_type):
        data = {}
        ip = ''
        port = 8080
        cmd = ''
        url = self.Ui.vuln_lineEdit_url.text()
        if not url:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "目标地址不能为空！")
            return
        if "http://" not in url and "https://" not in url:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "请以http://或https://开头！")
            return
        cms_name = self.Ui.vuln_type.currentText()
        exp_name = self.Ui.vuln_name.currentText()
        exp_file_name = self.sql_search(
            "select vuln_file from vuln_poc where vuln_name='%s' and cms_name='%s' and isexp ='1'" % (
                exp_name, cms_name))
        # print(exp_file_name)
        exp_path = vuln_plugins_dir + '/' + cms_name + '/' + exp_file_name[0][0]
        cookie = self.Ui.vuln_lineEdit_cookie.text()
        heads = self.Ui.plainTextEdit_heads.toPlainText()
        heads_dict = {}
        if cookie:
            heads_dict['Cookie'] = cookie
        heads = heads.splitlines()
        for head in heads:
            head = head.split(':')
            heads_dict[head[0].strip()] = head[1].strip()

        if exp_type == 'cmd':
            command = self.Ui.vuln_exp_input_cmd.text()
            self.Ui.vuln_exp_textEdit_log.append(
                "[%s]命令执行:%s" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), command))
            self.Ui.textEdit_result.append(
                "[%s]命令执行:%s" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), command))
            data['type'] = 'cmd'
            data['command'] = command

        elif exp_type == 'shell':
            data['type'] = 'shell'
            ip = self.Ui.vuln_exp_input_ip.text()
            port = self.Ui.vuln_exp_input_port.text()
            data['reverse_ip'] = ip
            data['reverse_port'] = port
            if not re.match(
                    r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                    ip):
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "请输入合法的IP地址！")
                return
            try:
                if port == '' or int(port) not in range(1, 65535):
                    box = QtWidgets.QMessageBox()
                    box.warning(self, "提示", "请输入合法的端口！")
                    return
            except Exception as e:
                self.__Logger.error(str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "请输入合法的端口！")
                return
            self.Ui.vuln_exp_textEdit_log.append(
                "[%s]反弹Shell:%s:%s" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), ip, port))
        elif exp_type == 'uploadfile':
            filename = self.Ui.vuln_exp_lineEdit_filename.text()
            shell_neirong = self.Ui.vuln_exp_textEdit_shell.toPlainText()
            data['type'] = 'uploadfile'
            data['filename'] = filename
            data['filename_contents'] = shell_neirong
        self.exp_flag_type = data['type']
        self.exp_send_obj = Vuln_Exp(exp_path, url, heads_dict, data)  # 创建一个线程
        self.exp_send_obj._data.connect(self.update_data_exp)  # 线程发过来的信号挂接到槽函数update_sum
        self.Ui.vuln_exp_button_shell.setEnabled(False)
        self.Ui.vuln_exp_button_cmd.setEnabled(False)
        self.exp_send_obj.start()  # 线程启动

    def update_data_exp(self, result):
        if result.get('Info'):
            self.Ui.vuln_exp_textEdit_log.append(
                "<a  style=\"color:blue\">[%s]Info:<br>%s</a>" % (
                    time.strftime('%H:%M:%S'), result.get("Info_Info")))
        if result.get('Result'):
            if self.exp_flag_type == 'cmd':
                # self.Ui.textEdit_result.append(result.get("Result_Info"))
                self.Ui.textEdit_result.append(
                    "[%s]执行结果:\n%s" % (time.strftime('%H:%M:%S'), result.get("Result_Info")))
            else:
                self.Ui.vuln_exp_textEdit_log.append(
                    "[%s]执行结果:%s" % (time.strftime('%H:%M:%S'), result.get("Result_Info")))
        # 不存在
        else:
            self.Ui.vuln_exp_textEdit_log.append(
                "<a  style=\"color:black\">[%s]%s:%s。</a>" % (
                    time.strftime('%H:%M:%S'), "Result", "执行失败,失败原因:" + str(result.get("Result_Info"))))
        if result.get('Error_Info'):
            self.Ui.vuln_exp_textEdit_log.append(
                "<a  style=\"color:red\">[%s]Error:<br>Error-Info:%s。</a>" % (
                    time.strftime('%H:%M:%S'), result.get("Error_Info")))
        if result.get('Debug_Info') and self.Ui.vuln_exp_debug.isChecked():
            self.Ui.vuln_exp_textEdit_log.append(
                "<a  style=\"color:blue\">[%s]Debug:<br>Debug-Info:%s。</a>" % (
                    time.strftime('%H:%M:%S'), result.get("Debug_Info")))

        self.Ui.vuln_exp_button_shell.setEnabled(True)  # 让按钮恢复可点击状态
        self.Ui.vuln_exp_button_cmd.setEnabled(True)  # 让按钮恢复可点击状态

    # 关于
    def about(self):
        box = QtWidgets.QMessageBox()
        # box.setIcon()
        box.about(self, "About",
                  "\t\t\tAbout\n       此程序为一款专为渗透测试人员开发的测试工具，请勿非法使用！\n\t\t\tPowered by qianxiao996")

    # 更新
    def version_update(self):
        try:
            response = requests.get("https://qianxiao996.cn/FrameScan-GUI/version.txt", timeout=3, verify=False)
            if (int(response.text.replace('.', '')) > int(version.replace('.', ''))):
                reply = QMessageBox.question(window, '软件更新',
                                             "当前版本：%s\n最新版本：%s\n检测到软件已发布新版本，是否前去下载?" % (version, response.text),
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    webbrowser.open('https://github.com/qianxiao996/Emperor/releases')
                else:
                    pass
            else:
                box = QtWidgets.QMessageBox()
                box.information(self, "软件更新", "当前版本：%s\n最新版本：%s\n已是最新版本" % (version, response.text))
        except:
            box = QtWidgets.QMessageBox()
            box.warning(self, "软件更新", "获取更新失败！")

    # 意见反馈
    def ideas(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about(self, "意见反馈", "作者邮箱：qianxiao996@126.com\n作者主页：http://qianxiao996.cn")

    # 全选
    def vuln_all(self):
        item = QtWidgets.QTreeWidgetItemIterator(self.Ui.treeWidget_Plugins)
        # 该类的value()即为QTreeWidgetItem
        while item.value():
            if item.value().checkState(0) != QtCore.Qt.Checked:
                item.value().setCheckState(0, QtCore.Qt.Checked)
            item = item.__iadd__(1)

    # 反选
    def vuln_noall(self):
        item = QtWidgets.QTreeWidgetItemIterator(self.Ui.treeWidget_Plugins)
        # 该类的value()即为QTreeWidgetItem
        while item.value():
            if item.value().checkState(0) == QtCore.Qt.Checked:
                item.value().setCheckState(0, QtCore.Qt.Unchecked)
            item = item.__iadd__(1)

    # 文件打开对话框
    def file_open(self, type):
        fileName, selectedFilter = QFileDialog.getOpenFileName(self, (r"上传文件"), '', type)
        return (fileName)  # 返回文件路径

    # 保存文件对话框
    def file_save(self, filename):
        fileName, filetype = QFileDialog.getSaveFileName(self, (r"保存文件"), (filename), r"All files(*.*)")
        return fileName

    def sql_search(self, sql, type='list'):
        if type == 'dict':
            conn = sqlite3.connect(DB_NAME)
            conn.row_factory = self.dict_factory
        else:
            conn = sqlite3.connect(DB_NAME)
        # 创建一个游标 curson
        cursor = conn.cursor()
        # self.Ui.textEdit_log.append("[%s]Info:正在查询数据..."%(time.strftime('%H:%M:%S', time.localtime(time.time()))))
        # 列出所有数据
        cursor.execute(sql)
        if type in ["delete", "update", "insert"]:
            conn.commit()
            return True
        values = cursor.fetchall()
        return values

    # sql查询返回字典
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def change_exp_list(self, exp_cms_name):
        self.Ui.vuln_name.clear()
        for exp_methods in self.exp_cms_name_dict[exp_cms_name]:
            # print(exp_methods)
            self.Ui.vuln_name.addItem(exp_methods['vuln_name'])

        self.change_exp_name_change()
        # print(exp_cms_name)

    # vuln_name 改变调用函数
    def change_exp_name_change(self):
        self.Ui.exp_tabWidget.setCurrentIndex(0)
        vuln_type_text = self.Ui.vuln_type.currentText()
        vuln_name_text = self.Ui.vuln_name.currentText()
        sql = "select * from vuln_poc where vuln_name='%s' and cms_name='%s'" % (vuln_name_text, vuln_type_text)
        vuln_data = self.sql_search(sql, 'dict')[0]
        # print(expdescription[0][0])
        # pass
        if vuln_data:
            if vuln_data.get('isexp'):
                vuln_exp = 'True'
            else:
                vuln_exp = 'False'
            if vuln_data.get('ispoc'):
                vuln_poc = 'True'
            else:
                vuln_poc = 'False'

            data = "漏洞名称：" + str(vuln_data.get('vuln_name')) + "\n漏洞编号：" + str(
                vuln_data.get('vuln_identifier')) + "\n漏洞分类：" + str(vuln_data.get('vuln_class')) + "\n资产分类：" + str(
                vuln_data.get('cms_name')) + "\n漏洞来源：" + str(vuln_data.get('vuln_referer')) + "\n插件作者：" + str(
                vuln_data.get('vuln_author')) + "\n插件位置：" + vuln_plugins_dir + "/" + str(
                vuln_data.get('cms_name')) + "/" + str(
                vuln_data.get('vuln_file')) + "\n是否有POC：" + vuln_poc + "\n是否有EXP：" + vuln_exp + "\n漏洞描述：" + str(
                vuln_data.get('vuln_description')) + "\n修复建议：" + str(vuln_data.get('vuln_solution'))
            self.Ui.vuln_exp_textEdit_info.setText(data)
        else:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "该EXP暂无描述信息！")

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            config_setup.write(open(config_file_dir, "r+", encoding="utf-8"))  # r+模式
            event.accept()
        else:
            event.ignore()

    def check_update(self):
        try:
            response = requests.get("https://qianxiao996.cn/Emperor/version.txt", timeout=3)
            if (int(response.text.replace('.', '')) > int(version.replace('.', ''))):
                reply = QtWidgets.QMessageBox.question(self,
                                                       '软件更新',
                                                       "检测到软件已发布新版本，是否前去下载?",
                                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                       QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    webbrowser.open('https://github.com/qianxiao996/Emperor/releases')
                else:
                    pass
        except Exception as e:
            pass

    # 得到选中的方法
    def get_methods_passwd_brute(self):
        all_data = []
        item = QtWidgets.QTreeWidgetItemIterator(self.Ui.treeWidget_passwd_brute_service)
        # 该类的value()即为QTreeWidgetItem
        while item.value():
            if not item.value().parent():  # 判断有没有父节点
                pass
            else:  # 输出所有子节点
                if item.value().checkState(0) == QtCore.Qt.Checked:
                    # print(item.value().text(0))
                    all_data.append(item.value().text(0))
            item = item.__iadd__(1)
        # print(all_data)
        # 返回所有选中的数据
        return all_data

    # 统一异常处理
    def HandleException(self, excType, excValue, tb):
        currentTime = datetime.datetime.now()  # 时间戳
        self.__Logger.info('Timestamp: %s' % (currentTime.strftime("%Y-%m-%d %H:%M:%S")))
        ErrorMessage = ''.join(traceback.format_exception(excType, excValue, tb))
        self.__Logger.error('ErrorMessage: %s' % ErrorMessage)  # 将异常信息记录到日志中
        self.__Logger.error('sys.excepthook: %s' % sys.excepthook)
        self.__Logger.error('excType: %s' % excType)
        self.__Logger.error('excValue: %s' % str(excValue))
        self.__Logger.error('tb: %s' % tb)
        self.Ui.textBrowser_log_log.append('ErrorMessage: %s' % ErrorMessage)
        self.Ui.textBrowser_log_log.append('sys.excepthook: %s' % sys.excepthook)
        self.Ui.textBrowser_log_log.append('excType: %s' % excType)
        self.Ui.textBrowser_log_log.append('tb: %s' % tb)
        # box = QtWidgets.QMessageBox()
        # box.warning(self, "错误", ErrorMessage)
        self.Ui.statusBar.showMessage("Error:程序发生错误，请查看程序日志页面！", 5000)
        # box.close()

    def get_dir_file(self, dir):
        all_plugins = []
        plugins_path = dir
        plugins_path = plugins_path.replace("\\", "/")
        for cms_name in os.listdir(plugins_path):  # 遍历目录名
            cms_path = os.path.join(plugins_path, cms_name).replace("\\", "/")
            for poc_file_dir, poc_dirs_list, poc_file_name_list in os.walk(cms_path):  # 遍历poc文件，得到方法名称
                # print(path,dirs,poc_methos_list)
                # print(poc_file_name_list)
                for poc_file_name in poc_file_name_list:
                    if '__pycache__' in poc_file_dir:
                        continue
                    # print(poc_file_name)
                    poc_name_path = poc_file_dir + "\\" + poc_file_name
                    poc_name_path = poc_name_path.replace("\\", "/")
                    # 判断是py文件在打开  文件存在
                    # print(poc_file_name[:8])
                    if os.path.isfile(poc_name_path) and (
                            os.path.splitext(poc_name_path)[1] in ['.pyd', '.pyc', '.so', '.py']) and len(
                        poc_file_name) >= 8 and poc_file_name[:8] == "Plugins_":
                        single_plugins = {}
                        single_plugins['cms_name'] = cms_name
                        single_plugins['poc_file_name'] = poc_file_name
                        single_plugins['poc_file_path'] = poc_name_path
                        all_plugins.append(single_plugins)
        return all_plugins


# 重新向输出
class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        text = text.strip()
        # print(text)
        if text:
            self.textWritten.emit(str(text))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # 创建启动界面，支持png透明图片
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap('./Conf/main.ico'))
    splash.show()
    splash.showMessage('正在加载……')
    app.processEvents()  # 防止进程卡死
    # 可以显示启动信息
    # # 关闭启动画面
    # splash.close()
    window = MainWindows()
    translator = QTranslator()
    translator.load('./conf/qm/qt_zh_CN.qm')  # 改变中文菜单
    app.installTranslator(translator)
    translator_2 = QTranslator()
    translator_2.load('./conf/qm/widgets_zh_cn.qm')  # 改变QTextEdit右键为中文
    app.installTranslator(translator_2)
    window.show()
    out_log_ui_obj = window.Ui.textBrowser_log_log
    window.load_proxy()
    splash.finish(window)  # 关闭启动界面
    splash.close()
    sys.exit(app.exec_())
