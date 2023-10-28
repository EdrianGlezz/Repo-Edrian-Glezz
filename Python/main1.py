# This Python file uses the following encoding: utf-8
#UAJ1MXX308--1312D0SC221121 power angle maq2
#UAJ1MXX308--1312D0SC220937 press force maq1
#UAJ1MXX308--1312D0SC220778 flow angle maq2
#UAJ1MXX308--1312D0SC220926 power glue maq1

import os
from pathlib import Path
import sys
import SoapClient
import datetime

from PySide2.QtWidgets import QApplication, QWidget,QComboBox,QMainWindow,QLabel,QPlainTextEdit,QLineEdit
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QFile,QTimer,Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QTextStream, QIODevice, QDate, Slot
from datetime import datetime
from sqlite3 import connect




class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.load_ui()
######################################Declaraciones####################################
        self.window.PB01.clicked.connect(self.refresh) 
        self.window.comboBox1.addItems(["Dyson"])
        self.setMinimumSize(1000,950)
        self.db_name = "data.db"
        self.createDb()
        self.window.QReset.clicked.connect(self.resetTable)
        self.window.TESerialNumber.setFocus()
        self.window.PB01.setDefault(True)
        self.window.TESerialNumber.textChanged.connect(self.stoper)
        self.window.TESerialNumber.textChanged.connect(self.limit_text)
#############################Limite de Texto################################################3333
    def limit_text(self):
        text = self.window.TESerialNumber.toPlainText()

        if len(text) > 26:
            self.window.TESerialNumber.setPlainText(text[:26])
            self.window.PB01.click()
 ###############################Delay de 500 milisegundos para que se muestre el texto###########       
    def stoper(self):
        timer = QTimer(self)
        timer.timeout.connect(self.limit_text)
        timer.start(500)
        
 ########################Reset de la tabla Query#######################################           
    
    def resetTable(self):
       self.run_query("""DELETE FROM production""")
       self.refreshCount()
       self.window.TESerialNumber.setFocus()
       
############################## refresh Data ######################################
        
    def refresh(self):
        
        Customer = self.window.comboBox1.currentText()
        SerialNumber = self.window.TESerialNumber.toPlainText()
        response = SoapClient.serverRequest.fnGetTestHistory(Customer,SerialNumber)

        finder = response.find('Status: Fail',0,30000)
        data = response[finder - 300:finder + 12]
        failureMode = data[data.find('<FailureLabel>') + 14:data.find('</FailureLabel>')]
        dataLow = failureMode.lower()
        
        machineName = data[data.find('<MachineName>') + 59:data.find('</MachineName>')]
        self.window.LBSerialNumber.setText(SerialNumber)
        self.window.LBFailmode.setText(failureMode)
        casilla = self.window.LBFailmode.setText(failureMode)
        if "OFFSET" in failureMode:
            self.window.LBRework.setText('RETORNAR A BGPT')
        else:
            self.window.LBRework.setText('DIAGNOSTICO/DESENSAMBLE')   
        


        if str(101) in machineName:
            Machine = "Maquina 1"
            self.window.LBMachine.setText(Machine)
            self.addProduction(Machine,dataLow)

        if str(201) in machineName:
            Machine = "Maquina 2"
            self.window.LBMachine.setText(Machine)
            self.addProduction(Machine,dataLow)

        
        
        self.refreshCount()
        self.window.TESerialNumber.setFocus()
        SerialNumber = self.window.TESerialNumber.clear()
        
############################## Refresh Count#############################################
    def refreshCount(self):
        data = self.run_query("""SELECT Machine,COUNT(Machine)
        FROM production GROUP BY Machine""")
        if data:
            for machine in data:
                
                Maquina,Num = machine

                if Maquina == "Maquina 1":
                    self.window.LBCounter1.setText(str(Num))
                
                if Maquina == "Maquina 2":
                    self.window.LBCounter2.setText(str(Num))
        else:
            self.window.LBCounter1.setText(str(0))
            self.window.LBCounter2.setText(str(0))

            
##############################Base de Datos #############################################
    def createDb(self):
        with connect(self.db_name) as conn:
            try:
                cursor = conn.cursor()
                dbValues = """CREATE TABLE IF NOT EXISTS production
                            (ID INTEGER NOT NULL UNIQUE,
                            Hour TEXT NOT NULL,
                            Date TEXT NOT NULL,
                            Machine NUMERIC NOT NULL,
                            FailMode TEXT NOT NULL,
                            PRIMARY KEY("ID" AUTOINCREMENT),
                            UNIQUE (ID))"""
                cursor.execute(dbValues)
            except IndexError as e:
                print(e)
            finally:
                pass
    

###################################Add Product###################################
    def addProduction(self,Machine,FailMode):
        try:
            timeNow = datetime.now()
            cDate = timeNow.strftime('%d/%m/%Y')
            cTime = timeNow.strftime('%H:%M:%S')

            self.run_query("""INSERT INTO production
                        (Hour,Date,Machine,FailMode)
                        VALUES(?,?,?,?)""",(cTime,cDate,Machine,FailMode))
        except AttributeError as e:
            print (e)
        finally:
            pass
##################################### Run_Query##################################
    def run_query(self,query,parameter = ()):
        try:
            with connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query,parameter)
                result=cursor.fetchall()
                conn.commit()
            return result
        except IndexError as e:
            print(e)
        finally:
            conn.close()


############################## Load Main Page ######################################

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)
        ui_file.close()
        self.timerFlag = False

if __name__ == "__main__":
    app = QApplication([])
    widget = main()     
    widget.show()
    sys.exit(app.exec_())
