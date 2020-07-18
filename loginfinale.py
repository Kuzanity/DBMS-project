from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import pymysql
from MAIN_WINDOWFinale import Mainmenu
class Ui_MainWindow(object):
    def success(self):
        self.window=QtWidgets.QMainWindow()
        self.main=Mainmenu()
        self.main.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowIcon(QtGui.QIcon('App logo.png'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

        if mess.Ok:
            self.success()

    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowIcon(QtGui.QIcon('App logo.png'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok| QtWidgets.QMessageBox.Cancel)
        mess.exec_()

        if mess.Ok:
            self.Username.clear()
            self.Password.clear()

    def login(self):
        Username=self.Username.text()
        Password=self.Password.text()
        params=(Username,Password)
        conn = pymysql.connect(host="localhost",port=3306,db="dboragon",user="DBMS",password="12345")
        cursor = conn.cursor()
        cursor.callproc('login',params)
        if (len(cursor.fetchall())>0):
            self.messagebox('You are in','Congratulations')
        else:
            self.warning('Error','Please try again')
            

    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('App logo.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 655)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(853, 655))
        MainWindow.setMaximumSize(QtCore.QSize(853, 655))
        MainWindow.setStyleSheet("background-color: rgb(255, 245, 163);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 853, 655))
        self.background.setPixmap(QPixmap('LOGIN PAGE.png'))
        self.background.setObjectName("background")

        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(380, 370, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(15)
        self.Username.setFont(font)
        self.Username.setText("")
        self.Username.setObjectName("Email")
        self.Username.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(380, 460, 401, 51))
        self.Password.setStyleSheet("background-color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates Black")
        font.setPointSize(15)
        self.Password.setFont(font)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Admin ID")

        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(380, 530, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates SemiBold")
        font.setPointSize(15)
        self.Submit.setFont(font)
        self.Submit.setObjectName('Submit')
        self.Submit.clicked.connect(self.login)
        self.Submit.setStyleSheet("QPushButton{background: orange}\QPushButton::hover{background:yellow}\QPushButton:flat{border:none}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)  
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Oragon Login"))
        self.Submit.setText(_translate("MainWindow", "Submit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())