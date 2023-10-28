import cv2
import numpy as np

# Inicializa la cámara web
cap = cv2.VideoCapture(1)

# Define el rango de colores en formato HSV para el azul
lower_blue = np.array([90, 50, 50])  # Valores para el azul
upper_blue = np.array([130, 255, 255])  # Valores para el azul

while True:
    # Captura un cuadro de la cámara
    ret, frame = cap.read()

    if not ret:
        break

    # Convierte la imagen a formato HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crea una máscara para el color azul
    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    # Encuentra los contornos en la máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Inicializa las coordenadas del centro del objeto
    center_x, center_y = None, None

    if contours:
        # Encuentra el contorno más grande (objeto circular)
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)

        if M["m00"] != 0:
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])

            # Dibuja el contorno del objeto en rojo
            cv2.drawContours(frame, [largest_contour], -1, (0, 0, 255), 2)

            # Dibuja el centroide del objeto en azul
            cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)

    # Calcula el desplazamiento con respecto al centro de la pantalla
    frame_height, frame_width, _ = frame.shape
    if center_x is not None:
        displacement_x = center_x - frame_width // 2
    else:
        displacement_x = 0
    if center_y is not None:
        displacement_y = center_y - frame_height // 2
    else:
        displacement_y = 0

    # Muestra el desplazamiento cerca del centroide del objeto
    if center_x is not None and center_y is not None:
        text = f"Desplazamiento X: {displacement_x}, Y: {displacement_y}"
        cv2.putText(frame, text, (center_x + 10, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Muestra el cuadro de la cámara en tiempo real
    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos y cierra las ventanas
cap.release()
cv2.destroyAllWindows()
