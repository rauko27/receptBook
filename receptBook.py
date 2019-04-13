from PyQt5 import QtWidgets
import sys
import sqlite3

from PyQt5.QtWidgets import QMessageBox

import MainWindow
from MainWindow import Ui_MainWindow
from alertWindow import Ui_Dialog
from Recept import Ui_recept
from createFrame import crF

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключение к бд
        self.conn = sqlite3.connect("receptBook.db")
        self.cursor = self.conn.cursor()

        # действия по кнопкам
        self.ui.disc_add_ingr.clicked.connect(self.direct)
        self.ui.disc_add_ingr.setAutoDefault(True)  # click on <Enter>
        self.ui.disc_name_ingr.returnPressed.connect(self.ui.disc_add_ingr.click)  # click on <Enter>

        self.ui.add_ingr.clicked.connect(self.add_to_ingr)
        self.ui.add_ingr.setAutoDefault(True)  # click on <Enter>

        self.ui.add_ingr_2.clicked.connect(self.add_to_ingr_e)
        self.ui.add_ingr_2.setAutoDefault(True)  # click on <Enter>

        self.ui.add_recept.clicked.connect(self.create_new_recept)
        self.ui.add_recept.setAutoDefault(True)  # click on <Enter>

        self.ui.srch_edit_btn.clicked.connect(self.edir_recept)
        self.ui.srch_edit_btn.setAutoDefault(True)  # click on <Enter>

        self.ui.save_btn_e.clicked.connect(self.save_change)
        self.ui.save_btn_e.setAutoDefault(True)  # click on <Enter>

        self.ui.srch_btn.clicked.connect(self.src_recept)
        self.ui.srch_btn.setAutoDefault(True)  # click on <Enter>
        self.ui.srch_line.returnPressed.connect(self.ui.srch_btn.click)  # click on <Enter>


        self.ui.del_btn_e.clicked.connect(self.del_recept)
        self.ui.del_btn_e.setAutoDefault(True)  # click on <Enter>

        # createFrame.pBtn.clicked.connect(self.open_recept())

        self.list_ingr = []
        self.list_ingr_e = []
        # self.desc_e = []


        # Вызов функций
        self.qComboBox()
        self.all_ing()


    # Добавление ингридиента в справочник
    def direct(self):
        try:
            name = self.ui.disc_name_ingr.text()
            if name != '':
                self.sql = "INSERT INTO indridient (name_ing) VALUES (?)"
                self.cursor.execute(self.sql, [name])
                self.conn.commit()
                self.ui.table_ingr.setRowCount(0)
                self.all_ing()
                self.textAlert = "Игридиент добавлен"
                self.alertWindow(self.textAlert)
                self.qComboBox()

        except:
            self.textAlert = "Такой ингридиент уже есть"
            self.alertWindow(self.textAlert)
        finally:
            self.ui.disc_name_ingr.clear()

    # Окно уведомлениq
    def alertWindow(self, textAlert):
        self.alertW = QtWidgets.QDialog()
        self.alertUi = Ui_Dialog()
        self.alertUi.setupUi(self.alertW)
        self.alertW.show()
        self.alertUi.label.setText(textAlert)


    # вывод всех ингридиентов в таблицу
    def all_ing(self):
        self.ui.table_ingr.setRowCount(0)
        self.cursor.execute("""SELECT * FROM indridient""")
        self.conn.commit()
        result = self.cursor.fetchall()
        for row, row_data in enumerate(result):
            self.ui.table_ingr.insertRow(row)
            for col, data in enumerate(row_data):
                id_ing = str(row_data[0])
                if id_ing == '':
                    break
                self.ui.table_ingr.setItem(row, col, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.table_ingr.setCellWidget(row, 2, self.btn_in_ing(id_ing))

    # кнопка удаления ингридиента
    def btn_in_ing(self, id_ing):
        self.btn = QtWidgets.QPushButton('Удалить')
        self.btn.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
                                    "font-weight: bold;\n"
                                    "border: 1px solid #00007f;\n"
                                    "border-radius: 10x;\n"
                                    "color: #00007f;\n"
                                    "background-color: #fff;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover, QPushButton:hover:focus {\n"
                                    "font-weight: bold;\n"
                                    "border: 1px solid #00007f;\n"
                                    "border-radius: 10px;\n"
                                    "color: #00007f;\n"
                                    "background-color: #eaffff;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed,QPushButton:pressed:focus {\n"
                                    "font-weight: bold;\n"
                                    "border: 1px solid #00007f;\n"
                                    "border-radius: 10px;\n"
                                    "color: #fff;\n"
                                    "background-color: #00007f;\n"
                                    "}")
        self.btn.setObjectName(id_ing)
        self.btn.clicked.connect(lambda: self.del_ing(id_ing))
        return self.btn

    # удаление ингридиента
    def del_ing(self, id_ing):
        reply = QMessageBox.question(self, ' ',
                                                 "Вы уверены что хотите удалить ингридиент?", QMessageBox.Yes |
                                                 QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            id_ing = int(id_ing)
            self.sql = "DELETE FROM indridient WHERE id =?"
            self.cursor.execute(self.sql, [(id_ing)])
            self.conn.commit()
            self.ui.table_ingr.setRowCount(0)
            self.all_ing()
            self.textAlert = "Ингридиент удален"
            self.alertWindow(self.textAlert)
            self.qComboBox()

    # Наполлнение выподающего спсика
    def qComboBox(self):
        self.ui.list_ingr.clear()
        self.ui.list_ingr_2.clear()
        self.ui.list_ingr.addItem('')
        self.ui.list_ingr_2.addItem('')

        self.cursor.execute("""SELECT * FROM indridient""")
        self.conn.commit()
        result = self.cursor.fetchall()
        for i in range(len(result)):
            id = str(result[i][0])
            name = result[i][1]
            self.ui.list_ingr.addItem(name, id)
            self.ui.list_ingr_2.addItem(name, id)

    # Добавдение ингридиентов создание
    def add_to_ingr(self):
        try:
            ingr = []
            id = self.ui.list_ingr.currentData()
            name = self.ui.list_ingr.currentText()
            vol = self.ui.vol_ing.text()
            self.ui.list_ing_n.append(name + ": " + vol)
            ingr.append(id)
            ingr.append(name)
            ingr.append(vol)
            self.list_ingr.append(ingr)
            self.ui.list_ingr.clearEditText()
            self.ui.vol_ing.clear()
            return ingr
        except:
            print("ошибка в добавлении ингридиента")

    # Добавдение ингридиентов редактирование
    def add_to_ingr_e(self):
        try:
            id = self.ui.list_ingr_2.currentData()
            name = self.ui.list_ingr_2.currentText()
            vol = self.ui.vol_ing_e.text()
            self.ui.list_ing_e.append(name + ": " + vol)
            self.list_ingr_e.append(id)
            self.list_ingr_e.append(name)
            self.list_ingr_e.append(vol)
            self.ui.list_ingr_2.clearEditText()
            self.ui.vol_ing_e.clear()
            self.ui.vol_ing.clear()
        except:
            print("a")

    # создание рецепта
    def create_new_recept(self):
        name = self.ui.name.text()
        ing_id = []
        for i in range(len(self.list_ingr)):
            c_ingr = self.list_ingr[i]
            for x in range(len(c_ingr)):
                id = c_ingr[0]
                vol = c_ingr[2]
                break
            ing_id.append(id)
            ing_id.append(vol)

        desc = self.ui.list_desc.toPlainText()
        desc = desc.splitlines()

        self.sql = "INSERT INTO recept (name) VALUES (?)"
        self.cursor.execute(self.sql, [name])
        id_recept = self.cursor.lastrowid

        for i in range(0,len(ing_id),2):
            id_ingr = ing_id[i]
            ing_vol = ing_id[i+1]
            self.sql = "INSERT INTO recept_ing (id_recept, id_ingr, vol_ing) VALUES (?,?,?)"
            self.cursor.execute(self.sql, [id_recept, id_ingr, ing_vol])

        for i in range(len(desc)):
            desc_row = desc[i]
            self.sql = "INSERT INTO description (id_recept, desc) VALUES (?,?)"
            self.cursor.execute(self.sql, [id_recept, desc_row])

        self.conn.commit()

        self.ui.name.clear()
        self.ui.list_ing_n.clear()
        self.ui.list_desc.clear()
        self.list_ingr.clear()

        self.textAlert = "Рецепт успешно добавлен"
        self.alertWindow(self.textAlert)

    # редактирование рецепта
    def edir_recept(self):
        try:
            self.ui.list_ing_e.clear()
            self.ui.list_desc_2.clear()

            rcpt = self.ui.src_edit_line.text()

            # вывод названия
            self.sql = "SELECT * FROM recept WHERE name=?"
            self.cursor.execute(self.sql,[(rcpt)])
            self.conn.commit()
            result = self.cursor.fetchall()
            for i in range(len(result)):
                rec = result[i]
                for r in range(len(rec)):
                    rec_id = rec[0]
                    rec_name = rec[1]
                    break
            self.ui.name_2.setText(rec_name)

            # вывод ингридиентов
            ing=[]
            self.sql = """SELECT i.id, i.name_ing, r.vol_ing
                                FROM indridient i
                                LEFT JOIN recept_ing r
                                ON r.id_ingr=i.id
                                WHERE r.id_recept=?"""
            self.cursor.execute(self.sql, [(rec_id)])
            self.conn.commit()
            result = self.cursor.fetchall()
            for i in range(len(result)):
                rec = result[i]
                for r in range(len(rec)):
                    ing_id = str(rec[0])
                    ing_name = rec[1]
                    vol_ing = str(rec[2])
                    break
                self.ui.list_ing_e.append(ing_name + ': ' + vol_ing)
                self.list_ingr_e.append(ing_id)
                self.list_ingr_e.append(ing_name)
                self.list_ingr_e.append(vol_ing)

            # вывод описания
            desc = []
            self.sql = """SELECT d.id, d.desc
                        FROM description d
                        LEFT JOIN recept r 
                        ON r.id = d.id_recept
                        WHERE r.id =?
                        ORDER BY d.id"""
            self.cursor.execute(self.sql, [(rec_id)])
            self.conn.commit()
            result = self.cursor.fetchall()
            for i in range(len(result)):
                rec = result[i]
                for r in range(len(rec)):
                    desc_name = rec[1]
                    break
                self.ui.list_desc_2.append(desc_name)
        except:
            self.textAlert = "Рецепт не найден"
            self.alertWindow(self.textAlert)

    # сохранение изменений
    def save_change(self):
        reply = QMessageBox.question(self, ' ',
                                         "Вы уверены что хотите изменить рецпт?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            name = self.ui.src_edit_line.text()
            self.sql = "SELECT id FROM recept WHERE name=?"
            self.cursor.execute(self.sql, [(name)])
            self.conn.commit()
            rec_id = self.cursor.fetchall()[0][0]
            rec_name = self.ui.name_2.text()

            desc = self.ui.list_desc_2.toPlainText()
            desc = desc.splitlines()

            self.sql = "UPDATE recept SET name=? WHERE id=?"
            self.cursor.execute(self.sql, [rec_name, rec_id])
            id_recept = rec_id
            self.conn.commit()

            self.sql = "DELETE FROM recept_ing WHERE id_recept=?"
            self.cursor.execute(self.sql, [id_recept])
            self.sql = "DELETE FROM description WHERE id_recept=?"
            self.cursor.execute(self.sql, [id_recept])

            for i in range(0,len(self.list_ingr_e),3):
                id_ingr = self.list_ingr_e[i]
                vol_ing = self.list_ingr_e[i+2]
                self.sql = "INSERT INTO recept_ing (id_recept, id_ingr, vol_ing) VALUES (?,?,?)"
                self.cursor.execute(self.sql, [id_recept, id_ingr, vol_ing])
            self.conn.commit()

            for i in range(len(desc)):
                desc_row = desc[i]
                self.sql = "INSERT INTO description (id_recept, desc) VALUES (?,?)"
                self.cursor.execute(self.sql, [id_recept, desc_row])
            self.conn.commit()

            self.ui.src_edit_line.clear()
            self.ui.name_2.clear()
            self.ui.list_ing_e.clear()
            self.ui.list_desc_2.clear()
            self.list_ingr_e.clear()
            self.textAlert = "Рецепт успешно обновлен"
            self.alertWindow(self.textAlert)

    # Удаление рецепта
    def del_recept(self):
        reply = QMessageBox.question(self, ' ',
                                         "Вы уверены что хотите удалить рецпт?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            name = self.ui.src_edit_line.text()
            self.sql = "SELECT id FROM recept WHERE name=?"
            self.cursor.execute(self.sql, [(name)])
            rec_id = self.cursor.fetchall()[0][0]
            self.sql = "DELETE FROM recept_ing WHERE id_recept=?"
            self.cursor.execute(self.sql, [rec_id])
            self.sql = "DELETE FROM description WHERE id_recept=?"
            self.cursor.execute(self.sql, [rec_id])
            self.sql = "DELETE FROM recept WHERE id=?"
            self.cursor.execute(self.sql, [rec_id])
            self.conn.commit()
            self.ui.src_edit_line.clear()
            self.ui.name_2.clear()
            self.ui.list_ing_e.clear()
            self.ui.list_desc_2.clear()
            self.textAlert = "Рецепт успешно удален"
            self.alertWindow(self.textAlert)

    # поиск рецепта
    def src_recept(self):
        name = self.ui.srch_line.text()
        if name == '':
            self.clean_search()
            self.cursor.execute("""SELECT * FROM recept""")
            self.conn.commit()
            result = self.cursor.fetchall()
            self.paint_result(result)

        else:
            self.clean_search()
            self.sql = "SELECT * FROM recept WHERE name LIKE ?"
            self.cursor.execute(self.sql, [('%' +name + '%')])
            self.conn.commit()
            result = self.cursor.fetchall()
            self.paint_result(result)

    # Выводим результат поиска
    def paint_result(self, result):
        for row in range(len(result)):
            name = result[row]
            for n in range(len(name)):
                nameRecept = name[1]
                self.ui.verticalLayout.addWidget(crF.createF(self, nameRecept))
                break

    # очистка фрейма поиска при новом поиске
    def clean_search(self):
        if self.ui.verticalLayout.count() != 0:
            for i in reversed(range(self.ui.verticalLayout.count())):
                self.ui.verticalLayout.itemAt(i).widget().setParent(None)

    # окно рецепта и вывод в него рецепт
    def receptWindow(self, nameRecept):

        self.receptW = QtWidgets.QWidget()
        self.receptUi = Ui_recept()
        self.receptUi.setupUi(self.receptW)
        self.receptW.show()
        self.receptUi.name_recept.setText(nameRecept)

        self.sql = "SELECT * FROM recept WHERE name=?"
        self.cursor.execute(self.sql, [(nameRecept)])
        self.conn.commit()
        result = self.cursor.fetchall()
        for i in range(len(result)):
            rec = result[i]
            for r in range(len(rec)):
                rec_id = rec[0]
                rec_name = rec[1]
                break

        # вывод ингридиентов
        self.sql = """SELECT i.id, i.name_ing, r.vol_ing
                                    FROM indridient i
                                    LEFT JOIN recept_ing r
                                    ON r.id_ingr=i.id
                                    WHERE r.id_recept=? ORDER BY r.id"""
        self.cursor.execute(self.sql, [(rec_id)])
        self.conn.commit()
        result = self.cursor.fetchall()
        for i in range(len(result)):
            rec = result[i]
            for r in range(len(rec)):
                ing_id = str(rec[0])
                ing_name = rec[1]
                vol_ing = str(rec[2])
                break
            self.receptUi.list_ingr.append(ing_name + ': ' + vol_ing)

        # вывод описания
        self.sql = """SELECT id, desc 
                        FROM description 
                        WHERE id_recept=? ORDER BY id"""
        self.cursor.execute(self.sql, [(rec_id)])
        self.conn.commit()
        result = self.cursor.fetchall()
        for i in range(len(result)):
            rec = result[i]
            for r in range(len(rec)):
                desc_id = rec[0]
                desc_name = rec[1]
                break
            self.receptUi.disc_recept.append(desc_name)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())



#     На всякий случай для alertWindow
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())