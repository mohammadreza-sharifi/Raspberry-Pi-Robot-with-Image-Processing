import numpy
import cv2
import os
import RPi.GPIO as io

faceCascade = cv2.CascadeClassifier('/home/pi/Desktop/facetracking/haarcascade_frontalface_default.xml')

# Choose camera for streaming 
cap = cv2.VideoCapture(0)

# Set raspberry pi GPIO pins
io.setwarnings(False)
io.setmode(io.BOARD)
io.setup(3,io.OUT)
io.setup(5,io.OUT)
io.setup(10,io.OUT)
io.setup(8,io.OUT)

# This function moves the robot forward
def forward():
    io.output(3,1)
    io.output(10,1)
    io.output(5,0)
    io.output(8,0)

# This function moves the robot backward    
def backward():
    io.output(3,0)
    io.output(10,0)
    io.output(8,1)
    io.output(5,1)

# This function stops the robot    
def stopfcn():
    io.output(3,0)
    io.output(10,0)
    io.output(8,0)
    io.output(5,0)

# This function moves the robot to the right    
def right():
    io.output(3,1)
    io.output(10,0)
    io.output(8,0)
    io.output(5,0)

# This function moves the robot to the left   
def left():
    io.output(3,0)
    io.output(10,1)
    io.output(8,0)
    io.output(5,0)

while True:
    
    # Start Streaming
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # face detection
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    # Draw a rectangle around the face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('Result', frame)
    
    # Control the robot with keyboard input ** i control the robot from my laptop in vnc viewer**
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    elif k == ord("w"):
        forward()
    elif k == ord("s"):
        backward()
    elif k == ord("a"):
        left()
    elif k == ord("d"):
        right()
    elif k == ord("b"):
        stopfcn()
    else:
        pass
        
        
cap.release()
cv2.destroyAllWindows()