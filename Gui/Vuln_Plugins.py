# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vuln_Plugins.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Vuln(object):
    def setupUi(self, Form_Vuln):
        Form_Vuln.setObjectName("Form_Vuln")
        Form_Vuln.resize(1459, 821)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_Vuln.setWindowIcon(icon)
        Form_Vuln.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form_Vuln.setAutoFillBackground(False)
        Form_Vuln.setStyleSheet("")
        Form_Vuln.setInputMethodHints(QtCore.Qt.ImhNone)
        self.gridLayout = QtWidgets.QGridLayout(Form_Vuln)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form_Vuln)
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.show_Plugins_comboBox_cms_name = QtWidgets.QComboBox(Form_Vuln)
        self.show_Plugins_comboBox_cms_name.setMinimumSize(QtCore.QSize(150, 0))
        self.show_Plugins_comboBox_cms_name.setStyleSheet("")
        self.show_Plugins_comboBox_cms_name.setEditable(True)
        self.show_Plugins_comboBox_cms_name.setObjectName("show_Plugins_comboBox_cms_name")
        self.show_Plugins_comboBox_cms_name.addItem("")
        self.horizontalLayout.addWidget(self.show_Plugins_comboBox_cms_name)
        self.label_2 = QtWidgets.QLabel(Form_Vuln)
        self.label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.show_Plugins_comboBox_vuln_class = QtWidgets.QComboBox(Form_Vuln)
        self.show_Plugins_comboBox_vuln_class.setMinimumSize(QtCore.QSize(150, 0))
        self.show_Plugins_comboBox_vuln_class.setStyleSheet("")
        self.show_Plugins_comboBox_vuln_class.setEditable(True)
        self.show_Plugins_comboBox_vuln_class.setObjectName("show_Plugins_comboBox_vuln_class")
        self.show_Plugins_comboBox_vuln_class.addItem("")
        self.horizontalLayout.addWidget(self.show_Plugins_comboBox_vuln_class)
        self.pushButton_show_Plugins_search = QtWidgets.QPushButton(Form_Vuln)
        self.pushButton_show_Plugins_search.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_show_Plugins_search.setObjectName("pushButton_show_Plugins_search")
        self.horizontalLayout.addWidget(self.pushButton_show_Plugins_search)
        self.pushButton_show_Plugins_add = QtWidgets.QPushButton(Form_Vuln)
        self.pushButton_show_Plugins_add.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_show_Plugins_add.setObjectName("pushButton_show_Plugins_add")
        self.horizontalLayout.addWidget(self.pushButton_show_Plugins_add)
        self.pushButton_show_Plugins_delete = QtWidgets.QPushButton(Form_Vuln)
        self.pushButton_show_Plugins_delete.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_show_Plugins_delete.setObjectName("pushButton_show_Plugins_delete")
        self.horizontalLayout.addWidget(self.pushButton_show_Plugins_delete)
        self.pushButton_show_Plugins_edit = QtWidgets.QPushButton(Form_Vuln)
        self.pushButton_show_Plugins_edit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_show_Plugins_edit.setObjectName("pushButton_show_Plugins_edit")
        self.horizontalLayout.addWidget(self.pushButton_show_Plugins_edit)
        self.pushButton_show_Plugins_reload = QtWidgets.QPushButton(Form_Vuln)
        self.pushButton_show_Plugins_reload.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_show_Plugins_reload.setObjectName("pushButton_show_Plugins_reload")
        self.horizontalLayout.addWidget(self.pushButton_show_Plugins_reload)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.show_Plugins = QtWidgets.QTableWidget(Form_Vuln)
        self.show_Plugins.setMinimumSize(QtCore.QSize(200, 0))
        self.show_Plugins.setSizeIncrement(QtCore.QSize(0, 0))
        self.show_Plugins.setTabletTracking(False)
        self.show_Plugins.setToolTip("")
        self.show_Plugins.setStatusTip("")
        self.show_Plugins.setAutoFillBackground(False)
        self.show_Plugins.setStyleSheet("")
        self.show_Plugins.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.show_Plugins.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.show_Plugins.setShowGrid(True)
        self.show_Plugins.setGridStyle(QtCore.Qt.SolidLine)
        self.show_Plugins.setWordWrap(True)
        self.show_Plugins.setCornerButtonEnabled(True)
        self.show_Plugins.setObjectName("show_Plugins")
        self.show_Plugins.setColumnCount(10)
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
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(9, item)
        self.show_Plugins.horizontalHeader().setVisible(True)
        self.show_Plugins.horizontalHeader().setCascadingSectionResizes(True)
        self.show_Plugins.horizontalHeader().setDefaultSectionSize(200)
        self.show_Plugins.horizontalHeader().setHighlightSections(False)
        self.show_Plugins.horizontalHeader().setSortIndicatorShown(True)
        self.show_Plugins.horizontalHeader().setStretchLastSection(True)
        self.show_Plugins.verticalHeader().setVisible(False)
        self.show_Plugins.verticalHeader().setCascadingSectionResizes(False)
        self.show_Plugins.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout.addWidget(self.show_Plugins)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form_Vuln)
        QtCore.QMetaObject.connectSlotsByName(Form_Vuln)

    def retranslateUi(self, Form_Vuln):
        _translate = QtCore.QCoreApplication.translate
        Form_Vuln.setWindowTitle(_translate("Form_Vuln", "漏洞插件"))
        self.label.setText(_translate("Form_Vuln", "应用名称"))
        self.show_Plugins_comboBox_cms_name.setItemText(0, _translate("Form_Vuln", "ALL"))
        self.label_2.setText(_translate("Form_Vuln", "漏洞类型"))
        self.show_Plugins_comboBox_vuln_class.setItemText(0, _translate("Form_Vuln", "ALL"))
        self.pushButton_show_Plugins_search.setText(_translate("Form_Vuln", "搜索插件"))
        self.pushButton_show_Plugins_add.setText(_translate("Form_Vuln", "新增插件"))
        self.pushButton_show_Plugins_delete.setText(_translate("Form_Vuln", "删除插件"))
        self.pushButton_show_Plugins_edit.setText(_translate("Form_Vuln", "编辑插件"))
        self.pushButton_show_Plugins_reload.setText(_translate("Form_Vuln", "重新加载"))
        self.show_Plugins.setSortingEnabled(True)
        item = self.show_Plugins.horizontalHeaderItem(0)
        item.setText(_translate("Form_Vuln", "ID"))
        item = self.show_Plugins.horizontalHeaderItem(1)
        item.setText(_translate("Form_Vuln", "应用名称"))
        item = self.show_Plugins.horizontalHeaderItem(2)
        item.setText(_translate("Form_Vuln", "漏洞名称"))
        item = self.show_Plugins.horizontalHeaderItem(3)
        item.setText(_translate("Form_Vuln", "漏洞类型"))
        item = self.show_Plugins.horizontalHeaderItem(4)
        item.setText(_translate("Form_Vuln", "漏洞编号"))
        item = self.show_Plugins.horizontalHeaderItem(5)
        item.setText(_translate("Form_Vuln", "漏洞来源"))
        item = self.show_Plugins.horizontalHeaderItem(6)
        item.setText(_translate("Form_Vuln", "漏洞描述"))
        item = self.show_Plugins.horizontalHeaderItem(7)
        item.setText(_translate("Form_Vuln", "插件路径"))
        item = self.show_Plugins.horizontalHeaderItem(8)
        item.setText(_translate("Form_Vuln", "插件作者"))
        item = self.show_Plugins.horizontalHeaderItem(9)
        item.setText(_translate("Form_Vuln", "修复建议"))
