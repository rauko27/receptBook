# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Recept.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_recept(object):
    def setupUi(self, recept):
        recept.setObjectName("recept")
        recept.resize(500, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(recept)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_recept = QtWidgets.QLabel(recept)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name_recept.setFont(font)
        self.name_recept.setStyleSheet("font-weight: bold;\n"
"color: #00007f;\n"
"")
        self.name_recept.setObjectName("name_recept")
        self.verticalLayout.addWidget(self.name_recept, 0, QtCore.Qt.AlignHCenter)
        self.list_ingr = QtWidgets.QTextBrowser(recept)
        self.list_ingr.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.list_ingr.setFont(font)
        self.list_ingr.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.list_ingr.setObjectName("list_ingr")
        self.verticalLayout.addWidget(self.list_ingr)
        self.disc_recept = QtWidgets.QTextBrowser(recept)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.disc_recept.setFont(font)
        self.disc_recept.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.disc_recept.setObjectName("disc_recept")
        self.verticalLayout.addWidget(self.disc_recept)
        self.quitBtn = QtWidgets.QPushButton(recept)
        self.quitBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.quitBtn.setFont(font)
        self.quitBtn.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
"font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 15px;\n"
"color: #00007f;\n"
"background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:hover:focus {\n"
"font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 15px;\n"
"color: #00007f;\n"
"background-color: #eaffff;\n"
"}\n"
"\n"
"QPushButton:pressed,QPushButton:pressed:focus {\n"
"font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 15px;\n"
"color: #fff;\n"
"background-color: #00007f;\n"
"}")
        self.quitBtn.setObjectName("quitBtn")
        self.verticalLayout.addWidget(self.quitBtn)

        self.retranslateUi(recept)
        self.quitBtn.clicked['bool'].connect(recept.close)
        QtCore.QMetaObject.connectSlotsByName(recept)

    def retranslateUi(self, recept):
        _translate = QtCore.QCoreApplication.translate
        recept.setWindowTitle(_translate("recept", "Form"))
        self.name_recept.setText(_translate("recept", "TextLabel"))
        self.quitBtn.setText(_translate("recept", "Закрыть"))

