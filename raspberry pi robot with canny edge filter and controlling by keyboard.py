import cv2
import numpy as np
import RPi.GPIO as io

cap = cv2.VideoCapture(0)

io.setwarnings(False)
io.setmode(io.BOARD)
io.setup(3,io.OUT)
io.setup(5,io.OUT)
io.setup(10,io.OUT)
io.setup(8,io.OUT)

def forward():
    io.output(3,1)
    io.output(10,1)
    io.output(5,0)
    io.output(8,0)
    
def backward():
    io.output(3,0)
    io.output(10,0)
    io.output(8,1)
    io.output(5,1)
    
def stopfcn():
    io.output(3,0)
    io.output(10,0)
    io.output(8,0)
    io.output(5,0)
    
def right():
    io.output(3,1)
    io.output(10,0)
    io.output(8,0)
    io.output(5,0)
    
def left():
    io.output(3,0)
    io.output(10,1)
    io.output(8,0)
    io.output(5,0)

while(1):
    ret , frame =cap.read()
    frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    result = cv2.Canny(frame,100,200)
    
    cv2.imshow('frame',frame)
    cv2.imshow('result',result)
    
    k = cv2.waitKey(5)
    if k==27 & 0xFF:
        break
    elif k ==ord("w"):
        forward()
    elif k == ord("s"):
        backward()
    elif k == ord("b"):
        stopfcn()
    elif k == ord("d"):
        right()
    elif k == ord("a"):
        left()
    else:
        pass
    
    
cv2.destroyAllWindows()

