import datetime
import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.maquina1_count = 0
        self.maquina2_count = 0
        
        # Obtener la fecha actual
        self.fecha_actual = datetime.date.today()

        # Cargar el archivo de registro de la fecha actual, si existe
        try:
            with open(f"registro-{self.fecha_actual}.txt", "r") as archivo:
                registros = archivo.readlines()
            # Leer los registros y actualizar los contadores
            self.maquina1_count = int(registros[0])
            self.maquina2_count = int(registros[1])
        except FileNotFoundError:
            pass
        
        # Crear los elementos de la interfaz
        self.maquina1_label = QtWidgets.QLabel(f"Máquina 1: {self.maquina1_count}")
        self.maquina2_label = QtWidgets.QLabel(f"Máquina 2: {self.maquina2_count}")
        self.reset_button = QtWidgets.QPushButton("Reset")
        self.save_button = QtWidgets.QPushButton("Guardar")
        
        # Conectar los botones a sus respectivas funciones
        self.reset_button.clicked.connect(self.reset_counters)
        self.save_button.clicked.connect(self.guardar_registros)
        
        # Crear un layout vertical y añadir los elementos a él
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.maquina1_label)
        layout.addWidget(self.maquina2_label)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.save_button)
        
        self.setLayout(layout)
        
    # Función para reiniciar los contadores
    def reset_counters(self):
        self.maquina1_count = 0
        self.maquina2_count = 0
        self.actualizar_labels()
    
    # Función para guardar los registros
    def guardar_registros(self):
        with open(f"registro-{self.fecha_actual}.txt", "w") as archivo:
            archivo.write(f"{self.maquina1_count}\n{self.maquina2_count}")
    
    # Función para actualizar los labels de la interfaz
    def actualizar_labels(self):
        self.maquina1_label.setText(f"Máquina 1: {self.maquina1_count}")
        self.maquina2_label.setText(f"Máquina 2: {self.maquina2_count}")
        
    # Función para manejar el evento de incrementar el contador de la máquina 1
    def incrementar_maquina1(self):
        self.maquina1_count += 1
        self.actualizar_labels()
    
    # Función para manejar el evento de incrementar el contador de la máquina 2
    def incrementar_maquina2(self):
        self.maquina2_count += 1
        self.actualizar_labels()
