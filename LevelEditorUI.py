# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LevelEditor.ui'
#
# Created: Fri Mar 01 14:49:23 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(800, 600)
        self.mainWidget = QtGui.QWidget(mainWindow)
        self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.mainWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.mainWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout.addWidget(self.graphicsView)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.BoxButton = QtGui.QPushButton(self.mainWidget)
        self.BoxButton.setObjectName(_fromUtf8("BoxButton"))
        self.gridLayout.addWidget(self.BoxButton, 0, 0, 1, 1)
        self.CircleButton = QtGui.QPushButton(self.mainWidget)
        self.CircleButton.setObjectName(_fromUtf8("CircleButton"))
        self.gridLayout.addWidget(self.CircleButton, 1, 0, 1, 1)
        self.SegmentButton = QtGui.QPushButton(self.mainWidget)
        self.SegmentButton.setObjectName(_fromUtf8("SegmentButton"))
        self.gridLayout.addWidget(self.SegmentButton, 2, 0, 1, 1)
        self.BoundButton = QtGui.QPushButton(self.mainWidget)
        self.BoundButton.setObjectName(_fromUtf8("BoundButton"))
        self.gridLayout.addWidget(self.BoundButton, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        mainWindow.setCentralWidget(self.mainWidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(mainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(mainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSave = QtGui.QAction(mainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionGeneral = QtGui.QAction(mainWindow)
        self.actionGeneral.setObjectName(_fromUtf8("actionGeneral"))
        self.actionInfo = QtGui.QAction(mainWindow)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionGeneral)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow", None))
        self.BoxButton.setText(_translate("mainWindow", "Box", None))
        self.CircleButton.setText(_translate("mainWindow", "Circle", None))
        self.SegmentButton.setText(_translate("mainWindow", "Segment", None))
        self.BoundButton.setText(_translate("mainWindow", "Bound", None))
        self.menuFile.setTitle(_translate("mainWindow", "File", None))
        self.menuEdit.setTitle(_translate("mainWindow", "Edit", None))
        self.actionOpen.setText(_translate("mainWindow", "Open", None))
        self.actionExit.setText(_translate("mainWindow", "Exit", None))
        self.actionSave.setText(_translate("mainWindow", "Save", None))
        self.actionGeneral.setText(_translate("mainWindow", "General/Info", None))
        self.actionInfo.setText(_translate("mainWindow", "Info", None))

