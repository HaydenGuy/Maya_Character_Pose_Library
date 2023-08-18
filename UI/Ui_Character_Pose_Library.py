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
        library_window.resize(507, 322)
        self.centralwidget = QWidget(library_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.setTextElideMode(Qt.ElideLeft)

        self.horizontalLayout_2.addWidget(self.listView)


        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.lb_pose_name = QLabel(self.centralwidget)
        self.lb_pose_name.setObjectName(u"lb_pose_name")

        self.horizontalLayout.addWidget(self.lb_pose_name)

        self.pose_name_input = QLineEdit(self.centralwidget)
        self.pose_name_input.setObjectName(u"pose_name_input")
        self.pose_name_input.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.pose_name_input)

        self.pb_save = QPushButton(self.centralwidget)
        self.pb_save.setObjectName(u"pb_save")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_save.sizePolicy().hasHeightForWidth())
        self.pb_save.setSizePolicy(sizePolicy)
        self.pb_save.setMaximumSize(QSize(150, 16777215))
        self.pb_save.setAutoDefault(False)
        self.pb_save.setFlat(False)

        self.horizontalLayout.addWidget(self.pb_save)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.hbox_buttons = QHBoxLayout()
        self.hbox_buttons.setObjectName(u"hbox_buttons")
        self.pb_recall = QPushButton(self.centralwidget)
        self.pb_recall.setObjectName(u"pb_recall")

        self.hbox_buttons.addWidget(self.pb_recall)

        self.pb_delete = QPushButton(self.centralwidget)
        self.pb_delete.setObjectName(u"pb_delete")

        self.hbox_buttons.addWidget(self.pb_delete)


        self.gridLayout.addLayout(self.hbox_buttons, 8, 0, 1, 1)

        library_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(library_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 507, 23))
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
        self.lb_pose_name.setText(QCoreApplication.translate("library_window", u"Pose Name:", None))
        self.pb_save.setText(QCoreApplication.translate("library_window", u"Save Pose", None))
        self.pb_recall.setText(QCoreApplication.translate("library_window", u"Recall Pose", None))
        self.pb_delete.setText(QCoreApplication.translate("library_window", u"Delete Pose", None))
    # retranslateUi

