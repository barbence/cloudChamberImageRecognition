import cv2
import numpy as np

kernel = np.ones((4,4),np.uint8)

# read demo image
img = cv2.imread('/home/bence/cc2.jpg', 0)

# median blurring
median = cv2.medianBlur(img, 5)
# erosion -> dilation
opening = cv2.morphologyEx(median, cv2.MORPH_OPEN, kernel)
# binary thresholding
ret, thresh1 = cv2.threshold(opening, 200, 255, cv2.THRESH_BINARY)


# save file
cv2.imwrite('opened_cc2.jpg', thresh1)
