import cv2
import sys
import time
import math
import numpy as np
import random as rng
from scipy import stats
from sklearn.cluster import KMeans

#test input cube
lab_array = [
    [64.7, 4.67, 2.87], [64.52, 3.9, 2.58], [62.75, -19.72, 0.54],
    [63.63, 4.94, 3.55], [63.06, 5.73, 3.86], [61.41, -21.06, 1.35],
    [65.19, 6.61, 5.33], [64.91, 7, 5.48], [62.27, -22.6, 2.02],
    
    [52.48, 9.84, -43.86], [52.59, 10.36, -44.24], [55.5, 10.86, -43.57],
    [49.67, 11.78, -46.62], [49.72, 12.03, -47.12], [52.84, 11.6, -46.11],
    [22.47, 15.19, -42.38], [22.68, 16.04, -43.3], [26.26, 13.76, -40.65],
    
    [72, 127, 71], [71, 124, 68], [129, 88, 58],
    [66, 127, 59], [63, 121, 53], [133, 80, 45],
    [138, 72, 28], [66, 128, 55], [142, 77, 37],
    
    [64, 59, 122], [65, 60, 121], [76, 71, 128],
    [49, 44, 116], [53, 45, 117], [64, 57, 123],
    [117, 118, 205], [115, 115, 205], [121, 121, 209],
    
    [81, 141, 77], [135, 93, 52], [138, 97, 58],
    [73, 138, 66], [138, 82, 35], [142, 88, 41],
    [75, 142, 62], [77, 139, 61], [154, 90, 40],
    
    [166, 150, 148], [100, 154, 140], [107, 158, 144],
    [170, 151, 146], [94, 154, 137], [104, 158, 141],
    [182, 155, 149], [104, 162, 143], [106, 162, 142]
]

lab_array_flattened = [element for sublist in lab_array for element in sublist]

lab_array = []

    



    

def main():
    # BGRtoLab(bgr_array)
    r_value = 255
    g_value = 128
    b_value = 64

    # Create a 1x1 pixel image with the specified RGB values
    rgb_pixel = np.array([[b_value, g_value, r_value]], dtype=np.uint8)

    # Convert RGB to LAB
    lab_pixel = cv2.cvtColor(rgb_pixel.reshape(1,-1,3), cv2.COLOR_BGR2LAB).reshape(-1,3)

    # Extract L, a, b values
    L_value, a_value, b_value = lab_pixel[0,0]

    # Print the results
    print(f"RGB: ({r_value}, {g_value}, {b_value})")
    print(f"LAB: ({L_value}, {a_value}, {b_value})")

if __name__ == "__main__":
    main()