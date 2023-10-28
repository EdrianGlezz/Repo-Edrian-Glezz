import cv2
captura=cv2.VideoCapture(0)

while True:
    ret,frame=captura.read()
    frame = cv2.flip(frame, 1)











    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
captura.release()
cv2.destroyAllWindows()
