import cv2

#start camera
cap=cv2.VideoCapture(0)

img1=cap.read()[1]  # take1
img2=cap.read()[1]  # take2
img3=cap.read()[1]  # take3

# to make more perfect detection, to avoid light and other problems
#converting to gray
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)   #converting to gray
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)   #converting to gray
gray3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)   

# now creating image differentiator
def img_diff(x,y,z):
    # diff between x,y      --d1
    d1=cv2.absdiff(x,y)
    # diff between y,z      --d2
    d2=cv2.absdiff(y,z)
    # absolute diff. b/w d1 and d2
    finalimg=cv2.bitwise_xor(d1,d2)
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

