import cv2
import sys
import time
import math
import numpy as np
import random as rng
from scipy import stats

#test input cube
rgb_array = np.array([
    [152, 154, 167], [152, 154, 165], [150, 162, 111],
    [148, 151, 165], [146, 149, 165], [145, 159, 105],
    [149, 154, 173], [148, 153, 173], [146, 162, 104],
    
    [201, 121, 104], [202, 122, 105], [209, 129, 115],
    [198, 114, 97], [199, 114, 97], [206, 122, 106],
    [118, 48, 38], [120, 48, 39], [125, 57, 48],
    
    [71, 127, 72], [68, 124, 71], [58, 88, 129],
    [59, 127, 66], [53, 121, 63], [45, 80, 133],
    [28, 72, 138], [55, 128, 66], [37, 77, 142],
    
    [122, 59, 64], [121, 60, 65], [128, 71, 76],
    [116, 44, 49], [117, 45, 53], [123, 57, 64],
    [205, 118, 117], [205, 115, 115], [209, 121, 121],
    
    [77, 141, 81], [52, 93, 135], [58, 97, 138],
    [66, 138, 73], [35, 82, 138], [41, 88, 142],
    [62, 142, 75], [61, 139, 77], [40, 90, 154],
    
    [148, 150, 166], [140, 154, 100], [144, 158, 107],
    [146, 151, 170], [137, 154, 94], [141, 158, 104],
    [149, 155, 182], [143, 162, 104], [142, 162, 106]
])

def rgb_to_lab(rgb_color):

    r, g, b = rgb_color[0], rgb_color[1], rgb_color[2]
    # Normalize RGB values
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Apply gamma correction
    r = (r / 12.92) if (r <= 0.04045) else math.pow((r + 0.055) / 1.055, 2.4)
    g = (g / 12.92) if (g <= 0.04045) else math.pow((g + 0.055) / 1.055, 2.4)
    b = (b / 12.92) if (b <= 0.04045) else math.pow((b + 0.055) / 1.055, 2.4)

    # Convert to XYZ space
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

    # Normalize XYZ to reference white
    x /= 0.95047
    y /= 1.00000
    z /= 1.08883

    # Convert to LAB space
    x = (x ** (1.0 / 3.0) if (x > 0.008856) else ((903.3 * x) + 16.0) / 116.0)
    y = (y ** (1.0 / 3.0) if (y > 0.008856) else ((903.3 * y) + 16.0) / 116.0)
    z = (z ** (1.0 / 3.0) if (z > 0.008856) else ((903.3 * z) + 16.0) / 116.0)

    l = max(0.0, (116.0 * y) - 16.0)
    a = (x - y) * 500.0
    b = (y - z) * 200.0

    return [l, a, b]

def ConvertAlltoLab():
    lab_array = []
    for rgb_color in rgb_array:
        lab_color = rgb_to_lab(rgb_color)
        lab_array.append(lab_color)
    if (len(lab_array) == 54):
        print("OKKKKK")
    return lab_array

def EuclideanDistance(lab1, lab2):
    L = lab1[0] - lab2[0]
    a = lab1[1] - lab2[1]
    b = lab1[2] - lab2[2]
    return math.sqrt(L * L + a * a + b * b)

def dL_CIE2000(lab1, lab2):
    return lab1[0] - lab2[0]

def de_CIE2000(lab1, lab2):
    L1, a1, b1, L2, a2, b2 = lab1[0], lab1[1], lab1[2], lab2[0], lab2[1], lab2[2]
    kl = kc = kh = 1
    C1 = math.sqrt(a1 * a1 + b1 * b1)
    C2 = math.sqrt(a2 * a2 + b2 * b2)

    Lpbar = (L1 + L2) / 2.0
    Cbar = 0.5 * (C1 + C2)
    Cbar_pow_7 = math.pow(Cbar, 7)
    pow_25_7 = math.pow(25, 7)

    G = 0.5 * (1 - math.sqrt(Cbar_pow_7 / (Cbar_pow_7 + pow_25_7)))
    
    a1p = (1 + G) * a1
    a2p = (1 + G) * a2

    C1p = math.sqrt(a1p * a1p + b1 * b1)
    C2p = math.sqrt(a2p * a2p + b2 * b2)

    Cpbar = (C1p + C2p) / 2
    h1p = math.atan2(b1, a1p)
    h1p += 2 * math.pi if h1p < 0 else 0
    h2p = math.atan2(b2, a2p)
    h2p += 2 * math.pi if h2p < 0 else 0

    dhp = h2p - h1p
    dhp += -2 * math.pi if dhp > math.pi else (2 * math.pi if dhp < -math.pi else 0)
    dhp = 0 if C1p * C2p == 0 else dhp

    dLp = dL_CIE2000(lab1, lab2)
    dCp = C2p - C1p

    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(dhp / 2)

    Hp = 0.5 * (h1p + h2p)
    Hp += math.pi if abs(h1p - h2p) > math.pi else 0
    if C1p * C2p == 0:
        Hp = h1p + h2p

    T = 1 - 0.17 * math.cos(Hp - 0.523599) + 0.24 * math.cos(2 * Hp) + 0.32 * math.cos(3 * Hp + 0.10472) - 0.20 * math.cos(4 * Hp - 1.09956)
    Lpbarpow502 = (Lpbar - 50) * (Lpbar - 50)
    Sl = 1 + 0.015 * Lpbarpow502 / math.sqrt(20 + Lpbarpow502)
    Sc = 1 + 0.045 * Cpbar
    Sh = 1 + 0.015 * Cpbar * T
    f = (math.degrees(Hp) - 275) / 25
    dOmega = (30 * math.pi / 180) * math.exp(-(f * f))
    Rc = 2 * math.sqrt(math.pow(Cpbar, 7) / (math.pow(Cpbar, 7) + math.pow(25, 7)))
    RT = -1 * math.sin(2 * dOmega) * Rc

    dLp = dLp / (kl * Sl)
    dCp = dCp / (kc * Sc)
    dHp = dHp / (kh * Sh)

    return math.sqrt(dLp * dLp + dCp * dCp + dHp * dHp + RT * dCp * dHp)

def k_means(lab_array, center_colors):
    arr_input = [-10] * 54
    
    arr_input[4] = 1 #Red
    arr_input[13] = 2 #Blue
    arr_input[22] = 3 #Yellow 
    arr_input[31] = 4 #Green
    arr_input[40] = 5 #White
    arr_input[49] = 6 #Orange

    center_dict = {
        tuple(lab_array[4]): 1,
        tuple(lab_array[13]): 2,
        tuple(lab_array[22]): 3,
        tuple(lab_array[31]): 4,
        tuple(lab_array[40]): 5,
        tuple(lab_array[49]): 6
    }
    center_colors = np.array([lab_array[4], lab_array[13], lab_array[22], 
                     lab_array[31], lab_array[40], lab_array[49]])

    max_distance = sys.float_info.max

    for x, blob_color in enumerate(lab_array):
        for y, center_color in enumerate(center_colors):
            distance = de_CIE2000(blob_color, center_color)
            if (distance < max_distance):
                #closest color
                max_distance = distance
                arr_input[x] = center_dict[tuple(center_color)]
        max_distance = sys.float_info.max
    
    check = True
    for val in arr_input:
        if (val == -10):
            check = False
    if (check == True):
        # convert input for kociemba
        for i in range(0,9):
            x = arr_input[i]
            arr_input[i] = arr_input[i+9]
            arr_input[i+9] = arr_input[i+18]
            arr_input[i+18] = x
        # print("OK") 
    
    return arr_input
