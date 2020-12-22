import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3),dtype='uint8')
# width,height, number of color channels
# uint8 is Data type of image

cv.imshow('blank',blank) 

# 1 .paint a certain color

# blank[200:300,200:300] = 0,255,0 # RGB

# cv.imshow('Green',blank)

# 2.draw a rectangle

cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=50)
# cv.imshow("Rectangle",blank)

# 3.Draw a circle
cv.circle(blank,(250,250),100,(255,0,200),thickness=-1)
# cv.imshow("Circle",blank)

#4 . Draw a line
cv.line(blank,(0,0),(250,250),(0,255,255),thickness=2)

# cv.imshow("new image",blank)

# 5 . Draw text
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0),2)
cv.imshow('Text',blank)
# img = cv.imread('photos/cat.jpg')

# cv.imshow('Cat ',img)

cv.waitKey(0)