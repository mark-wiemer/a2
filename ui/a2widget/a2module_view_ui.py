# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\eric\io\code\a2\ui\a2widget\a2module_view.ui',
# licensing of 'c:\Users\eric\io\code\a2\ui\a2widget\a2module_view.ui' applies.
#
# Created: Tue Jan 28 21:59:37 2020
#      by: pyside2-uic  running on PySide2 5.14.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_A2ModuleView(object):
    def setupUi(self, A2ModuleView):
        A2ModuleView.setObjectName("A2ModuleView")
        A2ModuleView.resize(616, 578)
        self.A2ModuleViewLayout = QtWidgets.QVBoxLayout(A2ModuleView)
        self.A2ModuleViewLayout.setSpacing(0)
        self.A2ModuleViewLayout.setContentsMargins(0, 0, 0, 0)
        self.A2ModuleViewLayout.setObjectName("A2ModuleViewLayout")
        self.head_widget = QtWidgets.QWidget(A2ModuleView)
        self.head_widget.setObjectName("head_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.head_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.modCheck = QtWidgets.QCheckBox(self.head_widget)
        self.modCheck.setText("")
        self.modCheck.setTristate(False)
        self.modCheck.setObjectName("modCheck")
        self.horizontalLayout.addWidget(self.modCheck)
        self.a2_mod_name = QtWidgets.QLabel(self.head_widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.a2_mod_name.setFont(font)
        self.a2_mod_name.setStatusTip("")
        self.a2_mod_name.setWhatsThis("")
        self.a2_mod_name.setAccessibleName("")
        self.a2_mod_name.setAccessibleDescription("")
        self.a2_mod_name.setText("ModName")
        self.a2_mod_name.setTextFormat(QtCore.Qt.PlainText)
        self.a2_mod_name.setObjectName("a2_mod_name")
        self.horizontalLayout.addWidget(self.a2_mod_name)
        self.modVersion = QtWidgets.QLabel(self.head_widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.modVersion.setFont(font)
        self.modVersion.setObjectName("modVersion")
        self.horizontalLayout.addWidget(self.modVersion)
        self.modAuthor = QtWidgets.QLabel(self.head_widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.modAuthor.setFont(font)
        self.modAuthor.setObjectName("modAuthor")
        self.horizontalLayout.addWidget(self.modAuthor)
        self.a2mod_view_source_label = QtWidgets.QLabel(self.head_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a2mod_view_source_label.sizePolicy().hasHeightForWidth())
        self.a2mod_view_source_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.a2mod_view_source_label.setFont(font)
        self.a2mod_view_source_label.setObjectName("a2mod_view_source_label")
        self.horizontalLayout.addWidget(self.a2mod_view_source_label)
        self.a2help_button = QtWidgets.QPushButton(self.head_widget)
        self.a2help_button.setFlat(True)
        self.a2help_button.setObjectName("a2help_button")
        self.horizontalLayout.addWidget(self.a2help_button)
        self.horizontalLayout.setStretch(4, 1)
        self.A2ModuleViewLayout.addWidget(self.head_widget)
        self.a2scroll_area = QtWidgets.QScrollArea(A2ModuleView)
        self.a2scroll_area.setWidgetResizable(True)
        self.a2scroll_area.setObjectName("a2scroll_area")
        self.scroll_area_contents = QtWidgets.QWidget()
        self.scroll_area_contents.setGeometry(QtCore.QRect(0, 0, 614, 481))
        self.scroll_area_contents.setObjectName("scroll_area_contents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scroll_area_contents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.a2scroll_area.setWidget(self.scroll_area_contents)
        self.A2ModuleViewLayout.addWidget(self.a2scroll_area)
        self.a2edit_okcancel_widget = QtWidgets.QWidget(A2ModuleView)
        self.a2edit_okcancel_widget.setObjectName("a2edit_okcancel_widget")
        self.a2edit_okcancel_layout = QtWidgets.QHBoxLayout(self.a2edit_okcancel_widget)
        self.a2edit_okcancel_layout.setContentsMargins(0, 0, 0, 0)
        self.a2edit_okcancel_layout.setObjectName("a2edit_okcancel_layout")
        self.a2ok_button = QtWidgets.QPushButton(self.a2edit_okcancel_widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.a2ok_button.setFont(font)
        self.a2ok_button.setObjectName("a2ok_button")
        self.a2edit_okcancel_layout.addWidget(self.a2ok_button)
        self.a2cancel_button = QtWidgets.QPushButton(self.a2edit_okcancel_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a2cancel_button.sizePolicy().hasHeightForWidth())
        self.a2cancel_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.a2cancel_button.setFont(font)
        self.a2cancel_button.setFlat(True)
        self.a2cancel_button.setObjectName("a2cancel_button")
        self.a2edit_okcancel_layout.addWidget(self.a2cancel_button)
        self.a2edit_okcancel_layout.setStretch(0, 3)
        self.a2edit_okcancel_layout.setStretch(1, 1)
        self.A2ModuleViewLayout.addWidget(self.a2edit_okcancel_widget)

        self.retranslateUi(A2ModuleView)
        QtCore.QMetaObject.connectSlotsByName(A2ModuleView)

    def retranslateUi(self, A2ModuleView):
        A2ModuleView.setWindowTitle(QtWidgets.QApplication.translate("A2ModuleView", "Form", None, -1))
        self.modVersion.setText(QtWidgets.QApplication.translate("A2ModuleView", "v0.0", None, -1))
        self.modAuthor.setText(QtWidgets.QApplication.translate("A2ModuleView", "- Author Name", None, -1))
        self.a2mod_view_source_label.setText(QtWidgets.QApplication.translate("A2ModuleView", "- Module Source", None, -1))
        self.a2help_button.setText(QtWidgets.QApplication.translate("A2ModuleView", "?", None, -1))
        self.a2ok_button.setText(QtWidgets.QApplication.translate("A2ModuleView", "OK", None, -1))
        self.a2cancel_button.setText(QtWidgets.QApplication.translate("A2ModuleView", "Cancel", None, -1))

