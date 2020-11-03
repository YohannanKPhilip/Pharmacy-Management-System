#Class 12 Computer Science with Python Project
#St. Thomas Convent Sr. Sec. School


from PyQt5.QtWidgets import *
import mysql.connector as MySQLdb
from PyQt5.uic import loadUiType
from xlrd import *
from xlsxwriter import *
from Python import login


ui,_=loadUiType('pharma.ui')


class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.setWindowTitle("Pharmacy Management System")
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()

        self.Show_Medicine()

        self.Show_Customers_data()
        self.Show_Debtors()

        self.Show_Category()
        self.Show_Manufacturer()

        self.Show_Category_Combobox()
        self.Show_Manufacturer_Combobox()

        self.setFixedWidth(1308)
        self.setFixedHeight(620)



    def Handel_UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)
        self.default_Theme()

    def Handel_Buttons(self):
        self.pushButton_User_Main.clicked.connect(self.Open_User_Tab)
        self.pushButton_Home.clicked.connect(self.Open_Home_Tab)
        self.pushButton_Medicine.clicked.connect(self.Open_Medicine_Tab)
        self.pushButton_Users.clicked.connect(self.Open_Users_Tab)
        self.pushButton_Settings.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_Add_Medicine_Save.clicked.connect(self.Add_New_Medicine)
        self.pushButton_M_SEARCH.clicked.connect(self.Search_Medicine)
        self.pushButton_SAVE_edit_Medicine.clicked.connect(self.Edit_Medicine)
        self.pushButton_DELETE_Medicine.clicked.connect(self.Delete_Medicine)
        #self.pushButton_Manufacturer_M_SEARCH.clicked.connect(self.Search_Manufacturer_Medicine_Purchase)

        self.pushButton_Add_Category.clicked.connect(self.Add_Category)
        self.pushButton_Add_Manufacturer.clicked.connect(self.Add_Manufacturer)

        self.pushButton_Customer_Save.clicked.connect(self.Add_Customers)
        self.pushButton_Customer_Save_3.clicked.connect(self.Edit_Customers)
        self.pushButton_Customer_Save_4.clicked.connect(self.Delete_Customers)

        self.pushButton_Add_User.clicked.connect(self.Add_New_User)
        self.pushButton_Login.clicked.connect(self.Login)
        self.pushButton_edit_users.clicked.connect(self.Edit_User)
        self.pushButton_Export_Excel.clicked.connect(self.Export_Medicine)

        self.pushButton_Manage_Customer.clicked.connect(self.Search_Customer)



    #--------------------Opening Tabs---------------------

    def Open_User_Tab(self):
        self.tabWidget.setCurrentIndex(5)

    def Open_Home_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Medicine_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    # --------------------Point Of Sale---------------------

    '''def POS_front(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()
        
        date = QDate.currentDate().toString(Qt.ISODate)

        self.textEdit.setText(date)
'''

        #Product_Name = self.Product_Name.currentText()
        #Client_Name  = self.comboBox_6.currentText()

    #--------------------Medicine---------------------

    def Show_Medicine(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        self.cur.execute('select Medicine_Name, Medicine_Category, Medicine_Manufacturer, Medicine_Qty, Medicine_Purchase_Price, Medicine_Sell_Price from medicine')
        data = self.cur.fetchall()

        #print(data)

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for r1, element in enumerate(data):
                for r2, item in enumerate(element):
                    self.tableWidget_4.setItem(r1, r2, QTableWidgetItem(str(item)))
                    r2 += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)




    def Add_New_Medicine(self):
        self.db = MySQLdb.connect(host='localhost',user='root',password='mysql',db='pharmacy-management-system')
        self.cur = self.db.cursor()

        Medicine_Name           = self.Medicine_Name.text()
        Medicine_Description    = self.Medicine_Description.toPlainText()
        Medicine_Category       = self.Medicine_Category.currentText()
        Medicine_Manufacturer   = self.Medicine_Manufacturer.currentText()
        Medicine_Purchase_Price = self.Medicine_Purchase_Price.text()   #Medicine_Purchase_Price
        Medicine_Sell_Price     = self.Medicine_Sell_Price.text()
        Medicine_Qty            = self.Medicine_Qty.text()


        self.cur.execute('''insert into medicine(Medicine_Name, Medicine_Description, Medicine_Category, Medicine_Manufacturer, Medicine_Purchase_Price, Medicine_Sell_Price, Medicine_Qty)
        values( %s, %s, %s, %s, %s, %s, %s )''', (Medicine_Name, Medicine_Description, Medicine_Category, Medicine_Manufacturer, Medicine_Purchase_Price,Medicine_Sell_Price, Medicine_Qty))
        self.db.commit()
        self.statusBar().showMessage('New Medicine Added')

        Medicine_Name           = self.Medicine_Name.setText('')
        Medicine_Description    = self.Medicine_Description.setPlainText('')
        Medicine_Purchase_Price = self.Medicine_Purchase_Price.setText('')
        Medicine_Sell_Price     = self.Medicine_Sell_Price.setText('')
        Medicine_Qty            = self.Medicine_Qty.setText('')

        self.Show_Medicine()


    def Search_Medicine(self):
        self.db  = MySQLdb.connect(host='localhost',user='root',password='mysql',db='pharmacy-management-system')
        self.cur = self.db.cursor()

        Medicine_Name = self.Search_Medicine_LineEdit.text()

        self.cur.execute('select * from Medicine where Medicine_name = %s',[(Medicine_Name)])

        data = self.cur.fetchone()

        #print(data)

        self.lineEdit_7.setText(data[1]) #Name
        self.Medicine_Description_2.setPlainText(data[2]) #Description
        self.comboBox_3.setCurrentText(data[3]) #Category
        self.comboBox_4.setCurrentText(data[4]) #Manufacturer
        self.lineEdit_21.setText(str(data[5])) #Purchase Price
        self.lineEdit_23.setText(str(data[6]))#Sell Price
        self.Edit_Qty.setText(str(data[7])) #Qty

    def Edit_Medicine(self):
        self.db = MySQLdb.connect(host='localhost',user='root',password='mysql',db='pharmacy-management-system')
        self.cur = self.db.cursor()

        Medicine_Name           = self.lineEdit_7.text()
        Medicine_Description    = self.Medicine_Description_2.toPlainText()
        Medicine_Category       = self.comboBox_3.currentText()
        Medicine_Manufacturer   = self.comboBox_4.currentText()
        Medicine_Purchase_Price = self.lineEdit_21.text()
        Medicine_Sell_Price     = self.lineEdit_23.text()
        Medicine_Qty            = self.Edit_Qty.text()

        self.cur.execute('''update medicine set Medicine_Name=%s, Medicine_Description=%s, Medicine_Category=%s, Medicine_Manufacturer=%s, Medicine_Purchase_Price=%s, Medicine_Sell_Price=%s, Medicine_Qty=%s where medicine_name=%s''', (Medicine_Name, Medicine_Description, Medicine_Category, Medicine_Manufacturer, Medicine_Purchase_Price, Medicine_Sell_Price, Medicine_Qty, Medicine_Name))

        self.db.commit()
        self.statusBar().showMessage("Medicine Updated")
        self.Show_Medicine()


    def Delete_Medicine(self):
        self.db  = MySQLdb.connect(host='localhost',user='root',password='mysql',db='pharmacy-management-system')
        self.cur = self.db.cursor()

        Medicine_Name = self.Search_Medicine_LineEdit.text()

        warning = QMessageBox.warning(self, ' Delete Medicine', "Are you sure you want to delete this item", QMessageBox.Yes | QMessageBox.No)

        if warning == QMessageBox.Yes :
            sql = ''' DELETE FROM medicine WHERE medicine_name = %s '''
            self.cur.execute(sql , [(Medicine_Name)])
            self.db.commit()
            self.statusBar().showMessage('Medicine Deleted')

            self.lineEdit_7.setText('')
            self.Medicine_Description_2.setPlainText('')
            self.lineEdit_21.setText('')
            self.lineEdit_23.setText('')
            self.Edit_Qty.setText('')
            self.Search_Medicine_LineEdit.setText('')

        self.Show_Medicine()

    #----------Medicine Purchase-----------

    # --------------------Client---------------------


    def Add_Customers(self):
        pass
        self.db  = MySQLdb.connect(host='localhost',user='root',password='mysql',db='pharmacy-management-system')
        self.cur = self.db.cursor()

        Customer_Name    = self.Customer_Name_Line.text()
        Customer_Mobile  = self.Customer_Mobile_Line.text()
        Customer_Address = self.Customer_Address_Line.toPlainText()

        self.cur.execute('insert into Customer(Customer_Name, Customer_Mobile, Customer_Address) values(%s,%s,%s)',(Customer_Name, Customer_Mobile, Customer_Address))

        self.db.commit()
        self.statusBar().showMessage('New Customer Added')

        Customer_Name    = self.Customer_Name_Line.setText('')
        Customer_Mobile  = self.Customer_Mobile_Line.setText('')
        Customer_Address = self.Customer_Address_Line.setPlainText('')

        self.Show_Customers_data()

    def Show_Customers_data(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        self.cur.execute('select Customer_Name, Customer_Mobile, Customer_Address from customer')
        data = self.cur.fetchall()

        #print(data)

        if data:
            self.tableWidget_Customer_Info.setRowCount(0)
            self.tableWidget_Customer_Info.insertRow(0)
            for r1, element in enumerate(data):
                for r2, item in enumerate(element):
                    self.tableWidget_Customer_Info.setItem(r1, r2, QTableWidgetItem(str(item)))
                    r2 += 1

                row_position = self.tableWidget_Customer_Info.rowCount()
                self.tableWidget_Customer_Info.insertRow(row_position)

    def Search_Customer(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        Customer_Name = self.Customer_Name_Line_SEARCH.text()

        self.cur.execute('select * from Customer where customer_name = %s', [(Customer_Name)])


        data = self.cur.fetchone()

        # print(data)

        self.Customer_Name_Line_2.setText(data[1])
        self.Customer_Mobile_Line_2.setText(str(data[2]))
        self.Customer_Address_Line_2.setPlainText(data[3])

    def Edit_Customers(self):
        self.db = MySQLdb.connect(host='localhost',user='root',password='mysql',db='pharmacy-management-system')
        self.cur = self.db.cursor()

        Customer_Name      = self.Customer_Name_Line_2.text()
        Customer_Mobile    = self.Customer_Mobile_Line_2.text()
        Customer_Address   = self.Customer_Address_Line_2.toPlainText()
        customer_old_Name  = self.Customer_Name_Line_SEARCH.text()

        self.cur.execute('update customer set Customer_name=%s, customer_mobile=%s, customer_address=%s where customer_name=%s', (Customer_Name, Customer_Mobile, Customer_Address, customer_old_Name))

        self.db.commit()
        self.statusBar().showMessage("Customer Updated")
        self.Show_Customers_data()
        
    

    def Delete_Customers(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        Customer_Name = self.Customer_Name_Line_SEARCH.text()


        warning = QMessageBox.warning(self, ' Delete Customer', "Are you sure you want to delete customer data",
                                      QMessageBox.Yes | QMessageBox.No)

        if warning == QMessageBox.Yes:
            sql = ''' DELETE FROM customer WHERE customer_name = %s '''
            self.cur.execute(sql, [(Customer_Name)])
            self.db.commit()
            self.db.close()
            self.statusBar().showMessage('Customer Deleted')

            self.Show_Customers_data()

            self.Customer_Name_Line_2.setText('')
            self.Customer_Address_Line_2.setPlainText('')
            self.Customer_Mobile_Line_2.setText('')
            self.Customer_Name_Line_SEARCH.setText('')

    # --------------------Debtors---------------------

    def Show_Debtors(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        self.cur.execute('select customer_name, customer_Mobile, customer_address, customer_default from customer where customer_default>=1')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_Debtors.setRowCount(0)
            self.tableWidget_Debtors.insertRow(0)
            for r1, element in enumerate(data):
                for r2, item in enumerate(element):
                    self.tableWidget_Debtors.setItem(r1, r2, QTableWidgetItem(str(item)))
                    r2 += 1

                row_position = self.tableWidget_Debtors.rowCount()
                self.tableWidget_Debtors.insertRow(row_position)
            

        self.cur.execute('select sum(customer_default) from customer where customer_default>=1')
        data = self.cur.fetchall()
        if data :
            amount = str(data).strip('[]')
            amount = "Total Balance: "+ amount.strip('()')
            amount = amount.replace(',' ,'')
            self.Total_Debtors_Text.setText(amount)


    # --------------------Debtors---------------------

    def Purchase(self):
        pass





    # --------------------Users---------------------

    def Add_New_User(self):
        self.db  = MySQLdb.connect(host='localhost',user='root',password='mysql',db='pharmacy-management-system')
        self.cur = self.db.cursor()

        username = self.Create_username_line.text()
        email = self.Create_email_line.text()
        password = self.Create_password_line.text()
        password_again = self.Create_password_again_line.text()

        if password == password_again :
            self.cur.execute('''
            insert into users(user_name, user_email, user_password) values(%s ,%s , %s)''', (username, email, password))

            self.db.commit()
            self.statusBar().showMessage("New User Added")

            username       = self.Create_username_line.setText('')
            email          = self.Create_email_line.setText('')
            password       = self.Create_password_line.setText('')
            password_again = self.Create_password_again_line.setText('')


        else:
            self.message_Add_User.setText("Please add a valid password")


    def Login(self):
        self.db  = MySQLdb.connect(host='localhost',user='root',password='mysql',db='pharmacy-management-system')
        self.cur = self.db.cursor()

        username = self.username_line.text()
        password = self.password_line.text()

        sql = 'select * from users'

        self.cur.execute(sql)
        data = self.cur.fetchall()

        for row in data:
            if username == row[1] or password == row[3]:
                self.statusBar().showMessage('Valid Username and Password')
                self.Group_Edit_Information.setEnabled(True)

                self.edit_username_line.setText(row[1])
                self.edit_email_line.setText(row[2])
                self.edit_password_line.setText(row[3])


    def Edit_User(self):

        username       = self.edit_username_line.text()
        email          = self.edit_email_line.text()
        password       = self.edit_password_line.text()
        password_again = self.edit_password_again_line.text()

        original_username = self.username_line.text()

        if password == password_again:
            self.db  = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
            self.cur = self.db.cursor()

            self.cur.execute('update users set user_name=%s, user_email=%s, user_password=%s where user_name=%s',(username , email , password , original_username))

            self.db.commit()
            self.statusBar().showMessage("User data updated successfully ")

        else:
            print("Make sure you entered your password correctly")



        sql = 'update users set(user_name=%s, user_email=%s, user_password=%s) where user_name=%s',





    # --------------------Settings---------------------

    def Add_Category(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        '''if self.db.is_connected():
            print("Connected")'''

        Category_name = self.Add_Category_Name.text()


        self.cur.execute('''insert into category (Category_name) values (%s)''', (Category_name,))

        self.db.commit()
        self.statusBar().showMessage('New Category Added')
        self.Add_Category_Name.setText('')
        self.Show_Category()
        self.Show_Category_Combobox()


    def Show_Category(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        self.cur.execute('select category_name from category')
        data = self.cur.fetchall()

        #print(data)

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for r1, element in enumerate(data):
                for r2, item in enumerate(element):
                    self.tableWidget_2.setItem(r1, r2, QTableWidgetItem(str(item)))
                    r2 += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    def Add_Manufacturer(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()


        Manufacturer_name = self.Add_Manufacturer_Name.text()

        self.cur.execute('''insert into manufacturer (Manufacturer_name) values (%s)''', (Manufacturer_name,))

        self.db.commit()
        self.statusBar().showMessage('New Manufacturer Added')
        self.Add_Manufacturer_Name.setText('')
        self.Show_Manufacturer()
        self.Show_Manufacturer_Combobox()


    def Show_Manufacturer(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        self.cur.execute('select manufacturer_name from manufacturer')
        data = self.cur.fetchall()

       #print(data)

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for r1, element in enumerate(data):
                for r2, item in enumerate(element):
                    self.tableWidget_3.setItem(r1, r2, QTableWidgetItem(str(item)))
                    r2 += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)



    #--------------------Show Settings data in UI---------------------
    def Show_Category_Combobox(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        self.cur.execute('select category_name from category')
        data = self.cur.fetchall()

        self.Medicine_Category.clear()
        for category in data:

            self.Medicine_Category.addItem(category[0])
            self.comboBox_3.addItem(category[0])


    def Show_Manufacturer_Combobox(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        self.cur.execute('select manufacturer_name from manufacturer')
        data = self.cur.fetchall()

        self.Medicine_Manufacturer.clear()
        for Manufacturer in data:

            self.Medicine_Manufacturer.addItem(Manufacturer[0])
            self.comboBox_4.addItem(Manufacturer[0])

    '''def Show_Product_Combobox(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        self.cur.execute('select medicine_name from medicine')
        data = self.cur.fetchall()

        self.Medicine_Name.clear()
        for product in data:

            self.Medicine_Name.addItem(product[0])
            self.comboBox_5.addItem(product[0])'''


    # --------------------Export Data---------------------

    def Export_Medicine(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
        self.cur = self.db.cursor()

        self.cur.execute('select Medicine_Name, Medicine_Category, Medicine_Manufacturer, Medicine_Qty, Medicine_Purchase_Price, Medicine_Sell_Price from medicine')
        data = self.cur.fetchall()

        #print(data)

        wb = Workbook('Medicines.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0,'Medicine Name')
        sheet1.write(0, 1, 'Category')
        sheet1.write(0, 2, 'Manufacturer')
        sheet1.write(0, 3, 'Qty')
        sheet1.write(0, 4, 'Purchase Price')
        sheet1.write(0, 5, 'Sell Price')

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number +=1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Report Created Successfully')





    #--------------------UI Themes---------------------

    def default_Theme(self):
       style = open('theme/Dark_Blue.css')
       style = style.read()
       self.setStyleSheet(style)


def main():
    app = QApplication(sys.argv)
    window = login.login()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()