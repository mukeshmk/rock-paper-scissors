import imutils as imutils
import numpy as np
import cv2
import os
import sys
import time

# In command line give first argument as folder name
# And press  Q to stop capturing

PATH = os.getcwd()+'\\'           # it returens current file directory path .
cap = cv2.VideoCapture(0)         # captures video from camera with help of OpenCv

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#sys.argv() take arguments from command line and return it as list .

label = sys.argv[1]    # it will take 2nd argument from command line and assign it to label variable .

SAVE_PATH = os.path.join(PATH, label) # it will make directory of 2nd argument name in the same path in which we have this .py file.

try:
    os.mkdir(SAVE_PATH)  # try to make dir
except FileExistsError:
    pass

print("Hit Q to stop capturing")
count=0
while (cap.isOpened()):
            ret , frame = cap.read()

            cv2.imwrite(SAVE_PATH + '\\' + label + '{}.jpg'.format(count), frame[200:680, 800:1260])
            print(SAVE_PATH + '\\' + label + '{}.jpg Captured'.format(count))
            count+=1

            cv2.rectangle(frame, (800, 680), (1260, 200), (0, 255, 0), 2)
            cv2.imshow("Display", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()
