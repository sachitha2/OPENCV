import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/cat.jpg')

cv.imshow('cat',img)

# plt.imshow(img)
# plt.show()


# BGR To Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# BGR to HSV 
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# BGR to LAB L*A*B
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('HCV -> BGR',lab_bgr)



cv.waitKey(0)