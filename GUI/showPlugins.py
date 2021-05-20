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
        Form.resize(1459, 821)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/main.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.show_Plugins_comboBox = QtWidgets.QComboBox(Form)
        self.show_Plugins_comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.show_Plugins_comboBox.setStyleSheet("")
        self.show_Plugins_comboBox.setEditable(True)
        self.show_Plugins_comboBox.setObjectName("show_Plugins_comboBox")
        self.show_Plugins_comboBox.addItem("")
        self.gridLayout.addWidget(self.show_Plugins_comboBox, 0, 0, 1, 1)
        self.show_Plugins = QtWidgets.QTableWidget(Form)
        self.show_Plugins.setMinimumSize(QtCore.QSize(200, 0))
        self.show_Plugins.setSizeIncrement(QtCore.QSize(0, 0))
        self.show_Plugins.setTabletTracking(False)
        self.show_Plugins.setToolTip("")
        self.show_Plugins.setStatusTip("")
        self.show_Plugins.setAutoFillBackground(False)
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
        self.show_Plugins.setShowGrid(True)
        self.show_Plugins.setGridStyle(QtCore.Qt.SolidLine)
        self.show_Plugins.setWordWrap(True)
        self.show_Plugins.setCornerButtonEnabled(True)
        self.show_Plugins.setObjectName("show_Plugins")
        self.show_Plugins.setColumnCount(9)
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
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(8, item)
        self.show_Plugins.horizontalHeader().setVisible(True)
        self.show_Plugins.horizontalHeader().setCascadingSectionResizes(True)
        self.show_Plugins.horizontalHeader().setDefaultSectionSize(200)
        self.show_Plugins.horizontalHeader().setHighlightSections(False)
        self.show_Plugins.horizontalHeader().setSortIndicatorShown(False)
        self.show_Plugins.horizontalHeader().setStretchLastSection(True)
        self.show_Plugins.verticalHeader().setVisible(False)
        self.show_Plugins.verticalHeader().setCascadingSectionResizes(False)
        self.show_Plugins.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout.addWidget(self.show_Plugins, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Show Plugins"))
        self.show_Plugins_comboBox.setItemText(0, _translate("Form", "ALL"))
        self.show_Plugins.setSortingEnabled(False)
        item = self.show_Plugins.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.show_Plugins.horizontalHeaderItem(1)
        item.setText(_translate("Form", "应用名称"))
        item = self.show_Plugins.horizontalHeaderItem(2)
        item.setText(_translate("Form", "漏洞名称"))
        item = self.show_Plugins.horizontalHeaderItem(3)
        item.setText(_translate("Form", "漏洞编号"))
        item = self.show_Plugins.horizontalHeaderItem(4)
        item.setText(_translate("Form", "漏洞来源"))
        item = self.show_Plugins.horizontalHeaderItem(5)
        item.setText(_translate("Form", "漏洞描述"))
        item = self.show_Plugins.horizontalHeaderItem(6)
        item.setText(_translate("Form", "插件路径"))
        item = self.show_Plugins.horizontalHeaderItem(7)
        item.setText(_translate("Form", "插件作者"))
        item = self.show_Plugins.horizontalHeaderItem(8)
        item.setText(_translate("Form", "修复建议"))

