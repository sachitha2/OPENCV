import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/nature.jpg')
blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

cv.imshow('cat',img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
# simple thresh holding
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)

cv.imshow("simple thresh",thresh)


threshold,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("simple thresh _inv",thresh_inv)


# Adaptive thresh
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive ',adaptive_thresh)

cv.waitKey(0)