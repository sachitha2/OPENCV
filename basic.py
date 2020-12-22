import cv2 as cv
img = cv.imread('photos/cat.jpg')

cv.imshow("Cat",img)


# Converting to gray scale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


cv.imshow('Gray',gray)


# Blur 

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

cv.imshow('Blur',blur)


# Edge cascade

canny = cv.Canny(blur,125,175)

cv.imshow("Canny Edges",canny)


# Dialating the image

dialated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dialated ",dialated)

# Eroding

eroded = cv.erode(dialated, (7,7),iterations=3)

cv.imshow("Eroded",eroded)

# Resize

resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized',resized)

# croping

cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)