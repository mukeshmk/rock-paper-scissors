import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

# Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Display the resulting frame
    cv2.imshow('frame',frame)

#time.sleep(01)
    Capture = cv2.CaptureFromCAM(0)