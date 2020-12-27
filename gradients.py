import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/cat.jpg')
blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

cv.imshow('cat',img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
# laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow('lap',lap)

# sobel

sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)

combined_sobel = cv.bitwise_or(sobelx,sobely)


cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel y',sobely)
cv.imshow('sobel',combined_sobel)

cv.waitKey(0)