# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dola.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(883, 850)
        MainWindow.setMinimumSize(QtCore.QSize(770, 740))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 549))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QPushButton{\n"
"background-color:gray;\n"
"border-radius: 50%;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.tab_3)
        self.frame_2.setMinimumSize(QtCore.QSize(420, 674))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8.addWidget(self.frame_2, 0, 0, 3, 1)
        self.frame = QtWidgets.QFrame(self.tab_3)
        self.frame.setMinimumSize(QtCore.QSize(420, 220))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_8.addWidget(self.frame, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.tab_3)
        self.frame_3.setMinimumSize(QtCore.QSize(420, 220))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.startButton = QtWidgets.QToolButton(self.frame_3)
        self.startButton.setMinimumSize(QtCore.QSize(100, 50))
        self.startButton.setMaximumSize(QtCore.QSize(100, 50))
        self.startButton.setObjectName("startButton")
        self.gridLayout_4.addWidget(self.startButton, 0, 0, 1, 1)
        self.loadButton = QtWidgets.QToolButton(self.frame_3)
        self.loadButton.setMinimumSize(QtCore.QSize(100, 50))
        self.loadButton.setMaximumSize(QtCore.QSize(100, 50))
        self.loadButton.setObjectName("loadButton")
        self.gridLayout_4.addWidget(self.loadButton, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.frame_3, 2, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.tab_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.levelComboBox = QtWidgets.QComboBox(self.frame_4)
        self.levelComboBox.setMinimumSize(QtCore.QSize(100, 30))
        self.levelComboBox.setMaximumSize(QtCore.QSize(100, 30))
        self.levelComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.levelComboBox.setObjectName("levelComboBox")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.gridLayout_5.addWidget(self.levelComboBox, 1, 1, 1, 1)
        self.level_label = QtWidgets.QLabel(self.frame_4)
        self.level_label.setMinimumSize(QtCore.QSize(100, 30))
        self.level_label.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.level_label.setFont(font)
        self.level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.level_label.setObjectName("level_label")
        self.gridLayout_5.addWidget(self.level_label, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pb40 = QtWidgets.QPushButton(self.tab_4)
        self.pb40.setMinimumSize(QtCore.QSize(100, 100))
        self.pb40.setText("")
        self.pb40.setObjectName("pb40")
        self.gridLayout_3.addWidget(self.pb40, 1, 0, 1, 1)
        self.pb41 = QtWidgets.QPushButton(self.tab_4)
        self.pb41.setMinimumSize(QtCore.QSize(100, 100))
        self.pb41.setMaximumSize(QtCore.QSize(100, 100))
        self.pb41.setText("")
        self.pb41.setObjectName("pb41")
        self.gridLayout_3.addWidget(self.pb41, 1, 1, 1, 1)
        self.pb56 = QtWidgets.QPushButton(self.tab_4)
        self.pb56.setMinimumSize(QtCore.QSize(100, 100))
        self.pb56.setMaximumSize(QtCore.QSize(100, 100))
        self.pb56.setText("")
        self.pb56.setObjectName("pb56")
        self.gridLayout_3.addWidget(self.pb56, 0, 6, 1, 1)
        self.pb45 = QtWidgets.QPushButton(self.tab_4)
        self.pb45.setMinimumSize(QtCore.QSize(100, 100))
        self.pb45.setMaximumSize(QtCore.QSize(100, 100))
        self.pb45.setText("")
        self.pb45.setObjectName("pb45")
        self.gridLayout_3.addWidget(self.pb45, 1, 5, 1, 1)
        self.pb53 = QtWidgets.QPushButton(self.tab_4)
        self.pb53.setMinimumSize(QtCore.QSize(100, 100))
        self.pb53.setMaximumSize(QtCore.QSize(100, 100))
        self.pb53.setText("")
        self.pb53.setObjectName("pb53")
        self.gridLayout_3.addWidget(self.pb53, 0, 3, 1, 1)
        self.pb22 = QtWidgets.QPushButton(self.tab_4)
        self.pb22.setMinimumSize(QtCore.QSize(100, 100))
        self.pb22.setMaximumSize(QtCore.QSize(100, 100))
        self.pb22.setText("")
        self.pb22.setObjectName("pb22")
        self.gridLayout_3.addWidget(self.pb22, 3, 2, 1, 1)
        self.pb50 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb50.sizePolicy().hasHeightForWidth())
        self.pb50.setSizePolicy(sizePolicy)
        self.pb50.setMinimumSize(QtCore.QSize(100, 100))
        self.pb50.setText("")
        self.pb50.setCheckable(True)
        self.pb50.setObjectName("pb50")
        self.gridLayout_3.addWidget(self.pb50, 0, 0, 1, 1)
        self.pb31 = QtWidgets.QPushButton(self.tab_4)
        self.pb31.setMinimumSize(QtCore.QSize(100, 100))
        self.pb31.setMaximumSize(QtCore.QSize(100, 100))
        self.pb31.setText("")
        self.pb31.setObjectName("pb31")
        self.gridLayout_3.addWidget(self.pb31, 2, 1, 1, 1)
        self.pb36 = QtWidgets.QPushButton(self.tab_4)
        self.pb36.setMinimumSize(QtCore.QSize(100, 100))
        self.pb36.setMaximumSize(QtCore.QSize(100, 100))
        self.pb36.setText("")
        self.pb36.setObjectName("pb36")
        self.gridLayout_3.addWidget(self.pb36, 2, 6, 1, 1)
        self.pb55 = QtWidgets.QPushButton(self.tab_4)
        self.pb55.setMinimumSize(QtCore.QSize(100, 100))
        self.pb55.setMaximumSize(QtCore.QSize(100, 100))
        self.pb55.setText("")
        self.pb55.setObjectName("pb55")
        self.gridLayout_3.addWidget(self.pb55, 0, 5, 1, 1)
        self.pb24 = QtWidgets.QPushButton(self.tab_4)
        self.pb24.setMinimumSize(QtCore.QSize(100, 100))
        self.pb24.setMaximumSize(QtCore.QSize(100, 100))
        self.pb24.setText("")
        self.pb24.setObjectName("pb24")
        self.gridLayout_3.addWidget(self.pb24, 3, 4, 1, 1)
        self.pb35 = QtWidgets.QPushButton(self.tab_4)
        self.pb35.setMinimumSize(QtCore.QSize(100, 100))
        self.pb35.setMaximumSize(QtCore.QSize(100, 100))
        self.pb35.setText("")
        self.pb35.setObjectName("pb35")
        self.gridLayout_3.addWidget(self.pb35, 2, 5, 1, 1)
        self.pb23 = QtWidgets.QPushButton(self.tab_4)
        self.pb23.setMinimumSize(QtCore.QSize(100, 100))
        self.pb23.setMaximumSize(QtCore.QSize(100, 100))
        self.pb23.setText("")
        self.pb23.setObjectName("pb23")
        self.gridLayout_3.addWidget(self.pb23, 3, 3, 1, 1)
        self.pb42 = QtWidgets.QPushButton(self.tab_4)
        self.pb42.setMinimumSize(QtCore.QSize(100, 100))
        self.pb42.setMaximumSize(QtCore.QSize(100, 100))
        self.pb42.setText("")
        self.pb42.setObjectName("pb42")
        self.gridLayout_3.addWidget(self.pb42, 1, 2, 1, 1)
        self.pb46 = QtWidgets.QPushButton(self.tab_4)
        self.pb46.setMinimumSize(QtCore.QSize(100, 100))
        self.pb46.setMaximumSize(QtCore.QSize(100, 100))
        self.pb46.setText("")
        self.pb46.setObjectName("pb46")
        self.gridLayout_3.addWidget(self.pb46, 1, 6, 1, 1)
        self.pb26 = QtWidgets.QPushButton(self.tab_4)
        self.pb26.setMinimumSize(QtCore.QSize(100, 100))
        self.pb26.setMaximumSize(QtCore.QSize(100, 100))
        self.pb26.setText("")
        self.pb26.setObjectName("pb26")
        self.gridLayout_3.addWidget(self.pb26, 3, 6, 1, 1)
        self.pb10 = QtWidgets.QPushButton(self.tab_4)
        self.pb10.setMinimumSize(QtCore.QSize(100, 100))
        self.pb10.setMaximumSize(QtCore.QSize(100, 100))
        self.pb10.setText("")
        self.pb10.setObjectName("pb10")
        self.gridLayout_3.addWidget(self.pb10, 4, 0, 1, 1)
        self.pb01 = QtWidgets.QPushButton(self.tab_4)
        self.pb01.setMinimumSize(QtCore.QSize(100, 100))
        self.pb01.setMaximumSize(QtCore.QSize(100, 100))
        self.pb01.setText("")
        self.pb01.setObjectName("pb01")
        self.gridLayout_3.addWidget(self.pb01, 5, 1, 1, 1)
        self.pb52 = QtWidgets.QPushButton(self.tab_4)
        self.pb52.setMinimumSize(QtCore.QSize(100, 100))
        self.pb52.setMaximumSize(QtCore.QSize(100, 100))
        self.pb52.setText("")
        self.pb52.setObjectName("pb52")
        self.gridLayout_3.addWidget(self.pb52, 0, 2, 1, 1)
        self.pb16 = QtWidgets.QPushButton(self.tab_4)
        self.pb16.setMinimumSize(QtCore.QSize(100, 100))
        self.pb16.setMaximumSize(QtCore.QSize(100, 100))
        self.pb16.setText("")
        self.pb16.setObjectName("pb16")
        self.gridLayout_3.addWidget(self.pb16, 4, 6, 1, 1)
        self.pb21 = QtWidgets.QPushButton(self.tab_4)
        self.pb21.setMinimumSize(QtCore.QSize(100, 100))
        self.pb21.setMaximumSize(QtCore.QSize(100, 100))
        self.pb21.setText("")
        self.pb21.setObjectName("pb21")
        self.gridLayout_3.addWidget(self.pb21, 3, 1, 1, 1)
        self.pb44 = QtWidgets.QPushButton(self.tab_4)
        self.pb44.setMinimumSize(QtCore.QSize(100, 100))
        self.pb44.setMaximumSize(QtCore.QSize(100, 100))
        self.pb44.setText("")
        self.pb44.setObjectName("pb44")
        self.gridLayout_3.addWidget(self.pb44, 1, 4, 1, 1)
        self.pb34 = QtWidgets.QPushButton(self.tab_4)
        self.pb34.setMinimumSize(QtCore.QSize(100, 100))
        self.pb34.setMaximumSize(QtCore.QSize(100, 100))
        self.pb34.setText("")
        self.pb34.setObjectName("pb34")
        self.gridLayout_3.addWidget(self.pb34, 2, 4, 1, 1)
        self.pb30 = QtWidgets.QPushButton(self.tab_4)
        self.pb30.setMinimumSize(QtCore.QSize(100, 100))
        self.pb30.setMaximumSize(QtCore.QSize(100, 100))
        self.pb30.setText("")
        self.pb30.setObjectName("pb30")
        self.gridLayout_3.addWidget(self.pb30, 2, 0, 1, 1)
        self.pb13 = QtWidgets.QPushButton(self.tab_4)
        self.pb13.setMinimumSize(QtCore.QSize(100, 100))
        self.pb13.setMaximumSize(QtCore.QSize(100, 100))
        self.pb13.setText("")
        self.pb13.setObjectName("pb13")
        self.gridLayout_3.addWidget(self.pb13, 4, 3, 1, 1)
        self.pb33 = QtWidgets.QPushButton(self.tab_4)
        self.pb33.setMinimumSize(QtCore.QSize(100, 100))
        self.pb33.setMaximumSize(QtCore.QSize(100, 100))
        self.pb33.setText("")
        self.pb33.setObjectName("pb33")
        self.gridLayout_3.addWidget(self.pb33, 2, 3, 1, 1)
        self.pb25 = QtWidgets.QPushButton(self.tab_4)
        self.pb25.setMinimumSize(QtCore.QSize(100, 100))
        self.pb25.setMaximumSize(QtCore.QSize(100, 100))
        self.pb25.setText("")
        self.pb25.setObjectName("pb25")
        self.gridLayout_3.addWidget(self.pb25, 3, 5, 1, 1)
        self.pb32 = QtWidgets.QPushButton(self.tab_4)
        self.pb32.setMinimumSize(QtCore.QSize(100, 100))
        self.pb32.setMaximumSize(QtCore.QSize(100, 100))
        self.pb32.setText("")
        self.pb32.setObjectName("pb32")
        self.gridLayout_3.addWidget(self.pb32, 2, 2, 1, 1)
        self.pb51 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb51.sizePolicy().hasHeightForWidth())
        self.pb51.setSizePolicy(sizePolicy)
        self.pb51.setMinimumSize(QtCore.QSize(100, 100))
        self.pb51.setMaximumSize(QtCore.QSize(100, 100))
        self.pb51.setText("")
        self.pb51.setObjectName("pb51")
        self.gridLayout_3.addWidget(self.pb51, 0, 1, 1, 1)
        self.pb43 = QtWidgets.QPushButton(self.tab_4)
        self.pb43.setMinimumSize(QtCore.QSize(100, 100))
        self.pb43.setMaximumSize(QtCore.QSize(100, 100))
        self.pb43.setText("")
        self.pb43.setObjectName("pb43")
        self.gridLayout_3.addWidget(self.pb43, 1, 3, 1, 1)
        self.pb54 = QtWidgets.QPushButton(self.tab_4)
        self.pb54.setMinimumSize(QtCore.QSize(100, 100))
        self.pb54.setMaximumSize(QtCore.QSize(100, 100))
        self.pb54.setText("")
        self.pb54.setObjectName("pb54")
        self.gridLayout_3.addWidget(self.pb54, 0, 4, 1, 1)
        self.pb20 = QtWidgets.QPushButton(self.tab_4)
        self.pb20.setMinimumSize(QtCore.QSize(100, 100))
        self.pb20.setMaximumSize(QtCore.QSize(100, 100))
        self.pb20.setText("")
        self.pb20.setObjectName("pb20")
        self.gridLayout_3.addWidget(self.pb20, 3, 0, 1, 1)
        self.pb15 = QtWidgets.QPushButton(self.tab_4)
        self.pb15.setMinimumSize(QtCore.QSize(100, 100))
        self.pb15.setMaximumSize(QtCore.QSize(100, 100))
        self.pb15.setText("")
        self.pb15.setObjectName("pb15")
        self.gridLayout_3.addWidget(self.pb15, 4, 5, 1, 1)
        self.pb04 = QtWidgets.QPushButton(self.tab_4)
        self.pb04.setMinimumSize(QtCore.QSize(100, 100))
        self.pb04.setMaximumSize(QtCore.QSize(100, 100))
        self.pb04.setText("")
        self.pb04.setObjectName("pb04")
        self.gridLayout_3.addWidget(self.pb04, 5, 4, 1, 1)
        self.pb14 = QtWidgets.QPushButton(self.tab_4)
        self.pb14.setMinimumSize(QtCore.QSize(100, 100))
        self.pb14.setMaximumSize(QtCore.QSize(100, 100))
        self.pb14.setText("")
        self.pb14.setObjectName("pb14")
        self.gridLayout_3.addWidget(self.pb14, 4, 4, 1, 1)
        self.pb05 = QtWidgets.QPushButton(self.tab_4)
        self.pb05.setMinimumSize(QtCore.QSize(100, 100))
        self.pb05.setMaximumSize(QtCore.QSize(100, 100))
        self.pb05.setText("")
        self.pb05.setObjectName("pb05")
        self.gridLayout_3.addWidget(self.pb05, 5, 5, 1, 1)
        self.pb03 = QtWidgets.QPushButton(self.tab_4)
        self.pb03.setMinimumSize(QtCore.QSize(100, 100))
        self.pb03.setMaximumSize(QtCore.QSize(100, 100))
        self.pb03.setText("")
        self.pb03.setObjectName("pb03")
        self.gridLayout_3.addWidget(self.pb03, 5, 3, 1, 1)
        self.pb11 = QtWidgets.QPushButton(self.tab_4)
        self.pb11.setMinimumSize(QtCore.QSize(100, 100))
        self.pb11.setMaximumSize(QtCore.QSize(100, 100))
        self.pb11.setText("")
        self.pb11.setObjectName("pb11")
        self.gridLayout_3.addWidget(self.pb11, 4, 1, 1, 1)
        self.pb12 = QtWidgets.QPushButton(self.tab_4)
        self.pb12.setMinimumSize(QtCore.QSize(100, 100))
        self.pb12.setMaximumSize(QtCore.QSize(100, 100))
        self.pb12.setText("")
        self.pb12.setObjectName("pb12")
        self.gridLayout_3.addWidget(self.pb12, 4, 2, 1, 1)
        self.pb02 = QtWidgets.QPushButton(self.tab_4)
        self.pb02.setMinimumSize(QtCore.QSize(100, 100))
        self.pb02.setMaximumSize(QtCore.QSize(100, 100))
        self.pb02.setText("")
        self.pb02.setObjectName("pb02")
        self.gridLayout_3.addWidget(self.pb02, 5, 2, 1, 1)
        self.pb06 = QtWidgets.QPushButton(self.tab_4)
        self.pb06.setMinimumSize(QtCore.QSize(100, 100))
        self.pb06.setMaximumSize(QtCore.QSize(100, 100))
        self.pb06.setText("")
        self.pb06.setObjectName("pb06")
        self.gridLayout_3.addWidget(self.pb06, 5, 6, 1, 1)
        self.pb00 = QtWidgets.QPushButton(self.tab_4)
        self.pb00.setMinimumSize(QtCore.QSize(100, 100))
        self.pb00.setMaximumSize(QtCore.QSize(100, 100))
        self.pb00.setText("")
        self.pb00.setObjectName("pb00")
        self.gridLayout_3.addWidget(self.pb00, 5, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.tab_4)
        self.saveButton.setMinimumSize(QtCore.QSize(100, 30))
        self.saveButton.setMaximumSize(QtCore.QSize(100, 40))
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_3.addWidget(self.saveButton, 6, 3, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 883, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "start"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
        self.levelComboBox.setItemText(0, _translate("MainWindow", "Easy"))
        self.levelComboBox.setItemText(1, _translate("MainWindow", "Medium"))
        self.levelComboBox.setItemText(2, _translate("MainWindow", "Hard"))
        self.level_label.setText(_translate("MainWindow", "level"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))

