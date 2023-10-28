# El elemento a visualizar en una ventana tiene que ser un Qwidget y en su interior debe de ir todo el contenido 

import os
from pathlib import Path
import sys
from PySide2.QtWidgets import QApplication, QWidget,QComboBox,QMainWindow,QLabel,QPlainTextEdit,QLineEdit,QPushButton
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Qt


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.load_ui()
        QWidget.showMaximized(self) #muestra la pantalla Maximizada
        


        
#..................................Aqui ve el Codigo todo con self.window!!!........................

        


        self.window.Boton.setDefault(True) #enfoque de "enter" para el push boton
        self.window.Texto.setFocus() #enfoca el cursor al cuadro de texto (es un QlineEdit con nombre "Texto")
       
        self.window.Boton.clicked.connect(self.copiar_texto) #cuando el boton clikea conecta con el evencon Copiar Texto
        self.window.Texto.returnPressed.connect(self.copiar_texto)  # Manejar el evento Enter

    def copiar_texto(self):
        respuesta = self.window.Texto.text()
        texto_predefinido= "Que Pedo Pinche "
        texto_completo= texto_predefinido + respuesta

        self.window.Respuesta.setText(texto_completo)
        self.window.Texto.clear()

        













    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "prueba.ui")  # Aqui debe de ir el nombre del archivo, en este caso es "prueba.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)
        ui_file.close()
        

if __name__ == "__main__":
    app = QApplication([])
    widget = main()     
    widget.show()
    sys.exit(app.exec_())
