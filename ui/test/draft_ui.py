# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'draft.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1333, 1158)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setAutoFillBackground(False)
        self.splitter.setFrameShape(QFrame.Box)
        self.splitter.setFrameShadow(QFrame.Plain)
        self.splitter.setLineWidth(0)
        self.splitter.setMidLineWidth(1)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(15)
        self.splitter.setChildrenCollapsible(False)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(150, 0))
        self.groupBox.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listView2 = QListView(self.groupBox)
        self.listView2.setObjectName(u"listView2")

        self.verticalLayout.addWidget(self.listView2)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(True)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 802, 906))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label)

        self.checkBox_4 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_4.addWidget(self.checkBox_4)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(True)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_5 = QCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_3.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.groupBox_3)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_3.addWidget(self.checkBox_6)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_12 = QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_2 = QScrollArea(self.tab_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -478, 768, 1628))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font = QFont()
        font.setBold(False)
        font.setStrikeOut(False)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setFlat(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_6.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.groupBox_4)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.textEdit)

        self.plainTextEdit = QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 100))
        self.plainTextEdit.setTabChangesFocus(True)

        self.verticalLayout_6.addWidget(self.plainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.lineEdit_5 = QLineEdit(self.groupBox_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout.addWidget(self.lineEdit_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_6.addWidget(self.lineEdit_3)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(self.groupBox_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_6.addWidget(self.lineEdit_4)


        self.verticalLayout_8.addWidget(self.groupBox_4)

        self.checkBox_7 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout_8.addWidget(self.checkBox_7)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_8.addWidget(self.pushButton_3)

        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFlat(False)
        self.groupBox_6.setCheckable(True)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_8 = QCheckBox(self.groupBox_6)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout_9.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.groupBox_6)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.verticalLayout_9.addWidget(self.checkBox_9)


        self.verticalLayout_8.addWidget(self.groupBox_6)

        self.line = QFrame(self.scrollAreaWidgetContents_2)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 20))
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_8.addWidget(self.line)

        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_2 = QComboBox(self.groupBox_7)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.commandLinkButton_2 = QCommandLinkButton(self.groupBox_7)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        self.commandLinkButton_2.setMaximumSize(QSize(100, 60))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(6)
        self.commandLinkButton_2.setFont(font1)
        self.commandLinkButton_2.setCheckable(True)
        self.commandLinkButton_2.setChecked(False)

        self.horizontalLayout_2.addWidget(self.commandLinkButton_2)


        self.verticalLayout_8.addWidget(self.groupBox_7)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.checkBox_2 = QCheckBox(self.frame_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_10.addWidget(self.checkBox_2)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lineEdit_2 = QLineEdit(self.groupBox_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_11.addWidget(self.lineEdit_2)

        self.textEdit_2 = QTextEdit(self.groupBox_8)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setEnabled(True)
        self.textEdit_2.setMaximumSize(QSize(16777215, 200))
        self.textEdit_2.setBaseSize(QSize(0, 200))

        self.verticalLayout_11.addWidget(self.textEdit_2)


        self.verticalLayout_8.addWidget(self.groupBox_8)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_8.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_8.addWidget(self.pushButton_6)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_12.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.splitter.addWidget(self.groupBox_2)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1333, 38))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"modules", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Module XY", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"A Text: A description text that mumbles across the window with so called words compromised of \"letters\" and punctuation. Sometimes it even has a meaning!", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"a checkbox that does something", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"A Button that calls some action", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox enablable", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"normal mode", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"module information:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"display name:", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"module name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"description:", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">A Text: A description text that mumbles across the window with so called words compromised of &quot;letters&quot; and punctuation. Sometimes it even has a meaning!</span></p></body></html>", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"asdasdf\n"
"", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"author:", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"my name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"version:", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"0.0.1", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"a checkbox that does something", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"A Button that calls some action", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox enablable", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"new element", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Text", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Include", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"GroupBox", None))

        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"This is something for a Text Label", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Edit Text:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Module1_Text", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This is something for a Text Label</span></p></body></html>", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"edit mode", None))
    # retranslateUi

