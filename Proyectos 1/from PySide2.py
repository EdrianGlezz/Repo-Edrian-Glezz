from PySide2.QtWidgets import QApplication, QMainWindow, QTextEdit
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.textbox = QTextEdit()
        self.setCentralWidget(self.textbox)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            # Obtener los datos del scanner y agregarlos al textbox
            scanner_data = obtener_datos_del_scanner()
            self.textbox.append(scanner_data)

def obtener_datos_del_scanner():
    # Código para obtener los datos del scanner
    # Se puede usar la librería PySerial o alguna otra librería para comunicarse con el scanner
    scanner_data = "datos del scanner"
    return scanner_data
    print()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
