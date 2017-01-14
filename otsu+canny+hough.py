import cv2
import numpy as np
from matplotlib import pyplot as plt

#import image
img = cv2.imread('/home/bence/cc2.jpg', 0)
#blur image w gaussian filtering
blur = cv2.GaussianBlur(img, (5, 5), 0)
#otsu's thresholding
ret, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#save image
cv2.imwrite('otsucc2.jpg', th)

#canny edges
edge = cv2.Canny(th, 100, 200)
#save image
cv2.imwrite('edgescc2.jpg', edge)



edges = cv2.Canny(th, 50, 150, apertureSize = 3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(th, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imwrite('houghlines3.jpg', th)






