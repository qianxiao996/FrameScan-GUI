#!/usr/bin/python
# -*- coding: UTF-8 -*-
import configparser,importlib

# import logging
import sys, os, webbrowser
sys.path.append('./modules')
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import csv, re, requests, time, sqlite3
from GUI.main import Ui_MainWindow
from GUI.showPlugins import Ui_Form
from GUI.Plugins_information import Ui_Plugins_information
import win32con
import win32clipboard as wincld
import frozen_dir
from modules.vuln_scanner import Vuln_scanner
from modules.vuln_exp import Vuln_exp
SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)
DB_NAME = 'VULN_DB.db'
version = '1.3.3'
plugins_dir_name = 'Plugins/'
update_time = '20210524'
# 禁用安全警告
# time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime(time.time()))
requests.packages.urllib3.disable_warnings()
# logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
#                     filename='log/FrameScan.log',
#                     filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
#                     #a是追加模式，默认如果不写的话，就是追加模式
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S %p'
#                     #日志格式
#                     )
class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):  # 主窗口
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) #去掉标题栏
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('main.ico'))
        # self.setFixedSize(self.width(), self.height())  # 设置宽高不可变
        # self.Ui.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)  #退出
        self.poc_cms_name_dict={}
        self.exp_cms_name_dict={}

        # 漏洞扫描
        self.Ui.pushButton_vuln_file.clicked.connect(self.vuln_import_file)  # 导入地址
        self.Ui.pushButton_vuln_start.clicked.connect(self.vuln_Start)  # 开始扫描
        self.Ui.pushButton_vuln_expstart.clicked.connect(self.vuln_exp)  # 一键利用
        self.Ui.pushButton_vuln_all.clicked.connect(self.vuln_all)  # 全选
        self.Ui.pushButton_vuln_noall.clicked.connect(self.vuln_noall)  # 反选


        #插件管理
        self.Ui.action_vuln_reload.triggered.connect(self.vuln_reload_Plugins)  # 重新加载插件
        self.Ui.action_vuln_showplubins.triggered.connect(self.vuln_ShowPlugins)  # 查看插件


        #选项
        self.Ui.action_about_start.triggered.connect(self.about)  # 关于
        self.Ui.action_update_start.triggered.connect(self.version_update)  # 更新
        self.Ui.action_ideas_start.triggered.connect(self.ideas)  # 意见反馈

        #漏洞利用
        self.Ui.vuln_exp_button_cmd.clicked.connect(lambda: self.exp_send('cmd'))
        self.Ui.vuln_exp_button_shell.clicked.connect(lambda: self.exp_send('shell'))
        self.Ui.vuln_type.activated[str].connect(self.change_exp_list)
        self.Ui.vuln_name.activated[str].connect(self.change_exp_name_change)

        # 漏洞扫描右键菜单
        self.Ui.tableWidget_vuln.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Ui.tableWidget_vuln.customContextMenuRequested['QPoint'].connect(self.createtableWidget_vulnMenu)

        #初始化加载插件
        self.loadplugins()
        self.url_list = []
        self.load_config()
        # 设置漏洞扫描表格属性  列宽度
        self.Ui.tableWidget_vuln.setColumnWidth(0, 250)
        self.Ui.tableWidget_vuln.setColumnWidth(1, 200)
        self.Ui.tableWidget_vuln.setColumnWidth(2, 300)
        self.Ui.tableWidget_vuln.setColumnWidth(3, 80)
        #选项
        othersmenubar = self.menuBar()  # 获取窗体的菜单栏
        others = othersmenubar.addMenu("选项")
        for i in ["关于",'更新','意见反馈']:
            sub_action = QAction(QIcon(''), i, self)
            others.addAction(sub_action)
        impMenu = QMenu("皮肤风格", self)
        # print(type(config_setup))
        for z in config_setup.options('QSS_List'):
            sub_action = QAction(QIcon(''), z, self)
            impMenu.addAction(sub_action)

        others.addMenu(impMenu)
        others.triggered[QAction].connect(self.show_others)
    def load_config(self):
        try:
            global config_setup
            global qss_style
            # 实例化configParser对象
            config_setup = configparser.ConfigParser()
            # -read读取ini文件
            config_setup.read('config.ini', encoding='utf-8')
            if 'QSS_Setup' not in config_setup:  # 如果分组type不存在则插入type分组
                config_setup.add_section('QSS_Setup')
                config_setup.set("QSS_Setup", "QSS", 'default.qss')
                config_setup.write(open('config.ini', "r+", encoding="utf-8"))  # r+模式
                qss_Setup= 'default.qss'
            else:
                qss_Setup= config_setup.get('QSS_Setup', 'QSS')
            with open("QSS/"+qss_Setup, 'r', encoding='utf-8') as f:
                qss_style = f.read()
                f.close()
                
            MainWindows.setStyleSheet(self,qss_style)
            f.close()
        except Exception as e :
            QMessageBox.critical(self,'Error',str(e))
            pass
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
        self.daochu = self.contextMenu.addAction(u'导出')
        self.second = self.contextMenu.addMenu(u'复制')
        self.copy_url = self.second.addAction(u'URL')
        self.copy_vuln_name = self.second.addAction(u'漏洞名称')
        self.copy_path = self.second.addAction(u'脚本路径')
        self.copy_payload = self.second.addAction(u'Payload')
        self.copy_all = self.second.addAction(u'全部')
        self.delete_textEdit= self.contextMenu.addAction(u'删除')
        self.clear_textEdit = self.contextMenu.addAction(u'清空')

        # 将动作与处理函数相关联
        # 这里为了简单，将所有action与同一个处理函数相关联，
        # 当然也可以将他们分别与不同函数关联，实现不同的功能
        self.daochu.triggered.connect(self.vuln_export_file)
        self.copy_url.triggered.connect(lambda:self.Copy_tableWidget_vuln('url'))
        self.copy_vuln_name.triggered.connect(lambda:self.Copy_tableWidget_vuln('vuln_name'))
        self.copy_path.triggered.connect(lambda:self.Copy_tableWidget_vuln('vuln_path'))
        self.copy_payload.triggered.connect(lambda:self.Copy_tableWidget_vuln('payload'))
        self.copy_all.triggered.connect(lambda:self.Copy_tableWidget_vuln('all'))
        self.clear_textEdit.triggered.connect(self.Clear_tableWidget_vuln)
        self.delete_textEdit.triggered.connect(self.Delete_tableWidget_vuln)
    # 右键点击时调用的函数，移动鼠标位置
    def showContextMenu(self, pos):
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu.move(QtGui.QCursor.pos())
        self.contextMenu.show()
    def Copy_tableWidget_vuln(self,type):
        try:
            data=''
            if type == 'url':
                data = self.Ui.tableWidget_vuln.selectedItems()[0].text()
            if type == 'vuln_name':
                data = self.Ui.tableWidget_vuln.selectedItems()[1].text()
            if type == 'vuln_path':
                data = self.Ui.tableWidget_vuln.selectedItems()[2].text()
            if type == 'payload':
                data = self.Ui.tableWidget_vuln.selectedItems()[4].text()
            if type == 'all':
                # data = self.Ui.tableWidget_vuln.selectedItems()
                for i in self.Ui.tableWidget_vuln.selectedItems():
                    data += str(i.text())+'  '
            # 访问剪切板，存入值
            wincld.OpenClipboard()
            wincld.EmptyClipboard()
            wincld.SetClipboardData(win32con.CF_UNICODETEXT, data)
            wincld.CloseClipboard()
        except:
            pass
    def Clear_tableWidget_vuln(self):
        for i in range(0, self.Ui.tableWidget_vuln.rowCount()):  # 循环行
            self.Ui.tableWidget_vuln.removeRow(0)
    def Delete_tableWidget_vuln(self):
        self.Ui.tableWidget_vuln.removeRow(self.Ui.tableWidget_vuln.currentRow())#删除选中的行
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
                            if poc['vuln_name'] ==item.value().text(0):
                                poc['vuln_file'] = poc['vuln_file']
                                poc['FofaQuery_link'] = poc['FofaQuery_link']
                                poc['FofaQuery'] = poc['FofaQuery']
                                all_data.append(poc)
            item = item.__iadd__(1)
        # print(all_data)
        #返回所有选中的数据
        return all_data
    # 开始扫描
    def vuln_Start(self):

        obj = Vuln_scanner(self,plugins_dir_name)
        obj.start()

    # 调用脚本
    
    # 初始化加载插件
    def loadplugins(self):
        if not os.path.isfile(DB_NAME):
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "数据文件不存在，正在重新加载数据库！")
            self.vuln_reload_Plugins()
            return 0
        #加载漏洞扫描模块
        try:
            # 列出所有数据
            sql_poc = "SELECT cms_name,vuln_name,vuln_file,FofaQuery_link,FofaQuery from vuln_poc where ispoc !=''"
            poc_dict = self.sql_search(sql_poc,'dict')
            if len(poc_dict)>=1:
                # print(self.poc_dict)
                sql_exp = "SELECT cms_name,vuln_name,vuln_file,vuln_description,FofaQuery_link,FofaQuery from vuln_poc where isexp !=''"
                exp_dict = self.sql_search(sql_exp,'dict')
            else:
                return
            # print(values)
        except Exception as e:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "数据文件错误：\n%s" % e)
            return 0
        # 将查询的值组合为字典包含列表的形式
        self.poc_cms_name_dict = {}
        for cms in poc_dict :
            self.poc_cms_name_dict[cms['cms_name']] = []
        # print(cms_name)
        for cms in poc_dict :
            poc_cms_sing= {}
            poc_cms_sing['cms_name'] = cms['cms_name']
            poc_cms_sing['vuln_name'] = cms['vuln_name']
            poc_cms_sing['vuln_file'] = cms['vuln_file']
            poc_cms_sing['FofaQuery_link'] = cms['FofaQuery_link']
            poc_cms_sing['FofaQuery'] = cms['FofaQuery']
            self.poc_cms_name_dict[cms['cms_name']].append(poc_cms_sing)
        for cms in self.poc_cms_name_dict:
            # 设置root为self.treeWidget_Plugins的子树，故root是根节点
            root = QTreeWidgetItem(self.Ui.treeWidget_Plugins)
            root.setText(0, cms)  # 设置根节点的名称
            root.setCheckState(0, Qt.Unchecked)  # 开启复选框
            # print(cms_name[cms])
            for cms_single in self.poc_cms_name_dict[cms]:
                # 为root节点设置子结点
                child1 = QTreeWidgetItem(root)
                child1.setText(0, cms_single['vuln_name'])
                child1.setCheckState(0, Qt.Unchecked)
        self.Ui.treeWidget_Plugins.itemChanged.connect(self.handleChanged)
        self.Ui.treeWidget_Plugins.doubleClicked.connect(self.Show_Plugins_info)
        self.Ui.textEdit_log.append(
            "<p style=\"color:green\">[%s]Success:插件加载完成，共%s个。</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time())), len(poc_dict)))
        # 将查询的值组合为字典包含列表的形式
        self.exp_cms_name_dict = {}
        for cms in exp_dict :
            self.exp_cms_name_dict[cms['cms_name']] = []
        # print(exp_cms_name_dict)
        for exp_cms in exp_dict :
            # print(cms['cmsname'] )
            # if cms['cmsname'] in cms_name.keys():
            exp_cms_sing= {}
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
        for exp_methods in list(self.exp_cms_name_dict.values())[0] :
            # print(exp_methods)
            self.Ui.vuln_name.addItem(exp_methods['vuln_name'])
            self.Ui.vuln_exp_textEdit_info.setText(exp_methods['vuln_description'])

    def Show_Plugins_info(self):
        poc_name = self.Ui.treeWidget_Plugins.currentItem().text(0)
        # 列出所有数据
        sql = "SELECT *  from vuln_poc where vuln_name='%s'"%poc_name
        values = self.sql_search(sql,'dict')
        # print(values)
        try:
            self.dialog.close()
        except:
            pass
        if len(values) !=0:
            self.WChild_info = Ui_Plugins_information()
            self.dialog = QtWidgets.QDialog(self)
            self.WChild_info.setupUi(self.dialog)
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

            self.WChild_info.vuln_file.setText("Plugins/" + values[0]['cms_name'] + '/' + values[0]['vuln_file'])
            self.WChild_info.vuln_url.setText('<a href="'+values[0]['vuln_referer']+'">'+values[0]['vuln_referer']+'</a>')
            self.WChild_info.vuln_miaoshu.setText(values[0]['vuln_description'])
            self.WChild_info.vuln_solution.setText(values[0]['vuln_solution'])
            self.WChild_info.vuln_identifier.setText(values[0]['vuln_identifier'])
            return 0
        else:
            return
    # 父节点关联子节点
    def handleChanged(self, item, column):
        count = item.childCount()
        # print dir(item)
        if item.checkState(column) == Qt.Checked:
            # print "checked", item, item.text(column)
            for f in range(count):
                item.child(f).setCheckState(0, Qt.Checked)
        if item.checkState(column) == Qt.Unchecked:
            # print "unchecked", item, item.text(column)
            for f in range(count):
                item.child(f).setCheckState(0, Qt.Unchecked)
        #  self.Ui.treeWidget_Plugins.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置item可以多选
        # self.tree.itemChanged.connect(self.handleChanged)
        # self.Ui.treeWidget_Plugins.addTopLevelItem(root)

    # 导入文件列表
    def vuln_import_file(self):
        self.url_list = []
        filename = self.file_open(r"Text Files (*.txt);;All files(*.*)")
        try:
            if os.path.isfile(filename):
                self.Ui.textEdit_log.append(
                    "<p style=\"color:black\">[%s]Info:正在从文件中读取URL...</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
                f = open(filename, 'r', encoding='utf-8')
                for line in f.readlines():
                    if 'http' in line:
                        line = line.replace('\n', '').strip()
                        self.url_list.append(line)
                self.Ui.textEdit_log.append(
                    "<p style=\"color:black\">[%s]Info:读取完成，共加载%s条。</p>" % (
                    (time.strftime('%H:%M:%S', time.localtime(time.time()))), len(self.url_list)))
            self.Ui.lineEdit_vuln_url.setText(filename)
        except:
            self.Ui.textEdit_log.append(
                "<p style=\"color:red\">[%s]Error:文件打开失败！</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
            pass
    # 导出扫描结果
    def vuln_export_file(self):
        data = []
        comdata = []
        for i in range(0, self.Ui.tableWidget_vuln.rowCount()):  # 循环行
            for j in range(0, self.Ui.tableWidget_vuln.columnCount()):  # 循环列
                if self.Ui.tableWidget_vuln.item(i, j) != None:  # 有数据
                    data.append(self.Ui.tableWidget_vuln.item(i, j).text())  # 空格分隔
            comdata.append(list(data))
            data = []
        if len(comdata) > 0:
            path = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '.csv').replace(' ', '-').replace('-','').replace(
                ':', '')
            # print(path)
            file_name = self.file_save(path)
            if file_name != "":
                with open(file_name, 'w', newline='') as f:
                    writer = csv.writer(f)
                    for row in comdata:
                        writer.writerow(row)
                f.close()
                box = QtWidgets.QMessageBox()
                box.information(self, "Success", "导出成功！\n文件位置："+file_name)
            else:
                # box2= QtWidgets.QMessageBox()
                # box2.warning(self, "Error", "保存失败！文件名错误！" )
                pass
        else:
            self.Ui.textEdit_log.append(
                "[%s]Faile:没有扫描结果！" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
    # 显示插件
    def vuln_ShowPlugins(self):
        self.form2 = QtWidgets.QWidget()
        self.widget = Ui_Form()
        self.widget.setupUi(self.form2)
        self.form2.setStyleSheet(qss_style)
        self.form2.show()
        self.widget.show_Plugins.setColumnWidth(0, 70)
        self.widget.show_Plugins.setColumnWidth(7, 150)
        # self.widget.show_Plugins.setColumnWidth(2, 320)
        # self.widget.show_Plugins.setColumnWidth(3, 360)
        # self.widget.show_Plugins.setColumnWidth(4, 218)
        # self.widget.show_Plugins.setColumnWidth(5, 218)
        sql = "SELECT * from vuln_poc"
        values = self.sql_search(sql,'dict')
        i = 0
        self.widget.show_Plugins.setRowCount(len(values))
        sql2 = "SELECT distinct cms_name from vuln_poc"
        sql_vuln_class = "SELECT distinct vuln_class from vuln_poc where vuln_class!='' and vuln_class not null"
        cms_name_data = self.sql_search(sql2)
        vuln_class_data = self.sql_search(sql_vuln_class)
        # 添加查询列表
        for cms_name in cms_name_data:
            self.widget.show_Plugins_comboBox_cms_name.addItem(cms_name[0])
        for vuln_class in vuln_class_data:
                self.widget.show_Plugins_comboBox_vuln_class.addItem(vuln_class[0])
            # print(cms_name[0])
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
            self.widget.show_Plugins.setItem(i, 0, id)
            self.widget.show_Plugins.setItem(i, 1, cms_name)
            self.widget.show_Plugins.setItem(i, 2, vuln_name)
            self.widget.show_Plugins.setItem(i, 3, vuln_class)
            self.widget.show_Plugins.setItem(i, 4, vuln_identifier)
            self.widget.show_Plugins.setItem(i, 5, vuln_referer)
            self.widget.show_Plugins.setItem(i, 6, vuln_description)
            self.widget.show_Plugins.setItem(i, 7, vuln_file)
            self.widget.show_Plugins.setItem(i, 8, vuln_author)
            self.widget.show_Plugins.setItem(i, 9, vuln_solution)
            i = i + 1
        self.widget.show_Plugins_comboBox_cms_name.currentIndexChanged.connect(self.show_plugins_go)  # comboBox事件选中触发刷新
        self.widget.show_Plugins_comboBox_vuln_class.currentIndexChanged.connect(self.show_plugins_go)  # comboBox事件选中触发刷新
    # 单击列表刷新显示控件
    def show_plugins_go(self):
        self.widget.show_Plugins.clearContents()
        cms_name = self.widget.show_Plugins_comboBox_cms_name.currentText()  # 获取文本
        vuln_class = self.widget.show_Plugins_comboBox_vuln_class.currentText()  # 获取文本
        if cms_name == "ALL" and vuln_class=="ALL":
            sql = "SELECT * from vuln_poc "
        elif  cms_name == "ALL" and vuln_class!="ALL":
            sql = "SELECT * from vuln_poc where vuln_class='%s'" % (vuln_class)
        elif cms_name != "ALL" and vuln_class == "ALL":
            sql = "SELECT * from vuln_poc where cms_name = '%s'" % (cms_name)
        else:
            sql = "SELECT * from vuln_poc where cms_name = '%s' and vuln_class='%s'" % (cms_name,vuln_class)
        cms_data = self.sql_search(sql,'dict')
        i = 0
        self.widget.show_Plugins.setRowCount(len(cms_data))
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
            self.widget.show_Plugins.setItem(i, 0, id)
            self.widget.show_Plugins.setItem(i, 1, cms_name)
            self.widget.show_Plugins.setItem(i, 2, vuln_name)
            self.widget.show_Plugins.setItem(i, 2, vuln_class)
            self.widget.show_Plugins.setItem(i, 3, vuln_identifier)
            self.widget.show_Plugins.setItem(i, 4, vuln_referer)
            self.widget.show_Plugins.setItem(i, 5, vuln_description)
            self.widget.show_Plugins.setItem(i, 6, vuln_file)
            self.widget.show_Plugins.setItem(i, 7, vuln_author)
            self.widget.show_Plugins.setItem(i, 8, vuln_solution)
            i = i + 1
    # 重新加载插件
    def vuln_reload_Plugins(self):
        self.Ui.treeWidget_Plugins.clear()
        self.Ui.textEdit_log.setText("[%s]Start:正在重新加载插件..." % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
        # 删除数据库，重新建立
        if os.path.isfile(DB_NAME):
            try:
                os.remove(DB_NAME)
            except Exception as e:
                self.Ui.textEdit_log.append("<p style=\"color:red\">[%s]Error:数据库文件删除失败！<br>[Exception]:<br>%s</p>" % (
                    (time.strftime('%H:%M:%S', time.localtime(time.time()))), e))
                return 0
            self.Ui.textEdit_log.append(
                "<p style=\"color:green\">[%s]Success:删除数据库完成！</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
        else:
            self.Ui.textEdit_log.append(
                "<p style=\"color:black\">[%s]Info:数据库文件不存在，尝试创建数据库！</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
        try:
            # 连接数据库。如果数据库不存在的话，将会自动创建一个 数据库
            conn = sqlite3.connect(DB_NAME)
            # 创建一个游标 curson
            cursor = conn.cursor()
            # 执行一条语句,创建 user表 如不存在创建
            sql ='CREATE TABLE `vuln_poc`  (`id` int(255) NULL DEFAULT NULL,`cms_name` varchar(255),`vuln_file` varchar(255),`vuln_name` varchar(255),`vuln_author` varchar(255),`vuln_referer` varchar(255),`vuln_description` varchar(255),`vuln_identifier` varchar(255),`vuln_solution` varchar(255),`ispoc` int(255) NULL DEFAULT NULL,`isexp` int(255) NULL DEFAULT NULL,`vuln_class` varchar(255),`FofaQuery_link` varchar(255),`target` varchar(1000),`FofaQuery` varchar(255))'
            # sql = 'create table IF NOT EXISTS vuln_poc ("id" integer PRIMARY KEY AUTOINCREMENT,"cms_name" varchar(30),"vuln_file" varchar(50),"vuln_name" varchar(30),"vuln_author" varchar(50),"vuln_referer" varchar(50),"vuln_description" varchar(200),"vuln_identifier" varchar(100),"vuln_solution" varchar(500),  "ispoc" integer(1),"isexp" integer(1))'
            cursor.execute(sql)
            self.Ui.textEdit_log.append(
                "<p style=\"color:green\">[%s]Success:创建数据库完成！</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
        except Exception as e:
            self.Ui.textEdit_log.append(
                "<p style=\"color:red\">[%s]Error:数据框创建失败！<br>[Exception]:<br>%s</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time())), e))
            return 0
        try:
            id=1
            plugins_path = "Plugins"
            plugins_path = plugins_path.replace("\\", "/")
            for cms_name in os.listdir(plugins_path):  # 遍历目录名
                cms_path = os.path.join(plugins_path, cms_name).replace("\\", "/")
                for poc_file_dir, poc_dirs_list, poc_file_name_list in os.walk(cms_path):  # 遍历poc文件，得到方法名称
                    # print(path,dirs,poc_methos_list)
                    # print(poc_file_name_list)
                    for poc_file_name in poc_file_name_list:
                        poc_name_path = poc_file_dir+ "\\" + poc_file_name
                        poc_name_path = poc_name_path.replace("\\", "/")
                        # 判断是py文件在打开  文件存在
                        # print(poc_file_name[:8])
                        if os.path.isfile(poc_name_path) and poc_file_name.endswith('.py') and len(poc_file_name)>=8 and poc_file_name[:8] =="Plugins_":
                            # print(poc_name_path)
                            try:
                                nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(poc_name_path[:-3], poc_name_path).load_module()
                                vuln_info = nnnnnnnnnnnn1.vuln_info()
                                if vuln_info.get('vuln_class'):
                                    vuln_class =vuln_info.get('vuln_class')
                                else:
                                    vuln_class='未分类'
                                if vuln_info.get('FofaQuery_link'):
                                    FofaQuery_link =(vuln_info.get('FofaQuery_link'))
                                else:
                                    FofaQuery_link=''
                                if vuln_info.get('FofaQuery'):
                                    FofaQuery =vuln_info.get('FofaQuery')
                                else:
                                    FofaQuery=''
                                insert_sql = 'insert into vuln_poc  (id,cms_name,vuln_file,vuln_name,vuln_author,vuln_referer,vuln_description,vuln_identifier,vuln_solution,ispoc,isexp,vuln_class,FofaQuery_link,FofaQuery,target) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

                                # 将数据插入到表中
                                cursor.execute(insert_sql, (
                                        id,cms_name, poc_file_name,vuln_info['vuln_name'],vuln_info['vuln_author'] , vuln_info['vuln_referer'], vuln_info['vuln_description'],
                                        vuln_info['vuln_identifier'],vuln_info['vuln_solution'],vuln_info['ispoc'],vuln_info['isexp'],vuln_class,FofaQuery_link,FofaQuery,'[]'))
                                id=id+1
                            except Exception as  e:
                                self.Ui.textEdit_log.append(
                                    "<p style=\"color:red\">[%s]Error:%s脚本执行错误！<br>[Exception]:<br>%s</p>" % (
                                        (time.strftime('%H:%M:%S', time.localtime(time.time()))), poc_file_name, e))
                                continue
                            conn.commit()  # 提交
            # print(result)
            cursor.execute("select count(ispoc) from vuln_poc where ispoc =1")
            poc_num = cursor.fetchall()
            cursor.execute("select count(isexp) from vuln_poc where isexp =1")
            exp_num = cursor.fetchall()
            conn.close()
            self.Ui.textEdit_log.append(
                "<p style=\"color:green\">[%s]Success:共写入%s个POC</p>" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), poc_num[0][0]))
            self.Ui.textEdit_log.append(
                "<p style=\"color:green\">[%s]Success:共写入%s个EXP</p>" % (
                (time.strftime('%H:%M:%S', time.localtime(time.time()))), exp_num[0][0]))

            self.loadplugins()  # 调用加载插件
            box = QtWidgets.QMessageBox()
            box.information(self, "Load Plugins", "数据更新完成！\nPOC数量：%s\nEXP数量：%s" % (poc_num[0][0],exp_num[0][0]))
            # reboot = sys.executable
            # os.execl(reboot, reboot, *sys.argv)
        except Exception as e:
            self.Ui.textEdit_log.append(
                "<p style=\"color:red\">[%s]Error:数据写入失败！\n[Exception]:\n%s</p>" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), e))
            return 0
    def show_others(self,q):
        if q.text() =="关于":
            self.about()
            return
        if q.text() =="更新":
            self.version_update()
            return
        if q.text() =="意见反馈":
            self.ideas()
            return
        else:
            try:
                global qss_style
                filename = config_setup.get('QSS_List', q.text())
                # print(filename)
                config_setup.set("QSS_Setup", "QSS", filename)
                config_setup.write(open('config.ini', "r+", encoding="utf-8"))  # r+模式
                with open('QSS/'+filename, 'r', encoding='utf-8') as f:
                    qss_style = f.read()
                    f.close()
                MainWindows.setStyleSheet(self, qss_style)
                # python = sys.executable
                # os.execl(python, python, *sys.argv)
            except Exception as e:
                QMessageBox.critical(self, 'Error', str(e))
                pass
    def vuln_exp(self):
        if self.Ui.tableWidget_vuln.selectedItems():
            url  = self.Ui.tableWidget_vuln.selectedItems()[0].text()
            poc_name= self.Ui.tableWidget_vuln.selectedItems()[1].text()
            sql = "select * from vuln_poc where vuln_name='%s'"%(poc_name)
            exp_data = self.sql_search(sql,'dict')
            #print(exp_data)
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
                "<p style=\"color:red\">[%s]Error:请选择一个结果！</p>" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
    def exp_send(self,exp_type):
        ip=''
        port=8080
        cmd=''
        url = self.Ui.vuln_lineEdit_url.text()
        if not url:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "目标地址不能为空！")
            return
        cms_name = self.Ui.vuln_type.currentText()
        exp_name =  self.Ui.vuln_name.currentText()
        exp_file_name = self.sql_search("select vuln_file from vuln_poc where vuln_name='%s' and cms_name='%s'"%(exp_name,cms_name))
        # print(exp_file_name)
        exp_path = plugins_dir_name+'/'+cms_name+'/'+exp_file_name[0][0]
        cookie= self.Ui.vuln_lineEdit_cookie.text()
        heads = self.Ui.plainTextEdit_heads.toPlainText()
        heads_dict  = {}
        if cookie:
            heads_dict['Cookie'] = cookie
        heads = heads.split('\n')
        for head in heads:
            head = head.split(':')
            heads_dict[head[0].strip()] = head[1].strip()
        if exp_type=='cmd':
            cmd = self.Ui.vuln_exp_input_cmd.text()
            self.Ui.vuln_exp_textEdit_log.append(
                "[%s]命令执行:%s" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), cmd))
        elif exp_type=='shell':
            ip = self.Ui.vuln_exp_input_ip.text()
            port = self.Ui.vuln_exp_input_port.text()
            if not re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "请输入合法的IP地址！")
                return
            try:
                if port=='' or int(port) not in range(1, 65535):
                    box = QtWidgets.QMessageBox()
                    box.warning(self, "提示", "请输入合法的端口！")
                    return
            except:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "请输入合法的端口！")
                return
            self.Ui.vuln_exp_textEdit_log.append(
                            "[%s]反弹Shell:%s:%s" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), ip,port))
        # self.cal = Vuln_exp(exp_path,url,heads_dict,cookie,exp_type,cmd,ip,int(port))  # 创建一个线程
        # self.cal._sum.connect(self.vuln_exp_log)  # 线程发过来的信号挂接到槽函数update_sum
        # self.cal.start()  # 线程启动
        self.cal = Vuln_exp(exp_path,url,heads_dict,exp_type,cmd,ip,port)  # 创建一个线程
        self.cal._sum.connect(self.update_sum)  # 线程发过来的信号挂接到槽函数update_sum
        self.Ui.vuln_exp_button_shell.setEnabled(False)  # 让按钮恢复可点击状态
        self.Ui.vuln_exp_button_cmd.setEnabled(False)  # 让按钮恢复可点击状态
        self.cal.start()  # 线程启动

    def update_sum(self, r):
        # print(r)
        if len(r)==2:
            self.vuln_exp_log(r.get('type'), r.get('value'))
        else:
            self.vuln_exp_log(r.get('type'), r.get('value'),r.get('color'))
        self.Ui.vuln_exp_button_shell.setEnabled(True)  # 让按钮恢复可点击状态
        self.Ui.vuln_exp_button_cmd.setEnabled(True)  # 让按钮恢复可点击状态
    # 关于
    def about(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about(self, "About",
                  "\t\t\tAbout\n       此程序为一款CMS扫描利用工具，可自行选择插件进行漏洞检查或利用，请勿非法使用！\n\t\t\t   Powered by qianxiao996")
    # 更新
    def version_update(self):
        webbrowser.open("https://github.com/qianxiao996/FrameScan-GUI/releases")

    # 意见反馈
    def ideas(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about(self, "意见反馈", "作者邮箱：qianxiao996@126.com\n作者主页：http://blog.qianxiao996.cn")

    # 全选
    def vuln_all(self):
        item = QtWidgets.QTreeWidgetItemIterator(self.Ui.treeWidget_Plugins)
        # 该类的value()即为QTreeWidgetItem
        while item.value():
            if item.value().checkState(0) != QtCore.Qt.Checked:
                item.value().setCheckState(0, Qt.Checked)
            item = item.__iadd__(1)
    # 反选
    def vuln_noall(self):
        item = QtWidgets.QTreeWidgetItemIterator(self.Ui.treeWidget_Plugins)
        # 该类的value()即为QTreeWidgetItem
        while item.value():
            if item.value().checkState(0) == QtCore.Qt.Checked:
                item.value().setCheckState(0, Qt.Unchecked)
            item = item.__iadd__(1)
    # 文件打开对话框
    def file_open(self, type):
        fileName, selectedFilter = QFileDialog.getOpenFileName(self, (r"上传文件"),'', type)
        return (fileName)  # 返回文件路径
    # 保存文件对话框
    def file_save(self, filename):
        fileName, filetype = QFileDialog.getSaveFileName(self, (r"保存文件"), (filename),r"All files(*.*)")
        return fileName
    def vuln_scanner_log(self,type,text='',payload='',all=['','','',''],color='black'):
        # print(type,text)
        if type=="Debug" and self.Ui.vuln_scanner_debug.checkState() == Qt.Checked:
            self.Ui.textEdit_log.append(
                "<p style=\"color:blue\">[%s]Debug:%s。</p>" % (time.strftime('%H:%M:%S'), text))
        if type=='Result':
            url = all[0]
            filename = all[1]
            poc_name =  all[3]
            self.Ui.textEdit_log.append(
                "<p style=\"color:green\">[%s]Result:%s----%s----%s。</p>" % (
                    (time.strftime('%H:%M:%S', time.localtime(time.time()))), url, poc_name,text))
            if text != '不存在' and text != '':
                row = self.Ui.tableWidget_vuln.rowCount()  # 获取行数
                self.Ui.tableWidget_vuln.setRowCount(row + 1)
                urlItem = QTableWidgetItem(url)
                nameItem = QTableWidgetItem(poc_name)
                payloadItem = QTableWidgetItem(payload)
                resultItem = QTableWidgetItem(text)
                filenameItem = QTableWidgetItem(filename)
                self.Ui.tableWidget_vuln.setItem(row, 0, urlItem)
                self.Ui.tableWidget_vuln.setItem(row, 1, nameItem)
                self.Ui.tableWidget_vuln.setItem(row, 3, resultItem)
                self.Ui.tableWidget_vuln.setItem(row, 2, filenameItem)
                self.Ui.tableWidget_vuln.setItem(row, 4, payloadItem)
        if type!="Debug" and type!='Result':
            self.Ui.textEdit_log.append(
                "<p style=\"color:%s\">[%s]%s:%s。</p>" % (color,time.strftime('%H:%M:%S'),type, text))

    def vuln_exp_log(self, type,text='',color='black'):
        # print(r)
        if type=='Result':
            self.Ui.textEdit_result.setText(text)
            self.Ui.vuln_exp_textEdit_log.append(
                "[%s]执行结果:%s" % (time.strftime('%H:%M:%S'),text))
        else:
            self.Ui.vuln_exp_textEdit_log.append(
                "<div><p style=\"color:%s\">[%s]%s:%s。</p></div>" % (color, time.strftime('%H:%M:%S'), type, text))
    def sql_search(self,sql,type='list'):
        if type=='dict':
            conn = sqlite3.connect(DB_NAME)
            conn.row_factory = self.dict_factory
        else:
            conn = sqlite3.connect(DB_NAME)
        # 创建一个游标 curson
        cursor = conn.cursor()
        # self.Ui.textEdit_log.append("[%s]Info:正在查询数据..."%(time.strftime('%H:%M:%S', time.localtime(time.time()))))
        # 列出所有数据
        cursor.execute(sql)
        values = cursor.fetchall()
        return  values
    #sql查询返回字典
    def dict_factory(self,cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
    def change_exp_list(self,exp_cms_name):
        self.Ui.vuln_name.clear()
        for exp_methods in self.exp_cms_name_dict[exp_cms_name] :
            # print(exp_methods)
            self.Ui.vuln_name.addItem(exp_methods['vuln_name'])

        self.change_exp_name_change()
        # print(exp_cms_name)
     #vuln_name 改变调用函数
    def change_exp_name_change(self):
        self.Ui.exp_tabWidget.setCurrentIndex(0)
        vuln_name_text = self.Ui.vuln_name.currentText()
        sql =  "select vuln_description from vuln_poc where vuln_name='%s'"%vuln_name_text
        expdescription = self.sql_search(sql)
        # print(expdescription[0][0])
        # pass
        if expdescription:
            self.Ui.vuln_exp_textEdit_info.setText(expdescription[0][0])
        else:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "该EXP暂无描述信息！")
def check_update():
    try:
        response = requests.get("https://qianxiao996.cn/FrameScan-GUI/version.txt",timeout = 3)
        if (int(response.text.replace('.',''))>int(version.replace('.',''))):
            reply = QMessageBox.question(window,'软件更新', "检测到软件已发布新版本，是否前去下载?",QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                webbrowser.open('https://github.com/qianxiao996/FrameScan-GUI/releases')
            else:
                pass
    except:
        pass


            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    window.setWindowTitle('FrameScan-GUI  by qianxiao996 v'+version+' '+update_time)
    window.show()
    try:
        check_update()
    except:
        pass
    sys.exit(app.exec_())
