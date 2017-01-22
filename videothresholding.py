import cv2
import numpy as np

cap = cv2.VideoCapture('/home/bence/Downloads/kodkamrademo.mp4')

while (True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # erosion -> dilation
    median = cv2.medianBlur(gray, 3)

    # binary thresholding
    ret, thresh1 = cv2.threshold(median, 200, 255, cv2.THRESH_BINARY)

    cv2.imshow('frame', thresh1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()