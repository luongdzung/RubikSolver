import cv2
import numpy as np
from test_detect_cube import *
# Open the webcam
cap = cv2.VideoCapture(0)

# Get the video frame dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)  + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"M", "J", "P", "G")
out = cv2.VideoWriter('videos/src2_detect_cube_video_part5.mp4', fourcc, 20.0, size)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    captureFrame(frame)
    cv2.imshow('Rubik\'s Cube Contours', frame)
    out.write(frame)
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam, close the output video, and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()
