# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShapeEdit.ui'
#
# Created: Sun Mar 03 13:41:04 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(382, 391)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 340, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 0, 363, 326))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.roleEdit = QtGui.QLineEdit(self.widget)
        self.roleEdit.setObjectName(_fromUtf8("roleEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.roleEdit)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.label)
        self.xEdit = QtGui.QLineEdit(self.widget)
        self.xEdit.setObjectName(_fromUtf8("xEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.xEdit)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_2)
        self.yEdit = QtGui.QLineEdit(self.widget)
        self.yEdit.setObjectName(_fromUtf8("yEdit"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.yEdit)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_3)
        self.wEdit = QtGui.QLineEdit(self.widget)
        self.wEdit.setObjectName(_fromUtf8("wEdit"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.wEdit)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.LabelRole, self.label_4)
        self.hEdit = QtGui.QLineEdit(self.widget)
        self.hEdit.setObjectName(_fromUtf8("hEdit"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.FieldRole, self.hEdit)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(16, QtGui.QFormLayout.SpanningRole, self.label_5)
        self.rEdit = QtGui.QLineEdit(self.widget)
        self.rEdit.setObjectName(_fromUtf8("rEdit"))
        self.formLayout.setWidget(17, QtGui.QFormLayout.FieldRole, self.rEdit)
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_10)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.x1Edit = QtGui.QLineEdit(self.widget)
        self.x1Edit.setObjectName(_fromUtf8("x1Edit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.x1Edit)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.x2Edit = QtGui.QLineEdit(self.widget)
        self.x2Edit.setObjectName(_fromUtf8("x2Edit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.x2Edit)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.y1Edit = QtGui.QLineEdit(self.widget)
        self.y1Edit.setObjectName(_fromUtf8("y1Edit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.y1Edit)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.y2Edit = QtGui.QLineEdit(self.widget)
        self.y2Edit.setObjectName(_fromUtf8("y2Edit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.y2Edit)
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_11)
        self.thicknessEdit = QtGui.QLineEdit(self.widget)
        self.thicknessEdit.setObjectName(_fromUtf8("thicknessEdit"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.thicknessEdit)
        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_12)
        self.frictionEdit = QtGui.QLineEdit(self.widget)
        self.frictionEdit.setObjectName(_fromUtf8("frictionEdit"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.frictionEdit)
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_13)
        self.elasticityEdit = QtGui.QLineEdit(self.widget)
        self.elasticityEdit.setObjectName(_fromUtf8("elasticityEdit"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.elasticityEdit)
        self.horizontalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "x", None))
        self.label_2.setText(_translate("Dialog", "y", None))
        self.label_3.setText(_translate("Dialog", "w", None))
        self.label_4.setText(_translate("Dialog", "h", None))
        self.label_5.setText(_translate("Dialog", "r", None))
        self.label_10.setText(_translate("Dialog", "role", None))
        self.label_6.setText(_translate("Dialog", "x1", None))
        self.label_7.setText(_translate("Dialog", "x2", None))
        self.label_8.setText(_translate("Dialog", "y1", None))
        self.label_9.setText(_translate("Dialog", "y2", None))
        self.label_11.setText(_translate("Dialog", "thickness", None))
        self.label_12.setText(_translate("Dialog", "friction", None))
        self.label_13.setText(_translate("Dialog", "elasticity", None))

