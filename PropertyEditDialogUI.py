# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PropertyEditDialog.ui'
#
# Created: Fri Mar 01 15:06:08 2013
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

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName(_fromUtf8("mainDialog"))
        mainDialog.resize(456, 340)
        self.verticalLayout = QtGui.QVBoxLayout(mainDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.titleGrid = QtGui.QGridLayout()
        self.titleGrid.setObjectName(_fromUtf8("titleGrid"))
        self.titleLabel = QtGui.QLabel(mainDialog)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.titleGrid.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.titleLineEdit = QtGui.QLineEdit(mainDialog)
        self.titleLineEdit.setObjectName(_fromUtf8("titleLineEdit"))
        self.titleGrid.addWidget(self.titleLineEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.titleGrid)
        self.descriptionGrid = QtGui.QGridLayout()
        self.descriptionGrid.setObjectName(_fromUtf8("descriptionGrid"))
        self.descriptionLabel = QtGui.QLabel(mainDialog)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.descriptionGrid.addWidget(self.descriptionLabel, 0, 0, 1, 1)
        self.descriptionLineEdit = QtGui.QLineEdit(mainDialog)
        self.descriptionLineEdit.setObjectName(_fromUtf8("descriptionLineEdit"))
        self.descriptionGrid.addWidget(self.descriptionLineEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.descriptionGrid)
        self.line = QtGui.QFrame(mainDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.gravityGrid = QtGui.QGridLayout()
        self.gravityGrid.setObjectName(_fromUtf8("gravityGrid"))
        self.gravityLabel = QtGui.QLabel(mainDialog)
        self.gravityLabel.setObjectName(_fromUtf8("gravityLabel"))
        self.gravityGrid.addWidget(self.gravityLabel, 0, 0, 1, 1)
        self.gravityLineEdit = QtGui.QLineEdit(mainDialog)
        self.gravityLineEdit.setObjectName(_fromUtf8("gravityLineEdit"))
        self.gravityGrid.addWidget(self.gravityLineEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gravityGrid)
        self.dampingGrid = QtGui.QGridLayout()
        self.dampingGrid.setObjectName(_fromUtf8("dampingGrid"))
        self.dampingLabel = QtGui.QLabel(mainDialog)
        self.dampingLabel.setObjectName(_fromUtf8("dampingLabel"))
        self.dampingGrid.addWidget(self.dampingLabel, 0, 0, 1, 1)
        self.dampingLineEdit = QtGui.QLineEdit(mainDialog)
        self.dampingLineEdit.setObjectName(_fromUtf8("dampingLineEdit"))
        self.dampingGrid.addWidget(self.dampingLineEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.dampingGrid)
        self.sizeGrid = QtGui.QGridLayout()
        self.sizeGrid.setObjectName(_fromUtf8("sizeGrid"))
        self.sizeLabel = QtGui.QLabel(mainDialog)
        self.sizeLabel.setObjectName(_fromUtf8("sizeLabel"))
        self.sizeGrid.addWidget(self.sizeLabel, 0, 0, 1, 1)
        self.sizeLineEdit = QtGui.QLineEdit(mainDialog)
        self.sizeLineEdit.setObjectName(_fromUtf8("sizeLineEdit"))
        self.sizeGrid.addWidget(self.sizeLineEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.sizeGrid)

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(_translate("mainDialog", "Dialog", None))
        self.titleLabel.setText(_translate("mainDialog", "title", None))
        self.descriptionLabel.setText(_translate("mainDialog", "description", None))
        self.gravityLabel.setText(_translate("mainDialog", "gravity", None))
        self.dampingLabel.setText(_translate("mainDialog", "damping", None))
        self.sizeLabel.setText(_translate("mainDialog", "size", None))

