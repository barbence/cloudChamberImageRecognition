import numpy as np
import cv2

# open haar cascade
alpha_cascade = cv2.CascadeClassifier('~/alpha_classifier/alpha_cascade.xml')

# open video feed
cap = cv2.VideoCapture('kodkamrademo.mp4')

# get frames while true
while(cap.isOpened()):
    ret, img = cap.read()
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # use cascade on frames
    alphas = alpha_cascade.detectMultiScale(gray, 1.3, 5)
    # draw rectangles around detected particles
    for (x,y,w,h) in alphas:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    # show feed
    cv2.imshow('img',img)
    # wait for q key press = user exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
