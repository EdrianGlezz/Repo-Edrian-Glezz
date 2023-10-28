import cv2
import numpy as np
cam = cv2.VideoCapture (0)
kernel = np.ones((8,8),np.uint8)

while (True):
    ret,frame = cam.read()
    rangomax = np.array ([90,255,90])
    rangomin = np.array([0,90,0])
    mascara = cv2.inRange (frame, rangomin,rangomax)
    opening = cv2.morphologyEx (mascara, cv2.MORPH_OPEN, kernel)
    x,y,w,h = cv2. boundingRect (opening)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,500,0),4)
    cv2.imshow('camara',frame)
    k = cv2.waitKey(1)&0xff
    if k==27:
        break

