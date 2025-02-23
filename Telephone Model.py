






from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import mysql.connector as m
import sys
import os
class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1800,950)
        self.setWindowTitle("Phone database")
        self.setWindowIcon(QIcon("D:\\photo\\phone.ico"))
        self.setStyleSheet("background-color:  rgb(230,230,250); color:  rgb(0,0,205);")
        
        self.my_con = None
        self.my_cur  = None
        
        self.tb = QTableWidget(self)
        self.tb.setFont(QFont("Poor Richard",20))
        self.tb.setVisible(False)
        
        #Modelni kiritish uchun 
        
        self.lb_model = QLabel("Model:   ",self)
        self.lb_model.setGeometry(50,30,250,50)
        self.lb_model.setFont(QFont("Consolas",20))
        
        self.txt_model = QLineEdit(self)
        self.txt_model.setGeometry(310,30,300,50)
        self.txt_model.setStyleSheet("""
                border-color: rgb(0,27,254);
                border-width: 2px;
                border-style: inset;
                border-radius: 15px;
                """)
        self.txt_model.setFont(QFont("Consolas",20))
        self.txt_model.setAlignment(Qt.AlignCenter)
        
        #Priceni kiritish uchun
        
        self.lb_price = QLabel("Price:   ",self)
        self.lb_price.setGeometry(1000,30,250,50)
        self.lb_price.setFont(QFont("Consolas",20))
        
        self.txt_price = QLineEdit(self)
        self.txt_price.setGeometry(1260,30,300,50)
        self.txt_price.setStyleSheet("""
                border-color: rgb(0,27,254);
                border-width: 2px;
                border-style: inset;
                border-radius: 15px;
                """)
        self.txt_price.setFont(QFont("Consolas",20))
        self.txt_price.setAlignment(Qt.AlignCenter)
        self.txt_price.setValidator(QIntValidator())
        
        #Esimni belgilash uchun
        
        self.lb_esim = QLabel("SELECT :   ",self)
        self.lb_esim.setGeometry(50,90,250,50)
        self.lb_esim.setFont(QFont("Consolas",20))
        
        self.txt_ESIM = QCheckBox("ESIM",self)
        self.txt_ESIM.setGeometry(350,90,100,50)
        self.txt_ESIM.setFont(QFont("Consolas",20))
        
        #Rangni tanlash uchun
        
        self.lb_color = QLabel("Color:   ",self)
        self.lb_color.setGeometry(1000,90,250,50)
        self.lb_color.setFont(QFont("Consolas",20))
        
        self.txt_color = QComboBox(self)
        self.txt_color.setGeometry(1260,90,300,50)
        self.txt_color.setStyleSheet("""
                border-color: rgb(0,27,254);
                border-width: 2px;
                border-style: inset;
                border-radius: 15px;
                """)
        self.txt_color.setFont(QFont("Consolas",20))
        self.txt_color.addItems(["RED","BLUE","BLACK","WHITE","GREEN","GOLD","SILVER","CYANG","MAGENTA","YELLOW"])
        
        #Ma'lumotlarni qo'shish uchun button
        
        self.insert_btn = QPushButton("INSERT INFO",self)
        self.insert_btn.setGeometry(1260,145,250,50)
        self.insert_btn.setStyleSheet("""
                background-color: black;
                border-color: rgb(0,255,0);
                border-width: 2px;
                border-style: outset;
                border-radius: 15px;
                color: rgb(0,255,0)
                """)
        self.insert_btn.setFont(QFont("Consolas",20))
        self.insert_btn.clicked.connect(self.insert_data)
        
        # Qidirayotgan ustunni tanlash uchun 
        
        self.lb_column = QLabel("Select Column:   ",self)
        self.lb_column.setGeometry(50,300,350,50)
        self.lb_column.setFont(QFont("Consolas",20))
        
        self.txt_column = QComboBox(self)
        self.txt_column.setGeometry(410,300,300,50)
        self.txt_column.setStyleSheet("""
                border-color: rgb(0,127,54);
                border-width: 2px;
                border-style: inset;
                border-radius: 15px;
                """)
        self.txt_column.setFont(QFont("Consolas",20))
        self.txt_column.addItems(["ID","Model","Price","ESIM","Color"])
        
        #Qidirilayotgan qiymatni kiritish uchun
        
        self.lb_value = QLabel("Value:   ",self)
        self.lb_value.setGeometry(50,360,250,50)
        self.lb_value.setFont(QFont("Consolas",20))
        
        self.txt_value = QLineEdit(self)
        self.txt_value.setGeometry(410,360,300,50)
        self.txt_value.setStyleSheet("""
                border-color: rgb(0,127,54);
                border-width: 2px;
                border-style: inset;
                border-radius: 15px;
                """)
        self.txt_value.setFont(QFont("Consolas",20))
        self.txt_value.setAlignment(Qt.AlignCenter)
        
        #Ma'lumotlarni qidirish uchun btn
        
        self.select_btn = QPushButton("SHOW INFO",self)
        self.select_btn.setGeometry(410,430,300,50)
        self.select_btn.setStyleSheet("""
                background-color: black;
                border-color: rgb(0,255,0);
                border-width: 2px;
                border-style: outset;
                border-radius: 15px;
                color: rgb(0,255,0)
                """)
        self.select_btn.setFont(QFont("Consolas",20))
        self.select_btn.clicked.connect(self.show_data)
        
         #QSaralashni tanlash uchun
        
        self.lb_sort = QLabel("Select sorting mode:   ",self)
        self.lb_sort.setGeometry(1000,300,400,50)
        self.lb_sort.setFont(QFont("Consolas",20))
        
        self.incr = QRadioButton("INCREASING",self)
        self.incr.setGeometry(1310,360,250,50)
        self.incr.setFont(QFont("Times New Roman",20))
        self.incr.setStyleSheet("color: rgb(0,127,54);")
        
        self.dec = QRadioButton("DECREASING",self)
        self.dec.setGeometry(1570,360,250,50)
        self.dec.setFont(QFont("Times New Roman",20))
        self.dec.setStyleSheet("color: rgb(0,127,54);")
        
        #Saralashni amalga oshirish uchun
        
        self.sort_btn = QPushButton("Sorting INFO",self)
        self.sort_btn.setGeometry(1400,410,300,50)
        self.sort_btn.setStyleSheet("""
                background-color: black;
                border-color: rgb(0,255,0);
                border-width: 2px;
                border-style: outset;
                border-radius: 15px;
                color: rgb(0,255,0)
                """)
        self.sort_btn.setFont(QFont("Consolas",20))
        self.sort_btn.clicked.connect(self.sort_data)
        
      
        # update

        self.lb_update = QLabel("Update:   ",self)
        self.lb_update.setGeometry(1000,470,300,50)
        self.lb_update.setFont(QFont("Consolas",20))


        self.txt_update = QLineEdit(self)
        self.txt_update.setGeometry(1260,470,500,50)
        self.txt_update.setStyleSheet("""
                border-color: rgb(0,127,54);
                border-width: 2px;
                border-style: inset;
                border-radius: 15px;
                """)
        self.txt_update.setFont(QFont("Consolas",20))
        self.txt_update.setAlignment(Qt.AlignCenter)


        self.update_btn = QPushButton("Update",self)
        self.update_btn.setGeometry(1400,540,300,50)
        self.update_btn.setStyleSheet("""
                background-color: black;
                border-color: rgb(0,255,0);
                border-width: 2px;
                border-style: outset;
                border-radius: 15px;
                color: rgb(0,255,0)
                """)
        self.update_btn.setFont(QFont("Consolas",20))
        self.update_btn.clicked.connect(self.update_data)
        

        
        # delete


        self.lb_delete = QLabel("Delete:   ",self)
        self.lb_delete.setGeometry(1000,610,300,50)
        self.lb_delete.setFont(QFont("Consolas",20))


        self.txt_delete = QLineEdit(self)
        self.txt_delete.setGeometry(1260,610,500,50)
        self.txt_delete.setStyleSheet("""
                border-color: rgb(0,127,54);
                border-width: 2px;
                border-style: inset;
                border-radius: 15px;
                """)
        self.txt_delete.setFont(QFont("Consolas",20))
        self.txt_delete.setAlignment(Qt.AlignCenter)


        self.delete_btn = QPushButton("Delete",self)
        self.delete_btn.setGeometry(1400,680,300,50)
        self.delete_btn.setStyleSheet("""
                background-color: black;
                border-color: rgb(0,255,0);
                border-width: 2px;
                border-style: outset;
                border-radius: 15px;
                color: rgb(0,255,0)
                """)
        self.delete_btn.setFont(QFont("Consolas",20))
        self.delete_btn.clicked.connect(self.delete_data)
        

    def update_data(self):
        self.baza_use()
        sql   = "UPDATE telefon SET model = %s,price = %s,ESIM = %s,color = %s WHERE id = %s;"
        id = int(self.txt_update.text())
        self.my_cur.execute(sql,(self.txt_update.text(),self.txt_update.text(),self.txt_update.text(),self.txt_update.text(),id))
        self.my_con.commit()
        print("UPDATE BTN RABOTAYET")
        self.show_info()




    def delete_data(self):
        
        self.baza_use()
        sql   = "DELETE FROM telefon WHERE id = %s;"
        id = int(self.txt_delete.text())
        self.my_cur.execute(sql,(id))
        self.my_con.commit()
        print("DELETE BTN RABOTAYET")
        self.show_info()



        
    def baza_use(self):
        self.my_con = m.connect(host = 'localhost',user= 'root',password = 'root',database = 'phone')
        self.my_cur = self.my_con.cursor()
        
    def insert_data(self):
        self.baza_use()
        sql   = "INSERT INTO telefon(model,price,ESIM,color) VALUES (%s,%s,%s,%s);"
        model = self.txt_model.text()
        price = int(self.txt_price.text())
        esim  = self.txt_ESIM.isChecked()
        color = self.txt_color.currentText()
        value = (model,price,esim,color) 
        self.my_cur.execute(sql,value)
        self.my_con.commit() 
        print("INSERT BTN RABOTAYET")
        self.show_info()
    
    def show_data(self):
        if self.txt_column.currentText() in ("ID","Price","ESIM"):
            sql = f"SELECT * from telefon where {self.txt_column.currentText()} = {self.txt_value.text()}"
        else:
            sql = f"SELECT * from telefon where {self.txt_column.currentText()} = '{self.txt_value.text()}'"
        print(sql)
        self.show_info(sql)
        
    def sort_data(self):
        if self.incr.isChecked():
            sql = f"SELECT * from telefon order by {self.txt_column.currentText()} asc "
        else:
            sql = f"SELECT * from telefon order by {self.txt_column.currentText()} desc "
        print(sql)
        self.show_info(sql)
    
        
        
    def  show_info(self,sql = "SELECT * from telefon"):
        
        self.tb.setVisible(True)
        self.tb.setGeometry(50,600,900,400)
        self.tb.setColumnCount(5)
        self.tb.setHorizontalHeaderLabels(["ID:","Model","Price","ESIM","Color"])

     
        
        self.baza_use()
        self.my_cur.execute(sql)
        result = self.my_cur.fetchall()
        row_c = len(result)
        self.tb.setRowCount(row_c+1)
        ls = []
        for x in range(row_c+1):
            ls.append("")
        self.tb.setVerticalHeaderLabels(ls)
        
        # header = self.tb.horizontalHeader()
        # for x in range(5):
        #     header.setSectionResizeMode(x,header.ResizeToContents)
        
        self.tb.setColumnWidth(0,50)
        self.tb.setColumnWidth(1,250)
        self.tb.setColumnWidth(2,150)
        self.tb.setColumnWidth(3,150)
        self.tb.setColumnWidth(4,250)
        
        ver = self.tb.verticalHeader()
        ver.setDefaultAlignment(Qt.AlignCenter)
        
        for x,y in zip(range(row_c),result):
            self.tb.setItem(x,0,QTableWidgetItem(str(y[0])))
            self.tb.setItem(x,1,QTableWidgetItem(str(y[1])))
            
            if y[3]:
                s = "ESIM"
            else:
                s = "SIM"
            self.tb.setItem(x,2,QTableWidgetItem(str(y[2])))
            self.tb.setItem(x,3,QTableWidgetItem(s))
            self.tb.setItem(x,4,QTableWidgetItem(str(y[4])))
            
       
        
        
    
if __name__ == "__main__":
    os.system("cls")
    app =QApplication(sys.argv)
    ilova = main_window()
    ilova.show()
    sys.exit(app.exec_())
        

















