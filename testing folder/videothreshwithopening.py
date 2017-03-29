import cv2
import numpy as np

kernel = np.ones((10,10),np.uint8)

# open video file
cap = cv2.VideoCapture('/home/bence/Downloads/kodkamrademo.mp4')

while True:
    # capture frames
    ret, frame = cap.read()
    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # median blurring
    median = cv2.medianBlur(gray, 9)
    # erosion -> dilation
    opening = cv2.morphologyEx(median, cv2.MORPH_OPEN, kernel)
    # binary thresholding
    ret, thresh1 = cv2.threshold(median, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow('frame', thresh1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
