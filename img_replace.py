import cv2

# reading image data
img1=cv2.imread('/home/abhinaay/python-prog/image1.jpg')
img2=cv2.imread('/home/abhinaay/python-prog/image2.jpg')

r1=img1[50:500,50:500].copy()
r2=img2[50:500,50:500].copy()

# replacing
img1[50:500,50:500]=r2
img2[50:500,50:500]=r1

# display
cv2.imshow('image1',img1)
cv2.imshow('image2',img2)

# replacing some 10 rows and 20 columns of image2 with that of image 1
img2[40:50,134:154] = img1[87:97,27:47].copy()
cv2.imshow('random',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

