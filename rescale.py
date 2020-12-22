import cv2 as cv;


img = cv.imread('photos/cat_large.jpg')
cv.imshow("Cat",img)


def changeRes(width,height):
    # Only works for live video
    capture.set(3,width)
    capture.set(4,height)

def rescaleFrame(frame, scale=0.75):
    # This is working for images , video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimentions = (width,height)


    return cv.resize(frame,dimentions,interpolation = cv.INTER_AREA)

resized_img = rescaleFrame(img,scale=0.1)

cv.imshow("Cat resized",resized_img)


# Reading videos
capture = cv.VideoCapture('video/dog.mp4')

# 0 for access web cam
# other numbers for next cameras
#1 for another camera

while True:
    isTrue , frame = capture.read()
    frame_resize = rescaleFrame(frame,scale=.3)


    cv.imshow('Video',frame)
    cv.imshow('Video resized',frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

cv.destroyAllWindows()