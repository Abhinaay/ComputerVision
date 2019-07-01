>Red color detection
```py
#!/usr/bin/python3

import cv2
# start camera
cap=cv2.VideoCapture(0)

# status of camera

while cap.isOpened():
    status,frame=cap.read()
# detecting red color
    cv2.inRange(frame,(0,0,0),(0,0,255))
    cv2.imshow('leveredcolor',frame)
    if cv2.waitKey(10) & 0xff = ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
```
> Motion Detection
```py
#!/usr/bin/python3
import cv2

#start camera
cap=cv2.VideoCapture(0)

img1=cap.read()[1]  # take1
img2=cap.read()[1]  # take2
img3=cap.read()[1]  # take3

# to make more perfect detection, to avoid light and other problems
#converting to gray
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR@GRAY)   #converting to gray
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR@GRAY)   #converting to gray
gray3=cv2.cvtColor(img3,cv2.COLOR_BGR@GRAY)   

# now creating image differentiator
def img_diff(x,y,z):
    # diff between x,y      --d1
    d1=cv2.absdiff(x,y)
    # diff between y,z      --d2
    d2=cv2.absdiff(y,z)
    # absolute diff. b/w d1 and d2
    finalimg=cv2.bitwise_and(d1,d2)
    return finalimg


# now apply function
while cap.isOpened():
    status,frame=cap.read()     # continue img taker
    motionimg=img_diff(gray1,gray2,gray3)
    # replacing image frame
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('live',frame)
    cv2.imshow('motion',motionimg)
    
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

```
> **read about google posenet
<!---->
>Human Face Detection

```py
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
        # only face
        # facedata=frame[x:x+h,y:y+w]
        # cv2.imshow('f',facedata)
    cv2.imshow('face',frame)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break
    
    
cv2.destroyAllWindows()
cap.release()


```
