#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os,webbrowser,threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import csv,re,requests,time,sqlite3
from GUI.FrameScan import Ui_MainWindow
from GUI.showPlugins import Ui_Form
from Plugins.Plugins import *
# from common.readqssfile import Common
DB_NAME = 'POC_DB.db'
# 禁用安全警告
requests.packages.urllib3.disable_warnings()
class MainWindows(QtWidgets.QMainWindow,Ui_MainWindow): #主窗口

    def __init__(self,parent=None):
        super(MainWindows,self).__init__(parent)
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) #去掉标题栏
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./img/main.jpg'))
        self.setFixedSize(self.width(), self.height()) #设置宽高不可变
        #self.Ui.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)  #退出
        self.Ui.action_vuln_import.triggered.connect(self.vuln_import_file)  # 导入文件列表
        self.Ui.pushButton_vuln_file.clicked.connect(self.vuln_import_file)  # 导入地址
        self.Ui.action_vuln_export.triggered.connect(self.vuln_export_file)  # 导出扫描结果
        self.Ui.pushButton_vuln_export.clicked.connect(self.vuln_export_file)  # 导出结果
        self.Ui.action_vuln_reload.triggered.connect(self.vuln_reload_Plugins)  #重新加载插件
        self.Ui.action_vuln_showplubins.triggered.connect(self.vuln_ShowPlugins)  # 查看插件
        self.Ui.pushButton_vuln_showplugins.clicked.connect(self.vuln_ShowPlugins)  # 查看插件
        self.Ui.pushButton_vuln_start.clicked.connect(self.vuln_Start)  # 开始扫描
        self.Ui.action_vuln_start.triggered.connect(self.vuln_Start)  # 重新加载插件
        self.Ui.action_about.triggered.connect(self.about)  # 关于
        self.Ui.action_update.triggered.connect(self.version_update)  # 更新
        self.Ui.action_version.triggered.connect(self.version)  #版本
        self.Ui.action_ideas.triggered.connect(self.ideas)  # 意见反馈
        self.Ui.pushButton_vuln_all.clicked.connect(self.vuln_all)  # 全选
        self.Ui.pushButton_vuln_noall.clicked.connect(self.vuln_noall)  # 反选


        self.timer = QTimer()  #设定一个定时器用来显示时间
        self.timer.timeout.connect(self.showtime)
        self.timer.start()
        self.loadplugins()

        #设置漏洞扫描表格属性  列宽度
        self.Ui.tableWidget_vuln.setColumnWidth(0, 222)
        self.Ui.tableWidget_vuln.setColumnWidth(1, 325)
        self.Ui.tableWidget_vuln.setColumnWidth(2, 370)
        self.Ui.tableWidget_vuln.setColumnWidth(3, 91)

        #设置树形控件  列宽度
        # self.Ui.treeWidget_2.setColumnWidth(0, 220)
        # self.Ui.treeWidget_2.setColumnWidth(1, 180)
        # self.Ui.treeWidget_2.setColumnWidth(2, 60)
        # self.Ui.treeWidget_2.setColumnWidth(3, 60)
    # 显示时间
    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString("yyyy-MM-dd hh:mm:ss")
        self.setWindowTitle("FrameScan  V1.0测试版    %s"%text)
    #开始扫描
    def vuln_Start(self):
        self.Ui.textEdit_log.clear()
        for i in range(0, self.Ui.tableWidget_vuln.rowCount()):  # 循环行
            self.Ui.tableWidget_vuln.removeRow(0)
        target = [] #存放扫描的URL
        path= self.Ui.lineEdit_vuln_url.text()
        if os.path.isfile(path):
            self.Ui.textEdit_log.append(
                "[%s]Info:正在从文件中读取URL..." % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
            f=open(path,'r',encoding='utf-8')
            for line in f.readlines():
                if 'http' in line:
                    target.append(line)
            self.Ui.textEdit_log.append(
                "[%s]Info:读取完成，共加载%s条。" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))),len(target)))
        if 'http://' in path or 'https://' in path:
            target.append(path)
        if not target:
            self.Ui.textEdit_log.append(
                "[%s]Info:未获取到URL地址。" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
            return  0
        poc_methods =[]   #保存的所有方法。
        item = QtWidgets.QTreeWidgetItemIterator(self.Ui.treeWidget_Plugins)
        # 该类的value()即为QTreeWidgetItem
        while item.value():
            if not item.value().parent(): #判断有没有父节点
                pass
            else:#输出所有子节点
                if item.value().checkState(0) == QtCore.Qt.Checked:
                 # 参考网上的方法，判断有无父母结点后再分别操作的那个，实在找不到更直接的
                    poc_methods.append(item.value().text(0))
            item = item.__iadd__(1)
        if not poc_methods :
            self.Ui.textEdit_log.append(
                "[%s]Info:未选择插件。" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
            return 0
        self.Ui.textEdit_log.append(
            "[%s]Info:共加载%s个插件。" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))),len(poc_methods)))
        self.Ui.textEdit_log.append(
            "[%s]Start:扫描开始..." % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
        for url in target:
            thread = threading.Thread(target=self.vuln_scan, args=(url.replace("\n",""),poc_methods))
            thread.setDaemon(True)  # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
            thread.start()
    #调用脚本
    def vuln_scan(self,url,data):
        for poc in data:
            try:
                result = eval(poc)(url).run()
                # print(result)
                result_url = url.replace("http://","").replace("https://","")
                # print(result)
                # print(result_url)
                self.Ui.textEdit_log.append(
                    "[%s]Info:%s----%s----%s。" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), result_url, result[0], result[2]))
                if result[2] !='不存在' and result[2] !='':
                    row = self.Ui.tableWidget_vuln.rowCount()  # 获取行数
                    self.Ui.tableWidget_vuln.setRowCount(row + 1)
                    urlItem = QTableWidgetItem(result_url)
                    nameItem = QTableWidgetItem(result[0])
                    payloadItem = QTableWidgetItem(result[1])
                    resultItem = QTableWidgetItem(result[2])
                    self.Ui.tableWidget_vuln.setItem(row, 0, urlItem)
                    self.Ui.tableWidget_vuln.setItem(row, 1, nameItem)
                    self.Ui.tableWidget_vuln.setItem(row, 2, payloadItem)
                    self.Ui.tableWidget_vuln.setItem(row, 3, resultItem)
            except Exception as e :
                self.Ui.textEdit_log.append(
                    "[%s]Error:%s脚本执行错误！\n[Exception]:\n%s" % (
                    (time.strftime('%H:%M:%S', time.localtime(time.time()))),poc,e))
    #初始化加载插件
    def loadplugins(self):
        path = sys.path[0]
        if os.path.isfile(path+'/'+DB_NAME):
            conn = sqlite3.connect(DB_NAME)
        else:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "数据文件不存在，正在重新加载数据库！")
            self.vuln_reload_Plugins()
            return 0
        try:
            # 创建一个游标 curson
            cursor = conn.cursor()
            # 列出所有数据
            sql = "SELECT cmsname,pocmethods from POC"
            cursor.execute(sql)
            values = cursor.fetchall()
        except Exception as e :
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "数据文件错误：\n%s"%e)
            return 0
        #将查询的值组合为字典包含列表的形式
        cms_name = {}
        for cms in values:
            cms_name[cms[0]]=[]
        for cms in values:
            if cms[0] in cms_name.keys():
                cms_name[cms[0]].append(cms[1])
        for cms in cms_name:
            # 设置root为self.treeWidget_Plugins的子树，故root是根节点
            root = QTreeWidgetItem(self.Ui.treeWidget_Plugins)
            root.setText(0, cms)  # 设置根节点的名称
            root.setCheckState(0, Qt.Unchecked)  # 开启复选框
            for poc in cms_name[cms]:
                # 为root节点设置子结点
                child1 = QTreeWidgetItem(root)
                child1.setText(0, poc)
                child1.setCheckState(0, Qt.Unchecked)
        self.Ui.treeWidget_Plugins.itemChanged.connect(self.handleChanged)
        self.Ui.textEdit_log.append("[%s]Success:插件加载完成，共%s个。"%(time.strftime('%H:%M:%S', time.localtime(time.time())),len(values)))
     #父节点关联子节点
    def handleChanged(self,item, column):
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
        #self.tree.itemChanged.connect(self.handleChanged)
        #self.Ui.treeWidget_Plugins.addTopLevelItem(root)

    #导入文件列表
    def vuln_import_file(self):
        filename = self.file_open(r"Text Files (*.txt);;All files(*.*)")
        self.Ui.lineEdit_vuln_url.setText(filename)

    #导出扫描结果
    def vuln_export_file(self):
        data = []
        comdata = []
        for i in range(0, self.Ui.tableWidget_vuln.rowCount()):  # 循环行
            for j in range(0, self.Ui.tableWidget_vuln.columnCount()):  # 循环列
                if self.Ui.tableWidget_vuln.item(i, j) != None:  # 有数据
                    data.append(self.Ui.tableWidget_vuln.item(i, j).text())  # 空格分隔
            comdata.append(list(data))
            data = []

        if len(comdata)>0  :
            path = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '.csv').replace(' ', '-').replace('-','').replace(':', '')
            # print(path)
            file_name = self.file_save(path)
            if file_name!="":

                with open(file_name, 'w', newline='') as f:
                    writer = csv.writer(f)
                    for row in comdata:
                        writer.writerow(row)
                f.close()

    #显示插件
    def vuln_ShowPlugins(self):
        self.widget = Ui_Form()
        self.dialog = QtWidgets.QDialog(self)
        self.widget.setupUi(self.dialog)
        self.dialog.setFixedSize(self.dialog.width(), self.dialog.height())  # 设置宽高不可变
        #设置查看插件表格属性  列宽度
        self.widget.show_Plugins.setColumnWidth(0, 100)
        self.widget.show_Plugins.setColumnWidth(1, 350)
        self.widget.show_Plugins.setColumnWidth(2, 350)
        self.widget.show_Plugins.setColumnWidth(3, 384)
        self.widget.show_Plugins.setColumnWidth(4, 250)
        conn2 = sqlite3.connect(DB_NAME)
        # 创建一个游标 curson
        cursor = conn2.cursor()
        self.Ui.textEdit_log.append("[%s]Info:正在查询数据..."%(time.strftime('%H:%M:%S', time.localtime(time.time()))))
        # 列出所有数据
        sql = "SELECT * from POC"
        cursor.execute(sql)
        values = cursor.fetchall()
        self.Ui.textEdit_log.append("[%s]Success:数据查询成功！"%(time.strftime('%H:%M:%S', time.localtime(time.time()))))
        i=0
        self.widget.show_Plugins.setRowCount( len(values))
        for single in values:
            vuln_name = QTableWidgetItem(str(single[1]))
            vuln_url = QTableWidgetItem(str(single[3]))
            vuln_payload = QTableWidgetItem( str(single[4]))
            vuln_result = QTableWidgetItem(str(single[5]))
            vuln_motheds = QTableWidgetItem(str(single[2]))
            self.widget.show_Plugins.setItem(i, 0, vuln_name)
            self.widget.show_Plugins.setItem(i, 1, vuln_url)
            self.widget.show_Plugins.setItem(i, 2, vuln_payload)
            self.widget.show_Plugins.setItem(i, 3, vuln_result)
            self.widget.show_Plugins.setItem(i, 4, vuln_motheds)
            i = i + 1
        conn2.close()
        self.dialog.show()
    # 重新加载插件
    def vuln_reload_Plugins(self):
        path_conn = sys.path[0]
        self.Ui.treeWidget_Plugins.clear()
        # 删除数据库，重新建立
        if os.path.isfile(DB_NAME):
            try:
                # print(DB_NAME)
                os.remove(path_conn+'/'+DB_NAME)
            except Exception as e:
                self.Ui.textEdit_log.append("[%s]Error:数据库文件删除失败！\n[Exception]:\n%s" % (
                (time.strftime('%H:%M:%S', time.localtime(time.time()))), e))
                return 0
            self.Ui.textEdit_log.append(
                "[%s]Success:删除数据库完成！" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
        else:
            self.Ui.textEdit_log.append(
                "[%s]Success:数据库文件不存在，尝试创建数据库！" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
        try:
            # 连接数据库。如果数据库不存在的话，将会自动创建一个 数据库
            conn = sqlite3.connect(DB_NAME)
            # 创建一个游标 curson
            cursor = conn.cursor()
            # 执行一条语句,创建 user表 如不存在创建
            sql = "create table IF NOT EXISTS POC (id integer primary key autoincrement , cmsname varchar(30),pocfilename varchar(40),pocname  varchar(30),pocreferer varchar(50),pocdescription varchar(200),pocmethods  varchar(40))"
            cursor.execute(sql)
            self.Ui.textEdit_log.append(
                "[%s]Success:创建数据库完成！" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
        except Exception as e:
            self.Ui.textEdit_log.append(
                "[%s]Error:数据框创建失败！\n[Exception]:\n%s" % (time.strftime('%H:%M:%S', time.localtime(time.time())), e))
            return 0
        try:
            cms_path = path_conn + "/Plugins"
            cms_path = cms_path.replace("\\", "/")
            # 创建一个文件来存储引入的模块
            cmsmain_file = open(cms_path + "/Plugins.py", "w", encoding="utf-8")
        except Exception as e:
            self.Ui.textEdit_log.append("[%s]Error:打开Plugins.py文件失败！\n[Exception]:\n%s" % (
            (time.strftime('%H:%M:%S', time.localtime(time.time()))), e))
            return 0
        try:
            cmsmain_file.write(r"#!/usr/bin/env python" + '\n'
                            r"# -*- coding: utf-8 -*-" + '\n'
                            r"'''" + '\n'
                            r"name: cms漏洞库" + '\n'
                            r"referer: unknow" + '\n'
                            r"author: qianxiao996" + '\n'                                                                                                                                                                                      r"'''" + '\n')
            for cms_name in os.listdir(cms_path):  # 遍历目录名
                cmsmain_file.write("#" + cms_name + "\n")
                poc_path = os.path.join(cms_path, cms_name)
                for path, dirs, poc_methos_list in os.walk(poc_path):  # 遍历poc文件，得到方法名称
                    for poc_file_name in poc_methos_list:
                        # self.Ui.textEdit_log.append(poc_file_name[-3:])
                        # self.Ui.textEdit_log.append(poc_file_name)
                        poc_name_path = cms_path + "\\" + cms_name + "\\" + poc_file_name
                        poc_name_path = poc_name_path.replace("\\", "/")
                        # print(poc_name_path)
                        # 判断是py文件在打开  文件存在
                        if os.path.isfile(poc_name_path) and poc_file_name.endswith('.py'):
                            # 判断py文件不包含.
                            if '.' not in poc_file_name.replace(".py", ""):
                                # print(poc_name_path)
                                f = open(poc_name_path, "r", encoding="utf-8")
                                # 获取poc的中文名称
                                # printSkyBlue(cms_name)
                                poc_methos = ""  # 定义局部变量 存放poc方法
                                poc_name = ""  # 定义局部变量 存放poc名称
                                poc_referer = ""
                                if cms_name[0:2] != "__":  # 判断文件夹的前两位不是下划线
                                    for name in f.readlines():
                                        # print(name)
                                        # 得到中文poc_name
                                        if "name:" in name:
                                            poc_name = name.split(":")[1].replace(" ", "")
                                            poc_name = poc_name.replace("\n", "").replace("\r", "").replace("\r\n", "")
                                            # print(poc_name)
                                        # 得到调用的poc_methos
                                        if "class " in name:
                                            # print(name)
                                            poc_methos = name.replace(":", "").split(" ")[1].replace("\n", "").replace(
                                                "\r", "").replace("\r\n", "").replace("()", "")
                                            # self.Ui.textEdit_log.append(poc_methos)
                                        # 得到调用的poc_referer
                                        if "referer" in name:
                                            poc_referer = name.replace(":", "").split(" ")[1].replace("\n", "").replace(
                                                "\r", "").replace("\r\n", "")
                                            # self.Ui.textEdit_log.append(poc_referer)
                                    # 读取文件光标恢复到初始位置
                                    f.seek(0)
                                    condata = f.read()  ##所有数据
                                    # print(condata)
                                    # 匹配描述
                                    comment = re.compile(r"description:(.*?)'''", re.DOTALL)
                                    poc_description = str(comment.findall(condata)[0]).replace("\"", "").replace(" ","")
                                    if poc_name != "" and poc_methos != "":
                                        # 将数据插入到表中
                                        cursor.execute(
                                            'insert into POC (cmsname, pocname,pocfilename,pocreferer,pocdescription,pocmethods) values ("%s","%s","%s","%s","%s","%s")' % (
                                                cms_name, poc_name, poc_file_name, poc_referer, poc_description,poc_methos))
                                        data = "from Plugins." + cms_name + "." + poc_file_name.replace(".py",
                                                                                                    "") + " import " + poc_methos + "\n"
                                        cmsmain_file.write(data)
                                f.close()
                            else:
                                self.Ui.textEdit_log.append("[%s]Error:%s文件加载失败，文件名中不允许包含英文符号点！" % (
                                    (time.strftime('%H:%M:%S', time.localtime(time.time())))(
                                        cms_name + "/" + poc_file_name)))
                                return 0
                        else:
                            pass
                cmsmain_file.write("\n")
            conn.commit()  # 提交
            result = cursor.fetchall()
            if not len(result):
                cursor.execute("select count(*) from POC")
                values = cursor.fetchall()
                self.Ui.textEdit_log.append(
                    "[%s]Success:共写入%s个插件" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), values[0][0]))
                self.loadplugins()  # 调用加载插件
                box = QtWidgets.QMessageBox()
                box.information(self, "End", "数据更新完成！\n插件数量：%s"%values[0][0])

            else:
                self.Ui.textEdit_log.append(
                    "[%s]Error:数据更新失败，原因:" % (time.strftime('%H:%M:%S', time.localtime(time.time()))), str(result))
                return 0
            conn.close()
            cmsmain_file.close()
        except Exception as e:
            self.Ui.textEdit_log.append(
                "[%s]Error:数据写入失败！\n[Exception]:\n%s" % ((time.strftime('%H:%M:%S', time.localtime(time.time()))), e))
            return 0

    #关于
    def about(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about(self, "About", "\t\t\tAbout\n       此程序为一款CMS扫描工具，可自行选择扫描的插件进行漏洞检查，请勿非法使用！\n\t\t\t   Powered by qanxiao996")
    #更新
    def version_update(self):
        webbrowser.open("http://blog.qianxiao996.cn")
    #版本
    def version(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about (self, "版本", "FrameScan\nV1.0测试版")
    #意见反馈
    def ideas(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about(self, "意见反馈", "作者邮箱：qianxiao996@126.com\n作者主页：http://blog.qianxiao.996.cn")
    #全选
    def vuln_all(self):
        item = QtWidgets.QTreeWidgetItemIterator(self.Ui.treeWidget_Plugins)
        # 该类的value()即为QTreeWidgetItem
        while item.value():
            if item.value().checkState(0) != QtCore.Qt.Checked:
                item.value().setCheckState(0, Qt.Checked)
            item = item.__iadd__(1)
    #反选
    def vuln_noall(self):
        item = QtWidgets.QTreeWidgetItemIterator(self.Ui.treeWidget_Plugins)
        # 该类的value()即为QTreeWidgetItem
        while item.value():
            if item.value().checkState(0) == QtCore.Qt.Checked:
                item.value().setCheckState(0,Qt.Unchecked)
            item = item.__iadd__(1)


    #文件打开对话框
    def file_open(self,type):
        fileName, selectedFilter = QFileDialog.getOpenFileName(self, (r"上传文件"), (r"C:\windows"),type)
        return (fileName)  # 返回文件路径

    # 保存文件对话框
    def file_save(self, filename):
        fileName, filetype = QFileDialog.getSaveFileName(self, (r"保存文件"), (r'C:\Users\Administrator\\' + filename),
                                                         r"All files(*.*)")
        # print(fileName)
        return fileName

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    try:
        from Plugins.Plugins import *
    except:
        a = MainWindows()
        a.vuln_reload_Plugins()
    # styleFile = './qss/black.qss'
    # qssStyle = Common.readQss(styleFile)
    # window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())


