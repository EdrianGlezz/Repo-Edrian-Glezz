import cv2
imagen= cv2.imread('cartas.png') #leer imagen
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) #convertir a gris
bordes=cv2.Canny(grises,100,200) #encontrar bordes con algoritmo de CANNY

contornos,_=cv2.findContours(bordes,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contornos,-1,(255,0,0),2)
print('Num de Contornos',len(contornos))

texto = 'Contornos encontrados: '+ str(len(contornos))
cv2.putText(imagen, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 0, 0), 1)

cv2.imshow('bordes',bordes)
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()