# -*- coding: utf-8 -*-

import cv2
print(cv2.__version__)

cascade_src = 'haarcascade_cars.xml'
#video_src = 'C:\\Users\\milindsawant\\Pictures\\IMG_0094.MOV'
video_src = 'video1.avi'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.5, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      
        cv2.putText(img,'Vehicle',(x-2,y-2),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()