import cv2
import numpy as np
# Inicializar la cámara web
cap = cv2.VideoCapture(1)
# Definir el rango de color para la detección de objetos (en este caso, rojo)
lower = np.array([200,0,0])
upper = np.array([255,50,50])
# Punto de origen
origin = (0,0)
while True:
    # Leer un fotograma de la cámara
    _, frame = cap.read()
    # Convertir el fotograma a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Aplicar una máscara para detectar solo el color especificado
    mask = cv2.inRange(hsv, lower, upper)
    # Encontrar el contorno del objeto detectado
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Dibujar un círculo alrededor del objeto detectado
    for c in contours:
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cX, cY), 10, (0, 0, 255), -1)
            # Calcular la distancia desde el punto de origen en milímetros
            distance = np.sqrt((cX - origin[0])**2 + (cY - origin[1])**2)
            distance_mm = distance / 10 # assuming 1 pixel = 0.1mm
            cv2.putText(frame, f"{distance_mm}mm", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    # Mostrar la imagen resultante
    cv2.imshow("Object Detection", frame)
    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()