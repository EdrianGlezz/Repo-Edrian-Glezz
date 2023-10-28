import sys
import cv2
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()

        self.camera_capture = cv2.VideoCapture(0)  # Abre la cámara 0 (puede ser diferente en tu sistema)
        self.camera_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Ancho del marco
        self.camera_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Alto del marco

        self.image_folder = "imagen_maestra"
        if not os.path.exists(self.image_folder):
            os.mkdir(self.image_folder)

        self.image_label = QLabel(self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)

        self.capture_button = QPushButton("Tomar Foto")
        self.layout.addWidget(self.capture_button)
        self.capture_button.clicked.connect(self.take_photo)

        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(20)  # Actualiza el feed de video cada 20 ms

    def update_frame(self):
        ret, frame = self.camera_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            self.image_label.setPixmap(pixmap)

    def take_photo(self):
        ret, frame = self.camera_capture.read()
        if ret:
            image_path = os.path.join(self.image_folder, "captured_image.jpg")
            cv2.imwrite(image_path, frame)
            self.show_saved_image(image_path)

    def show_saved_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CameraApp()
    window.setWindowTitle('Capturadora de Imágenes')
    window.show()
    sys.exit(app.exec_())
