# RubiksCube (3x3x3)
This project concentrates on solving a unsolved Rubik's Cube. The program contains OpenCV libraries and when executed will show a live video from the webcam. It then capture the cube, then print the answer of it, by using kociemba algorithm

1. Run the file: video.py. It should open your webcam
2.  Capturing the whole cube with the order below:__
	Press 1: Capture the Front Face__
	Press 2: Capture the Up Face__
	Press 3: Capture the Right Face__
	Press 4: Capture the Down Face__
	Press 5: Capture the Left Face__
	Press 6: Capture the Back Face
3.  After capturing the whole cube correctly, the program will print out the way to solve it. Here are some certain symbols to know:__
	R :rotate the right side of the cube 90 degrees clockwise__
	R' :rotate the right side of the cube 90 degrees clockwise__
	R2 : rotate the right side of the cube 180 degrees__
	We label: Front (F), Up (U), Right (R), Down (D), Left (L), Back (B)__
	Keep in mind that you need to remember the order of the cube to solve it. Or else you might stuck at an unknown state
4. Reference links:__
[Kociemba Algorithm](https://ruwix.com/the-rubiks-cube/herbert-kociemba-optimal-cube-solver-cube-explorer/)__
[Kociemba Library](https://github.com/muodov/kociemba)__
[1st Github Repo for references](https://www.youtube.com/watch?v=WJRhB39BxWQ&list=PLrhQ-QWgC9sj_tZj-8Ho5_v5PkUwBEHqx&index=11&t=797s)__
[2nd Github Repo for references](https://github.com/thatc0der/3x3x3-Rubiks-Cube-Solver)
