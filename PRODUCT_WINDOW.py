# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PRODUCT_WINDOW.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtGui import QPixmap
class insertWin(object):
    # def insert_data(self):
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 455)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(653, 455))
        MainWindow.setMaximumSize(QtCore.QSize(653, 455))
        MainWindow.setSizeIncrement(QtCore.QSize(653, 455))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.backgroundLABEL = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLABEL.setGeometry(QtCore.QRect(0, 0, 653, 455))
        self.backgroundLABEL.setPixmap(QPixmap('product.png'))
        self.backgroundLABEL.setText("")
        self.backgroundLABEL.setObjectName("backgroundLABEL")

        self.Product_Qty = QtWidgets.QLabel(self.centralwidget)
        self.Product_Qty.setGeometry(QtCore.QRect(40, 90, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Product_Qty.setFont(font)
        self.Product_Qty.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Product_Qty.setObjectName("Product_Qty")
        self.Product_name = QtWidgets.QLabel(self.centralwidget)
        self.Product_name.setGeometry(QtCore.QRect(40, 150, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Product_name.setFont(font)
        self.Product_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Product_name.setObjectName("Product_name")
        self.Product_price = QtWidgets.QLabel(self.centralwidget)
        self.Product_price.setGeometry(QtCore.QRect(40, 210, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Product_price.setFont(font)
        self.Product_price.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Product_price.setObjectName("Product_price")
        self.Product_ID = QtWidgets.QLabel(self.centralwidget)
        self.Product_ID.setGeometry(QtCore.QRect(40, 270, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Product_ID.setFont(font)
        self.Product_ID.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Product_ID.setObjectName("Product_ID")
        self.Product_type = QtWidgets.QLabel(self.centralwidget)
        self.Product_type.setGeometry(QtCore.QRect(40, 330, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Product_type.setFont(font)
        self.Product_type.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Product_type.setObjectName("Product_type")
        self.ADD_PRODUCT = QtWidgets.QLabel(self.centralwidget)
        self.ADD_PRODUCT.setGeometry(QtCore.QRect(220, 20, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ADD_PRODUCT.setFont(font)
        self.ADD_PRODUCT.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ADD_PRODUCT.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ADD_PRODUCT.setObjectName("ADD_PRODUCT")
        self.prodqty_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.prodqty_LE.setGeometry(QtCore.QRect(280, 110, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.prodqty_LE.setFont(font)
        self.prodqty_LE.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.prodqty_LE.setAlignment(QtCore.Qt.AlignCenter)
        self.prodqty_LE.setObjectName("prodqty_LE")
        self.prodname_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.prodname_LE.setGeometry(QtCore.QRect(280, 170, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.prodname_LE.setFont(font)
        self.prodname_LE.setAlignment(QtCore.Qt.AlignCenter)
        self.prodname_LE.setObjectName("prodname_LE")
        self.prodprice_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.prodprice_LE.setGeometry(QtCore.QRect(280, 230, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.prodprice_LE.setFont(font)
        self.prodprice_LE.setAlignment(QtCore.Qt.AlignCenter)
        self.prodprice_LE.setObjectName("prodprice_LE")
        self.prodid_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.prodid_LE.setGeometry(QtCore.QRect(280, 290, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.prodid_LE.setFont(font)
        self.prodid_LE.setAlignment(QtCore.Qt.AlignCenter)
        self.prodid_LE.setObjectName("prodid_LE")
        self.prodtype_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.prodtype_LE.setGeometry(QtCore.QRect(280, 350, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.prodtype_LE.setFont(font)
        self.prodtype_LE.setAlignment(QtCore.Qt.AlignCenter)
        self.prodtype_LE.setObjectName("prodtype_LE")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(390, 390, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        # self.submit_button.clicked.connect()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Product_Qty.setText(_translate("MainWindow", "Product Quantity:"))
        self.Product_name.setText(_translate("MainWindow", "Product Name:"))
        self.Product_price.setText(_translate("MainWindow", "Product Price:"))
        self.Product_ID.setText(_translate("MainWindow", "Product ID:"))
        self.Product_type.setText(_translate("MainWindow", "Product Type:"))
        self.ADD_PRODUCT.setText(_translate("MainWindow", "ADD PRODUCT"))
        self.submit_button.setText(_translate("MainWindow", "SUBMIT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = insertWin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())