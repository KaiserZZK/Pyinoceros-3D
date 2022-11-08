# Hey! Welcome to 3D Engine (ver. Beta).

`Zekai Zhang (zz2919@columbia.edu); latest updated on 11/06/2022`

## 0. Environment Pre-requisites
The programs run in the `Python3` environment; in addition, please ensure that the following modules/libraries have been
properly installed:
- `pygame` is used as the graphic user interface for displaying 3D models;
- `numpy` is used for ease of performing matrix multiplication and transformations;
- `pyOpenGL` is used for 
- *disclaimer:* all the parsing, modeling, and mathematical calculation algorithms were implemented locally; all the aforementioned libraries and packages
are used solely for the purpose of displaying models and standardizing matrix inputs.
```
$ pip3 intall pygame
$ pip3 install numpy
$ pip3 install PyOpenGL
```

## 1. Running the Programs
### 1.1 Wireframe Viewer
The first program will allow you to inspect the provided 3D model as a wireframe. <br>
In directory `./1_wireframe` you will find executable `run_wireframe.py`; kindly navigate to the direactory and 
in terminal, run the program in the following format:
```
$ python3 run_wireframe.py <object_file_name>
```
For instance, if `object.txt`, the text file containing information about the 3D model, is placed witin the parent 
directory of the program, you will run command:
```
$ python3 run_wireframe.py ../object.txt
```
If you provide 0 or more than 1 filename input, the system will generate an error message.
Specific features (e.g. rotating the model, zooming and rotating the camera, and toggling the axes) will be elaborated
in Section 2. 
### 1.2 Rendered Viewer
Similar to the wireframe viewer, in `./2_rendered` you will find `run_rendered.py`; run the program using formate
```
$ python3 run_rendered.py <object_file_name>
```


## 2. Viewer Features
### 2.1 Wireframe Viewer
The wireframe viewer comes with the following features:
- Press mouse and drag LEFT/RIGHT to rotate the model around the y-axis
- Press mouse and drag UP/DOWN to rotate the model around the x-axis
- Press mouse and drag diagonally to rotate the model around the z-axis
- Press `w`, `a`, `s`, `d` on keyboard to move camera closer to or further from the object
- Press `up`, `down` on keyboard to rotate camera vertically
- Press `left`, `right` on keyboard to rotate camera horizontally
- Press and hold `x` on keyboard to display the coordinates: RED, GREEN, and BLUE represent x-, y-, and z-zxes respectively. 

### 2.1 Rendered Viewer
The rendered viewer comes with the following features:
- Press mouse and drag LEFT/RIGHT to rotate the model around the y-axis
- Press mouse and drag UP/DOWN to rotate the model around the x-axis
- Press mouse and drag diagonally to rotate the model around the z-axis
