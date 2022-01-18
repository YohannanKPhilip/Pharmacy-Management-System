##Work Learning tests##

'''import mysql.connector as MySQLdb
def Show_Category():
    db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
    cur = db.cursor()

    cur.execute('select category_name from category')
    data = cur.fetchall()

    count = 1
    for element in data:
        print(count, element)
        count += 1

Show_Category()

from sys import stdout
from datetime import datetime

def get_part_of_day(hour):
    return (
        "morning" if 5 <= hour <= 11
        else
        "afternoon" if 12 <= hour <= 17
        else
        "evening" if 18 <= hour <= 22
        else
        "night"
    )






import datetime

x = datetime.datetime.now()

print(x.strftime("%x"))


from PyQt5.QtCore import QDate, Qt


date = QDate.currentDate().toString(Qt.ISODate)
print(date)


def Search_Customer(self):
    self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
    self.cur = self.db.cursor()

    Customer_Name = self.Customer_Name_Line_SEARCH.text()

    #self.cur.execute('select * from Customer where customer_name = %s', [(Customer_Name)])
    self.cur.execute('select * from customer')

    data = self.cur.fetchall()

    for row in data:
        if row[1]==Customer_Name:
            self.Customer_Name_Line_2.setText(data[1])
            self.Customer_Mobile_Line_2.setText(str(data[2]))
            self.Customer_Address_Line_2.setPlainText(data[3])


    # print(data)

    # self.groupBox_Manage_Customer.setEnabled(True)
    self.Customer_Name_Line_2.setText(data[1])
    self.Customer_Mobile_Line_2.setText(str(data[2]))
    self.Customer_Address_Line_2.setPlainText(data[3])


######################################

def Search_Customer(self):
    self.db = MySQLdb.connect(host='localhost', user='root', password='mysql', db='pharmacy-management-system')
    self.cur = self.db.cursor()

    Customer_Name = self.Customer_Name_Line_SEARCH.text()

    self.cur.execute('select * from Customer where customer_name = %s', [(Customer_Name)])

    data = self.cur.fetchone()

    # print(data)

    # self.groupBox_Manage_Customer.setEnabled(True)
    self.Customer_Name_Line_2.setText(data[1])
    self.Customer_Mobile_Line_2.setText(str(data[2]))
    self.Customer_Address_Line_2.setPlainText(data[3])


def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    if not last_invoice:
        return 'MAG0001'
    invoice_no = last_invoice.invoice_no
    invoice_int = int(invoice_no.split('MAG')[-1])
    width = 4
    new_invoice_int = invoice_int + 1
    formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
    new_invoice_no = 'MAG' + str(formatted)
    return new_invoice_no

class Invoice(models.Model):
    invoice_no = models.CharField(max_length = 500, default = increment_invoice_number, null = True, blank = True)

rec = 10

def autoIncrement():
    global rec
    pStart = 1 #adjust start value, if req'd
    pInterval = 1 #adjust interval value, if req'd
    if (rec == 0):
        rec = pStart
    else:
        rec = rec + pInterval
        return 'ABC'+str(rec).zfill(3)
print(rec)
a = autoIncrement()

print(a)

'''
