import os
import cv2

# write your code here to open your laptop's camera
# and store images for rock paper scissors

# I would highly recommend storing these images in folders stucture like below:
# training_data\
#           |-- empty\
#           |-- rock\
#           |-- paper\
#           |-- scissors\
# having a folder structure like this will make it easy for you to read the images while pre-processing
import cv2
import numpy as np
import os

def data():
    x, y, h, w = (50, 50, 300, 300)
    vid = cv2.VideoCapture(0)
    c=1
    while(True):
        ret, frame=vid.read() 
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('collected images', frame)      
        cv2.imwrite(os.path.join(path,"img-" + str(c) + ".jpg"),frame[50:350,50:350])
        c+=1
        if c>250:
            break
        if cv2.waitKey(1) == 0x1b:
            break
    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    folder_of_choice=int(input("enter the type: \n1.empty \n2.rock \n3.paper \n4.scissors \n"))
    if folder_of_choice == 1:
        path='E:/Augray/training_data/empty'
        data()
    elif folder_of_choice == 2:
        path='E:/Augray/training_data/rock'
        data()
    elif folder_of_choice == 3:
        path='E:/Augray/training_data/paper'
        data()
    elif folder_of_choice == 4:
        path='E:/Augray/training_data/scissors'
        data()
    else:
        print('enter correct folder:')
