# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PROGRAMS\NTO\GUI\qt_Karno\menu_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.title.setAutoFillBackground(False)
        self.title.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setScaledContents(False)
        self.title.setOpenExternalLinks(False)
        self.title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setEnabled(True)
        self.table.setMouseTracking(True)
        self.table.setTabletTracking(True)
        self.table.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table.setAutoFillBackground(False)
        self.table.setTabKeyNavigation(True)
        self.table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.table.setGridStyle(QtCore.Qt.SolidLine)
        self.table.setObjectName("table")
        self.table.setColumnCount(8)
        self.table.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("-")
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        brush = QtGui.QBrush(QtGui.QColor(109, 0, 218))
        brush.setStyle(QtCore.Qt.Dense4Pattern)
        item.setForeground(brush)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("9")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setStrikeOut(False)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.Dense5Pattern)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(1, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(2, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(3, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(3, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(4, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(4, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(5, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(5, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(5, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(6, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(6, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(6, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(7, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(7, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table.setItem(7, 7, item)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setDefaultSectionSize(100)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.horizontalHeader().setMinimumSectionSize(41)
        self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(True)
        self.table.verticalHeader().setDefaultSectionSize(59)
        self.table.verticalHeader().setHighlightSections(True)
        self.table.verticalHeader().setMinimumSectionSize(21)
        self.table.verticalHeader().setSortIndicatorShown(True)
        self.table.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.table, 1, 0, 1, 1)
        self.buttonFile = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.buttonFile.setObjectName("buttonFile")
        self.gridLayout.addWidget(self.buttonFile, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Karno</p></body></html>"))
        self.table.setSortingEnabled(False)
        item = self.table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "-"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "-"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        item = self.table.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table.item(0, 1)
        item.setText(_translate("MainWindow", "2"))
        item = self.table.item(0, 2)
        item.setText(_translate("MainWindow", "3"))
        item = self.table.item(0, 3)
        item.setText(_translate("MainWindow", "4"))
        item = self.table.item(0, 4)
        item.setText(_translate("MainWindow", "5"))
        item = self.table.item(0, 5)
        item.setText(_translate("MainWindow", "6"))
        item = self.table.item(0, 6)
        item.setText(_translate("MainWindow", "7"))
        item = self.table.item(0, 7)
        item.setText(_translate("MainWindow", "8"))
        item = self.table.item(1, 1)
        item.setText(_translate("MainWindow", "10"))
        item = self.table.item(1, 2)
        item.setText(_translate("MainWindow", "11"))
        item = self.table.item(1, 3)
        item.setText(_translate("MainWindow", "12"))
        item = self.table.item(1, 4)
        item.setText(_translate("MainWindow", "13"))
        item = self.table.item(1, 5)
        item.setText(_translate("MainWindow", "14"))
        item = self.table.item(1, 6)
        item.setText(_translate("MainWindow", "15"))
        item = self.table.item(1, 7)
        item.setText(_translate("MainWindow", "16"))
        item = self.table.item(2, 0)
        item.setText(_translate("MainWindow", "17"))
        item = self.table.item(2, 1)
        item.setText(_translate("MainWindow", "18"))
        item = self.table.item(2, 2)
        item.setText(_translate("MainWindow", "19"))
        item = self.table.item(2, 3)
        item.setText(_translate("MainWindow", "20"))
        item = self.table.item(2, 4)
        item.setText(_translate("MainWindow", "21"))
        item = self.table.item(2, 5)
        item.setText(_translate("MainWindow", "22"))
        item = self.table.item(2, 6)
        item.setText(_translate("MainWindow", "23"))
        item = self.table.item(2, 7)
        item.setText(_translate("MainWindow", "24"))
        item = self.table.item(3, 0)
        item.setText(_translate("MainWindow", "25"))
        item = self.table.item(3, 1)
        item.setText(_translate("MainWindow", "26"))
        item = self.table.item(3, 2)
        item.setText(_translate("MainWindow", "27"))
        item = self.table.item(3, 3)
        item.setText(_translate("MainWindow", "28"))
        item = self.table.item(3, 4)
        item.setText(_translate("MainWindow", "29"))
        item = self.table.item(3, 5)
        item.setText(_translate("MainWindow", "30"))
        item = self.table.item(3, 6)
        item.setText(_translate("MainWindow", "31"))
        item = self.table.item(3, 7)
        item.setText(_translate("MainWindow", "32"))
        item = self.table.item(4, 0)
        item.setText(_translate("MainWindow", "33"))
        item = self.table.item(4, 1)
        item.setText(_translate("MainWindow", "34"))
        item = self.table.item(4, 2)
        item.setText(_translate("MainWindow", "35"))
        item = self.table.item(4, 3)
        item.setText(_translate("MainWindow", "36"))
        item = self.table.item(4, 4)
        item.setText(_translate("MainWindow", "37"))
        item = self.table.item(4, 5)
        item.setText(_translate("MainWindow", "38"))
        item = self.table.item(4, 6)
        item.setText(_translate("MainWindow", "39"))
        item = self.table.item(4, 7)
        item.setText(_translate("MainWindow", "40"))
        item = self.table.item(5, 0)
        item.setText(_translate("MainWindow", "41"))
        item = self.table.item(5, 1)
        item.setText(_translate("MainWindow", "42"))
        item = self.table.item(5, 2)
        item.setText(_translate("MainWindow", "43"))
        item = self.table.item(5, 3)
        item.setText(_translate("MainWindow", "44"))
        item = self.table.item(5, 4)
        item.setText(_translate("MainWindow", "45"))
        item = self.table.item(5, 5)
        item.setText(_translate("MainWindow", "46"))
        item = self.table.item(5, 6)
        item.setText(_translate("MainWindow", "47"))
        item = self.table.item(5, 7)
        item.setText(_translate("MainWindow", "48"))
        item = self.table.item(6, 0)
        item.setText(_translate("MainWindow", "49"))
        item = self.table.item(6, 1)
        item.setText(_translate("MainWindow", "50"))
        item = self.table.item(6, 2)
        item.setText(_translate("MainWindow", "51"))
        item = self.table.item(6, 3)
        item.setText(_translate("MainWindow", "52"))
        item = self.table.item(6, 4)
        item.setText(_translate("MainWindow", "53"))
        item = self.table.item(6, 5)
        item.setText(_translate("MainWindow", "54"))
        item = self.table.item(6, 6)
        item.setText(_translate("MainWindow", "55"))
        item = self.table.item(6, 7)
        item.setText(_translate("MainWindow", "56"))
        item = self.table.item(7, 0)
        item.setText(_translate("MainWindow", "57"))
        item = self.table.item(7, 1)
        item.setText(_translate("MainWindow", "58"))
        item = self.table.item(7, 2)
        item.setText(_translate("MainWindow", "59"))
        item = self.table.item(7, 3)
        item.setText(_translate("MainWindow", "60"))
        item = self.table.item(7, 4)
        item.setText(_translate("MainWindow", "61"))
        item = self.table.item(7, 5)
        item.setText(_translate("MainWindow", "62"))
        item = self.table.item(7, 6)
        item.setText(_translate("MainWindow", "63"))
        item = self.table.item(7, 7)
        item.setText(_translate("MainWindow", "64"))
        self.table.setSortingEnabled(__sortingEnabled)
        self.buttonFile.setText(_translate("MainWindow", "Open File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())