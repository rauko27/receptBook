# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setMaximumSize(QtCore.QSize(600, 800))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("font-weight: bold;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.tabWidget.setObjectName("tabWidget")
        self.search = QtWidgets.QWidget()
        self.search.setObjectName("search")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.search)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.srch_btn = QtWidgets.QPushButton(self.search)
        self.srch_btn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.srch_btn.setFont(font)
        self.srch_btn.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
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
        self.srch_btn.setObjectName("srch_btn")
        self.gridLayout_2.addWidget(self.srch_btn, 0, 1, 1, 1)
        self.srch_line = QtWidgets.QLineEdit(self.search)
        self.srch_line.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.srch_line.setFont(font)
        self.srch_line.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.srch_line.setInputMask("")
        self.srch_line.setCursorPosition(0)
        self.srch_line.setClearButtonEnabled(True)
        self.srch_line.setObjectName("srch_line")
        self.gridLayout_2.addWidget(self.srch_line, 0, 0, 1, 1)
        self.widget = QtWidgets.QScrollArea(self.search)
        self.widget.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.widget.setWidgetResizable(True)
        self.widget.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.widget.setObjectName("widget")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 556, 642))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.widget, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.search)
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
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.tabWidget.addTab(self.search, "")
        self.new_recipe = QtWidgets.QWidget()
        self.new_recipe.setObjectName("new_recipe")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.new_recipe)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.add_recept = QtWidgets.QPushButton(self.new_recipe)
        self.add_recept.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_recept.setFont(font)
        self.add_recept.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
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
        self.add_recept.setObjectName("add_recept")
        self.gridLayout_3.addWidget(self.add_recept, 5, 2, 1, 3)
        self.description = QtWidgets.QLabel(self.new_recipe)
        self.description.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.description.setFont(font)
        self.description.setStyleSheet("font-weight: bold;\n"
"color: #00007f;")
        self.description.setObjectName("description")
        self.gridLayout_3.addWidget(self.description, 4, 0, 1, 1)
        self.list_ingr = QtWidgets.QComboBox(self.new_recipe)
        self.list_ingr.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_ingr.setFont(font)
        self.list_ingr.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.list_ingr.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 5px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.list_ingr.setEditable(True)
        self.list_ingr.setFrame(True)
        self.list_ingr.setObjectName("list_ingr")
        self.list_ingr.addItem("")
        self.list_ingr.setItemText(0, "")
        self.gridLayout_3.addWidget(self.list_ingr, 1, 2, 1, 1)
        self.name_recipe = QtWidgets.QLabel(self.new_recipe)
        self.name_recipe.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_recipe.setFont(font)
        self.name_recipe.setStyleSheet("font-weight: bold;\n"
"color: #00007f;\n"
"")
        self.name_recipe.setObjectName("name_recipe")
        self.gridLayout_3.addWidget(self.name_recipe, 0, 0, 1, 1)
        self.list_ing_n = QtWidgets.QTextBrowser(self.new_recipe)
        self.list_ing_n.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_ing_n.setFont(font)
        self.list_ing_n.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.list_ing_n.setObjectName("list_ing_n")
        self.gridLayout_3.addWidget(self.list_ing_n, 2, 2, 1, 3)
        self.list_desc = QtWidgets.QTextEdit(self.new_recipe)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_desc.setFont(font)
        self.list_desc.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.list_desc.setObjectName("list_desc")
        self.gridLayout_3.addWidget(self.list_desc, 4, 2, 1, 3)
        self.ingr = QtWidgets.QLabel(self.new_recipe)
        self.ingr.setMinimumSize(QtCore.QSize(79, 0))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ingr.setFont(font)
        self.ingr.setStyleSheet("font-weight: bold;\n"
"color: #00007f;")
        self.ingr.setObjectName("ingr")
        self.gridLayout_3.addWidget(self.ingr, 1, 0, 1, 1)
        self.add_ingr = QtWidgets.QPushButton(self.new_recipe)
        self.add_ingr.setMinimumSize(QtCore.QSize(100, 30))
        self.add_ingr.setMaximumSize(QtCore.QSize(84, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_ingr.setFont(font)
        self.add_ingr.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
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
"}\n"
"")
        self.add_ingr.setObjectName("add_ingr")
        self.gridLayout_3.addWidget(self.add_ingr, 1, 4, 1, 1)
        self.name = QtWidgets.QLineEdit(self.new_recipe)
        self.name.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.name.setObjectName("name")
        self.gridLayout_3.addWidget(self.name, 0, 2, 1, 3)
        self.vol_ing = QtWidgets.QLineEdit(self.new_recipe)
        self.vol_ing.setMinimumSize(QtCore.QSize(0, 30))
        self.vol_ing.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.vol_ing.setFont(font)
        self.vol_ing.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.vol_ing.setObjectName("vol_ing")
        self.gridLayout_3.addWidget(self.vol_ing, 1, 3, 1, 1)
        self.cln_ing = QtWidgets.QPushButton(self.new_recipe)
        self.cln_ing.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cln_ing.setFont(font)
        self.cln_ing.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
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
"}\n"
"")
        self.cln_ing.setObjectName("cln_ing")
        self.gridLayout_3.addWidget(self.cln_ing, 3, 4, 1, 1)
        self.tabWidget.addTab(self.new_recipe, "")
        self.edit_recipe = QtWidgets.QWidget()
        self.edit_recipe.setObjectName("edit_recipe")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.edit_recipe)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.del_btn_e = QtWidgets.QPushButton(self.edit_recipe)
        self.del_btn_e.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.del_btn_e.setFont(font)
        self.del_btn_e.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
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
"}\n"
"")
        self.del_btn_e.setObjectName("del_btn_e")
        self.gridLayout_4.addWidget(self.del_btn_e, 7, 3, 1, 1)
        self.description_2 = QtWidgets.QLabel(self.edit_recipe)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.description_2.setFont(font)
        self.description_2.setObjectName("description_2")
        self.gridLayout_4.addWidget(self.description_2, 6, 0, 1, 1)
        self.list_desc_2 = QtWidgets.QTextEdit(self.edit_recipe)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_desc_2.setFont(font)
        self.list_desc_2.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.list_desc_2.setObjectName("list_desc_2")
        self.gridLayout_4.addWidget(self.list_desc_2, 6, 1, 1, 3)
        self.save_btn_e = QtWidgets.QPushButton(self.edit_recipe)
        self.save_btn_e.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn_e.setFont(font)
        self.save_btn_e.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
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
"}\n"
"")
        self.save_btn_e.setObjectName("save_btn_e")
        self.gridLayout_4.addWidget(self.save_btn_e, 7, 1, 1, 1)
        self.name_recipe_2 = QtWidgets.QLabel(self.edit_recipe)
        self.name_recipe_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_recipe_2.setFont(font)
        self.name_recipe_2.setObjectName("name_recipe_2")
        self.gridLayout_4.addWidget(self.name_recipe_2, 2, 0, 1, 1)
        self.name_2 = QtWidgets.QLineEdit(self.edit_recipe)
        self.name_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_2.setFont(font)
        self.name_2.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.name_2.setObjectName("name_2")
        self.gridLayout_4.addWidget(self.name_2, 2, 1, 1, 3)
        self.list_ingr_2 = QtWidgets.QComboBox(self.edit_recipe)
        self.list_ingr_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.list_ingr_2.setFont(font)
        self.list_ingr_2.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.list_ingr_2.setEditable(True)
        self.list_ingr_2.setCurrentText("")
        self.list_ingr_2.setFrame(True)
        self.list_ingr_2.setObjectName("list_ingr_2")
        self.list_ingr_2.addItem("")
        self.list_ingr_2.setItemText(0, "")
        self.gridLayout_4.addWidget(self.list_ingr_2, 3, 1, 1, 1)
        self.add_ingr_2 = QtWidgets.QPushButton(self.edit_recipe)
        self.add_ingr_2.setMinimumSize(QtCore.QSize(100, 30))
        self.add_ingr_2.setMaximumSize(QtCore.QSize(84, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_ingr_2.setFont(font)
        self.add_ingr_2.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
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
"}\n"
"")
        self.add_ingr_2.setObjectName("add_ingr_2")
        self.gridLayout_4.addWidget(self.add_ingr_2, 3, 3, 1, 1)
        self.ingr_2 = QtWidgets.QLabel(self.edit_recipe)
        self.ingr_2.setMinimumSize(QtCore.QSize(79, 0))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ingr_2.setFont(font)
        self.ingr_2.setObjectName("ingr_2")
        self.gridLayout_4.addWidget(self.ingr_2, 3, 0, 1, 1)
        self.list_ing_e = QtWidgets.QTextBrowser(self.edit_recipe)
        self.list_ing_e.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_ing_e.setFont(font)
        self.list_ing_e.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.list_ing_e.setObjectName("list_ing_e")
        self.gridLayout_4.addWidget(self.list_ing_e, 4, 1, 1, 3)
        self.cln_btn_e = QtWidgets.QPushButton(self.edit_recipe)
        self.cln_btn_e.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cln_btn_e.setFont(font)
        self.cln_btn_e.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
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
"}\n"
"")
        self.cln_btn_e.setObjectName("cln_btn_e")
        self.gridLayout_4.addWidget(self.cln_btn_e, 5, 3, 1, 1)
        self.srch_edit_btn = QtWidgets.QPushButton(self.edit_recipe)
        self.srch_edit_btn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.srch_edit_btn.setFont(font)
        self.srch_edit_btn.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
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
"}\n"
"")
        self.srch_edit_btn.setObjectName("srch_edit_btn")
        self.gridLayout_4.addWidget(self.srch_edit_btn, 1, 3, 1, 1)
        self.vol_ing_e = QtWidgets.QLineEdit(self.edit_recipe)
        self.vol_ing_e.setMinimumSize(QtCore.QSize(0, 30))
        self.vol_ing_e.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.vol_ing_e.setFont(font)
        self.vol_ing_e.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.vol_ing_e.setObjectName("vol_ing_e")
        self.gridLayout_4.addWidget(self.vol_ing_e, 3, 2, 1, 1)
        self.src_edit_line = QtWidgets.QLineEdit(self.edit_recipe)
        self.src_edit_line.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.src_edit_line.setFont(font)
        self.src_edit_line.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.src_edit_line.setObjectName("src_edit_line")
        self.gridLayout_4.addWidget(self.src_edit_line, 1, 1, 1, 2)
        self.tabWidget.addTab(self.edit_recipe, "")
        self.directory = QtWidgets.QWidget()
        self.directory.setObjectName("directory")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.directory)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.table_ingr = QtWidgets.QTableWidget(self.directory)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.table_ingr.setFont(font)
        self.table_ingr.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.table_ingr.setLineWidth(0)
        self.table_ingr.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_ingr.setTabKeyNavigation(False)
        self.table_ingr.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.table_ingr.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_ingr.setShowGrid(True)
        self.table_ingr.setGridStyle(QtCore.Qt.DotLine)
        self.table_ingr.setRowCount(0)
        self.table_ingr.setColumnCount(3)
        self.table_ingr.setObjectName("table_ingr")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        item.setFont(font)
        self.table_ingr.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        item.setFont(font)
        self.table_ingr.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        item.setFont(font)
        self.table_ingr.setHorizontalHeaderItem(2, item)
        self.table_ingr.horizontalHeader().setCascadingSectionResizes(True)
        self.table_ingr.horizontalHeader().setDefaultSectionSize(175)
        self.table_ingr.horizontalHeader().setHighlightSections(True)
        self.table_ingr.horizontalHeader().setMinimumSectionSize(50)
        self.table_ingr.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.table_ingr, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.directory)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.disc_add_ingr = QtWidgets.QPushButton(self.frame)
        self.disc_add_ingr.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.disc_add_ingr.setFont(font)
        self.disc_add_ingr.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
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
"}\n"
"")
        self.disc_add_ingr.setObjectName("disc_add_ingr")
        self.gridLayout_5.addWidget(self.disc_add_ingr, 1, 1, 1, 1)
        self.disc_ingr = QtWidgets.QLabel(self.frame)
        self.disc_ingr.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.disc_ingr.setFont(font)
        self.disc_ingr.setObjectName("disc_ingr")
        self.gridLayout_5.addWidget(self.disc_ingr, 0, 0, 1, 1)
        self.disc_name_ingr = QtWidgets.QLineEdit(self.frame)
        self.disc_name_ingr.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.disc_name_ingr.setFont(font)
        self.disc_name_ingr.setStyleSheet("font-weight: bold;\n"
"border: 1px solid #00007f;\n"
"border-radius: 10px;\n"
"color: #00007f;\n"
"background-color: #fff;")
        self.disc_name_ingr.setObjectName("disc_name_ingr")
        self.gridLayout_5.addWidget(self.disc_name_ingr, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget.addTab(self.directory, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.list_ingr.setCurrentIndex(0)
        self.cln_ing.clicked.connect(self.list_ing_n.clear)
        self.cln_btn_e.clicked.connect(self.list_ing_e.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.srch_line, self.srch_btn)
        MainWindow.setTabOrder(self.srch_btn, self.name)
        MainWindow.setTabOrder(self.name, self.list_ingr)
        MainWindow.setTabOrder(self.list_ingr, self.vol_ing)
        MainWindow.setTabOrder(self.vol_ing, self.add_ingr)
        MainWindow.setTabOrder(self.add_ingr, self.list_desc)
        MainWindow.setTabOrder(self.list_desc, self.add_recept)
        MainWindow.setTabOrder(self.add_recept, self.src_edit_line)
        MainWindow.setTabOrder(self.src_edit_line, self.srch_edit_btn)
        MainWindow.setTabOrder(self.srch_edit_btn, self.name_2)
        MainWindow.setTabOrder(self.name_2, self.list_ingr_2)
        MainWindow.setTabOrder(self.list_ingr_2, self.vol_ing_e)
        MainWindow.setTabOrder(self.vol_ing_e, self.add_ingr_2)
        MainWindow.setTabOrder(self.add_ingr_2, self.list_desc_2)
        MainWindow.setTabOrder(self.list_desc_2, self.save_btn_e)
        MainWindow.setTabOrder(self.save_btn_e, self.del_btn_e)
        MainWindow.setTabOrder(self.del_btn_e, self.disc_name_ingr)
        MainWindow.setTabOrder(self.disc_name_ingr, self.disc_add_ingr)
        MainWindow.setTabOrder(self.disc_add_ingr, self.table_ingr)
        MainWindow.setTabOrder(self.table_ingr, self.list_ing_e)
        MainWindow.setTabOrder(self.list_ing_e, self.cln_btn_e)
        MainWindow.setTabOrder(self.cln_btn_e, self.list_ing_n)
        MainWindow.setTabOrder(self.list_ing_n, self.cln_ing)
        MainWindow.setTabOrder(self.cln_ing, self.widget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Книга рецептов"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>Книга рецептов</p></body></html>"))
        self.srch_btn.setText(_translate("MainWindow", "Поиск"))
        self.srch_line.setPlaceholderText(_translate("MainWindow", "Введите название рецепта..."))
        self.label.setText(_translate("MainWindow", "Результат поиска:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search), _translate("MainWindow", "Поиск"))
        self.add_recept.setText(_translate("MainWindow", "Создать"))
        self.description.setText(_translate("MainWindow", "Описание"))
        self.name_recipe.setText(_translate("MainWindow", "Название"))
        self.list_desc.setPlaceholderText(_translate("MainWindow", "Опишите приготовление"))
        self.ingr.setText(_translate("MainWindow", "Ингридиенты"))
        self.add_ingr.setText(_translate("MainWindow", "Добавить"))
        self.name.setPlaceholderText(_translate("MainWindow", "Введите название..."))
        self.vol_ing.setPlaceholderText(_translate("MainWindow", "Количество"))
        self.cln_ing.setText(_translate("MainWindow", "Очистить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new_recipe), _translate("MainWindow", "Новый рецепт"))
        self.del_btn_e.setText(_translate("MainWindow", "Удалить"))
        self.description_2.setText(_translate("MainWindow", "Описание"))
        self.save_btn_e.setText(_translate("MainWindow", "Сохранить"))
        self.name_recipe_2.setText(_translate("MainWindow", "Название"))
        self.name_2.setPlaceholderText(_translate("MainWindow", "Название..."))
        self.add_ingr_2.setText(_translate("MainWindow", "Добавить"))
        self.ingr_2.setText(_translate("MainWindow", "Ингридиенты"))
        self.cln_btn_e.setText(_translate("MainWindow", "Очистить"))
        self.srch_edit_btn.setText(_translate("MainWindow", "Поиск"))
        self.vol_ing_e.setPlaceholderText(_translate("MainWindow", "Количество"))
        self.src_edit_line.setPlaceholderText(_translate("MainWindow", "Введите название..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.edit_recipe), _translate("MainWindow", "Редактирование"))
        item = self.table_ingr.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table_ingr.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.table_ingr.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Действие"))
        self.disc_add_ingr.setText(_translate("MainWindow", "Добавить"))
        self.disc_ingr.setText(_translate("MainWindow", "Ингридиент"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.directory), _translate("MainWindow", "Справочники"))

