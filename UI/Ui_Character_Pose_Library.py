# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Character_Pose_Library.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_library_window(object):
    def setupUi(self, library_window):
        if not library_window.objectName():
            library_window.setObjectName(u"library_window")
        library_window.resize(472, 357)
        self.centralwidget = QWidget(library_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_save = QPushButton(self.centralwidget)
        self.pb_save.setObjectName(u"pb_save")
        self.pb_save.setAutoDefault(False)
        self.pb_save.setFlat(False)

        self.verticalLayout.addWidget(self.pb_save)

        self.pb_recall = QPushButton(self.centralwidget)
        self.pb_recall.setObjectName(u"pb_recall")

        self.verticalLayout.addWidget(self.pb_recall)

        library_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(library_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 472, 23))
        library_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(library_window)
        self.statusbar.setObjectName(u"statusbar")
        library_window.setStatusBar(self.statusbar)

        self.retranslateUi(library_window)

        self.pb_save.setDefault(False)


        QMetaObject.connectSlotsByName(library_window)
    # setupUi

    def retranslateUi(self, library_window):
        library_window.setWindowTitle(QCoreApplication.translate("library_window", u"Character Pose Library", None))
        self.pb_save.setText(QCoreApplication.translate("library_window", u"Save Position", None))
        self.pb_recall.setText(QCoreApplication.translate("library_window", u"Recall Position", None))
    # retranslateUi

