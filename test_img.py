import cv2
import matplotlib.pyplot as plt 
import numpy as np
from random import *
from test_detect_cube import *

# Load ảnh 
img = cv2.imread('images/worst_rubik.jpeg')
# plt.rcParams['figure.figsize'] = [10, 8]
# copy = img.copy()

# #canny để tìm cạnh: 
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Apply Gaussian blur to reduce noise
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# edges = cv2.Canny(blurred, 100, 150)
# # Apply adaptive thresholding
# adaptive_thresh = cv2.adaptiveThreshold(
#     blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
# )

# # Perform morphological closing
# kernel = np.ones((5, 5), np.uint8)

# # open xong close
# opened = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_CLOSE, kernel)

# # Perform morphological opening
# closed = cv2.morphologyEx(opened, cv2.MORPH_OPEN, kernel)

# # #close xong open 
# # closed = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_CLOSE, kernel)

# # # Perform morphological opening
# # opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)


# # Display the results
# cv2.imshow('Original Image', img)
# cv2.imshow('Edges', adaptive_thresh)  # Display the edges explicitly
# cv2.imshow('Closed', closed)
# cv2.imshow('Opened', opened)
# cv2.imshow("Kenny edge", edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
captureFrame(img)
cv2.imshow("test img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
