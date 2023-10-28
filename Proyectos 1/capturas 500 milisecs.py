import cv2
import time

# Crear objeto de captura de video
cap = cv2.VideoCapture(0)

# Establecer el temporizador a 500 milisegundos
timer = time.time() + 5000

while True:
    # Verificar si el temporizador ha expirado
    if time.time() >= timer:
        # Capturar una imagen desde la cámara
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        # Guardar la imagen en un archivo
        cv2.imwrite('foto.jpg', frame)
        cv2.imshow('foto.jpg', frame)
        # Reiniciar el temporizador
        timer = time.time() + 5000

# Liberar objeto de captura de video y destruir todas las ventanas de visualización
cap.release()
cv2.destroyAllWindows()
