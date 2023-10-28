import cv2
imagen = cv2.imread('monedas.jpg') #jalar la imagen con mismo nombre y formato

############## Proceso de humbralizacion#####################
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) #volver la imagen a gris
_,humbralizacion = cv2.threshold(gris,240,255, cv2.THRESH_BINARY_INV) # Humbralizarla 

contornos,_ = cv2.findContours(humbralizacion,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #encontrar contornos ()

"""cv2.drawContours (imagen,contornos,-1,(255,0,0),2)
print('Contornos:',len(contornos))



cv2.imshow('imagen',imagen) #mostrar la imagen
cv2.imshow('Humbralizacion',humbralizacion) #mostrar la imagen humbralizada
cv2.waitKey(0)
cv2.destroyAllWindows()"""

fuente = cv2.FONT_HERSHEY_SIMPLEX
i=0
for c in contornos:
    M = cv2.moments(c)
    if (M["m00"]==0): M["m00"]=1
    cx = int(M["m10"]/M["m00"])
    cy = int(M['m01']/M['m00'])

    mensaje= 'Num:' +str(i+1)
    cv2.putText(imagen,mensaje,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,0.80,(255,0,0),2,cv2.LINE_AA)
    cv2.drawContours( imagen,[c],0,(255,0,0),2)
    cv2.imshow('imagen',imagen)
    cv2.waitKey(0)
    i = i+1
cv2.destroyAllWindows()