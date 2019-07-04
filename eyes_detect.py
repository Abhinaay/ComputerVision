#!/usr/bin/python3

import cv2

# calling classifier
casclf=cv2.CascadeClassifier('eyedata.xml')

#loading eyeglasses data


# start camera
cap=cv2.VideoCapture(0)

# status of camera

while cap.isOpened():
    status,frame=cap.read()
    # now we can apply classifier in live frame
    eye=casclf.detectMultiScale(frame,1.13,5)
                        # Classifier tuning parameter
    for x,y,h,w in eye:
        cv2.circle(frame,(x+int((h/2)),y+int((w/2))),20,(0,255,0),2)

    cv2.imshow('face',frame)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break
    
    
cv2.destroyAllWindows()
cap.release()

