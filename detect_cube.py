import cv2
import math
import numpy as np
import random as rng
from scipy import stats

Cube = []
NewCube = []

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
        # Draw a rectangle around the contour
        start_x = (int) (x + w / 3)
        end_x = (int) (x + 2 * w / 3)
        start_y = (int) (y + h / 3)
        end_y = (int) (y + 2 * h / 3)
    
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
    return BGRColorArray
        

def take_All_side(frame, BlobContours, event, Cube, convert):
    if (len(BlobContours) == 9):
        if (event == ord("1")): #1: Front 
            print("Capture Front Side complete")
            bgr_side_array = getColorforBlob(frame, BlobContours)
            Cube.append(bgr_side_array)
            # print(bgr_side_array)
        elif (event == ord("2")): #2: Up
            print("Capture Up Side complete")
            bgr_side_array = getColorforBlob(frame, BlobContours)
            Cube.append(bgr_side_array)
            # print(bgr_side_array)
        elif (event == ord("3")): #3: Right 
            print("Capture Right Side complete")
            bgr_side_array = getColorforBlob(frame, BlobContours)
            Cube.append(bgr_side_array)
            # print(bgr_side_array)
        elif (event == ord("4")): #4: Down
            print("Capture Down Side complete")
            bgr_side_array = getColorforBlob(frame, BlobContours)
            Cube.append(bgr_side_array)
            # print(bgr_side_array)
        elif (event == ord("5")): #5: Left
            print("Capture Left Side complete")
            bgr_side_array = getColorforBlob(frame, BlobContours)
            Cube.append(bgr_side_array)
            # print(bgr_side_array)
        elif (event == ord("6")): #6: Back
            print("Capture Back Side complete")
            bgr_side_array = getColorforBlob(frame, BlobContours)
            Cube.append(bgr_side_array)
            # print(bgr_side_array)
       
    # print(len(Cube))
    drawRectangleforBlob(frame, BlobContours)
    
    if (len(Cube) == 6 and convert == False):
        print("Convert Success for Kociemba")
        convert = True
    

