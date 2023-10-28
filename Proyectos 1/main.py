# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import SoapClient
import datetime

from PySide2.QtWidgets import QApplication, QWidget,QComboBox,QMainWindow,QLabel
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QFile,QTimer
from PySide2.QtUiTools import QUiLoader


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.load_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.clear)
        self.window.PB01.clicked.connect(self.refresh) 
        self.window.comboBox1.addItems(["Dyson"])
        self.setMinimumSize(1200,950)
        
        

############################## refresh Data ######################################
        
    def refresh(self):
        
        Customer = self.window.comboBox1.currentText()
        SerialNumber = self.window.TESerialNumber.toPlainText()
        response = SoapClient.serverRequest.fnGetTestHistory(Customer,SerialNumber)
        
       

        finder = response.find('Status: Fail',0,7000)
        data = response[finder - 440:finder + 12]
        failureMode = data[data.find('<FailureLabel>') + 14:data.find('</FailureLabel>')]
        dataLow = failureMode.lower()

        machineName = data[data.find('<MachineName>') + 60:data.find('</MachineName>')]

        self.window.LBSerialNumber.setText(SerialNumber)
        self.window.LBFailmode.setText(failureMode)
        if (dataLow.find('plate_offset') == 0):
            self.window.LBRework.setText('RETORNAR')
        else:
            self.window.LBRework.setText('DIAGNOSTICO')

        if (machineName == 101):
            self.window.LBMachine.setText('Maquina 1')
        
        else:
            self.window.LBMachine.setText('Maquina 2')

        self.timer.start(500)
##############################Counter#############################################

#UAJ1MXX308--1309D0SB150595
############################## clear Labels ######################################

    def clear(self):
        self.window.LBSerialNumber.setText('N/A')


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
