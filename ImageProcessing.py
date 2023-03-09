import cv2
import numpy as np

imageName = input('image name with extention : ')
# Load an image from file
img = cv2.imread(('/images/', imageName) , cv2.IMREAD_COLOR)

# Convert the image to grayscale
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the image
# img = cv2.GaussianBlur(img, (0,0), 0)

# Apply Canny edge detection to the image
# img = cv2.Canny(img, 0, 0)

# Find contours in the image
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
# cv2.drawContours(img, gray, -1, (0, 255, 0), 2)

# Resize the contours on the original image
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Show the resulting image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.imwrite('New_'+imageName, img)
cv2.destroyAllWindows()


''' 50% 리사이징
img = cv2.imread("test.jpg", cv2.IMREAD_COLOR)
img_half = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

cv2.imshow("resize", img_half)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''