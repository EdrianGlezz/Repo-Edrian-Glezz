import cv2
captura = cv2.VideoCapture(0)

while (captura.isOpened()):
  ret, imagen = captura.read()
  imagen= cv2.flip(imagen,1)


  
  if ret == True:
    cv2.imshow('video', imagen)
    if cv2.waitKey(1) & 0xFF == ord(' '):
      break
  else: break
captura.release()
cv2.destroyAllWindows()