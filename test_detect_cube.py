import cv2
import sys
import time
import math
import numpy as np
import random as rng
from scipy import stats


#make frame easier to detect cube
def captureFrame(frame):
    # preprocessing frame
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 5, 75, 75)
    canny = cv2.Canny(blur, 20, 40, 3)
    dilate = cv2.dilate(canny, (7,7), iterations = 6)
    BlobContours = []
    #cv2.imwrite()
    findBlob(dilate, BlobContours)
    if (len(BlobContours) != 0):
        BlobContours = sorted(BlobContours, key = lambda cnt: cv2.boundingRect(cnt)[0] * 100
                          + cv2.boundingRect(cnt)[1] * 500)
    drawRectangleforBlob(frame, BlobContours)
    getColorforBlob(frame, BlobContours)

# find 9 blobs of a face of a cube in an order
def findBlob(dilate, BlobContours):
    # cv2.RETR_TREE: contour with this [Next, Previous, First_Child, Parent]
    # cv2.CHAIN_APPROX_SIMPLE: find 4 points of the bounding box of contour, instead of 1000 points
    try:
         _, contours, hierarchy = cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    except:
         contours, hierarchy = cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        perimeter = cv2.arcLength(contours[i], True)
        if (math.pow(perimeter, 2) != 0):
            #check if a contour is a small square
            squareness = 4 * math.pi * area / math.pow(perimeter, 2)
            if (squareness >= 0.5 and squareness <= 1 and area >= 900):
            # if (cv2.norm((perimeter / 4) * (perimeter / 4) - area <= 100) and area >= 800):
                # avoid colision
                if (hierarchy[0, i, 3] != -1 and hierarchy[0, i, 2] == -1):
                    BlobContours.append(contours[i])

def checkAndSortBlob(BlobContours):
    if (len(BlobContours) == 9):
        print ("9 OK")
        BlobContours = sorted(BlobContours, key = lambda cnt: cv2.boundingRect(cnt)[0] * 100
                          + cv2.boundingRect(cnt)[1] * 500)

def drawRectangleforBlob(frame, BlobContours):
    for i, Blobcnt in enumerate(BlobContours):
        epsilon = cv2.arcLength(Blobcnt, True) * 0.05 
        approx = cv2.approxPolyDP(Blobcnt, epsilon, True)
        x, y, w, h = cv2.boundingRect(approx)
        # index_str = str(i)
        # Draw a rectangle around the contour
        BlobFrame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)
        index_str = str(i)
        cv2.putText(BlobFrame, index_str, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0)) 

def getColorforBlob(frame, BlobContours):
    BGRColorArray = []
    test = ""
    for i, Blobcnt in enumerate(BlobContours):
        epsilon = cv2.arcLength(Blobcnt, True) * 0.05 
        approx = cv2.approxPolyDP(Blobcnt, epsilon, True)
        x, y, w, h = cv2.boundingRect(approx)
        # index_str = str(i)
        # Draw a rectangle around the contour
        start_x = (int) (x + w / 3)
        end_x = (int) (x + 2 * w / 3)
        start_y = (int) (y + h / 3)
        end_y = (int) (y + 2 * h / 3)

        
        '''
        # height FIRST, THEN WIDTH: Nho dung co sua
        roi = frame[start_y:end_y, start_x:end_x]
        color = cv2.mean(roi)
        b, g, r = color[0], color[1], color[2]
        BGRColorArray.append([b,g,r])

        '''
    
        roi = frame[start_y:end_y, start_x:end_x]
        roi_lab = cv2.cvtColor(roi, cv2.COLOR_BGR2LAB)

        color = cv2.mean(roi_lab)
        L, a, b = color[0], color[1], color[2]
        L = L * 100 / 255
        a = a - 128
        b = b - 128
        BGRColorArray.append([L, a, b])
        

        if (i == 4 and len(BlobContours) == 9):
            print(f"x:{x}, y:{y}, w:{w}, h:{h}")
            
    if (len(BGRColorArray) == 9):
        # print(BGRColorArray)
        print(BGRColorArray[0])
        #MakeSideCube(BGRColorArray)

def MakeSideCube(BGRColorArray):
    CubeSize = []
    red_range = (np.array([0, 0, 200]), np.array([50, 50, 255]))
    blue_range = (np.array([200, 0, 0]), np.array([255, 50, 50]))
    green_range = (np.array([0, 200, 0]), np.array([50, 255, 50]))
    yellow_range = (np.array([0, 200, 200]), np.array([50, 255, 255]))
    orange_range = (np.array([0, 100, 200]), np.array([50, 150, 255]))
    white_range = (np.array([200, 200, 200]), np.array([255, 255, 255]))
    s = ""

    for color in BGRColorArray:
        if (color_check_range(color, red_range)):
            CubeSize.append(1)
        elif (color_check_range(color, blue_range)):
            CubeSize.append(2)
        elif (color_check_range(color, green_range)):
            CubeSize.append(3)
        elif (color_check_range(color, orange_range)):
            CubeSize.append(4)
        elif (color_check_range(color, yellow_range)):
            CubeSize.append(5)
        elif (color_check_range(color, white_range)):
            CubeSize.append(6)
    for i in CubeSize:
        s += str(i) + " "
    print(s)

def color_check_range(color, color_range):
    return all(color_range[0] <= color <= color_range[1])
