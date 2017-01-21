import cv2

# read demo image
img = cv2.imread('~/cc2.jpg', 0)

# erosion -> dilation
median = cv2.medianBlur(img, 5)
# binary thresholding
ret, thresh1 = cv2.threshold(median, 200, 255, cv2.THRESH_BINARY)

# save file
cv2.imwrite('binarycc2.jpg', thresh1)






