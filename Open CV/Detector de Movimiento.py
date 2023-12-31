import cv2
import numpy as np

video= cv2.VideoCapture(0)
i=0


while True:
    ret, frame= video.read()
    frame= cv2.flip(frame,1)
    if ret == False: break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if  i == 20:
        bgGray = gray
    if  i > 20:
        dif = cv2.absdiff(gray,bgGray)
        _,humbralizacion =cv2.threshold(dif,30,255,cv2.THRESH_BINARY)
        contorns,_=cv2.findContours(humbralizacion,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame,contorns,-1,(0,0,255),2)
        #cv2.imshow('dif',dif)
        #cv2.imshow('humbralizacion',humbralizacion)
        for C in contorns:
            area=cv2.contourArea(C)
            if area > 9000:
                x,y,w,h =cv2.boundingRect(C)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)


    cv2.imshow('frame',frame)
    i = i+1
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break
video.release()
