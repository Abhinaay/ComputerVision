#!/usr/bin/python3

import cv2

# calling classifier
casclf=cv2.CascadeClassifier('facedata.xml')

#loading face data


# start camera
cap=cv2.VideoCapture(0)

# status of camera

while cap.isOpened():
    status,frame=cap.read()
    # now we can apply classifier in live frame
    face=casclf.detectMultiScale(frame,1.13,5)    
                        # Classifier tuning parameter
    for x,y,h,w in face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),2)
        #only face
        facedata=frame[x:x+h,y:y+w]
        cv2.imshow('f',facedata)
    cv2.imshow('face',frame)
    
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()


