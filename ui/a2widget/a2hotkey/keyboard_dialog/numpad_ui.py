# -*- coding: utf-8 -*-

"""
Form generated from reading UI file 'numpad.ui'

Created by: Qt User Interface Compiler version 6.4.2

WARNING! All changes made in this file will be lost when recompiling UI file!
"""

from a2qt.QtWidgets import (QGridLayout, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from a2qt.QtCore import QMetaObject, QSize, Qt

class Ui_Numpad:
    def setupUi(self, Numpad):
        if not Numpad.objectName():
            Numpad.setObjectName('Numpad')
        Numpad.setWindowTitle('Form')
        self.gridLayout = QGridLayout(Numpad)
        self.gridLayout.setObjectName('gridLayout')
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.numlock = QPushButton(Numpad)
        self.numlock.setObjectName('numlock')
        self.numlock.setText('Num\nLock')
        self.gridLayout.addWidget(self.numlock, 1, 0, 1, 1)
        self.numpaddiv = QPushButton(Numpad)
        self.numpaddiv.setObjectName('numpaddiv')
        self.numpaddiv.setText('/')
        self.gridLayout.addWidget(self.numpaddiv, 1, 1, 1, 1)
        self.numpad1 = QPushButton(Numpad)
        self.numpad1.setObjectName('numpad1')
        self.numpad1.setText('1')
        self.gridLayout.addWidget(self.numpad1, 4, 0, 1, 1)
        self.numpad5 = QPushButton(Numpad)
        self.numpad5.setObjectName('numpad5')
        self.numpad5.setText('5')
        self.gridLayout.addWidget(self.numpad5, 3, 1, 1, 1)
        self.numpadmult = QPushButton(Numpad)
        self.numpadmult.setObjectName('numpadmult')
        self.numpadmult.setText('*')
        self.gridLayout.addWidget(self.numpadmult, 1, 2, 1, 1)
        self.numpad8 = QPushButton(Numpad)
        self.numpad8.setObjectName('numpad8')
        self.numpad8.setText('8')
        self.gridLayout.addWidget(self.numpad8, 2, 1, 1, 1)
        self.numpad4 = QPushButton(Numpad)
        self.numpad4.setObjectName('numpad4')
        self.numpad4.setText('4')
        self.gridLayout.addWidget(self.numpad4, 3, 0, 1, 1)
        self.numpad3 = QPushButton(Numpad)
        self.numpad3.setObjectName('numpad3')
        self.numpad3.setText('3')
        self.gridLayout.addWidget(self.numpad3, 4, 2, 1, 1)
        self.numpad6 = QPushButton(Numpad)
        self.numpad6.setObjectName('numpad6')
        self.numpad6.setText('6')
        self.gridLayout.addWidget(self.numpad6, 3, 2, 1, 1)
        self.numpad7 = QPushButton(Numpad)
        self.numpad7.setObjectName('numpad7')
        self.numpad7.setText('7')
        self.gridLayout.addWidget(self.numpad7, 2, 0, 1, 1)
        self.numpad2 = QPushButton(Numpad)
        self.numpad2.setObjectName('numpad2')
        self.numpad2.setText('2')
        self.gridLayout.addWidget(self.numpad2, 4, 1, 1, 1)
        self.numpaddot = QPushButton(Numpad)
        self.numpaddot.setObjectName('numpaddot')
        self.numpaddot.setText('.')
        self.gridLayout.addWidget(self.numpaddot, 5, 2, 1, 1)
        self.numpad9 = QPushButton(Numpad)
        self.numpad9.setObjectName('numpad9')
        self.numpad9.setText('9')
        self.gridLayout.addWidget(self.numpad9, 2, 2, 1, 1)
        self.numpad0 = QPushButton(Numpad)
        self.numpad0.setObjectName('numpad0')
        self.numpad0.setText('0')
        self.gridLayout.addWidget(self.numpad0, 5, 0, 1, 2)
        self.numpadsub = QPushButton(Numpad)
        self.numpadsub.setObjectName('numpadsub')
        self.numpadsub.setText('-')
        self.gridLayout.addWidget(self.numpadsub, 1, 3, 1, 1)
        self.num_spacer = QWidget(Numpad)
        self.num_spacer.setObjectName('num_spacer')
        self.gridLayout.addWidget(self.num_spacer, 0, 0, 1, 5)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.numpadadd = QPushButton(Numpad)
        self.numpadadd.setObjectName('numpadadd')
        self.numpadadd.setMinimumSize(QSize(0, 120))
        self.numpadadd.setText('+')
        self.verticalLayout_2.addWidget(self.numpadadd, 0, Qt.AlignTop)
        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 3, 2, 1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName('verticalLayout')
        self.numpadenter = QPushButton(Numpad)
        self.numpadenter.setObjectName('numpadenter')
        self.numpadenter.setMinimumSize(QSize(0, 90))
        self.numpadenter.setText('Enter')
        self.verticalLayout.addWidget(self.numpadenter)
        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer_2)
        self.gridLayout.addLayout(self.verticalLayout, 4, 3, 2, 1)
        self.gridLayout.setRowStretch(0, 1)
        QMetaObject.connectSlotsByName(Numpad)
