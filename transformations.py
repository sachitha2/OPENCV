import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpg')

cv.imshow("Cat",img)


# Translations 

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1],img.shape[0])

    return cv.warpAffine(img,transMat,dimentions)


#  -x -->Left
#  -y -->Up
#  x --> Right
#  y -->down


translated = translate(img,100,100)

cv.imshow("Translated",translated)


# Rotation

def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
         rotPoint = (width//2,height//2)


    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)

    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,180)
cv.imshow("Rotated image",rotated)

# Resissing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)

cv.imshow('Resized ',resized)


# Flipping
flip = cv.flip(img,0)

# 0 for verticaly
#  1 for horizontally
#  -1 for vertically and horizontally

cv.imshow("Flip",flip)


# cropping 

cropped = img[200:400,300:400]

cv.imshow("cropped",cropped)

cv.waitKey(0)