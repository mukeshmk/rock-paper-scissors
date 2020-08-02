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
import os
cap=cv2.VideoCapture(0)
def capture(var):
    path=r'C:\Users\Sowmya\Desktop\rockpaperscissor'
    start = False
    count = 0
    path1=os.path.join(path,var)
    while(True):
        ret,frame=cap.read()
        if not ret:
            continue
        if count ==200:
             break
        cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
        if start:
            roi = frame[100:500, 100:500]
            save_path = os.path.join(path1, '{}.jpg'.format(count + 1))
            cv2.imwrite(save_path, roi)
            count += 1
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Collecting {}".format(count),
                (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('collecting images',frame)
        k = cv2.waitKey(5000)
        if k == ord('a'):
            start = not start
        if k == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
image=input('image')
capture(image)
