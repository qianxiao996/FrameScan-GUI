# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vuln_Plugins.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form_Vuln(object):
    def setupUi(self, Form_Vuln):
        if not Form_Vuln.objectName():
            Form_Vuln.setObjectName(u"Form_Vuln")
        Form_Vuln.resize(1459, 821)
        icon = QIcon()
        icon.addFile(u":/logo/main.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_Vuln.setWindowIcon(icon)
        Form_Vuln.setLayoutDirection(Qt.LeftToRight)
        Form_Vuln.setAutoFillBackground(False)
        Form_Vuln.setStyleSheet(u"")
        Form_Vuln.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(Form_Vuln)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form_Vuln)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.show_Plugins_comboBox_cms_name = QComboBox(Form_Vuln)
        self.show_Plugins_comboBox_cms_name.addItem("")
        self.show_Plugins_comboBox_cms_name.setObjectName(u"show_Plugins_comboBox_cms_name")
        self.show_Plugins_comboBox_cms_name.setMinimumSize(QSize(150, 0))
        self.show_Plugins_comboBox_cms_name.setStyleSheet(u"")
        self.show_Plugins_comboBox_cms_name.setEditable(True)

        self.horizontalLayout.addWidget(self.show_Plugins_comboBox_cms_name)

        self.label_2 = QLabel(Form_Vuln)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout.addWidget(self.label_2)

        self.show_Plugins_comboBox_vuln_class = QComboBox(Form_Vuln)
        self.show_Plugins_comboBox_vuln_class.addItem("")
        self.show_Plugins_comboBox_vuln_class.setObjectName(u"show_Plugins_comboBox_vuln_class")
        self.show_Plugins_comboBox_vuln_class.setMinimumSize(QSize(150, 0))
        self.show_Plugins_comboBox_vuln_class.setStyleSheet(u"")
        self.show_Plugins_comboBox_vuln_class.setEditable(True)

        self.horizontalLayout.addWidget(self.show_Plugins_comboBox_vuln_class)

        self.pushButton_show_Plugins_search = QPushButton(Form_Vuln)
        self.pushButton_show_Plugins_search.setObjectName(u"pushButton_show_Plugins_search")
        self.pushButton_show_Plugins_search.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_show_Plugins_search)

        self.pushButton_show_Plugins_add = QPushButton(Form_Vuln)
        self.pushButton_show_Plugins_add.setObjectName(u"pushButton_show_Plugins_add")
        self.pushButton_show_Plugins_add.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_show_Plugins_add)

        self.pushButton_show_Plugins_delete = QPushButton(Form_Vuln)
        self.pushButton_show_Plugins_delete.setObjectName(u"pushButton_show_Plugins_delete")
        self.pushButton_show_Plugins_delete.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_show_Plugins_delete)

        self.pushButton_show_Plugins_edit = QPushButton(Form_Vuln)
        self.pushButton_show_Plugins_edit.setObjectName(u"pushButton_show_Plugins_edit")
        self.pushButton_show_Plugins_edit.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_show_Plugins_edit)

        self.pushButton_show_Plugins_reload = QPushButton(Form_Vuln)
        self.pushButton_show_Plugins_reload.setObjectName(u"pushButton_show_Plugins_reload")
        self.pushButton_show_Plugins_reload.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_show_Plugins_reload)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.show_Plugins = QTableWidget(Form_Vuln)
        if (self.show_Plugins.columnCount() < 10):
            self.show_Plugins.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.show_Plugins.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.show_Plugins.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.show_Plugins.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.show_Plugins.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.show_Plugins.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.show_Plugins.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.show_Plugins.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.show_Plugins.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.show_Plugins.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.show_Plugins.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.show_Plugins.setObjectName(u"show_Plugins")
        self.show_Plugins.setMinimumSize(QSize(200, 0))
        self.show_Plugins.setSizeIncrement(QSize(0, 0))
        self.show_Plugins.setTabletTracking(False)
        self.show_Plugins.setAutoFillBackground(False)
        self.show_Plugins.setStyleSheet(u"")
        self.show_Plugins.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.show_Plugins.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.show_Plugins.setShowGrid(True)
        self.show_Plugins.setGridStyle(Qt.SolidLine)
        self.show_Plugins.setSortingEnabled(True)
        self.show_Plugins.setWordWrap(True)
        self.show_Plugins.setCornerButtonEnabled(True)
        self.show_Plugins.horizontalHeader().setVisible(True)
        self.show_Plugins.horizontalHeader().setCascadingSectionResizes(True)
        self.show_Plugins.horizontalHeader().setDefaultSectionSize(200)
        self.show_Plugins.horizontalHeader().setHighlightSections(False)
        self.show_Plugins.horizontalHeader().setProperty("showSortIndicator", True)
        self.show_Plugins.horizontalHeader().setStretchLastSection(True)
        self.show_Plugins.verticalHeader().setVisible(False)
        self.show_Plugins.verticalHeader().setCascadingSectionResizes(False)
        self.show_Plugins.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout.addWidget(self.show_Plugins)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form_Vuln)

        QMetaObject.connectSlotsByName(Form_Vuln)
    # setupUi

    def retranslateUi(self, Form_Vuln):
        Form_Vuln.setWindowTitle(QCoreApplication.translate("Form_Vuln", u"\u6f0f\u6d1e\u63d2\u4ef6", None))
        self.label.setText(QCoreApplication.translate("Form_Vuln", u"\u5e94\u7528\u540d\u79f0", None))
        self.show_Plugins_comboBox_cms_name.setItemText(0, QCoreApplication.translate("Form_Vuln", u"ALL", None))

        self.label_2.setText(QCoreApplication.translate("Form_Vuln", u"\u6f0f\u6d1e\u7c7b\u578b", None))
        self.show_Plugins_comboBox_vuln_class.setItemText(0, QCoreApplication.translate("Form_Vuln", u"ALL", None))

        self.pushButton_show_Plugins_search.setText(QCoreApplication.translate("Form_Vuln", u"\u641c\u7d22\u63d2\u4ef6", None))
        self.pushButton_show_Plugins_add.setText(QCoreApplication.translate("Form_Vuln", u"\u65b0\u589e\u63d2\u4ef6", None))
        self.pushButton_show_Plugins_delete.setText(QCoreApplication.translate("Form_Vuln", u"\u5220\u9664\u63d2\u4ef6", None))
        self.pushButton_show_Plugins_edit.setText(QCoreApplication.translate("Form_Vuln", u"\u7f16\u8f91\u63d2\u4ef6", None))
        self.pushButton_show_Plugins_reload.setText(QCoreApplication.translate("Form_Vuln", u"\u91cd\u65b0\u52a0\u8f7d", None))
        ___qtablewidgetitem = self.show_Plugins.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_Vuln", u"ID", None));
        ___qtablewidgetitem1 = self.show_Plugins.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_Vuln", u"\u5e94\u7528\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.show_Plugins.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_Vuln", u"\u6f0f\u6d1e\u540d\u79f0", None));
        ___qtablewidgetitem3 = self.show_Plugins.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_Vuln", u"\u6f0f\u6d1e\u7c7b\u578b", None));
        ___qtablewidgetitem4 = self.show_Plugins.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_Vuln", u"\u6f0f\u6d1e\u7f16\u53f7", None));
        ___qtablewidgetitem5 = self.show_Plugins.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_Vuln", u"\u6f0f\u6d1e\u6765\u6e90", None));
        ___qtablewidgetitem6 = self.show_Plugins.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_Vuln", u"\u6f0f\u6d1e\u63cf\u8ff0", None));
        ___qtablewidgetitem7 = self.show_Plugins.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_Vuln", u"\u63d2\u4ef6\u8def\u5f84", None));
        ___qtablewidgetitem8 = self.show_Plugins.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_Vuln", u"\u63d2\u4ef6\u4f5c\u8005", None));
        ___qtablewidgetitem9 = self.show_Plugins.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form_Vuln", u"\u4fee\u590d\u5efa\u8bae", None));
#if QT_CONFIG(tooltip)
        self.show_Plugins.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.show_Plugins.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

