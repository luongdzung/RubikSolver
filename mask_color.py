import cv2
import numpy as np

def GetColor(frame, Blob_x, Blob_y, Blob_w, Blob_h):
    red_range = (20, 128, 128), (255, 255, 255)
    blue_range = (32, 128, 128), (173, 255, 255)
    green_range = (87, 128, 128), (180, 255, 255)
    yellow_range = (102, 128, 128), (255, 255, 255)
    white_range= (0, 128, 128), (255, 128, 255)
    orange_range = (0, 128, 128), (255, 255, 255)

    new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    roi_hsv = new_frame[Blob_y: Blob_y+Blob_h, Blob_x: Blob_x + Blob_w]
    mean_color_hsv = cv2.mean(roi_hsv)
    if is_color_in_range(mean_color_hsv, red_range):
        return "Red"
    elif is_color_in_range(mean_color_hsv, blue_range):
        return "Blue"
    elif is_color_in_range(mean_color_hsv, green_range):
        return "Green"
    elif is_color_in_range(mean_color_hsv, yellow_range):
        return "Yellow"
    elif is_color_in_range(mean_color_hsv, white_range):
        return "White"
    elif is_color_in_range(mean_color_hsv, orange_range):
        return "Orange"
    else:
        return "None of the specified colors"

def is_color_in_range(color, color_range):
    return all(color_range[0][i] <= color[i] <= color_range[1][i] for i in range(3))