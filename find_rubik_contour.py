import cv2
import sys
import time
import math
import numpy as np
import random as rng
from scipy import stats

def detect_face(bgr_image_input):

    gray = cv2.cvtColor(bgr_image_input,cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
    gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

    gray = cv2.adaptiveThreshold(gray,20,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,0)
    #cv2.imwrite()
    try:
         _, contours, hierarchy = cv2.findContours(gray,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    except:
         contours, hierarchy = cv2.findContours(gray,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)


    i = 0
    contour_id = 0
    #print(len(contours))
    count = 0
    blob_colors = []
    for contour in contours:
        A1 = cv2.contourArea(contour)
        contour_id = contour_id + 1

        if A1 < 3000 and A1 > 1000:
            perimeter = cv2.arcLength(contour, True)
            epsilon = 0.01 * perimeter
            approx = cv2.approxPolyDP(contour, epsilon, True)
            hull = cv2.convexHull(contour)
            if cv2.norm(((perimeter / 4) * (perimeter / 4)) - A1) < 150:
                #if cv2.ma
                count = count + 1
                x, y, w, h = cv2.boundingRect(contour)
                #cv2.rectangle(bgr_image_input, (x, y), (x + w, y + h), (0, 255, 255), 2)
                #cv2.imshow('cutted contour', bgr_image_input[y:y + h, x:x + w])
                val = (50*y) + (10*x)
                blob_color = np.array(cv2.mean(bgr_image_input[y:y+h,x:x+w])).astype(int)
                cv2.drawContours(bgr_image_input,[contour],0,(255, 255, 0),2)
                cv2.drawContours(bgr_image_input, [approx], 0, (255, 255, 0), 2)
                blob_color = np.append(blob_color, val)
                blob_color = np.append(blob_color, x)
                blob_color = np.append(blob_color, y)
                blob_color = np.append(blob_color, w)
                blob_color = np.append(blob_color, h)
                blob_colors.append(blob_color)
    if len(blob_colors) > 0:
        blob_colors = np.asarray(blob_colors)
        blob_colors = blob_colors[blob_colors[:, 4].argsort()]
    face = np.array([0,0,0,0,0,0,0,0,0])
    if len(blob_colors) == 9:
        #print(blob_colors)
        for i in range(9):
            #print(blob_colors[i])
            if blob_colors[i][0] > 120 and blob_colors[i][1] > 120 and blob_colors[i][2] > 100:
                blob_colors[i][3] = 1
                face[i] = 1
            elif blob_colors[i][0] < 100 and blob_colors[i][1] > 120 and blob_colors[i][2] > 120 and np.abs(blob_colors[i][1]-blob_colors[i][2])<30:
                blob_colors[i][3] = 2
                face[i] = 2
            elif blob_colors[i][0] > blob_colors[i][1] and blob_colors[i][1] > blob_colors[i][2]:
                blob_colors[i][3] = 3
                face[i] = 3
            elif blob_colors[i][1] > blob_colors[i][0] and blob_colors[i][1] > blob_colors[i][2] and np.abs(blob_colors[i][0] - blob_colors[i][2]) < 30:
                blob_colors[i][3] = 4
                face[i] = 4
            elif blob_colors[i][2] > blob_colors[i][0] and blob_colors[i][2] > blob_colors[i][1] and np.abs(blob_colors[i][0] - blob_colors[i][1]) < 30 and blob_colors[i][0] < 80:
                blob_colors[i][3] = 5
                face[i] = 5
            elif blob_colors[i][1] < blob_colors[i][2] and blob_colors[i][0] < blob_colors[i][1] and blob_colors[i][2] > 120:
                blob_colors[i][3] = 6
                face[i] = 6
        #print(face)
        if np.count_nonzero(face) == 9:
            print(face)
            print (blob_colors)
            return face, blob_colors
        else:
            return [0,0], blob_colors
    else:
        return [0,0,0], blob_colors
        #break


# Read an image from file
img = cv2.imread('rubik1.PNG')
image = img.copy()

# Display the result
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
gray = cv2.adaptiveThreshold(gray,20,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,0)
#cv2.imwrite()
try:
    _, contours, hierarchy = cv2.findContours(gray,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
except:
    contours, hierarchy = cv2.findContours(gray,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

i = 0
contour_id = 0
#print(len(contours))
count = 0
blob_colors = []

contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Iterate over the sorted contours
for i, contour in enumerate(contours):
    # Draw the contour on the original image
    area = cv2.contourArea(contour)
    if (area > 3000):
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

        # Display the area of each contour
        print(f"Contour {i + 1}: Area = {area}")
"""
for contour in contours:
    A1 = cv2.contourArea(contour)
    contour_id = contour_id + 1
    if A1 < 3000 and A1 > 1000:
        perimeter = cv2.arcLength(contour, True)
        epsilon = 0.01 * perimeter
        approx = cv2.approxPolyDP(contour, epsilon, True)
        hull = cv2.convexHull(contour)
        if cv2.norm(((perimeter / 4) * (perimeter / 4)) - A1) < 150:
            #if cv2.ma
            count = count + 1
            x, y, w, h = cv2.boundingRect(contour)
            #cv2.rectangle(bgr_image_input, (x, y), (x + w, y + h), (0, 255, 255), 2)
            #cv2.imshow('cutted contour', bgr_image_input[y:y + h, x:x + w])
            val = (50*y) + (10*x)
            blob_color = np.array(cv2.mean(image[y:y+h,x:x+w])).astype(int)
            cv2.drawContours(image,[contour],0,(255, 255, 0),2)
            cv2.drawContours(image, [approx], 0, (255, 255, 0), 2)
            blob_color = np.append(blob_color, val)
            blob_color = np.append(blob_color, x)
            blob_color = np.append(blob_color, y)
            blob_color = np.append(blob_color, w)
            blob_color = np.append(blob_color, h)
            blob_colors.append(blob_color)
if len(blob_colors) > 0:
    blob_colors = np.asarray(blob_colors)
    blob_colors = blob_colors[blob_colors[:, 4].argsort()]
face = np.array([0,0,0,0,0,0,0,0,0])
if len(blob_colors) == 9:
    #print(blob_colors)
    for i in range(9):
        #print(blob_colors[i])
        if blob_colors[i][0] > 120 and blob_colors[i][1] > 120 and blob_colors[i][2] > 100:
            blob_colors[i][3] = 1
            face[i] = 1
        elif blob_colors[i][0] < 100 and blob_colors[i][1] > 120 and blob_colors[i][2] > 120 and np.abs(blob_colors[i][1]-blob_colors[i][2])<30:
            blob_colors[i][3] = 2
            face[i] = 2
        elif blob_colors[i][0] > blob_colors[i][1] and blob_colors[i][1] > blob_colors[i][2]:
            blob_colors[i][3] = 3
            face[i] = 3
        elif blob_colors[i][1] > blob_colors[i][0] and blob_colors[i][1] > blob_colors[i][2] and np.abs(blob_colors[i][0] - blob_colors[i][2]) < 30:
            blob_colors[i][3] = 4
            face[i] = 4
        elif blob_colors[i][2] > blob_colors[i][0] and blob_colors[i][2] > blob_colors[i][1] and np.abs(blob_colors[i][0] - blob_colors[i][1]) < 30 and blob_colors[i][0] < 80:
            blob_colors[i][3] = 5
            face[i] = 5
        elif blob_colors[i][1] < blob_colors[i][2] and blob_colors[i][0] < blob_colors[i][1] and blob_colors[i][2] > 120:
            blob_colors[i][3] = 6
            face[i] = 6
    print(face)
    if np.count_nonzero(face) == 9:
        print(face)
        print (blob_colors)
    """
cv2.imshow("Test", image)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()