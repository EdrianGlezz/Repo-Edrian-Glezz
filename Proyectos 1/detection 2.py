import cv2
import numpy as np

# Cargar el modelo pre-entrenado para la detección de rostros
face_detector = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000.caffemodel')

# Cargar las características de referencia para cada persona a reconocer
known_faces = {}

# Definir una función para realizar el reconocimiento de rostros
def recognize_face(frame, face_detector):
    # Preprocesar el frame
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], False, False)
    face_detector.setInput(blob)
    detections = face_detector.forward()
    # Iterar sobre las detecciones
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            # Obtener las coordenadas del rostro
            x1, y1, x2, y2 = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            face = frame[int(y1):int(y2), int(x1):int(x2)]
            face_blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), [104, 117, 123], False, False)
            # Extraer las características del rostro y compararlas con las caras conocidas
            face_features = face_recognizer.predict(face_blob)
            best_match = min(known_faces, key=lambda x: np.linalg.norm(known_faces[x] - face_features))
            return best_match
    return None

# Capturar video desde la webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        height, width, _ = frame.shape
        # Realizar el reconocimiento de rostros
        recognized_face = recognize_face(frame, face_detector)
        if recognized_face is not None:
            cv2.putText(frame, recognized_face, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow('Reconocimiento de Rostros', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
