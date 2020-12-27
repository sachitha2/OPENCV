import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/nature.jpg')
blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

cv.imshow('cat',img)


# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# cv.imshow('gray',gray)

# # Gray scale histogram
# gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])


# plt.figure()
# plt.title('Gray scale')
# plt.xlabel('Bins')
# plt.ylabel('# number of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


# Color histograms



plt.figure()
plt.title('Gray scale')
plt.xlabel('Bins')
plt.ylabel('# number of pixels')
colors = ('b','g','r')

for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)