import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class CounterWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.count = 0

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 250, 150)

        self.label = QLabel('Maquina 1', self)
        self.label.setGeometry(50, 20, 150, 20)

        self.counter_label = QLabel('0', self)
        self.counter_label.setGeometry(100, 50, 50, 20)

        self.increment_button = QPushButton('+', self)
        self.increment_button.setGeometry(50, 80, 50, 30)
        self.increment_button.clicked.connect(self.increment_counter)

        self.reset_button = QPushButton('Reset', self)
        self.reset_button.setGeometry(110, 80, 70, 30)
        self.reset_button.clicked.connect(self.reset_counter)

        self.save_button = QPushButton('Guardar', self)
        self.save_button.setGeometry(50, 120, 130, 30)
        self.save_button.clicked.connect(self.save_count)

    def increment_counter(self):
        self.count += 1
        self.counter_label.setText(str(self.count))

    def reset_counter(self):
        self.count = 0
        self.counter_label.setText('0')

    def save_count(self):
        # Aquí podrías guardar el valor del contador en una base de datos, archivo, etc.
        print(f'Se ha guardado el valor {self.count}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CounterWindow()
    window.show()
    sys.exit(app.exec_())
