# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'a2module_view.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from a2qt.QtCore import *
from a2qt.QtGui import *
from a2qt.QtWidgets import *


class Ui_A2ModuleView(object):
    def setupUi(self, A2ModuleView):
        if not A2ModuleView.objectName():
            A2ModuleView.setObjectName(u"A2ModuleView")

        self.A2ModuleViewLayout = QVBoxLayout(A2ModuleView)
        self.A2ModuleViewLayout.setSpacing(0)
        self.A2ModuleViewLayout.setContentsMargins(0, 0, 0, 0)
        self.A2ModuleViewLayout.setObjectName(u"A2ModuleViewLayout")
        self.head_widget = QWidget(A2ModuleView)
        self.head_widget.setObjectName(u"head_widget")
        self.horizontalLayout = QHBoxLayout(self.head_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mod_check = QCheckBox(self.head_widget)
        self.mod_check.setObjectName(u"mod_check")
        self.mod_check.setTristate(False)

        self.horizontalLayout.addWidget(self.mod_check, 0, Qt.AlignBottom)

        self.icon_label = QLabel(self.head_widget)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setMinimumSize(QSize(20, 20))
        self.icon_label.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.icon_label, 0, Qt.AlignBottom)

        self.a2_mod_name = QLabel(self.head_widget)
        self.a2_mod_name.setObjectName(u"a2_mod_name")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.a2_mod_name.setFont(font)
        self.a2_mod_name.setText(u"ModName")
        self.a2_mod_name.setTextFormat(Qt.PlainText)

        self.horizontalLayout.addWidget(self.a2_mod_name, 0, Qt.AlignBottom)

        self.mod_version = QLabel(self.head_widget)
        self.mod_version.setObjectName(u"mod_version")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.mod_version.setFont(font1)
        self.mod_version.setText(u"v0.0")

        self.horizontalLayout.addWidget(self.mod_version, 0, Qt.AlignBottom)

        self.mod_author = QLabel(self.head_widget)
        self.mod_author.setObjectName(u"mod_author")
        self.mod_author.setFont(font1)
        self.mod_author.setText(u"- Author Name")

        self.horizontalLayout.addWidget(self.mod_author, 0, Qt.AlignBottom)

        self.a2mod_view_source_label = QLabel(self.head_widget)
        self.a2mod_view_source_label.setObjectName(u"a2mod_view_source_label")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a2mod_view_source_label.sizePolicy().hasHeightForWidth())
        self.a2mod_view_source_label.setSizePolicy(sizePolicy)
        self.a2mod_view_source_label.setFont(font1)
        self.a2mod_view_source_label.setText(u"- Module Source")

        self.horizontalLayout.addWidget(self.a2mod_view_source_label, 0, Qt.AlignBottom)

        self.a2help_button = QPushButton(self.head_widget)
        self.a2help_button.setObjectName(u"a2help_button")
        self.a2help_button.setText(u"?")
        self.a2help_button.setFlat(True)

        self.horizontalLayout.addWidget(self.a2help_button)

        self.horizontalLayout.setStretch(5, 1)

        self.A2ModuleViewLayout.addWidget(self.head_widget)

        self.a2scroll_area = QScrollArea(A2ModuleView)
        self.a2scroll_area.setObjectName(u"a2scroll_area")
        self.a2scroll_area.setWidgetResizable(True)
        self.scroll_area_contents = QWidget()
        self.scroll_area_contents.setObjectName(u"scroll_area_contents")
        self.scroll_area_contents.setGeometry(QRect(0, 0, 917, 495))
        self.verticalLayout_4 = QVBoxLayout(self.scroll_area_contents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.a2scroll_area.setWidget(self.scroll_area_contents)

        self.A2ModuleViewLayout.addWidget(self.a2scroll_area)

        self.a2edit_okcancel_widget = QWidget(A2ModuleView)
        self.a2edit_okcancel_widget.setObjectName(u"a2edit_okcancel_widget")
        self.a2edit_okcancel_layout = QHBoxLayout(self.a2edit_okcancel_widget)
        self.a2edit_okcancel_layout.setObjectName(u"a2edit_okcancel_layout")
        self.a2ok_button = QPushButton(self.a2edit_okcancel_widget)
        self.a2ok_button.setObjectName(u"a2ok_button")
        font2 = QFont()
        font2.setPointSize(11)
        self.a2ok_button.setFont(font2)
        self.a2ok_button.setText(u"OK")

        self.a2edit_okcancel_layout.addWidget(self.a2ok_button)

        self.a2cancel_button = QPushButton(self.a2edit_okcancel_widget)
        self.a2cancel_button.setObjectName(u"a2cancel_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.a2cancel_button.sizePolicy().hasHeightForWidth())
        self.a2cancel_button.setSizePolicy(sizePolicy1)
        self.a2cancel_button.setFont(font2)
        self.a2cancel_button.setText(u"Cancel")
        self.a2cancel_button.setFlat(True)

        self.a2edit_okcancel_layout.addWidget(self.a2cancel_button)

        self.a2edit_okcancel_layout.setStretch(0, 3)
        self.a2edit_okcancel_layout.setStretch(1, 1)

        self.A2ModuleViewLayout.addWidget(self.a2edit_okcancel_widget)


        self.retranslateUi(A2ModuleView)

        QMetaObject.connectSlotsByName(A2ModuleView)
    # setupUi

    def retranslateUi(self, A2ModuleView):
        self.mod_check.setText("")
        self.icon_label.setText("")
        pass
    # retranslateUi

