# EyeLidSimulator (ELS)
## ELS: GT Generator

![alt text](images/main_image.jpg "Main")


 This tool let's you generate millions of different sythetic data, combining skin,iris color, eyelid apperture, etc.. in order to train your AI model to detect different features of the eye:

- Iris 
- Pupil
- Eye-Gaze
- Eyelid

## Download link

ELS (Beta 1.0):


## Manual

### KeyBoard

i : Change Iris color.
s : Change Skin and color.
l : Change Eyeslash type.
esc-> Stop the GT generation.

### Mouse 

Left Buttom: Control the Eye movement.
Right Buttom: Move the Head pose.
Wheel: Close (down) or Open (up) the Eyelid.

### GUI

Automatic Eyelid: Blinks the eyelid automatically.
Pupil: Control the aperture of the pupil.
Iris: Control the size of the Iris.
LandMarks: Show/Hidde the landmarks

Generate GT: Generate a folder with your time system and create random poses, iris,skin,skin color, and save it into an image and json file.

## JSON File

"eyelid_left": Left Eyelid 2D backward projection (x,y,z)
"eyelid_right": Right Eyelid 2D backward projection (x,y,z)
"iris_left": Left Iris 2D backward projection (x,y,z)
"iris_right": Right Iris 2D backward projection (x,y,z)
"pupil_left": Left Pupil 2D backward projection (x,y,z)
"pupil_right": Right Pupil 2D backward projection (x,y,z)
"look_vec_left": Left Gaze 2D backward projection (x,y,z)
"look_vec_right": Right Gaze 2D backward projection (x,y,z)
"head_rotation": Head rotation (Euler) in degrees ()
