import cv2 as cv;


# img = cv.imread('photos/cat_large.jpg')

# cv.imshow("Cat",img);

# Reading videos
capture = cv.VideoCapture('video/dog.mp4')

# 0 for access web cam
# other numbers for next cameras
#1 for another camera

while True:
    isTrue , frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

cv.destroyAllWindows()
