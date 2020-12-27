import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


blank =  np.zeros((400,400),dtype='uint8')

rectanlge = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rect',rectanlge)
cv.imshow('circle',circle)

# bitwise AND
b_and = cv.bitwise_and(circle,rectanlge)

cv.imshow('AND',b_and)


b_or = cv.bitwise_or(rectanlge,circle)

cv.imshow("or",b_or)


b_xor = cv.bitwise_xor(rectanlge,circle)
cv.imshow("xor",b_xor)

# bitwise not

b_not = cv.bitwise_not(rectanlge)
cv.imshow('not',b_not)


cv.waitKey(0)