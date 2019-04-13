# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alertWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 100)
        Dialog.setMinimumSize(QtCore.QSize(320, 100))
        Dialog.setMaximumSize(QtCore.QSize(320, 100))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setMinimumSize(QtCore.QSize(100, 30))
        self.buttonBox.setStyleSheet("QDialogButtonBox, QDialogButtonBox:focus, QDialogButtonBox:focus {\n"
"font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 15px;\n"
"color: #00007f;\n"
"background-color: #fff;\n"
"}\n"
"\n"
"QDialogButtonBox:hover, QDialogButtonBox:hover:focus {\n"
"font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 15px;\n"
"color: #00007f;\n"
"background-color: #eaffff;\n"
"}\n"
"\n"
"QDialogButtonBox:pressed,QDialogButtonBox:pressed:focus {\n"
"font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 15px;\n"
"color: #fff;\n"
"background-color: #00007f;\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font-weight: bold;\n"
"color: #00007f;\n"
"")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Внимание"))
        self.label.setText(_translate("Dialog", "Рецепт не найден"))

