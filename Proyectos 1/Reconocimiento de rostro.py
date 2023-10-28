import cv2
# Inicializar la cámara
cap = cv2.VideoCapture(1)
# Cargar el classificador de rostros pre-entrenado
face_cascade = cv2.CascadeClassifier('C:/Users/1281581/OneDrive - Jabil/Documents/Python/Proyectos 1/haarcascade_frontalface_default.xml')
while True:
    # Leer un fotograma de la cámara
    ret, frame = cap.read()
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detectar rostros en el fotograma
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Dibujar un rectángulo alrededor de los rostros detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    frame = cv2.flip(frame,1)
    # Mostrar el fotograma con los rostros detectados
    cv2.imshow('Face Detection', frame)
    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()

