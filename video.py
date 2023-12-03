import cv2
import numpy as np
from detect_cube import *
from clustering import *
import kociemba
from mapping import *

# Open the webcam
cap = cv2.VideoCapture(0)

# Get the video frame dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)  + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"M", "J", "P", "G")
out = cv2.VideoWriter('videos/final_video.mp4', fourcc, 20.0, size)

def main():
    Cube = []
    arr_input = [-10] * 54
    center_colors = []
    lab_cube = []
    convert = False
    solve = ""
    str_input = ""
    found_solution = False
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        event = cv2.waitKey(1)

        # preprocessing frame
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur = cv2.bilateralFilter(gray, 5, 75, 75)
        canny = cv2.Canny(blur, 20, 40, 3)
        dilate = cv2.dilate(canny, (7,7), iterations = 6)
        BlobContours = []

        findBlob(dilate, BlobContours)
        if (len(BlobContours) != 0):
            BlobContours = sorted(BlobContours, key = lambda cnt: cv2.boundingRect(cnt)[0] * 100
                            + cv2.boundingRect(cnt)[1] * 500)
        take_All_side(frame, BlobContours, event, Cube, convert)

        if (len(Cube) == 6 and convert == False):
            for i in range(len(Cube)):
                for j in range(len(Cube[i])):
                    lab_cube.append(Cube[i][j])
            arr_input = k_means(lab_cube, center_colors)
            # print("Kmean OK")
            print(arr_input)
            for i in arr_input:
                str_input += (my_dict[i][1])
            
            solve = kociemba.solve(str_input)
            print(str_input)
            convert = True

        cv2.imshow('Rubik\'s Cube Contours', frame)
        if (solve != "" and found_solution == False):
            print(f"Solution: {solve}")
            found_solution = True
        
        if (event == ord('q')):
            break
        out.write(frame)

    # Release the webcam, close the output video, and close all windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
