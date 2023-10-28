import cv2
import numpy as np


# Umbral de porcentaje de píxeles azules para la detección
threshold_percentage = 0.1  # Cambia este valor según tus necesidades

# Tamaño mínimo de área para la detección (ajusta este valor según tus necesidades)
min_area = 5000

# Inicializa la cámara web
cap = cv2.VideoCapture(0)

# Define el rango de colores en formato HSV para el azul
lower_blue = np.array([90, 50, 50])  # Valores para el azul
upper_blue = np.array([130, 255, 255])  # Valores para el azul


# Configura el kernel para la dilatación
kernel = np.ones((6,6), np.uint8)

while True:
    # Captura un cuadro de la cámara
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) #Gira en modo espejo la imagen
    if not ret:
        break

    # Obtiene las dimensiones del cuadro
    frame_height, frame_width, _ = frame.shape

    # Convierte la imagen a formato HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crea una máscara para el color azul
    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    # Aplica una dilatación a la máscara
    mask = cv2.dilate(mask, kernel, iterations=2)
    
    # Encuentra todos los contornos en la máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Inicializa una lista para almacenar las coordenadas de los centros de los objetos detectados
    centers = []

    # Inicializa una lista para almacenar las áreas de los contornos
    areas = []

    # Itera a través de los contornos
    for contour in contours:
        # Calcula el área del contorno
        area = cv2.contourArea(contour)

        # Calcula el porcentaje de píxeles azules en el contorno
        blue_pixels = cv2.countNonZero(mask)
        blue_percentage = blue_pixels / area if area > 0 else 0
        
        # Encuentra el centroide del contorno
        M = cv2.moments(contour)

        # Verifica si el área supera el tamaño mínimo
        if M["m00"] != 0 and blue_percentage > threshold_percentage and area > min_area:
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
            centers.append((center_x, center_y))
            areas.append(area)

    # Ordena las áreas en orden descendente y almacena los índices de la lista ordenada
    sorted_indexes = np.argsort(areas)[::-1]

    # Dibuja los contornos y asigna etiquetas a las áreas en función de su orden en la lista ordenada
    for i, index in enumerate(sorted_indexes):
        contour = contours[index]
        area = areas[index]
        center_x, center_y = centers[index]

        # Dibuja el contorno del objeto en rojo
        cv2.drawContours(frame, [contour], -1, (0, 0, 255), 2)
        # Dibuja el centroide del objeto en azul
        cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)

        # Dibuja la etiqueta del área
        cv2.putText(frame, f"A {i + 1}", (center_x + 10, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # Calcula el desplazamiento con respecto al centro de la pantalla para el objeto detectado
        #frame_height, frame_width, _ = frame.shape
        displacement_x = center_x - frame_width // 2
        displacement_y = center_y - frame_height // 2
        # Muestra el desplazamiento cerca del centroide del objeto
        text = f"D = X: {displacement_x}, Y: {displacement_y}"
        cv2.putText(frame, text, (center_x + 10, center_y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    # Dibuja el punto central en verde
    cv2.circle(frame, (frame_width // 2, frame_height // 2), 5, (0, 255, 0), -1)

    # Dibuja puntos en el plano cartesiano cada 20 unidades en x e y
    for i in range(20, frame_width, 20):
        cv2.circle(frame, (i, frame_height // 2), 2, (0, 255, 0), -1)
    for j in range(20, frame_height, 20):
        cv2.circle(frame, (frame_width // 2, j), 2, (0, 255, 0), -1)

    # Muestra el cuadro de la cámara en tiempo real
    cv2.imshow("Object Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos y cierra las ventanas
cap.release()
cv2.destroyAllWindows()