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
    video = cv2.VideoCapture(0)
    ret, bgr_image_input = video.read()
    broke = 0
    
    #đọc camera đầu vào của thiết bị
    if not ret:
        print("Cannot read video source")
        sys.exit()

    h1 = bgr_image_input.shape[0]
    w1 = bgr_image_input.shape[1]
    faces = []
    
    #tạo video đầu ra
    try:
        fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        fname = "OUTPUT5.avi"
        fps = 20.0
        videoWriter = cv2.VideoWriter(fname, fourcc, fps, (w1, h1))
    except:
        print("Error: can't create output video: %s" % fname)
        sys.exit()
    
    while True:
        ret, bgr_image_input = video.read()
        if not ret:
            break
        while True:
            #print("Show Front Face")
            front_face = find_face(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face, text="Show Front Face")
            mf = front_face[0,4]
            print(front_face)
            print(mf)
            #print("Show Up Face")
            #time.sleep(2)
            up_face = find_face(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face, text="Show Top Face")
            start_time = datetime.now()
            while True:
                if (datetime.now() - start_time).total_seconds() > 3:
                    break
                else:
                    ret, bgr_image_input = video.read()
                    if not ret:
                        broke = 1
                        break
                    bgr_image_input = cv2.putText(bgr_image_input, "Show Down Face", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                    videoWriter.write(bgr_image_input)
                    cv2.imshow("Output Image", bgr_image_input)
                    key_pressed = cv2.waitKey(1) & 0xFF
                    if key_pressed == 27 or key_pressed == ord('q'):
                        broke = 1
                        break
            if broke == 1:
                break
            mu = up_face[0, 4]
            print(up_face)
            print(mu)
            #print("Show Down Face")
            #time.sleep(2)
            down_face = find_face(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face, text="Show Down Face")
            start_time = datetime.now()
            while True:
                if (datetime.now() - start_time).total_seconds() > 3:
                    break
                else:
                    ret, bgr_image_input = video.read()
                    if not ret:
                        broke = 1
                        break
                    bgr_image_input = cv2.putText(bgr_image_input, "Show Right Face", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                    videoWriter.write(bgr_image_input)
                    cv2.imshow("Output Image", bgr_image_input)
                    key_pressed = cv2.waitKey(1) & 0xFF
                    if key_pressed == 27 or key_pressed == ord('q'):
                        broke = 1
                        break
            if broke == 1:
                break
            md = down_face[0, 4]
            print(down_face)
            print(md)
            #print("Show Right Face")
            #time.sleep(2)
            right_face = find_face(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face, text="Show Right Face")
            start_time = datetime.now()
            while True:
                if (datetime.now() - start_time).total_seconds() > 3:
                    break
                else:
                    ret, bgr_image_input = video.read()
                    if not ret:
                        broke = 1
                        break
                    bgr_image_input = cv2.putText(bgr_image_input, "Show Left Face", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                    videoWriter.write(bgr_image_input)
                    cv2.imshow("Output Image", bgr_image_input)
                    key_pressed = cv2.waitKey(1) & 0xFF
                    if key_pressed == 27 or key_pressed == ord('q'):
                        broke = 1
                        break
            if broke == 1:
                break
            mr = right_face[0, 4]
            print(right_face)
            print(mr)
            #print("Show Left Face")
            #time.sleep(2)
            left_face = find_face(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face, text="Show Left Face")
            start_time = datetime.now()
            while True:
                if (datetime.now() - start_time).total_seconds() > 3:
                    break
                else:
                    ret, bgr_image_input = video.read()
                    if not ret:
                        broke = 1
                        break
                    bgr_image_input = cv2.putText(bgr_image_input, "Show Back Face", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                    videoWriter.write(bgr_image_input)
                    cv2.imshow("Output Image", bgr_image_input)
                    key_pressed = cv2.waitKey(1) & 0xFF
                    if key_pressed == 27 or key_pressed == ord('q'):
                        broke = 1
                        break
            if broke == 1:
                break
            ml = left_face[0, 4]
            print(left_face)
            print(ml)
            #print("Show Back Face")
            #time.sleep(2)
            back_face = find_face(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face, text="Show Back Face")
            start_time = datetime.now()
            while True:
                if (datetime.now() - start_time).total_seconds() > 3:
                    break
                else:
                    ret, bgr_image_input = video.read()
                    if not ret:
                        broke = 1
                        break
                    bgr_image_input = cv2.putText(bgr_image_input, "Show Front Face", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                    videoWriter.write(bgr_image_input)
                    cv2.imshow("Output Image", bgr_image_input)
                    key_pressed = cv2.waitKey(1) & 0xFF
                    if key_pressed == 27 or key_pressed == ord('q'):
                        broke = 1
                        break
            if broke == 1:
                break
            mb = back_face[0, 4]
            print(back_face)
            #time.sleep(2)
            print(mb)

            solution = concat(up_face,right_face,front_face,down_face,left_face,back_face)
            #print(solution)
            cube_solved = [mu, mu, mu, mu, mu, mu, mu, mu, mu, mr, mr, mr, mr, mr, mr, mr, mr, mr, mf, mf, mf, mf, mf,
                           mf, mf, mf, mf, md, md, md, md, md, md, md, md, md, ml, ml, ml, ml, ml, ml, ml, ml, ml, mb,
                           mb, mb, mb, mb, mb, mb, mb, mb]
            if (concat(up_face, right_face, front_face, down_face, left_face, back_face) == cube_solved).all():
                # print("CUBE IS SOLVED")
                ret, bgr_image_input = video.read()
                bgr_image_input = cv2.putText(bgr_image_input, "CUBE ALREADY SOLVED", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                videoWriter.write(bgr_image_input)
                cv2.imshow("Output Image", bgr_image_input)
                key_pressed = cv2.waitKey(1) & 0xFF
                if key_pressed == 27 or key_pressed == ord('q'):
                    break
                time.sleep(5)
                break

            final_str = ''
            for val in range(len(solution)):
                if solution[val] == mf:
                    final_str = final_str + 'F'
                elif solution[val] == mr:
                    final_str = final_str + 'R'
                elif solution[val] == mb:
                    final_str = final_str + 'B'
                elif solution[val] == ml:
                    final_str = final_str + 'L'
                elif solution[val] == mu:
                    final_str = final_str + 'U'
                elif solution[val] == md:
                    final_str = final_str + 'D'

            print(final_str)
            try:
                solved = kociemba.solve(final_str)
                print(solved)
                break
            except:
                up_face = [0, 0]
                front_face = [0, 0]
                left_face = [0, 0]
                right_face = [0, 0]
                down_face = [0, 0]
                back_face = [0, 0]

        if broke == 1:
            break
        steps = solved.split()
        for step in steps:
            if step == "R":
                [up_face, right_face, front_face, down_face, left_face, back_face] = right_cw(video,videoWriter,up_face,right_face,front_face,down_face,left_face,back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "R'":
                [up_face, right_face, front_face, down_face, left_face, back_face] = right_ccw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "R2":
                [up_face, right_face, front_face, down_face, left_face, back_face] = right_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = right_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "L":
                [up_face, right_face, front_face, down_face, left_face, back_face] = left_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "L'":
                [up_face, right_face, front_face, down_face, left_face, back_face] = left_ccw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "L2":
                [up_face, right_face, front_face, down_face, left_face, back_face] = left_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = left_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "F":
                [up_face, right_face, front_face, down_face, left_face, back_face] = front_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "F'":
                [up_face, right_face, front_face, down_face, left_face, back_face] = front_ccw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "F2":
                [up_face, right_face, front_face, down_face, left_face, back_face] = front_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = front_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "B":
                [up_face, right_face, front_face, down_face, left_face, back_face] = turn_to_right(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = right_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = turn_to_front(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "B'":
                #print(up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = turn_to_right(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = right_ccw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = turn_to_front(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
            elif step == "B2":
                [up_face, right_face, front_face, down_face, left_face, back_face] = turn_to_right(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = right_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = right_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = turn_to_front(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "U":
                [up_face, right_face, front_face, down_face, left_face, back_face] = up_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "U'":
                [up_face, right_face, front_face, down_face, left_face, back_face] = up_ccw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "U2":
                [up_face, right_face, front_face, down_face, left_face, back_face] = up_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = up_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "D":
                [up_face, right_face, front_face, down_face, left_face, back_face] = down_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "D'":
                [up_face, right_face, front_face, down_face, left_face, back_face] = down_ccw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))
            elif step == "D2":
                [up_face, right_face, front_face, down_face, left_face, back_face] = down_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                [up_face, right_face, front_face, down_face, left_face, back_face] = down_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face)
                #print(concat(up_face, right_face, front_face, down_face, left_face, back_face))

        cube_solved = [mu, mu, mu, mu, mu, mu, mu, mu, mu, mr, mr, mr, mr, mr, mr, mr, mr, mr, mf, mf, mf, mf, mf, mf, mf, mf, mf, md, md, md, md, md, md, md, md, md, ml, ml, ml, ml, ml, ml, ml, ml, ml, mb, mb, mb, mb, mb, mb, mb, mb, mb]
        if (concat(up_face, right_face, front_face, down_face, left_face, back_face) == cube_solved).all():
            #print("CUBE IS SOLVED")
            ret, bgr_image_input = video.read()
            bgr_image_input = cv2.putText(bgr_image_input, "CUBE SOLVED", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

            videoWriter.write(bgr_image_input)
            cv2.imshow("Output Image", bgr_image_input)
            key_pressed = cv2.waitKey(1) & 0xFF
            if key_pressed == 27 or key_pressed == ord('q'):
                break
            start_time = datetime.now()
            while True:
                if (datetime.now() - start_time).total_seconds() > 5:
                    break
                else:
                    ret, bgr_image_input = video.read()
                    if not ret:
                        broke = 1
                        break
                    bgr_image_input = cv2.putText(bgr_image_input, "CUBE SOLVED", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                    videoWriter.write(bgr_image_input)
                    cv2.imshow("Output Image", bgr_image_input)
                    key_pressed = cv2.waitKey(1) & 0xFF
                    if key_pressed == 27 or key_pressed == ord('q'):
                        broke = 1
                        break
            if broke == 1:
                break
            break
        #print(front_face)
        #print(up_face)

        videoWriter.write(bgr_image_input)
        cv2.imshow("Output Image", bgr_image_input)
        # print(count)
        # print(blob_color)
        # print(face)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


if __name__ == "__main__":
    main()
