import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



img = cv.imread('photos/cat.jpg')

blank =  np.zeros(img.shape[:2],dtype='uint8')

cv.imshow('cat',img)

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('merged blue',blue)
cv.imshow('merged green',green)
cv.imshow('merged red',red)


cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


merged = cv.merge([b,g,r])

cv.imshow('Merged',merged)


cv.waitKey(0)