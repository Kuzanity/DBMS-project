# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Insert.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Insert_Win(object):
    
    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowIcon(QtGui.QIcon('App logo.png'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

        if mess.Ok:
            self.ID.clear()
            self.Qty.clear()
            self.Name.clear()
            self.Price.clear()
            self.Type.clear()
            
    def insert_data(self):
        ID=self.ID.text()
        qty=self.Qty.text()
        Name=self.Name.text()
        Price=self.Price.text()
        prod_type=self.Type.text()
        conn = pymysql.connect(host="localhost",port=3306,db="oragon",user="DBMS",password="12345")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sales_products(product_id,prod_qty,prod_name,prod_price,product_type) VALUES (%s,%s,%s,%s,%s)",(ID,qty,Name,Price,prod_type))
        conn.commit()
        conn.close()
        self.messagebox('Success','Enter another value')

    def setupUi(self, Insert_Win):
        Insert_Win.setObjectName("Insert_Win")
        Insert_Win.resize(511, 306)
        Insert_Win.setStyleSheet("background-color: rgb(255, 245, 163);")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Insert_Win.sizePolicy().hasHeightForWidth())
        Insert_Win.setSizePolicy(sizePolicy)

        self.centralwidget = QtWidgets.QWidget(Insert_Win)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label_5.setObjectName("label_5")
        self.ID = QtWidgets.QLineEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(90, 40, 401, 20))
        self.ID.setObjectName("ID")
        self.ID.setInputMask('9999')
        self.Qty = QtWidgets.QLineEdit(self.centralwidget)
        self.Qty.setGeometry(QtCore.QRect(90, 90, 401, 20))
        self.Qty.setObjectName("Qty")
        self.Qty.setInputMask('999')
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(90, 140, 401, 20))
        self.Name.setObjectName("Name")
        self.Price = QtWidgets.QLineEdit(self.centralwidget)
        self.Price.setGeometry(QtCore.QRect(90, 190, 401, 20))
        self.Price.setObjectName("Price")
        self.Price.setInputMask('999')
        self.Type = QtWidgets.QLineEdit(self.centralwidget)
        self.Type.setGeometry(QtCore.QRect(90, 240, 401, 20))
        self.Type.setObjectName("Type")
        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(220, 270, 75, 31))
        self.Submit.setObjectName("Submit")
        self.Submit.clicked.connect(self.insert_data)
        Insert_Win.setCentralWidget(self.centralwidget)

        self.retranslateUi(Insert_Win)
        QtCore.QMetaObject.connectSlotsByName(Insert_Win)

    def retranslateUi(self, Insert_Win):
        _translate = QtCore.QCoreApplication.translate
        Insert_Win.setWindowTitle(_translate("Insert_Win", "Insert Window"))
        self.label.setText(_translate("Insert_Win", "Quantity"))
        self.label_2.setText(_translate("Insert_Win", "Product Name"))
        self.label_3.setText(_translate("Insert_Win", "Product Price"))
        self.label_4.setText(_translate("Insert_Win", "Product Type"))
        self.label_5.setText(_translate("Insert_Win", "Product ID"))
        self.Submit.setText(_translate("Insert_Win", "Submit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Insert_Win()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())