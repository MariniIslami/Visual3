# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kategori.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector as mc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Kategori(object):
    def setupUi(self, Kategori):
        Kategori.setObjectName("Kategori")
        Kategori.resize(469, 314)
        self.verticalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 221, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(240, 20, 221, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_id = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.verticalLayout_2.addWidget(self.lineEdit_id)
        self.lineEdit_nama = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_nama.setObjectName("lineEdit_nama")
        self.verticalLayout_2.addWidget(self.lineEdit_nama)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 160, 431, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnInsert = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        self.btnInsert.clicked.connect(self.insertKategori)
        self.btnInsert.setObjectName("btnInsert")
        self.horizontalLayout_2.addWidget(self.btnInsert)
        self.labelResult = QtWidgets.QLabel(Kategori)
        self.labelResult.setGeometry(QtCore.QRect(20, 210, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("labelResult")

        self.retranslateUi(Kategori)
        QtCore.QMetaObject.connectSlotsByName(Kategori)

    def insertKategori(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "penjualan2"
            )
            cursor = mydb.cursor()
            idkat = self.lineEdit_id.text()
            namekat = self.lineEdit_nama.text()

            sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
            val = (idkat, namekat)
            cursor.execute(sql, val)
            mydb.commit()
            self.labelResult.setText("Data Kategori Berhasil Dimasukkan!")
            self.lineEdit_id.setText("")
            self.lineEdit_nama.setText("")
        except mc.Error as e:
            error_message = f"Error: {e}"
            self.labelResult.setText(error_message)

    def retranslateUi(self, Kategori):
        _translate = QtCore.QCoreApplication.translate
        Kategori.setWindowTitle(_translate("Kategori", "Form"))
        self.label.setText(_translate("Kategori", "ID Kategori"))
        self.label_2.setText(_translate("Kategori", "Nama Kategori"))
        self.btnInsert.setText(_translate("Kategori", "INSERT DATA"))
        self.labelResult.setText(_translate("Kategori", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Kategori = QtWidgets.QWidget()
    ui = Ui_Kategori()
    ui.setupUi(Kategori)
    Kategori.show()
    sys.exit(app.exec_())