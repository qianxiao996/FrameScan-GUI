# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1411, 888)
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u":/logo/main.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"")
        self.action_port_start = QAction(MainWindow)
        self.action_port_start.setObjectName(u"action_port_start")
        self.action_zhiwen_start = QAction(MainWindow)
        self.action_zhiwen_start.setObjectName(u"action_zhiwen_start")
        self.action_dir_stop = QAction(MainWindow)
        self.action_dir_stop.setObjectName(u"action_dir_stop")
        self.action_dir_start = QAction(MainWindow)
        self.action_dir_start.setObjectName(u"action_dir_start")
        self.action_vuln_showplubins = QAction(MainWindow)
        self.action_vuln_showplubins.setObjectName(u"action_vuln_showplubins")
        self.action_vuln_reload = QAction(MainWindow)
        self.action_vuln_reload.setObjectName(u"action_vuln_reload")
        self.action_vuln_reload.setCheckable(False)
        self.action_vuln_reload.setChecked(False)
        self.action_vuln_import = QAction(MainWindow)
        self.action_vuln_import.setObjectName(u"action_vuln_import")
        self.action_sub_import = QAction(MainWindow)
        self.action_sub_import.setObjectName(u"action_sub_import")
        self.action_port_import = QAction(MainWindow)
        self.action_port_import.setObjectName(u"action_port_import")
        self.action_vuln_export = QAction(MainWindow)
        self.action_vuln_export.setObjectName(u"action_vuln_export")
        self.action_sub_export = QAction(MainWindow)
        self.action_sub_export.setObjectName(u"action_sub_export")
        self.action_port_export = QAction(MainWindow)
        self.action_port_export.setObjectName(u"action_port_export")
        self.action_zhiwen_import = QAction(MainWindow)
        self.action_zhiwen_import.setObjectName(u"action_zhiwen_import")
        self.action_zhiwen_export = QAction(MainWindow)
        self.action_zhiwen_export.setObjectName(u"action_zhiwen_export")
        self.action_ideas = QAction(MainWindow)
        self.action_ideas.setObjectName(u"action_ideas")
        self.action_version = QAction(MainWindow)
        self.action_version.setObjectName(u"action_version")
        self.action_update = QAction(MainWindow)
        self.action_update.setObjectName(u"action_update")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_reload = QAction(MainWindow)
        self.action_reload.setObjectName(u"action_reload")
        self.action_dir_Import = QAction(MainWindow)
        self.action_dir_Import.setObjectName(u"action_dir_Import")
        self.action_dir_export = QAction(MainWindow)
        self.action_dir_export.setObjectName(u"action_dir_export")
        self.action_zhiwen_stop = QAction(MainWindow)
        self.action_zhiwen_stop.setObjectName(u"action_zhiwen_stop")
        self.action_sub_stop = QAction(MainWindow)
        self.action_sub_stop.setObjectName(u"action_sub_stop")
        self.action_port_stop = QAction(MainWindow)
        self.action_port_stop.setObjectName(u"action_port_stop")
        self.action_sub_start = QAction(MainWindow)
        self.action_sub_start.setObjectName(u"action_sub_start")
        self.action_vuln_expstart = QAction(MainWindow)
        self.action_vuln_expstart.setObjectName(u"action_vuln_expstart")
        self.action_vuln_start = QAction(MainWindow)
        self.action_vuln_start.setObjectName(u"action_vuln_start")
        self.action_vuln_stop = QAction(MainWindow)
        self.action_vuln_stop.setObjectName(u"action_vuln_stop")
        self.action_update_start = QAction(MainWindow)
        self.action_update_start.setObjectName(u"action_update_start")
        self.action_about_start = QAction(MainWindow)
        self.action_about_start.setObjectName(u"action_about_start")
        self.action_ideas_start = QAction(MainWindow)
        self.action_ideas_start.setObjectName(u"action_ideas_start")
        self.action_domain_reload = QAction(MainWindow)
        self.action_domain_reload.setObjectName(u"action_domain_reload")
        self.action_domain_showplubins = QAction(MainWindow)
        self.action_domain_showplubins.setObjectName(u"action_domain_showplubins")
        self.action_zhishiku = QAction(MainWindow)
        self.action_zhishiku.setObjectName(u"action_zhishiku")
        self.action_proxy = QAction(MainWindow)
        self.action_proxy.setObjectName(u"action_proxy")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_vuln_update = QAction(MainWindow)
        self.action_vuln_update.setObjectName(u"action_vuln_update")
        self.action_vuln_reload_update = QAction(MainWindow)
        self.action_vuln_reload_update.setObjectName(u"action_vuln_reload_update")
        self.action_about_ = QAction(MainWindow)
        self.action_about_.setObjectName(u"action_about_")
        self.action_update_ = QAction(MainWindow)
        self.action_update_.setObjectName(u"action_update_")
        self.action_fankui_ = QAction(MainWindow)
        self.action_fankui_.setObjectName(u"action_fankui_")
        self.action_mingliang = QAction(MainWindow)
        self.action_mingliang.setObjectName(u"action_mingliang")
        self.action_mingliang.setCheckable(True)
        self.action_mingliang.setChecked(False)
        self.action_anhei = QAction(MainWindow)
        self.action_anhei.setObjectName(u"action_anhei")
        self.action_anhei.setCheckable(True)
        self.action_default = QAction(MainWindow)
        self.action_default.setObjectName(u"action_default")
        self.action_default.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_50 = QGridLayout(self.centralwidget)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setHorizontalSpacing(7)
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(1411, 0))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.tabWidget.setFont(font1)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.vuln_scanner = QWidget()
        self.vuln_scanner.setObjectName(u"vuln_scanner")
        self.gridLayout_9 = QGridLayout(self.vuln_scanner)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_2 = QTabWidget(self.vuln_scanner)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMaximumSize(QSize(400, 16777215))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_12 = QGridLayout(self.tab_5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.plainTextEdit_vuln_url = QPlainTextEdit(self.tab_5)
        self.plainTextEdit_vuln_url.setObjectName(u"plainTextEdit_vuln_url")
        self.plainTextEdit_vuln_url.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_12.addWidget(self.plainTextEdit_vuln_url, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_11 = QGridLayout(self.tab_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_vuln_zhankai = QPushButton(self.tab_6)
        self.pushButton_vuln_zhankai.setObjectName(u"pushButton_vuln_zhankai")
        self.pushButton_vuln_zhankai.setMinimumSize(QSize(60, 28))

        self.horizontalLayout_2.addWidget(self.pushButton_vuln_zhankai)

        self.pushButton_vuln_zhedie = QPushButton(self.tab_6)
        self.pushButton_vuln_zhedie.setObjectName(u"pushButton_vuln_zhedie")
        self.pushButton_vuln_zhedie.setMinimumSize(QSize(60, 28))

        self.horizontalLayout_2.addWidget(self.pushButton_vuln_zhedie)

        self.pushButton_vuln_all = QPushButton(self.tab_6)
        self.pushButton_vuln_all.setObjectName(u"pushButton_vuln_all")
        self.pushButton_vuln_all.setMinimumSize(QSize(60, 28))
        self.pushButton_vuln_all.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.pushButton_vuln_all)

        self.pushButton_vuln_noall = QPushButton(self.tab_6)
        self.pushButton_vuln_noall.setObjectName(u"pushButton_vuln_noall")
        self.pushButton_vuln_noall.setMinimumSize(QSize(60, 28))
        self.pushButton_vuln_noall.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.pushButton_vuln_noall)


        self.gridLayout_10.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.treeWidget_Plugins = QTreeWidget(self.tab_6)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.treeWidget_Plugins.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_Plugins.setObjectName(u"treeWidget_Plugins")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.treeWidget_Plugins.sizePolicy().hasHeightForWidth())
        self.treeWidget_Plugins.setSizePolicy(sizePolicy1)
        self.treeWidget_Plugins.setMinimumSize(QSize(0, 0))
        self.treeWidget_Plugins.setMaximumSize(QSize(16777215, 16777215))
        self.treeWidget_Plugins.setStyleSheet(u"")
        self.treeWidget_Plugins.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.gridLayout_10.addWidget(self.treeWidget_Plugins, 1, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_6, "")

        self.verticalLayout.addWidget(self.tabWidget_2)


        self.gridLayout_9.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.vuln_scanner)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comboBox_timeout = QComboBox(self.vuln_scanner)
        self.comboBox_timeout.addItem("")
        self.comboBox_timeout.addItem("")
        self.comboBox_timeout.addItem("")
        self.comboBox_timeout.setObjectName(u"comboBox_timeout")
        self.comboBox_timeout.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.comboBox_timeout)

        self.label = QLabel(self.vuln_scanner)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.label)

        self.threadsnum = QComboBox(self.vuln_scanner)
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.threadsnum.addItem("")
        self.threadsnum.setObjectName(u"threadsnum")
        self.threadsnum.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.threadsnum)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.jump_fofa = QCheckBox(self.vuln_scanner)
        self.jump_fofa.setObjectName(u"jump_fofa")
        self.jump_fofa.setMinimumSize(QSize(131, 0))
        self.jump_fofa.setCheckable(True)
        self.jump_fofa.setChecked(True)

        self.horizontalLayout.addWidget(self.jump_fofa)

        self.vuln_scanner_debug = QCheckBox(self.vuln_scanner)
        self.vuln_scanner_debug.setObjectName(u"vuln_scanner_debug")
        self.vuln_scanner_debug.setMinimumSize(QSize(118, 0))
        self.vuln_scanner_debug.setCheckable(True)
        self.vuln_scanner_debug.setChecked(False)

        self.horizontalLayout.addWidget(self.vuln_scanner_debug)

        self.jump_url = QCheckBox(self.vuln_scanner)
        self.jump_url.setObjectName(u"jump_url")
        self.jump_url.setMinimumSize(QSize(131, 0))
        self.jump_url.setCheckable(True)
        self.jump_url.setChecked(False)

        self.horizontalLayout.addWidget(self.jump_url)

        self.pushButton_vuln_start = QPushButton(self.vuln_scanner)
        self.pushButton_vuln_start.setObjectName(u"pushButton_vuln_start")
        self.pushButton_vuln_start.setMinimumSize(QSize(80, 28))
        self.pushButton_vuln_start.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButton_vuln_start)

        self.pushButton_vuln_stop = QPushButton(self.vuln_scanner)
        self.pushButton_vuln_stop.setObjectName(u"pushButton_vuln_stop")
        self.pushButton_vuln_stop.setEnabled(False)

        self.horizontalLayout.addWidget(self.pushButton_vuln_stop)

        self.pushButton_vuln_expstart = QPushButton(self.vuln_scanner)
        self.pushButton_vuln_expstart.setObjectName(u"pushButton_vuln_expstart")
        self.pushButton_vuln_expstart.setMinimumSize(QSize(80, 28))

        self.horizontalLayout.addWidget(self.pushButton_vuln_expstart)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableWidget_vuln = QTableWidget(self.vuln_scanner)
        if (self.tableWidget_vuln.columnCount() < 5):
            self.tableWidget_vuln.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_vuln.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_vuln.setObjectName(u"tableWidget_vuln")
        self.tableWidget_vuln.setMinimumSize(QSize(1061, 0))
        self.tableWidget_vuln.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_vuln.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_vuln.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget_vuln.setAlternatingRowColors(False)
        self.tableWidget_vuln.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_vuln.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_vuln.setTextElideMode(Qt.ElideRight)
        self.tableWidget_vuln.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_vuln.setShowGrid(True)
        self.tableWidget_vuln.setGridStyle(Qt.SolidLine)
        self.tableWidget_vuln.setSortingEnabled(True)
        self.tableWidget_vuln.setWordWrap(True)
        self.tableWidget_vuln.horizontalHeader().setDefaultSectionSize(210)
        self.tableWidget_vuln.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_vuln.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableWidget_vuln)

        self.tabWidget_9 = QTabWidget(self.vuln_scanner)
        self.tabWidget_9.setObjectName(u"tabWidget_9")
        self.tabWidget_9.setMaximumSize(QSize(16777215, 200))
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_8 = QGridLayout(self.tab_14)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.textEdit_log = QTextEdit(self.tab_14)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setMinimumSize(QSize(600, 0))
        self.textEdit_log.setMaximumSize(QSize(16777215, 200))
        self.textEdit_log.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.textEdit_log, 0, 0, 1, 1)

        self.tabWidget_9.addTab(self.tab_14, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout = QGridLayout(self.tab_15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vuln_scanner_textEdit_heads = QTextEdit(self.tab_15)
        self.vuln_scanner_textEdit_heads.setObjectName(u"vuln_scanner_textEdit_heads")
        self.vuln_scanner_textEdit_heads.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.vuln_scanner_textEdit_heads, 0, 0, 1, 1)

        self.tabWidget_9.addTab(self.tab_15, "")

        self.verticalLayout_2.addWidget(self.tabWidget_9)


        self.gridLayout_9.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.tabWidget.addTab(self.vuln_scanner, "")
        self.vuln_exp = QWidget()
        self.vuln_exp.setObjectName(u"vuln_exp")
        self.gridLayout_6 = QGridLayout(self.vuln_exp)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.vuln_exp)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(800, 16777215))
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(70, 20))
        self.label_7.setMaximumSize(QSize(70, 20))

        self.horizontalLayout_7.addWidget(self.label_7)

        self.vuln_lineEdit_url = QLineEdit(self.groupBox)
        self.vuln_lineEdit_url.setObjectName(u"vuln_lineEdit_url")
        self.vuln_lineEdit_url.setMinimumSize(QSize(0, 28))
        self.vuln_lineEdit_url.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.vuln_lineEdit_url)


        self.gridLayout_7.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(60, 0))
        self.label_12.setMaximumSize(QSize(70, 20))

        self.horizontalLayout_5.addWidget(self.label_12)

        self.vuln_type = QComboBox(self.groupBox)
        self.vuln_type.setObjectName(u"vuln_type")
        self.vuln_type.setMinimumSize(QSize(0, 30))
        self.vuln_type.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.vuln_type)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(60, 0))
        self.label_13.setMaximumSize(QSize(70, 16777215))
        self.label_13.setLayoutDirection(Qt.LeftToRight)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_13)

        self.vuln_name = QComboBox(self.groupBox)
        self.vuln_name.setObjectName(u"vuln_name")
        self.vuln_name.setMinimumSize(QSize(0, 30))
        self.vuln_name.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.vuln_name)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)


        self.gridLayout_7.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.vuln_exp)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(800, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 28))
        self.label_4.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_10.addWidget(self.label_4)

        self.vuln_exp_input_ip = QLineEdit(self.groupBox_2)
        self.vuln_exp_input_ip.setObjectName(u"vuln_exp_input_ip")
        self.vuln_exp_input_ip.setMinimumSize(QSize(200, 28))
        self.vuln_exp_input_ip.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.vuln_exp_input_ip)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(35, 28))
        self.label_5.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout_10.addWidget(self.label_5)

        self.vuln_exp_input_port = QLineEdit(self.groupBox_2)
        self.vuln_exp_input_port.setObjectName(u"vuln_exp_input_port")
        self.vuln_exp_input_port.setMinimumSize(QSize(50, 28))
        self.vuln_exp_input_port.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_10.addWidget(self.vuln_exp_input_port)

        self.vuln_exp_button_shell = QPushButton(self.groupBox_2)
        self.vuln_exp_button_shell.setObjectName(u"vuln_exp_button_shell")
        self.vuln_exp_button_shell.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.vuln_exp_button_shell)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)


        self.verticalLayout_5.addWidget(self.groupBox_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_5)

        self.groupBox_7 = QGroupBox(self.vuln_exp)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(0, 150))
        self.groupBox_7.setMaximumSize(QSize(16777215, 230))
        self.gridLayout_3 = QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plainTextEdit_heads = QPlainTextEdit(self.groupBox_7)
        self.plainTextEdit_heads.setObjectName(u"plainTextEdit_heads")

        self.gridLayout_3.addWidget(self.plainTextEdit_heads, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.groupBox_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.exp_tabWidget = QTabWidget(self.vuln_exp)
        self.exp_tabWidget.setObjectName(u"exp_tabWidget")
        self.exp_tabWidget.setMinimumSize(QSize(0, 550))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(7)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.vuln_exp_textEdit_info = QTextEdit(self.tab)
        self.vuln_exp_textEdit_info.setObjectName(u"vuln_exp_textEdit_info")
        self.vuln_exp_textEdit_info.setMinimumSize(QSize(950, 0))

        self.gridLayout_5.addWidget(self.vuln_exp_textEdit_info, 0, 0, 1, 1)

        self.exp_tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(55, 28))
        self.label_14.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_19.addWidget(self.label_14)

        self.vuln_exp_input_cmd = QLineEdit(self.tab_2)
        self.vuln_exp_input_cmd.setObjectName(u"vuln_exp_input_cmd")
        self.vuln_exp_input_cmd.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_19.addWidget(self.vuln_exp_input_cmd)

        self.vuln_exp_button_cmd = QPushButton(self.tab_2)
        self.vuln_exp_button_cmd.setObjectName(u"vuln_exp_button_cmd")
        self.vuln_exp_button_cmd.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_19.addWidget(self.vuln_exp_button_cmd)

        self.vuln_exp_button_clear = QPushButton(self.tab_2)
        self.vuln_exp_button_clear.setObjectName(u"vuln_exp_button_clear")

        self.horizontalLayout_19.addWidget(self.vuln_exp_button_clear)


        self.gridLayout_2.addLayout(self.horizontalLayout_19, 0, 0, 1, 1)

        self.textEdit_result = QTextEdit(self.tab_2)
        self.textEdit_result.setObjectName(u"textEdit_result")

        self.gridLayout_2.addWidget(self.textEdit_result, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.exp_tabWidget.addTab(self.tab_2, "")
        self.tab_33 = QWidget()
        self.tab_33.setObjectName(u"tab_33")
        self.gridLayout_82 = QGridLayout(self.tab_33)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_37 = QLabel(self.tab_33)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_50.addWidget(self.label_37)

        self.vuln_exp_lineEdit_filename = QLineEdit(self.tab_33)
        self.vuln_exp_lineEdit_filename.setObjectName(u"vuln_exp_lineEdit_filename")

        self.horizontalLayout_50.addWidget(self.vuln_exp_lineEdit_filename)

        self.label_35 = QLabel(self.tab_33)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_50.addWidget(self.label_35)

        self.vuln_exp_comboBox_shell = QComboBox(self.tab_33)
        self.vuln_exp_comboBox_shell.setObjectName(u"vuln_exp_comboBox_shell")
        self.vuln_exp_comboBox_shell.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_50.addWidget(self.vuln_exp_comboBox_shell)

        self.vuln_exp_button_getfile = QPushButton(self.tab_33)
        self.vuln_exp_button_getfile.setObjectName(u"vuln_exp_button_getfile")

        self.horizontalLayout_50.addWidget(self.vuln_exp_button_getfile)

        self.vuln_exp_button_uploadfile = QPushButton(self.tab_33)
        self.vuln_exp_button_uploadfile.setObjectName(u"vuln_exp_button_uploadfile")

        self.horizontalLayout_50.addWidget(self.vuln_exp_button_uploadfile)

        self.vuln_exp_button_clear_shell = QPushButton(self.tab_33)
        self.vuln_exp_button_clear_shell.setObjectName(u"vuln_exp_button_clear_shell")

        self.horizontalLayout_50.addWidget(self.vuln_exp_button_clear_shell)


        self.verticalLayout_40.addLayout(self.horizontalLayout_50)

        self.label_36 = QLabel(self.tab_33)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_40.addWidget(self.label_36)

        self.vuln_exp_textEdit_shell = QTextEdit(self.tab_33)
        self.vuln_exp_textEdit_shell.setObjectName(u"vuln_exp_textEdit_shell")

        self.verticalLayout_40.addWidget(self.vuln_exp_textEdit_shell)


        self.gridLayout_82.addLayout(self.verticalLayout_40, 0, 0, 1, 1)

        self.exp_tabWidget.addTab(self.tab_33, "")

        self.horizontalLayout_11.addWidget(self.exp_tabWidget)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.vuln_exp)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.vuln_exp_debug = QCheckBox(self.vuln_exp)
        self.vuln_exp_debug.setObjectName(u"vuln_exp_debug")
        self.vuln_exp_debug.setMinimumSize(QSize(60, 0))
        self.vuln_exp_debug.setMaximumSize(QSize(120, 16777215))
        self.vuln_exp_debug.setCheckable(True)
        self.vuln_exp_debug.setChecked(False)

        self.horizontalLayout_9.addWidget(self.vuln_exp_debug)

        self.pushButtovuln_exp_clearlog = QPushButton(self.vuln_exp)
        self.pushButtovuln_exp_clearlog.setObjectName(u"pushButtovuln_exp_clearlog")
        self.pushButtovuln_exp_clearlog.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_9.addWidget(self.pushButtovuln_exp_clearlog)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.vuln_exp_textEdit_log = QTextEdit(self.vuln_exp)
        self.vuln_exp_textEdit_log.setObjectName(u"vuln_exp_textEdit_log")
        self.vuln_exp_textEdit_log.setMinimumSize(QSize(430, 0))
        self.vuln_exp_textEdit_log.setMaximumSize(QSize(400, 16777215))

        self.verticalLayout_7.addWidget(self.vuln_exp_textEdit_log)


        self.horizontalLayout_11.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.gridLayout_6.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.vuln_exp, "")
        self.tab_32 = QWidget()
        self.tab_32.setObjectName(u"tab_32")
        self.gridLayout_78 = QGridLayout(self.tab_32)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.textBrowser_log_log = QTextBrowser(self.tab_32)
        self.textBrowser_log_log.setObjectName(u"textBrowser_log_log")

        self.gridLayout_78.addWidget(self.textBrowser_log_log, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_32, "")

        self.gridLayout_50.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1411, 22))
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.pushButton_vuln_all, self.pushButton_vuln_noall)
        QWidget.setTabOrder(self.pushButton_vuln_noall, self.treeWidget_Plugins)
        QWidget.setTabOrder(self.treeWidget_Plugins, self.comboBox_timeout)
        QWidget.setTabOrder(self.comboBox_timeout, self.jump_url)
        QWidget.setTabOrder(self.jump_url, self.threadsnum)
        QWidget.setTabOrder(self.threadsnum, self.vuln_scanner_debug)
        QWidget.setTabOrder(self.vuln_scanner_debug, self.pushButton_vuln_stop)
        QWidget.setTabOrder(self.pushButton_vuln_stop, self.pushButton_vuln_expstart)
        QWidget.setTabOrder(self.pushButton_vuln_expstart, self.tabWidget_9)
        QWidget.setTabOrder(self.tabWidget_9, self.textEdit_log)
        QWidget.setTabOrder(self.textEdit_log, self.vuln_scanner_textEdit_heads)
        QWidget.setTabOrder(self.vuln_scanner_textEdit_heads, self.vuln_lineEdit_url)
        QWidget.setTabOrder(self.vuln_lineEdit_url, self.vuln_type)
        QWidget.setTabOrder(self.vuln_type, self.vuln_name)
        QWidget.setTabOrder(self.vuln_name, self.vuln_exp_input_ip)
        QWidget.setTabOrder(self.vuln_exp_input_ip, self.vuln_exp_input_port)
        QWidget.setTabOrder(self.vuln_exp_input_port, self.vuln_exp_button_shell)
        QWidget.setTabOrder(self.vuln_exp_button_shell, self.plainTextEdit_heads)
        QWidget.setTabOrder(self.plainTextEdit_heads, self.exp_tabWidget)
        QWidget.setTabOrder(self.exp_tabWidget, self.vuln_exp_textEdit_info)
        QWidget.setTabOrder(self.vuln_exp_textEdit_info, self.vuln_exp_input_cmd)
        QWidget.setTabOrder(self.vuln_exp_input_cmd, self.vuln_exp_button_cmd)
        QWidget.setTabOrder(self.vuln_exp_button_cmd, self.textEdit_result)
        QWidget.setTabOrder(self.textEdit_result, self.vuln_exp_lineEdit_filename)
        QWidget.setTabOrder(self.vuln_exp_lineEdit_filename, self.vuln_exp_comboBox_shell)
        QWidget.setTabOrder(self.vuln_exp_comboBox_shell, self.vuln_exp_button_getfile)
        QWidget.setTabOrder(self.vuln_exp_button_getfile, self.vuln_exp_button_uploadfile)
        QWidget.setTabOrder(self.vuln_exp_button_uploadfile, self.vuln_exp_button_clear_shell)
        QWidget.setTabOrder(self.vuln_exp_button_clear_shell, self.vuln_exp_textEdit_shell)
        QWidget.setTabOrder(self.vuln_exp_textEdit_shell, self.vuln_exp_debug)
        QWidget.setTabOrder(self.vuln_exp_debug, self.pushButtovuln_exp_clearlog)
        QWidget.setTabOrder(self.pushButtovuln_exp_clearlog, self.vuln_exp_textEdit_log)
        QWidget.setTabOrder(self.vuln_exp_textEdit_log, self.textBrowser_log_log)

        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu_5.addAction(self.action_vuln_reload)
        self.menu_5.addAction(self.action_vuln_reload_update)
        self.menu_5.addAction(self.action_vuln_update)
        self.menu_5.addAction(self.action_vuln_showplubins)
        self.menu.addAction(self.action_proxy)
        self.menu_3.addAction(self.action_about_)
        self.menu_3.addAction(self.action_update_)
        self.menu_3.addAction(self.action_fankui_)

        self.retranslateUi(MainWindow)
        self.pushButtovuln_exp_clearlog.clicked.connect(self.vuln_exp_textEdit_log.clear)
        self.vuln_exp_button_clear.clicked.connect(self.textEdit_result.clear)
        self.vuln_exp_button_clear_shell.clicked.connect(self.vuln_exp_textEdit_shell.clear)
        self.pushButton_vuln_zhankai.clicked.connect(self.treeWidget_Plugins.expandAll)
        self.pushButton_vuln_zhedie.clicked.connect(self.treeWidget_Plugins.collapseAll)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_9.setCurrentIndex(0)
        self.exp_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FrameScan-GUI by  qianxiao996", None))
        self.action_port_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u626b\u63cf", None))
        self.action_zhiwen_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u626b\u63cf", None))
        self.action_dir_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u626b\u63cf", None))
        self.action_dir_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u626b\u63cf", None))
        self.action_vuln_showplubins.setText(QCoreApplication.translate("MainWindow", u"\u63d2\u4ef6\u7ba1\u7406", None))
        self.action_vuln_reload.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u52a0\u8f7d(\u672c\u5730)", None))
