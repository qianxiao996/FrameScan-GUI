# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrameScan.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 790)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/main.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget_Plugins = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_Plugins.setGeometry(QtCore.QRect(0, 36, 231, 729))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_Plugins.sizePolicy().hasHeightForWidth())
        self.treeWidget_Plugins.setSizePolicy(sizePolicy)
        self.treeWidget_Plugins.setStyleSheet("\n"
"/**********表头**********/\n"
"QHeaderView{\n"
"        border: none;\n"
"        background: rgb(57, 58, 60);\n"
"        min-height: 30px;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"        border: none;\n"
"        padding-left: 5px;\n"
"}\n"
"/*滑动条*/\n"
"QScrollBar:vertical  \n"
"{\n"
"    width:15px;\n"
"    border-radius:7px;  /* 滚动条的滑轨的圆角*/\n"
"   /* background:blue; */ /* 滚动条的滑轨的背景颜色*/\n"
"    padding-top:14px;  /* 滚动条上部增加padding*/\n"
"    padding-bottom:14px;  /* 同理*/\n"
" \n"
"}\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background:rgb(225, 225, 225)/*darkgray*/;  /* 滚动条颜色*/\n"
"    border-radius:6px;  /* 滚动条圆角*/\n"
"    margin-left:0px;  /* 滚动条和滑轨之间的左间隙*/\n"
"    margin-right:1px;  /* 同理*/\n"
"}\n"
"QScrollBar::handle:vertical:hover  /* 鼠标放上滑块滑块变色*/\n"
"{\n"
"    background:gray;\n"
"    border-radius:6px;\n"
"}\n"
"QScrollBar::add-line:vertical  /* 下方箭头*/\n"
"{\n"
"    height:15px;width:8px;  /* 设置箭头区域的宽高*/\n"
"  /*  image:url(\'./pictures/down-arrow.jpg\');  /* 自己在网上找的箭头图片。如果不需要箭头，可将引号里面的路径去除，设置为image:url(\'\')即可*/\n"
"}\n"
"QScrollBar::sub-line:vertical  /* 上方箭头*/\n"
"{\n"
"    height:14px;width:8px;\n"
"   /* image:url(\'\');  /* 这里设置为空，方便和下箭头对比\n"
"*/}\n"
"QScrollBar::add-line:vertical:hover  /* 鼠标放到下箭头箭头变成其他图片*/\n"
"{\n"
"    height:14px;width:8px;\n"
"   /* image:url(\'./pictures/down-down-arrow.jpg\');*/\n"
"    subcontrol-position:bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover  /* 鼠标放到上箭头箭头变成其他图片*/\n"
"{\n"
"    height:14px;width:8px;\n"
"    /*image:url(\'\');  *//* 这里设置为空，方便和下箭头对比*/\n"
"    subcontrol-position:top;\n"
"}\n"
"QScrollBar::add-page:vertical  /* 滑块已经经过的滑轨区域的颜色，若没有这里的设置，该区域会呈现网格状，不美观\n"
"*/{\n"
"    background:green;\n"
"}\n"
"QScrollBar::sub-page:vertical  /*  滑块还没经过的滑轨区域的颜色，若没有这里的设置，该区域会呈现网格状，不美观\n"
"*/{\n"
"    background:red; \n"
"}")
        self.treeWidget_Plugins.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_Plugins.setObjectName("treeWidget_Plugins")
        self.treeWidget_Plugins.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.tableWidget_vuln = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_vuln.setGeometry(QtCore.QRect(229, 36, 1011, 531))
        self.tableWidget_vuln.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_vuln.setStyleSheet("\n"
"/**********表头**********/\n"
"QHeaderView{\n"
"        border: none;\n"
"        background: rgb(57, 58, 60);\n"
"        min-height: 30px;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"        border: none;\n"
"        padding-left: 5px;\n"
"}\n"
"QTableView::item {\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"        border: none;\n"
"}\n"
"/**********表格选中颜色**********/\n"
"QTableView::item:selected {\n"
"color:rgb(0, 0, 0) ;\n"
"        background:  rgb(240, 240, 240);\n"
"}\n"
"QTableView::item:selected:!active {\n"
"        color:rgb(0, 0, 0) ;\n"
"}\n"
"\n"
"QTableView::indicator {\n"
"       /* width: 20px;*/\n"
"        height: 20px;\n"
"}")
        self.tableWidget_vuln.setObjectName("tableWidget_vuln")
        self.tableWidget_vuln.setColumnCount(4)
        self.tableWidget_vuln.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_vuln.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_vuln.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_vuln.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_vuln.setHorizontalHeaderItem(3, item)
        self.tableWidget_vuln.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget_vuln.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_vuln.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_vuln.verticalHeader().setVisible(False)
        self.tableWidget_vuln.verticalHeader().setSortIndicatorShown(False)
        self.textEdit_log = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_log.setGeometry(QtCore.QRect(229, 565, 1011, 201))
        self.textEdit_log.setStyleSheet("")
        self.textEdit_log.setObjectName("textEdit_log")
        self.lineEdit_vuln_url = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_vuln_url.setGeometry(QtCore.QRect(271, 3, 321, 30))
        self.lineEdit_vuln_url.setStyleSheet("QLineEdit {\n"
"        border-radius: 4px;\n"
"        height: 25px;\n"
"        border: 1px solid rgb(100, 100, 100);\n"
"        background: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit:enabled {\n"
"        color: rgb(175, 175, 175);\n"
"}\n"
"QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color:rgb(255, 85, 255)\n"
"}\n"
"QLineEdit:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}")
        self.lineEdit_vuln_url.setObjectName("lineEdit_vuln_url")
        self.label_vuln_url = QtWidgets.QLabel(self.centralwidget)
        self.label_vuln_url.setGeometry(QtCore.QRect(223, 3, 53, 30))
        self.label_vuln_url.setObjectName("label_vuln_url")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(600, 3, 501, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_vuln_file = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_vuln_file.setStyleSheet("\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"border: 1px solid;\n"
"         background: rgb(255, 255, 255);\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为10点*/\n"
"    font-size:10pt;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(225, 225, 225);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:2px;\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(170, 170, 255);\n"
"   color:white;\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为2像素，让按下时字向右移动3像素*/  \n"
"    padding-left:2px;\n"
"    /*上内边距为2像素，让按下时字向下移动3像素*/  \n"
"    padding-top:2px;\n"
"}\n"
"\n"
"")
        self.pushButton_vuln_file.setObjectName("pushButton_vuln_file")
        self.horizontalLayout.addWidget(self.pushButton_vuln_file)
        self.pushButton_vuln_start = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_vuln_start.setStyleSheet("\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"border: 1px solid;\n"
"         background: rgb(255, 255, 255);\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为10点*/\n"
"    font-size:10pt;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(225, 225, 225);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:2px;\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(170, 170, 255);\n"
"   color:white;\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为2像素，让按下时字向右移动3像素*/  \n"
"    padding-left:2px;\n"
"    /*上内边距为2像素，让按下时字向下移动3像素*/  \n"
"    padding-top:2px;\n"
"}\n"
"\n"
"")
        self.pushButton_vuln_start.setObjectName("pushButton_vuln_start")
        self.horizontalLayout.addWidget(self.pushButton_vuln_start)
        self.pushButton_vuln_export = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_vuln_export.setStyleSheet("\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"border: 1px solid;\n"
"         background: rgb(255, 255, 255);\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为10点*/\n"
"    font-size:10pt;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(225, 225, 225);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:2px;\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(170, 170, 255);\n"
"   color:white;\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为2像素，让按下时字向右移动3像素*/  \n"
"    padding-left:2px;\n"
"    /*上内边距为2像素，让按下时字向下移动3像素*/  \n"
"    padding-top:2px;\n"
"}\n"
"")
        self.pushButton_vuln_export.setObjectName("pushButton_vuln_export")
        self.horizontalLayout.addWidget(self.pushButton_vuln_export)
        self.pushButton_vuln_showplugins = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_vuln_showplugins.setStyleSheet("\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"border: 1px solid;\n"
"         background: rgb(255, 255, 255);\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为10点*/\n"
"    font-size:10pt;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(225, 225, 225);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:2px;\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(170, 170, 255);\n"
"   color:white;\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为2像素，让按下时字向右移动3像素*/  \n"
"    padding-left:2px;\n"
"    /*上内边距为2像素，让按下时字向下移动3像素*/  \n"
"    padding-top:2px;\n"
"}\n"
"")
        self.pushButton_vuln_showplugins.setObjectName("pushButton_vuln_showplugins")
        self.horizontalLayout.addWidget(self.pushButton_vuln_showplugins)
        self.pushButton_vuln_exit = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_vuln_exit.setStyleSheet("\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"border: 1px solid;\n"
"         background: rgb(255, 255, 255);\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为10点*/\n"
"    font-size:10pt;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(225, 225, 225);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:2px;\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(170, 170, 255);\n"
"   color:white;\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为2像素，让按下时字向右移动3像素*/  \n"
"    padding-left:2px;\n"
"    /*上内边距为2像素，让按下时字向下移动3像素*/  \n"
"    padding-top:2px;\n"
"}\n"
"")
        self.pushButton_vuln_exit.setObjectName("pushButton_vuln_exit")
        self.horizontalLayout.addWidget(self.pushButton_vuln_exit)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(16, 3, 195, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_vuln_all = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_vuln_all.setStyleSheet("\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"border: 1px solid;\n"
"         background: rgb(255, 255, 255);\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为10点*/\n"
"    font-size:10pt;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(225, 225, 225);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:2px;\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(170, 170, 255);\n"
"   color:white;\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为2像素，让按下时字向右移动3像素*/  \n"
"    padding-left:2px;\n"
"    /*上内边距为2像素，让按下时字向下移动3像素*/  \n"
"    padding-top:2px;\n"
"}\n"
"")
        self.pushButton_vuln_all.setObjectName("pushButton_vuln_all")
        self.horizontalLayout_2.addWidget(self.pushButton_vuln_all)
        self.pushButton_vuln_noall = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_vuln_noall.setStyleSheet("\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"border: 1px solid;\n"
"         background: rgb(255, 255, 255);\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为10点*/\n"
"    font-size:10pt;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(225, 225, 225);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:2px;\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(170, 170, 255);\n"
"   color:white;\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为2像素，让按下时字向右移动3像素*/  \n"
"    padding-left:2px;\n"
"    /*上内边距为2像素，让按下时字向下移动3像素*/  \n"
"    padding-top:2px;\n"
"}\n"
"")
        self.pushButton_vuln_noall.setObjectName("pushButton_vuln_noall")
        self.horizontalLayout_2.addWidget(self.pushButton_vuln_noall)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(1108, 2, 121, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.threadsnum = QtWidgets.QComboBox(self.layoutWidget_2)
        self.threadsnum.setStyleSheet("QComboBox {\n"
"    \n"
"    /* 边框宽度,线条样式,颜色 */\n"
"    border:1px solid black;\n"
"\n"
"    /* 倒角 */\n"
"    border-radius:4px;\n"
"\n"
"    /* 内边框 */\n"
"    padding:1px 10px 1px 3px;\n"
"\n"
"    max-width:35px;\n"
"}\n"
"QComboBox:editable {\n"
"  /*  background:green;*/\n"
"}\n"
"/* 当下拉框打开时, 移动显示框文本位置*/\n"
"QComboBox:on {\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"/* 下拉按钮 */\n"
"QComboBox::drop-down {\n"
"\n"
"    subcontrol-origin: padding;\n"
"\n"
"    /* 按钮位置,右上角 */\n"
"    subcontrol-position: top right;\n"
"\n"
"    width: 17px;\n"
"  \n"
"    \n"
"\n"
"}")
        self.threadsnum.setObjectName("threadsnum")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.horizontalLayout_3.addWidget(self.threadsnum)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1240, 26))
        self.menubar.setObjectName("menubar")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.action_dir_export = QtWidgets.QAction(MainWindow)
        self.action_dir_export.setObjectName("action_dir_export")
        self.action_dir_Import = QtWidgets.QAction(MainWindow)
        self.action_dir_Import.setObjectName("action_dir_Import")
        self.action_reload = QtWidgets.QAction(MainWindow)
        self.action_reload.setObjectName("action_reload")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_update = QtWidgets.QAction(MainWindow)
        self.action_update.setObjectName("action_update")
        self.action_version = QtWidgets.QAction(MainWindow)
        self.action_version.setObjectName("action_version")
        self.action_ideas = QtWidgets.QAction(MainWindow)
        self.action_ideas.setObjectName("action_ideas")
        self.action_zhiwen_export = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_export.setObjectName("action_zhiwen_export")
        self.action_zhiwen_import = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_import.setObjectName("action_zhiwen_import")
        self.action_port_export = QtWidgets.QAction(MainWindow)
        self.action_port_export.setObjectName("action_port_export")
        self.action_sub_export = QtWidgets.QAction(MainWindow)
        self.action_sub_export.setObjectName("action_sub_export")
        self.action_vuln_export = QtWidgets.QAction(MainWindow)
        self.action_vuln_export.setObjectName("action_vuln_export")
        self.action_port_import = QtWidgets.QAction(MainWindow)
        self.action_port_import.setObjectName("action_port_import")
        self.action_sub_import = QtWidgets.QAction(MainWindow)
        self.action_sub_import.setObjectName("action_sub_import")
        self.action_vuln_import = QtWidgets.QAction(MainWindow)
        self.action_vuln_import.setObjectName("action_vuln_import")
        self.action_vuln_reload = QtWidgets.QAction(MainWindow)
        self.action_vuln_reload.setObjectName("action_vuln_reload")
        self.action_vuln_showplubins = QtWidgets.QAction(MainWindow)
        self.action_vuln_showplubins.setObjectName("action_vuln_showplubins")
        self.action_dir_start = QtWidgets.QAction(MainWindow)
        self.action_dir_start.setObjectName("action_dir_start")
        self.action_dir_stop = QtWidgets.QAction(MainWindow)
        self.action_dir_stop.setObjectName("action_dir_stop")
        self.action_zhiwen_start = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_start.setObjectName("action_zhiwen_start")
        self.action_zhiwen_stop = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_stop.setObjectName("action_zhiwen_stop")
        self.action_port_start = QtWidgets.QAction(MainWindow)
        self.action_port_start.setObjectName("action_port_start")
        self.action_port_stop = QtWidgets.QAction(MainWindow)
        self.action_port_stop.setObjectName("action_port_stop")
        self.action_sub_start = QtWidgets.QAction(MainWindow)
        self.action_sub_start.setObjectName("action_sub_start")
        self.action_sub_stop = QtWidgets.QAction(MainWindow)
        self.action_sub_stop.setObjectName("action_sub_stop")
        self.action_vuln_start = QtWidgets.QAction(MainWindow)
        self.action_vuln_start.setObjectName("action_vuln_start")
        self.action_vuln_stop = QtWidgets.QAction(MainWindow)
        self.action_vuln_stop.setObjectName("action_vuln_stop")
        self.menu_3.addAction(self.action_about)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_update)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_ideas)
        self.menu_5.addAction(self.action_vuln_start)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.action_vuln_export)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.action_vuln_import)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.action_vuln_reload)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.action_vuln_showplubins)
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_vuln_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FrameScan  by  qianxiao996"))
        self.treeWidget_Plugins.headerItem().setText(0, _translate("MainWindow", "Plugins"))
        item = self.tableWidget_vuln.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "网页地址"))
        item = self.tableWidget_vuln.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "漏洞名称"))
        item = self.tableWidget_vuln.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Payload"))
        item = self.tableWidget_vuln.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "检测结果"))
        self.label_vuln_url.setText(_translate("MainWindow", " 目标："))
        self.pushButton_vuln_file.setText(_translate("MainWindow", "导入地址"))
        self.pushButton_vuln_start.setText(_translate("MainWindow", "开始扫描"))
        self.pushButton_vuln_export.setText(_translate("MainWindow", "导出结果"))
        self.pushButton_vuln_showplugins.setText(_translate("MainWindow", "查看插件"))
        self.pushButton_vuln_exit.setText(_translate("MainWindow", "退出程序"))
        self.pushButton_vuln_all.setText(_translate("MainWindow", "全  选"))
        self.pushButton_vuln_noall.setText(_translate("MainWindow", "反  选"))
        self.label.setText(_translate("MainWindow", "线程数量"))
        self.threadsnum.setItemText(0, _translate("MainWindow", "5"))
        self.threadsnum.setItemText(1, _translate("MainWindow", "10"))
        self.threadsnum.setItemText(2, _translate("MainWindow", "15"))
        self.threadsnum.setItemText(3, _translate("MainWindow", "30"))
        self.threadsnum.setItemText(4, _translate("MainWindow", "50"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.menu_5.setTitle(_translate("MainWindow", "选项"))
        self.action_dir_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_dir_Import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_reload.setText(_translate("MainWindow", "重新加载插件"))
        self.action_about.setText(_translate("MainWindow", "关于"))
        self.action_update.setText(_translate("MainWindow", "更新"))
        self.action_version.setText(_translate("MainWindow", "版本"))
        self.action_ideas.setText(_translate("MainWindow", "意见反馈"))
        self.action_zhiwen_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_zhiwen_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_port_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_sub_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_vuln_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_port_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_sub_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_vuln_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_vuln_reload.setText(_translate("MainWindow", "重新加载插件"))
        self.action_vuln_showplubins.setText(_translate("MainWindow", "查看插件信息"))
        self.action_dir_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_dir_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_zhiwen_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_zhiwen_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_port_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_port_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_sub_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_sub_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_vuln_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_vuln_stop.setText(_translate("MainWindow", "停止扫描"))

