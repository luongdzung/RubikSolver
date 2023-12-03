# RubiksCube (3x3x3)
This project concentrates on solving a unsolved Rubik's Cube. The program contains OpenCV libraries and when executed will show a live video from the webcam. It then capture the cube, then print the answer of it, by using kociemba algorithm

1. Run the file: video.py. It should open your webcam
2.  Capturing the whole cube with the order below
	Press 1: Capture the Front Face
	Press 2: Capture the Up Face
	Press 3: Capture the Right Face
	Press 4: Capture the Down Face
	Press 5: Capture the Left Face
	Press 6: Capture the Back Face
3.  After capturing the whole cube correctly, the program will print out the way to solve it. Here are some certain symbols to know
	R :rotate the right side of the cube 90 degrees clockwise
	R' :rotate the right side of the cube 90 degrees clockwise
	R2 : rotate the right side of the cube 180 degrees
	We label: Front (F), Up (U), Right (R), Down (D), Left (L), Back (B)
	Keep in mind that you need to remember the order of the cube to solve it. Or else you might stuck at an unknown state
4. Reference link:
https://github.com/muodov/kociemba
https://www.youtube.com/watch?v=WJRhB39BxWQ&list=PLrhQ-QWgC9sj_tZj-8Ho5_v5PkUwBEHqx&index=11&t=797s 
https://www.youtube.com/watch?v=afAGtExoiLQ&list=PLrhQ-QWgC9sj_tZj-8Ho5_v5PkUwBEHqx&index=12 