#if QT_CONFIG(statustip)
        self.action_vuln_reload.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.action_vuln_import.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u626b\u63cf\u5217\u8868", None))
        self.action_sub_import.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u626b\u63cf\u5217\u8868", None))
        self.action_port_import.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u626b\u63cf\u5217\u8868", None))
        self.action_vuln_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u626b\u63cf\u7ed3\u679c", None))
        self.action_sub_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u626b\u63cf\u7ed3\u679c", None))
        self.action_port_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u626b\u63cf\u7ed3\u679c", None))
        self.action_zhiwen_import.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u626b\u63cf\u5217\u8868", None))
        self.action_zhiwen_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u626b\u63cf\u7ed3\u679c", None))
        self.action_ideas.setText(QCoreApplication.translate("MainWindow", u"\u610f\u89c1\u53cd\u9988", None))
        self.action_version.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c", None))
        self.action_update.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_reload.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u52a0\u8f7d\u63d2\u4ef6", None))
        self.action_dir_Import.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u626b\u63cf\u5217\u8868", None))
        self.action_dir_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u626b\u63cf\u7ed3\u679c", None))
        self.action_zhiwen_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u626b\u63cf", None))
        self.action_sub_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u626b\u63cf", None))
        self.action_port_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u626b\u63cf", None))
        self.action_sub_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u626b\u63cf", None))
        self.action_vuln_expstart.setText(QCoreApplication.translate("MainWindow", u"\u6f0f\u6d1e\u4e00\u952e\u5229\u7528", None))
        self.action_vuln_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u626b\u63cf", None))
        self.action_vuln_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u626b\u63cf", None))
        self.action_update_start.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.action_about_start.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_ideas_start.setText(QCoreApplication.translate("MainWindow", u"\u610f\u89c1\u53cd\u9988", None))
        self.action_domain_reload.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u52a0\u8f7d", None))
        self.action_domain_showplubins.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u63d2\u4ef6", None))
        self.action_zhishiku.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u5168\u77e5\u8bc6\u5e93", None))
        self.action_proxy.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u8bbe\u7f6e", None))
        self.action_vuln_update.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u8bbe\u7f6e", None))
        self.action_vuln_reload_update.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0(\u7f51\u7edc)", None))
        self.action_about_.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u8f6f\u4ef6", None))
        self.action_update_.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.action_fankui_.setText(QCoreApplication.translate("MainWindow", u"\u610f\u89c1\u53cd\u9988", None))
        self.action_mingliang.setText(QCoreApplication.translate("MainWindow", u"\u660e\u4eae\u98ce\u683c", None))
        self.action_anhei.setText(QCoreApplication.translate("MainWindow", u"\u6697\u9ed1\u98ce\u683c", None))
        self.action_default.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u98ce\u683c", None))
        self.plainTextEdit_vuln_url.setPlainText("")
        self.plainTextEdit_vuln_url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684url", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u76ee\u6807", None))
        self.pushButton_vuln_zhankai.setText(QCoreApplication.translate("MainWindow", u"\u5c55\u5f00", None))
        self.pushButton_vuln_zhedie.setText(QCoreApplication.translate("MainWindow", u"\u6298\u53e0", None))
        self.pushButton_vuln_all.setText(QCoreApplication.translate("MainWindow", u"\u5168  \u9009", None))
        self.pushButton_vuln_noall.setText(QCoreApplication.translate("MainWindow", u"\u53cd  \u9009", None))
        ___qtreewidgetitem = self.treeWidget_Plugins.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Plugins", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u63d2\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u65f6", None))
        self.comboBox_timeout.setItemText(0, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox_timeout.setItemText(1, QCoreApplication.translate("MainWindow", u"60", None))
        self.comboBox_timeout.setItemText(2, QCoreApplication.translate("MainWindow", u"100", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u7a0b", None))
        self.threadsnum.setItemText(0, QCoreApplication.translate("MainWindow", u"3", None))
        self.threadsnum.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.threadsnum.setItemText(2, QCoreApplication.translate("MainWindow", u"10", None))
        self.threadsnum.setItemText(3, QCoreApplication.translate("MainWindow", u"15", None))

        self.jump_fofa.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528FOFA\u68c0\u6d4b", None))
        self.vuln_scanner_debug.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793aDebug\u4fe1\u606f", None))
        self.jump_url.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u5730\u5740\u5b58\u6d3b", None))
        self.pushButton_vuln_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u626b\u63cf", None))
        self.pushButton_vuln_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u626b\u63cf", None))
        self.pushButton_vuln_expstart.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u5229\u7528", None))
        ___qtablewidgetitem = self.tableWidget_vuln.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u9875\u5730\u5740", None));
        ___qtablewidgetitem1 = self.tableWidget_vuln.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6f0f\u6d1e\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget_vuln.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u63d2\u4ef6\u8def\u5f84", None));
        ___qtablewidgetitem3 = self.tableWidget_vuln.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None));
        ___qtablewidgetitem4 = self.tableWidget_vuln.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u4fe1\u606f", None));
        self.textEdit_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun';\"><br /></p></body></html>", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Scanner log", None))
        self.vuln_scanner_textEdit_heads.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun';\">User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36</span></p></body></html>", None))
        self.vuln_scanner_textEdit_heads.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6362\u884c\u5206\u5272", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Headers\u5934", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vuln_scanner), QCoreApplication.translate("MainWindow", u"\u6f0f\u6d1e\u626b\u63cf", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u914d\u7f6e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u5730\u5740", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6f0f\u6d1e\u7c7b\u578b", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6f0f\u6d1e\u540d\u79f0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u53cd\u5f39Shell", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"IP\u5730\u5740:", None))
        self.vuln_exp_input_ip.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.vuln_exp_input_port.setText("")
        self.vuln_exp_button_shell.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u5f39shell", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Headers", None))
        self.plainTextEdit_heads.setPlainText(QCoreApplication.translate("MainWindow", u"User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36", None))
        self.vuln_exp_textEdit_info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun';\">\u4fe1\u606f</span></p></body></html>", None))
        self.exp_tabWidget.setTabText(self.exp_tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u4fe1\u606f", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CMD\u547d\u4ee4", None))
        self.vuln_exp_input_cmd.setText(QCoreApplication.translate("MainWindow", u"whoami", None))
        self.vuln_exp_button_cmd.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c\u547d\u4ee4", None))
        self.vuln_exp_button_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u7ed3\u679c", None))
        self.textEdit_result.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun';\"><br /></p></body></html>", None))
        self.textEdit_result.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u6267\u884c\u7684\u7ed3\u679c\u5c06\u4f1a\u663e\u793a\u5728\u8fd9\u91cc\u3002", None))
        self.exp_tabWidget.setTabText(self.exp_tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u6267\u884c", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165\u6587\u4ef6\u540d", None))
        self.vuln_exp_lineEdit_filename.setText(QCoreApplication.translate("MainWindow", u"996.php", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"shell\u6587\u4ef6", None))
        self.vuln_exp_button_getfile.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.vuln_exp_button_uploadfile.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u6587\u4ef6", None))
        self.vuln_exp_button_clear_shell.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u5185\u5bb9", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5185\u5bb9", None))
        self.exp_tabWidget.setTabText(self.exp_tabWidget.indexOf(self.tab_33), QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4e0a\u4f20", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Exp Logs", None))
        self.vuln_exp_debug.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793aDebug\u4fe1\u606f", None))
        self.pushButtovuln_exp_clearlog.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u65e5\u5fd7", None))
        self.vuln_exp_textEdit_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun';\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vuln_exp), QCoreApplication.translate("MainWindow", u"\u6f0f\u6d1e\u5229\u7528", None))
        self.textBrowser_log_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun';\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_32), QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u65e5\u5fd7", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u63d2\u4ef6\u7ba1\u7406", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
    # retranslateUi

