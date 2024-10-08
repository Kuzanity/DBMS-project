
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtGui import QPixmap

# class mysql.connections.connection(host="localhost",port=3306,db="db_oragon",user="DBMS",password="12345")
class Mainmenu(object):
    # def transact(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Update_win()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    def view(self):
        conn = pymysql.connect(host="localhost",port=3306,db="db_oragon",user="DBMS",password="12345")
        cursor = conn.cursor()
        cursor.callproc('GetProducts')
        result = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    # def update(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = transactionwin()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    # def transact(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = transactionwin()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    # def insert(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = insertWin()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 655)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(853, 655))
        MainWindow.setMaximumSize(QtCore.QSize(853, 655))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 853, 655))
        self.Background.setPixmap(QPixmap('Main.png'))
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(10, 70, 141, 61))
        self.Add.setStyleSheet("QPushButton{background:LawnGreen;border-style: solid;border-color: black;border-width: 4px;border-radius: 8px}\QPushButton::hover{background:ForestGreen}\QPushButton:pressed{background:GreenYellow}")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Add.setFont(font)
        self.Add.setObjectName("Add")
        # self.Add.clicked.connect(self.insert)
        self.Delete = QtWidgets.QPushButton(self.centralwidget)
        self.Delete.setGeometry(QtCore.QRect(10, 130, 141, 61))
        self.Delete.setStyleSheet("QPushButton{background:LawnGreen;border-style: solid;border-color: black;border-width: 4px;border-radius: 8px}\QPushButton::hover{background:ForestGreen}\QPushButton:pressed{background:GreenYellow}")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Delete.setFont(font)
        self.Delete.setObjectName("Delete")
        self.Edit = QtWidgets.QPushButton(self.centralwidget)
        self.Edit.setGeometry(QtCore.QRect(10, 190, 141, 61))
        self.Edit.setStyleSheet("QPushButton{background:LawnGreen;border-style: solid;border-color: black;border-width: 4px;border-radius: 8px}\QPushButton::hover{background:ForestGreen}\QPushButton:pressed{background:GreenYellow}")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Edit.setFont(font)
        self.Edit.setObjectName("Edit")
        # self.Edit.clicked.connect(self.update)
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(10, 320, 141, 61))
        self.Search.setStyleSheet("QPushButton{background:LawnGreen;border-style: solid;border-color: black;border-width: 4px;border-radius: 8px}\QPushButton::hover{background:ForestGreen}\QPushButton:pressed{background:GreenYellow}")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Search.setFont(font)
        self.Search.setObjectName("Search")
        self.Order = QtWidgets.QPushButton(self.centralwidget)
        self.Order.setGeometry(QtCore.QRect(10, 550, 141, 61))
        self.Order.setStyleSheet("QPushButton{background:LawnGreen;border-style: solid;border-color: black;border-width: 4px;border-radius: 8px}\QPushButton::hover{background:ForestGreen}\QPushButton:pressed{background:GreenYellow}")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Order.setFont(font)
        self.Order.setObjectName("Order")
        self.Order.clicked.connect(self.view)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(160, 70, 681, 541))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 280, 131, 21))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Add.setText(_translate("MainWindow", "ADD"))
        self.Delete.setText(_translate("MainWindow", "DELETE"))
        self.Edit.setText(_translate("MainWindow", "EDIT"))
        self.Search.setText(_translate("MainWindow", "SEARCH"))
        self.Order.setText(_translate("MainWindow", "ORDER"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Quantity"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Type"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Mainmenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())