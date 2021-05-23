# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1411, 865)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/qianxiao996/.designer/img/main.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1411, 0))
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.vuln_scanner = QtWidgets.QWidget()
        self.vuln_scanner.setObjectName("vuln_scanner")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.vuln_scanner)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_vuln_all = QtWidgets.QPushButton(self.vuln_scanner)
        self.pushButton_vuln_all.setMinimumSize(QtCore.QSize(60, 28))
        self.pushButton_vuln_all.setStyleSheet("")
        self.pushButton_vuln_all.setObjectName("pushButton_vuln_all")
        self.horizontalLayout_2.addWidget(self.pushButton_vuln_all)
        self.pushButton_vuln_noall = QtWidgets.QPushButton(self.vuln_scanner)
        self.pushButton_vuln_noall.setMinimumSize(QtCore.QSize(60, 28))
        self.pushButton_vuln_noall.setStyleSheet("")
        self.pushButton_vuln_noall.setObjectName("pushButton_vuln_noall")
        self.horizontalLayout_2.addWidget(self.pushButton_vuln_noall)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.treeWidget_Plugins = QtWidgets.QTreeWidget(self.vuln_scanner)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_Plugins.sizePolicy().hasHeightForWidth())
        self.treeWidget_Plugins.setSizePolicy(sizePolicy)
        self.treeWidget_Plugins.setMinimumSize(QtCore.QSize(250, 0))
        self.treeWidget_Plugins.setMaximumSize(QtCore.QSize(350, 16777215))
        self.treeWidget_Plugins.setStyleSheet("")
        self.treeWidget_Plugins.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_Plugins.setObjectName("treeWidget_Plugins")
        self.treeWidget_Plugins.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.treeWidget_Plugins)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_vuln_url = QtWidgets.QLabel(self.vuln_scanner)
        self.label_vuln_url.setObjectName("label_vuln_url")
        self.horizontalLayout_5.addWidget(self.label_vuln_url)
        self.lineEdit_vuln_url = QtWidgets.QLineEdit(self.vuln_scanner)
        self.lineEdit_vuln_url.setMinimumSize(QtCore.QSize(200, 26))
        self.lineEdit_vuln_url.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_vuln_url.setStyleSheet("")
        self.lineEdit_vuln_url.setObjectName("lineEdit_vuln_url")
        self.horizontalLayout_5.addWidget(self.lineEdit_vuln_url)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.pushButton_vuln_file = QtWidgets.QToolButton(self.vuln_scanner)
        self.pushButton_vuln_file.setMinimumSize(QtCore.QSize(20, 28))
        self.pushButton_vuln_file.setObjectName("pushButton_vuln_file")
        self.horizontalLayout.addWidget(self.pushButton_vuln_file)
        self.pushButton_vuln_start = QtWidgets.QPushButton(self.vuln_scanner)
        self.pushButton_vuln_start.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_vuln_start.setStyleSheet("")
        self.pushButton_vuln_start.setObjectName("pushButton_vuln_start")
        self.horizontalLayout.addWidget(self.pushButton_vuln_start)
        self.pushButton_vuln_expstart = QtWidgets.QPushButton(self.vuln_scanner)
        self.pushButton_vuln_expstart.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_vuln_expstart.setObjectName("pushButton_vuln_expstart")
        self.horizontalLayout.addWidget(self.pushButton_vuln_expstart)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tableWidget_vuln = QtWidgets.QTableWidget(self.vuln_scanner)
        self.tableWidget_vuln.setMinimumSize(QtCore.QSize(1100, 550))
        self.tableWidget_vuln.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_vuln.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget_vuln.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_vuln.setAutoFillBackground(False)
        self.tableWidget_vuln.setStyleSheet("selection-background-color:lightblue;")
        self.tableWidget_vuln.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_vuln.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_vuln.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_vuln.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_vuln.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_vuln.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget_vuln.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_vuln.setShowGrid(True)
        self.tableWidget_vuln.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget_vuln.setWordWrap(True)
        self.tableWidget_vuln.setCornerButtonEnabled(True)
        self.tableWidget_vuln.setObjectName("tableWidget_vuln")
        self.tableWidget_vuln.setColumnCount(5)
        self.tableWidget_vuln.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(4, item)
        self.tableWidget_vuln.horizontalHeader().setVisible(True)
        self.tableWidget_vuln.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_vuln.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget_vuln.horizontalHeader().setHighlightSections(False)
        self.tableWidget_vuln.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_vuln.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_vuln.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_vuln.verticalHeader().setVisible(False)
        self.tableWidget_vuln.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_vuln.verticalHeader().setDefaultSectionSize(35)
        self.tableWidget_vuln.verticalHeader().setHighlightSections(False)
        self.tableWidget_vuln.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_vuln.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_4.addWidget(self.tableWidget_vuln)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.vuln_scanner)
        self.groupBox_5.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.textEdit_log = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_log.setMinimumSize(QtCore.QSize(600, 0))
        self.textEdit_log.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEdit_log.setStyleSheet("")
        self.textEdit_log.setObjectName("textEdit_log")
        self.gridLayout_9.addWidget(self.textEdit_log, 0, 0, 1, 1)
        self.horizontalLayout_6.addWidget(self.groupBox_5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.vuln_scanner)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.comboBox_timeout = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_timeout.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_timeout.setObjectName("comboBox_timeout")
        self.comboBox_timeout.addItem("")
        self.comboBox_timeout.addItem("")
        self.comboBox_timeout.addItem("")
        self.comboBox_timeout.addItem("")
        self.comboBox_timeout.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_timeout)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.threadsnum = QtWidgets.QComboBox(self.groupBox_3)
        self.threadsnum.setStyleSheet("")
        self.threadsnum.setObjectName("threadsnum")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.horizontalLayout_3.addWidget(self.threadsnum)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.vuln_scanner_debug = QtWidgets.QCheckBox(self.groupBox_3)
        self.vuln_scanner_debug.setMinimumSize(QtCore.QSize(118, 0))
        self.vuln_scanner_debug.setCheckable(True)
        self.vuln_scanner_debug.setChecked(False)
        self.vuln_scanner_debug.setObjectName("vuln_scanner_debug")
        self.verticalLayout.addWidget(self.vuln_scanner_debug)
        self.jump_url = QtWidgets.QCheckBox(self.groupBox_3)
        self.jump_url.setMinimumSize(QtCore.QSize(131, 0))
        self.jump_url.setCheckable(True)
        self.jump_url.setChecked(False)
        self.jump_url.setObjectName("jump_url")
        self.verticalLayout.addWidget(self.jump_url)
        self.jump_fofa = QtWidgets.QCheckBox(self.groupBox_3)
        self.jump_fofa.setMinimumSize(QtCore.QSize(131, 0))
        self.jump_fofa.setCheckable(True)
        self.jump_fofa.setChecked(True)
        self.jump_fofa.setObjectName("jump_fofa")
        self.verticalLayout.addWidget(self.jump_fofa)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.vuln_scanner)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.vuln_scanner_textEdit_heads = QtWidgets.QTextEdit(self.groupBox_4)
        self.vuln_scanner_textEdit_heads.setMaximumSize(QtCore.QSize(16777215, 200))
        self.vuln_scanner_textEdit_heads.setObjectName("vuln_scanner_textEdit_heads")
        self.gridLayout_8.addWidget(self.vuln_scanner_textEdit_heads, 0, 0, 1, 1)
        self.horizontalLayout_6.addWidget(self.groupBox_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.gridLayout_10.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.vuln_scanner, "")
        self.vuln_exp = QtWidgets.QWidget()
        self.vuln_exp.setObjectName("vuln_exp")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.vuln_exp)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.exp_tabWidget = QtWidgets.QTabWidget(self.vuln_exp)
        self.exp_tabWidget.setMinimumSize(QtCore.QSize(0, 545))
        self.exp_tabWidget.setObjectName("exp_tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setVerticalSpacing(7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.vuln_exp_textEdit_info = QtWidgets.QTextEdit(self.tab)
        self.vuln_exp_textEdit_info.setMinimumSize(QtCore.QSize(950, 0))
        self.vuln_exp_textEdit_info.setObjectName("vuln_exp_textEdit_info")
        self.gridLayout_5.addWidget(self.vuln_exp_textEdit_info, 0, 0, 1, 1)
        self.exp_tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setMinimumSize(QtCore.QSize(55, 28))
        self.label_14.setMaximumSize(QtCore.QSize(55, 16777215))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_19.addWidget(self.label_14)
        self.vuln_exp_input_cmd = QtWidgets.QLineEdit(self.tab_2)
        self.vuln_exp_input_cmd.setMinimumSize(QtCore.QSize(0, 28))
        self.vuln_exp_input_cmd.setObjectName("vuln_exp_input_cmd")
        self.horizontalLayout_19.addWidget(self.vuln_exp_input_cmd)
        self.vuln_exp_button_cmd = QtWidgets.QPushButton(self.tab_2)
        self.vuln_exp_button_cmd.setMinimumSize(QtCore.QSize(0, 30))
        self.vuln_exp_button_cmd.setObjectName("vuln_exp_button_cmd")
        self.horizontalLayout_19.addWidget(self.vuln_exp_button_cmd)
        self.gridLayout_2.addLayout(self.horizontalLayout_19, 0, 0, 1, 1)
        self.textEdit_result = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_result.setObjectName("textEdit_result")
        self.gridLayout_2.addWidget(self.textEdit_result, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.exp_tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_11.addWidget(self.exp_tabWidget)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.vuln_exp)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.vuln_exp_textEdit_log = QtWidgets.QTextEdit(self.vuln_exp)
        self.vuln_exp_textEdit_log.setMaximumSize(QtCore.QSize(400, 16777215))
        self.vuln_exp_textEdit_log.setObjectName("vuln_exp_textEdit_log")
        self.verticalLayout_8.addWidget(self.vuln_exp_textEdit_log)
        self.horizontalLayout_11.addLayout(self.verticalLayout_8)
        self.gridLayout_6.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.vuln_exp)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setMinimumSize(QtCore.QSize(60, 20))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_13.addWidget(self.label_7)
        self.vuln_lineEdit_url = QtWidgets.QLineEdit(self.groupBox)
        self.vuln_lineEdit_url.setMinimumSize(QtCore.QSize(0, 28))
        self.vuln_lineEdit_url.setSizeIncrement(QtCore.QSize(0, 0))
        self.vuln_lineEdit_url.setObjectName("vuln_lineEdit_url")
        self.horizontalLayout_13.addWidget(self.vuln_lineEdit_url)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setMinimumSize(QtCore.QSize(60, 20))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_14.addWidget(self.label_8)
        self.vuln_lineEdit_cookie = QtWidgets.QLineEdit(self.groupBox)
        self.vuln_lineEdit_cookie.setMinimumSize(QtCore.QSize(0, 28))
        self.vuln_lineEdit_cookie.setObjectName("vuln_lineEdit_cookie")
        self.horizontalLayout_14.addWidget(self.vuln_lineEdit_cookie)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setMinimumSize(QtCore.QSize(60, 0))
        self.label_12.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_16.addWidget(self.label_12)
        self.vuln_type = QtWidgets.QComboBox(self.groupBox)
        self.vuln_type.setMinimumSize(QtCore.QSize(0, 30))
        self.vuln_type.setStyleSheet("")
        self.vuln_type.setObjectName("vuln_type")
        self.horizontalLayout_16.addWidget(self.vuln_type)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setMinimumSize(QtCore.QSize(60, 0))
        self.label_13.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_17.addWidget(self.label_13)
        self.vuln_name = QtWidgets.QComboBox(self.groupBox)
        self.vuln_name.setMinimumSize(QtCore.QSize(300, 30))
        self.vuln_name.setStyleSheet("")
        self.vuln_name.setObjectName("vuln_name")
        self.horizontalLayout_17.addWidget(self.vuln_name)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)
        self.verticalLayout_6.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_20.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.vuln_exp)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setMinimumSize(QtCore.QSize(60, 28))
        self.label_4.setMaximumSize(QtCore.QSize(55, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.vuln_exp_input_ip = QtWidgets.QLineEdit(self.groupBox_2)
        self.vuln_exp_input_ip.setMinimumSize(QtCore.QSize(200, 28))
        self.vuln_exp_input_ip.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.vuln_exp_input_ip.setText("")
        self.vuln_exp_input_ip.setObjectName("vuln_exp_input_ip")
        self.horizontalLayout_10.addWidget(self.vuln_exp_input_ip)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setMinimumSize(QtCore.QSize(35, 28))
        self.label_5.setMaximumSize(QtCore.QSize(32, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.vuln_exp_input_port = QtWidgets.QLineEdit(self.groupBox_2)
        self.vuln_exp_input_port.setMinimumSize(QtCore.QSize(50, 28))
        self.vuln_exp_input_port.setMaximumSize(QtCore.QSize(60, 16777215))
        self.vuln_exp_input_port.setText("")
        self.vuln_exp_input_port.setObjectName("vuln_exp_input_port")
        self.horizontalLayout_10.addWidget(self.vuln_exp_input_port)
        self.vuln_exp_button_shell = QtWidgets.QPushButton(self.groupBox_2)
        self.vuln_exp_button_shell.setMinimumSize(QtCore.QSize(0, 30))
        self.vuln_exp_button_shell.setObjectName("vuln_exp_button_shell")
        self.horizontalLayout_10.addWidget(self.vuln_exp_button_shell)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.groupBox_7 = QtWidgets.QGroupBox(self.vuln_exp)
        self.groupBox_7.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 230))
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plainTextEdit_heads = QtWidgets.QPlainTextEdit(self.groupBox_7)
        self.plainTextEdit_heads.setObjectName("plainTextEdit_heads")
        self.gridLayout_3.addWidget(self.plainTextEdit_heads, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_7)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.vuln_exp, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1411, 26))
        self.menubar.setObjectName("menubar")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.action_port_start = QtWidgets.QAction(MainWindow)
        self.action_port_start.setObjectName("action_port_start")
        self.action_zhiwen_start = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_start.setObjectName("action_zhiwen_start")
        self.action_dir_stop = QtWidgets.QAction(MainWindow)
        self.action_dir_stop.setObjectName("action_dir_stop")
        self.action_dir_start = QtWidgets.QAction(MainWindow)
        self.action_dir_start.setObjectName("action_dir_start")
        self.action_vuln_showplubins = QtWidgets.QAction(MainWindow)
        self.action_vuln_showplubins.setObjectName("action_vuln_showplubins")
        self.action_vuln_reload = QtWidgets.QAction(MainWindow)
        self.action_vuln_reload.setObjectName("action_vuln_reload")
        self.action_vuln_import = QtWidgets.QAction(MainWindow)
        self.action_vuln_import.setObjectName("action_vuln_import")
        self.action_sub_import = QtWidgets.QAction(MainWindow)
        self.action_sub_import.setObjectName("action_sub_import")
        self.action_port_import = QtWidgets.QAction(MainWindow)
        self.action_port_import.setObjectName("action_port_import")
        self.action_vuln_export = QtWidgets.QAction(MainWindow)
        self.action_vuln_export.setObjectName("action_vuln_export")
        self.action_sub_export = QtWidgets.QAction(MainWindow)
        self.action_sub_export.setObjectName("action_sub_export")
        self.action_port_export = QtWidgets.QAction(MainWindow)
        self.action_port_export.setObjectName("action_port_export")
        self.action_zhiwen_import = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_import.setObjectName("action_zhiwen_import")
        self.action_zhiwen_export = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_export.setObjectName("action_zhiwen_export")
        self.action_ideas = QtWidgets.QAction(MainWindow)
        self.action_ideas.setObjectName("action_ideas")
        self.action_version = QtWidgets.QAction(MainWindow)
        self.action_version.setObjectName("action_version")
        self.action_update = QtWidgets.QAction(MainWindow)
        self.action_update.setObjectName("action_update")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_reload = QtWidgets.QAction(MainWindow)
        self.action_reload.setObjectName("action_reload")
        self.action_dir_Import = QtWidgets.QAction(MainWindow)
        self.action_dir_Import.setObjectName("action_dir_Import")
        self.action_dir_export = QtWidgets.QAction(MainWindow)
        self.action_dir_export.setObjectName("action_dir_export")
        self.action_zhiwen_stop = QtWidgets.QAction(MainWindow)
        self.action_zhiwen_stop.setObjectName("action_zhiwen_stop")
        self.action_sub_stop = QtWidgets.QAction(MainWindow)
        self.action_sub_stop.setObjectName("action_sub_stop")
        self.action_port_stop = QtWidgets.QAction(MainWindow)
        self.action_port_stop.setObjectName("action_port_stop")
        self.action_sub_start = QtWidgets.QAction(MainWindow)
        self.action_sub_start.setObjectName("action_sub_start")
        self.action_vuln_expstart = QtWidgets.QAction(MainWindow)
        self.action_vuln_expstart.setObjectName("action_vuln_expstart")
        self.action_vuln_start = QtWidgets.QAction(MainWindow)
        self.action_vuln_start.setObjectName("action_vuln_start")
        self.action_vuln_stop = QtWidgets.QAction(MainWindow)
        self.action_vuln_stop.setObjectName("action_vuln_stop")
        self.action_update_start = QtWidgets.QAction(MainWindow)
        self.action_update_start.setObjectName("action_update_start")
        self.action_about_start = QtWidgets.QAction(MainWindow)
        self.action_about_start.setObjectName("action_about_start")
        self.action_ideas_start = QtWidgets.QAction(MainWindow)
        self.action_ideas_start.setObjectName("action_ideas_start")
        self.menu_5.addAction(self.action_vuln_reload)
        self.menu_5.addAction(self.action_vuln_showplubins)
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.exp_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FrameScan  by  qianxiao996"))
        self.pushButton_vuln_all.setText(_translate("MainWindow", "全  选"))
        self.pushButton_vuln_noall.setText(_translate("MainWindow", "反  选"))
        self.treeWidget_Plugins.headerItem().setText(0, _translate("MainWindow", "Plugins"))
        self.label_vuln_url.setText(_translate("MainWindow", " 目标："))
        self.pushButton_vuln_file.setText(_translate("MainWindow", "文件导入"))
        self.pushButton_vuln_start.setText(_translate("MainWindow", "开始扫描"))
        self.pushButton_vuln_expstart.setText(_translate("MainWindow", "一键利用"))
        self.tableWidget_vuln.setSortingEnabled(False)
        item = self.tableWidget_vuln.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "网页地址"))
        item = self.tableWidget_vuln.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "漏洞名称"))
        item = self.tableWidget_vuln.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "插件路径"))
        item = self.tableWidget_vuln.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "检测结果"))
        item = self.tableWidget_vuln.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Payload"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Scanner Log"))
        self.textEdit_log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Scanner Setting"))
        self.label_2.setText(_translate("MainWindow", "超时设置"))
        self.comboBox_timeout.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox_timeout.setItemText(1, _translate("MainWindow", "3"))
        self.comboBox_timeout.setItemText(2, _translate("MainWindow", "10"))
        self.comboBox_timeout.setItemText(3, _translate("MainWindow", "15"))
        self.comboBox_timeout.setItemText(4, _translate("MainWindow", "30"))
        self.label.setText(_translate("MainWindow", "线程数量"))
        self.threadsnum.setItemText(0, _translate("MainWindow", "3"))
        self.threadsnum.setItemText(1, _translate("MainWindow", "5"))
        self.threadsnum.setItemText(2, _translate("MainWindow", "10"))
        self.threadsnum.setItemText(3, _translate("MainWindow", "15"))
        self.vuln_scanner_debug.setText(_translate("MainWindow", "开启调试信息"))
        self.jump_url.setText(_translate("MainWindow", "检测地址存活"))
        self.jump_fofa.setText(_translate("MainWindow", "启用FOFA检测"))
        self.groupBox_4.setTitle(_translate("MainWindow", "headers"))
        self.vuln_scanner_textEdit_heads.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vuln_scanner), _translate("MainWindow", "漏洞扫描"))
        self.vuln_exp_textEdit_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">信息</p></body></html>"))
        self.exp_tabWidget.setTabText(self.exp_tabWidget.indexOf(self.tab), _translate("MainWindow", "信息"))
        self.label_14.setText(_translate("MainWindow", "CMD命令"))
        self.vuln_exp_input_cmd.setText(_translate("MainWindow", "whoami"))
        self.vuln_exp_button_cmd.setText(_translate("MainWindow", "执行命令"))
        self.textEdit_result.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">命令执行的结果将会显示在这里。</p></body></html>"))
        self.exp_tabWidget.setTabText(self.exp_tabWidget.indexOf(self.tab_2), _translate("MainWindow", "命令执行"))
        self.label_3.setText(_translate("MainWindow", "Exp Log"))
        self.vuln_exp_textEdit_log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "基本配置"))
        self.label_7.setText(_translate("MainWindow", "目标地址"))
        self.label_8.setText(_translate("MainWindow", "Cookie"))
        self.label_12.setText(_translate("MainWindow", "漏洞类型"))
        self.label_13.setText(_translate("MainWindow", "漏洞名称"))
        self.groupBox_2.setTitle(_translate("MainWindow", "反弹Shell"))
        self.label_4.setText(_translate("MainWindow", "IP地址:"))
        self.label_5.setText(_translate("MainWindow", "Port"))
        self.vuln_exp_button_shell.setText(_translate("MainWindow", "反弹shell"))
        self.groupBox_7.setTitle(_translate("MainWindow", "headers"))
        self.plainTextEdit_heads.setPlainText(_translate("MainWindow", "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vuln_exp), _translate("MainWindow", "漏洞利用"))
        self.menu_5.setTitle(_translate("MainWindow", "插件管理"))
        self.action_port_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_zhiwen_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_dir_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_dir_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_vuln_showplubins.setText(_translate("MainWindow", "查看插件信息"))
        self.action_vuln_reload.setText(_translate("MainWindow", "重新加载插件"))
        self.action_vuln_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_sub_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_port_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_vuln_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_sub_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_port_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_zhiwen_import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_zhiwen_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_ideas.setText(_translate("MainWindow", "意见反馈"))
        self.action_version.setText(_translate("MainWindow", "版本"))
        self.action_update.setText(_translate("MainWindow", "更新"))
        self.action_about.setText(_translate("MainWindow", "关于"))
        self.action_reload.setText(_translate("MainWindow", "重新加载插件"))
        self.action_dir_Import.setText(_translate("MainWindow", "导入扫描列表"))
        self.action_dir_export.setText(_translate("MainWindow", "导出扫描结果"))
        self.action_zhiwen_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_sub_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_port_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_sub_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_vuln_expstart.setText(_translate("MainWindow", "漏洞一键利用"))
        self.action_vuln_start.setText(_translate("MainWindow", "开始扫描"))
        self.action_vuln_stop.setText(_translate("MainWindow", "停止扫描"))
        self.action_update_start.setText(_translate("MainWindow", "更新"))
        self.action_about_start.setText(_translate("MainWindow", "关于"))
        self.action_ideas_start.setText(_translate("MainWindow", "意见反馈"))

