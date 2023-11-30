import cv2
import sys
import time
import math
import numpy as np
import random as rng
from scipy import stats
import kociemba
from datetime import datetime
from rotate import *
from facecube_detect import *

def concat(up_face,right_face,front_face,down_face,left_face,back_face):
    # solution = [up_face,right_face,front_face,down_face,left_face,back_face]
    solution = np.concatenate((up_face, right_face), axis=None)
    solution = np.concatenate((solution, front_face), axis=None)
    solution = np.concatenate((solution, down_face), axis=None)
    solution = np.concatenate((solution, left_face), axis=None)
    solution = np.concatenate((solution, back_face), axis=None)
    # print(solution)
    return solution

def main():
    #định nghĩa các tham số đầu vào
    up_face = [0, 0]
    front_face = [0, 0]
    left_face = [0, 0]
    right_face = [0, 0]
    down_face = [0, 0]
    back_face = [0, 0]
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    broke = 0
    
    #đọc camera đầu vào của thiết bị
    if not ret:
        print("Cannot read video source")
        sys.exit()

    faces = []
    
    #tạo video đầu ra
    # fps = 20
    # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    # size = (width, height)

    # Set up VideoWriter to save the video in MP4 format
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 format
    # videoWriter = cv2.VideoWriter('OUTPUT.mp4', fourcc, fps, size)  # Adjust the resolution if needed
        
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Cannot read video source")
            sys.exit()
        face, blob_colors = detect_face(frame)
        frame = cv2.putText(frame, "Hello", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                face_array = np.array(faces)
                # print('INNNNN')
                # face_array = np.transpose(face_array)
                detected_face = stats.mode(face_array)[0]
                # print(final_face)
                uf = np.asarray(uf)
                ff = np.asarray(ff)
                detected_face = np.asarray(detected_face)
                #print(np.array_equal(detected_face, tf))
                print(np.array_equal(detected_face, ff))
                faces = []
                if np.array_equal(detected_face, uf) == False and np.array_equal(detected_face, ff) == False and np.array_equal(detected_face, bf) == False and np.array_equal(detected_face, df) == False and np.array_equal(detected_face, lf) == False and np.array_equal(detected_face, rf) == False:
                    return detected_face
        # videoWriter.write(frame)
        cv2.imshow("Output Image", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break

if __name__ == "__main__":
    main()
