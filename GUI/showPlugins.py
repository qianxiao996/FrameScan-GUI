# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showPlugins.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1452, 821)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/main.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("        background: rgb(255, 255, 255)")
        self.show_Plugins = QtWidgets.QTableWidget(Form)
        self.show_Plugins.setGeometry(QtCore.QRect(-1, 20, 1461, 801))
        self.show_Plugins.setMinimumSize(QtCore.QSize(200, 0))
        self.show_Plugins.setSizeIncrement(QtCore.QSize(0, 0))
        self.show_Plugins.setTabletTracking(False)
        self.show_Plugins.setStyleSheet("\n"
"/**********表头**********/\n"
"QHeaderView{\n"
"        border: none;\n"
"        background:  rgb(240, 240, 240);\n"
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
        self.show_Plugins.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.show_Plugins.setObjectName("show_Plugins")
        self.show_Plugins.setColumnCount(5)
        self.show_Plugins.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(4, item)
        self.show_Plugins.horizontalHeader().setVisible(True)
        self.show_Plugins.horizontalHeader().setCascadingSectionResizes(True)
        self.show_Plugins.horizontalHeader().setDefaultSectionSize(291)
        self.show_Plugins.horizontalHeader().setHighlightSections(False)
        self.show_Plugins.horizontalHeader().setSortIndicatorShown(False)
        self.show_Plugins.horizontalHeader().setStretchLastSection(True)
        self.show_Plugins.verticalHeader().setVisible(True)
        self.show_Plugins.verticalHeader().setCascadingSectionResizes(False)
        self.show_Plugins.verticalHeader().setSortIndicatorShown(False)
        self.show_Plugins_comboBox = QtWidgets.QComboBox(Form)
        self.show_Plugins_comboBox.setGeometry(QtCore.QRect(0, 0, 161, 21))
        self.show_Plugins_comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.show_Plugins_comboBox.setStyleSheet("QComboBox {\n"
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
        self.show_Plugins_comboBox.setObjectName("show_Plugins_comboBox")
        self.show_Plugins_comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Show Plugins"))
        item = self.show_Plugins.horizontalHeaderItem(0)
        item.setText(_translate("Form", "CMS_NAME"))
        item = self.show_Plugins.horizontalHeaderItem(1)
        item.setText(_translate("Form", "POC_NAME"))
        item = self.show_Plugins.horizontalHeaderItem(2)
        item.setText(_translate("Form", "POC_REFERER"))
        item = self.show_Plugins.horizontalHeaderItem(3)
        item.setText(_translate("Form", "POC_DESCRIPTION"))
        item = self.show_Plugins.horizontalHeaderItem(4)
        item.setText(_translate("Form", "FILE_NAME"))
        self.show_Plugins_comboBox.setItemText(0, _translate("Form", "ALL"))

