import numpy as np
import cv2

alpha_cascade = cv2.CascadeClassifier('alpha_classifier/alpha_cascade.xml')

img = cv2.imread('/smallcc2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
alphas = alpha_cascade.detectMultiScale(gray, 1.7, 5)
for (x,y,w,h) in alphas:
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #cv2.putText(img,'alpha',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
