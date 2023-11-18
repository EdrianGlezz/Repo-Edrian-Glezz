import cv2
import numpy as np

# Inicializa la cámara web
cap = cv2.VideoCapture(0)

# Define el rango de colores en formato HSV para el negro
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 30])

while True:
    # Captura un cuadro de la cámara
    ret, frame = cap.read()

    if not ret:
        break

    # Convierte la imagen a formato HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crea una máscara para el color negro
    mask = cv2.inRange(hsv_frame, lower_black, upper_black)

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

            # Dibuja un cuadro verde alrededor del objeto
            cv2.rectangle(frame, (center_x - 50, center_y - 50), (center_x + 50, center_y + 50), (0, 255, 0), 2)

            # Calcula el desplazamiento con respecto al centro de la pantalla
            frame_height, frame_width, _ = frame.shape
            displacement_x = center_x - frame_width // 2
            displacement_y = center_y - frame_height // 2

            # Muestra el desplazamiento en la pantalla
            cv2.putText(frame, f"Desplazamiento X: {displacement_x}, Y: {displacement_y}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Muestra el cuadro de la cámara en tiempo real
    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos y cierra las ventanas
cap.release()
cv2.destroyAllWindows()
