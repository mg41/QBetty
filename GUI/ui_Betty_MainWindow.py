# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\Betty\src\GUI\Betty_MainWindow.ui'
#
# Created: Tue Feb 02 01:50:26 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Betty_MainWindow(object):
    def setupUi(self, Betty_MainWindow):
        Betty_MainWindow.setObjectName("Betty_MainWindow")
        Betty_MainWindow.resize(802, 600)
        self.centralwidget = QtGui.QWidget(Betty_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.raceTable = QtGui.QTableView(self.centralwidget)
        self.raceTable.setObjectName("raceTable")
        self.verticalLayout_4.addWidget(self.raceTable)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.addButton = QtGui.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_4.addWidget(self.addButton)
        self.deleteButton = QtGui.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_4.addWidget(self.deleteButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        Betty_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Betty_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Betty_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Betty_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Betty_MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Betty_MainWindow)
        self.toolBar.setObjectName("toolBar")
        Betty_MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.raceDockWidget = QtGui.QDockWidget(Betty_MainWindow)
        self.raceDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.raceDockWidget.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.raceDockWidget.setObjectName("raceDockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtGui.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dateEdit = QtGui.QDateEdit(self.frame)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.timeEdit = QtGui.QTimeEdit(self.frame)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout.addWidget(self.timeEdit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.comboBox_2 = QtGui.QComboBox(self.frame)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.spinBox = QtGui.QSpinBox(self.frame)
        self.spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox.setMaximum(10000000)
        self.spinBox.setSingleStep(1000)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addWidget(self.frame)
        self.raceDockWidget.setWidget(self.dockWidgetContents)
        Betty_MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.raceDockWidget)
        self.dockWidget = QtGui.QDockWidget(Betty_MainWindow)
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        spacerItem3 = QtGui.QSpacerItem(20, 141, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.dockWidget.setWidget(self.dockWidgetContents_2)
        Betty_MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionNew = QtGui.QAction(Betty_MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/New"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(Betty_MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/Open"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(Betty_MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Save"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionDownload = QtGui.QAction(Betty_MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/Web"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownload.setIcon(icon3)
        self.actionDownload.setObjectName("actionDownload")
        self.actionQuit = QtGui.QAction(Betty_MainWindow)
        self.actionQuit.setCheckable(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/Quit"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon4)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRecent_Files = QtGui.QAction(Betty_MainWindow)
        self.actionRecent_Files.setObjectName("actionRecent_Files")
        self.actionSave_As = QtGui.QAction(Betty_MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/Save As"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon5)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionPrint = QtGui.QAction(Betty_MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/Print"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon6)
        self.actionPrint.setObjectName("actionPrint")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDownload)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRecent_Files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_As)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDownload)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQuit)
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.comboBox)
        self.label_3.setBuddy(self.dateEdit)
        self.label_4.setBuddy(self.timeEdit)
        self.label_5.setBuddy(self.comboBox_2)
        self.label_8.setBuddy(self.spinBox)
        self.label_6.setBuddy(self.lineEdit_2)
        self.label_7.setBuddy(self.lineEdit_3)

        self.retranslateUi(Betty_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Betty_MainWindow)

    def retranslateUi(self, Betty_MainWindow):
        Betty_MainWindow.setWindowTitle(QtGui.QApplication.translate("Betty_MainWindow", "Betty", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Betty_MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("Betty_MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Betty_MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("Betty_MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.raceDockWidget.setWindowTitle(QtGui.QApplication.translate("Betty_MainWindow", "Race Information", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Betty_MainWindow", "Race &Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Betty_MainWindow", "Race &Course", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Betty_MainWindow", "Ascot", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Betty_MainWindow", "Aintree", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Betty_MainWindow", "Cheltenham", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Betty_MainWindow", "Kempton", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Betty_MainWindow", "Newmarket", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Betty_MainWindow", "&Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Betty_MainWindow", "&Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Betty_MainWindow", "Race C&lass", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("Betty_MainWindow", "Class A", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("Betty_MainWindow", "Class B", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(2, QtGui.QApplication.translate("Betty_MainWindow", "Class C", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(3, QtGui.QApplication.translate("Betty_MainWindow", "Class D", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Betty_MainWindow", "Prize Money", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox.setPrefix(QtGui.QApplication.translate("Betty_MainWindow", "£", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("Betty_MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Betty_MainWindow", "&Odds", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Betty_MainWindow", "D&ecimal", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Betty_MainWindow", "&Betfair", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("Betty_MainWindow", "&Fractional", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Betty_MainWindow", "Download Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Betty_MainWindow", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Betty_MainWindow", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("Betty_MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setToolTip(QtGui.QApplication.translate("Betty_MainWindow", "Create a new race", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setStatusTip(QtGui.QApplication.translate("Betty_MainWindow", "Create a new race", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("Betty_MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("Betty_MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setToolTip(QtGui.QApplication.translate("Betty_MainWindow", "Open a race file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("Betty_MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("Betty_MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("Betty_MainWindow", "Save this race", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("Betty_MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownload.setText(QtGui.QApplication.translate("Betty_MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownload.setToolTip(QtGui.QApplication.translate("Betty_MainWindow", "Download race information", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownload.setShortcut(QtGui.QApplication.translate("Betty_MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("Betty_MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setToolTip(QtGui.QApplication.translate("Betty_MainWindow", "Quit Betty", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_Files.setText(QtGui.QApplication.translate("Betty_MainWindow", "Recent Files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("Betty_MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setToolTip(QtGui.QApplication.translate("Betty_MainWindow", "Save this race in a new file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setShortcut(QtGui.QApplication.translate("Betty_MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setText(QtGui.QApplication.translate("Betty_MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setToolTip(QtGui.QApplication.translate("Betty_MainWindow", "Print this race", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setShortcut(QtGui.QApplication.translate("Betty_MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))

import Betty_rc
