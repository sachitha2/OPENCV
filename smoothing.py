import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



img = cv.imread('photos/cat.jpg')

blank =  np.zeros(img.shape[:2],dtype='uint8')

cv.imshow('cat',img)


# Averaging

average = cv.blur(img,(7,7))

cv.imshow("average",average)

# Gaussian blur

gauss = cv.GaussianBlur(img,(7,7),0)

cv.imshow('Gauss',gauss)

# Meadian blur

median = cv.medianBlur(img,3)
cv.imshow('median',median) 

#  Bilateral blur
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral',bilateral)


cv.waitKey(0)