# vehicle-counter--image-processing<br>
## Project Description
-> vehicle-counter is an image-processing based project made using made using python, OpenCV library.<br>
-> This project counts vehicle passing through a particular point.
-> It automatically detects the vehicles (by marking it with a green rectangle and a red point at the centre) and counts while passing through a particular location. 

# Introduction-
I love the idea of smart cities. The thought of automated smart energy systems, electrical grids, one-touch access ports – it’s an enthralling concept! Honestly, it’s a dream for a data scientist and I’m delighted that a lot of cities around the world are moving towards becoming smarter. <br>
One of the core components of a smart city is automated traffic management. And that got me thinking – could I use my data science chops to build a vehicle detection model that could play a part in smart traffic management?
Think about it – if you could integrate a vehicle detection system in a traffic light camera, you could easily track a number of useful things simultaneously: <br>

* How many vehicles are present at the traffic junction during the day?<br>
* What time does the traffic build up? <br>
* What kind of vehicles are traversing the junction (heavy vehicles, cars, etc.)?
* Is there a way to optimize the traffic and distribute it through a different street?
* And so on. The applications are endless!

We humans can easily detect and recognize objects from complex scenes in a flash. Translating that thought process to a machine, however, requires us to learn the art of object detection using computer vision algorithms.
So in this project, we will be building an automatic vehicle detector and counter model.

### Tools and Languages:
<img align="left" alt="pycharm" width="26px" src="pycharm.png" />
<img align="left" alt="Python" width="30px" src="python.png" />
<img align="left" alt="pip" width="36px" height="37px" src="pip.png" />
<img align="left" alt="numpy" width="36px" src="numpy.png" />
<img align="left" alt="OpenCV" width="30px" src="opencv.png" />
<br>

### Installing Libraries

```cmd
pip install numpy
pip install opencv
pip install times

```

-> We will use numpy library because it contains a multi-dimensional array and matrix data structures. It can be utilised to perform a number of mathematical operations on arrays such as trigonometric, statistical, and algebraic routines.
-> We use OpenCV library because it is a cross-platform library using which we can develop real-time computer vision applications. It mainly focuses on image processing, video capture and analysis including features like face detection and object detection


### Steps to follow
-Install the given libraries<br>
-Download the code from the given github repository<br>
-Run the code<br><br>


###  steps followed while making this project:---
1.Read the video frame by frame.

2.Apply some fileters to the frame(dilation, etc.).

3.Use BackgroundSubtractor to split the foreground from background(white-foreground, black-background).

4.Detect the contours of the foreground(moving objects).

5.Calculate the centroid of each moving object.

6.For each centroid, detect if there's a nearby centroid of the last frame. If so, assign them to the same vehicle.

7.For each vehicle, detect whether it crossed the target line.


# The Idea Behind Detecting Moving Objects in Videos---
Object detection is a fascinating field in computer vision. It goes to a whole new level when we’re dealing with video data. The complexity rises up a notch, but so do the rewards! <br>
We can perform super useful high-value tasks such as surveillance, traffic management, fighting crime, etc. using object detection algorithms<br>


-> Here is the output of the project <br> 

### Output
<img alt="output"  src="op.png" />

### Developed by:
<a href="https://github.com/sambit221">Sambit Kumar Tripathy</a>
