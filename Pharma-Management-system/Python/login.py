
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import mysql.connector as MySQLdb
from PyQt5.uic import loadUiType
import index

from sys import stdout
from datetime import datetime


login,_=loadUiType('login.ui')

class login(QWidget , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton_Login.clicked.connect(self.Handel_Login)
        self.welcome_day()

        self.setFixedWidth(950)
        self.setFixedHeight(550)



    def Handel_Login(self):
        #username = self.Login_Username_Line.text()
        #password = self.login_Password_Line.text()
        #welcome = self.Login_Welcome_Line.text()

        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        username = self.Login_Username_Line.text()
        password = self.login_Password_Line.text()

        sql = 'select * from users'

        self.cur.execute(sql)
        data = self.cur.fetchall()

        for row in data:
            if username == row[1] or password == row[3]:
                #print("user match")
                self.window2 = index.MainApp()
                self.close()
                self.window2.show()

            else:
                self.Warning_Line.setText('Make Sure you entered correct information')



    def welcome_day(self):
        hour = datetime.now().hour

        if 5 <= hour <= 11:
            self.Login_Welcome_Line.setText("Have a Good Morning")
        elif 12 <= hour <= 17:
            self.Login_Welcome_Line.setText("Have a Good Afternoon")
        elif 18 <= hour <= 22:
            self.Login_Welcome_Line.setText("Have a Good Evening")
        else:
            self.Login_Welcome_Line.setText("Have a Good Night")

