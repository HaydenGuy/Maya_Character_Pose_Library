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
        self.actionSave = QAction(library_window)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(library_window)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionNew = QAction(library_window)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(library_window)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionQuit = QAction(library_window)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(library_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        font = QFont()
        font.setPointSize(13)
        self.listView.setFont(font)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.setTextElideMode(Qt.ElideLeft)

        self.horizontalLayout_2.addWidget(self.listView)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)

        self.hbox_buttons = QHBoxLayout()
        self.hbox_buttons.setObjectName(u"hbox_buttons")
        self.pb_recall = QPushButton(self.centralwidget)
        self.pb_recall.setObjectName(u"pb_recall")

        self.hbox_buttons.addWidget(self.pb_recall)

        self.pb_delete = QPushButton(self.centralwidget)
        self.pb_delete.setObjectName(u"pb_delete")

        self.hbox_buttons.addWidget(self.pb_delete)


        self.gridLayout.addLayout(self.hbox_buttons, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.lb_pose_name = QLabel(self.centralwidget)
        self.lb_pose_name.setObjectName(u"lb_pose_name")
        font1 = QFont()
        font1.setPointSize(11)
        self.lb_pose_name.setFont(font1)

        self.horizontalLayout.addWidget(self.lb_pose_name)

        self.pose_name_input = QLineEdit(self.centralwidget)
        self.pose_name_input.setObjectName(u"pose_name_input")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pose_name_input.sizePolicy().hasHeightForWidth())
        self.pose_name_input.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(12)
        self.pose_name_input.setFont(font2)
        self.pose_name_input.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.pose_name_input)

        self.pb_save = QPushButton(self.centralwidget)
        self.pb_save.setObjectName(u"pb_save")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_save.sizePolicy().hasHeightForWidth())
        self.pb_save.setSizePolicy(sizePolicy1)
        self.pb_save.setMaximumSize(QSize(150, 16777215))
        self.pb_save.setAutoDefault(False)
        self.pb_save.setFlat(False)

        self.horizontalLayout.addWidget(self.pb_save)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        library_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(library_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 507, 25))
        self.menubar.setFont(font2)
        self.menubar.setStyleSheet(u"border-bottom: 1px solid grey;")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setEnabled(True)
        library_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(library_window)
        self.statusbar.setObjectName(u"statusbar")
        library_window.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pose_name_input, self.pb_save)
        QWidget.setTabOrder(self.pb_save, self.listView)
        QWidget.setTabOrder(self.listView, self.pb_recall)
        QWidget.setTabOrder(self.pb_recall, self.pb_delete)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(library_window)

        self.pb_save.setDefault(False)


        QMetaObject.connectSlotsByName(library_window)
    # setupUi

    def retranslateUi(self, library_window):
        library_window.setWindowTitle(QCoreApplication.translate("library_window", u"Character Pose Library", None))
        self.actionSave.setText(QCoreApplication.translate("library_window", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("library_window", u"Save As..", None))
        self.actionNew.setText(QCoreApplication.translate("library_window", u"New...", None))
        self.actionOpen.setText(QCoreApplication.translate("library_window", u"Open...", None))
        self.actionQuit.setText(QCoreApplication.translate("library_window", u"Quit", None))
        self.pb_recall.setText(QCoreApplication.translate("library_window", u"Recall Pose", None))
        self.pb_delete.setText(QCoreApplication.translate("library_window", u"Delete Pose", None))
        self.lb_pose_name.setText(QCoreApplication.translate("library_window", u"Pose Name:", None))
        self.pb_save.setText(QCoreApplication.translate("library_window", u"Save Pose", None))
        self.menuFile.setTitle(QCoreApplication.translate("library_window", u"File", None))
    # retranslateUi

