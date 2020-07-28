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



def get_images():
    
    cap = cv2.VideoCapture(0)
    cnt1=0
    while(cnt1<=250):
        ret , frame = cap.read()
        if ret == True:
            frame = cv2.rectangle(frame,(100,100),(300,300),(0,0,255),5)
            cv2.imshow('frame',frame)
            #for i in range(2011):
            cv2.imwrite('img'+str(cnt1)+'.jpg',frame[100:300,100:300])
            cnt1=cnt1+1
                
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()

    for i in range(50):
        os.remove('img'+str(i)+'.jpg')


def make_directory():
    gesture = input('enter the gesture for which data is being collected')
    present_dir = os.getcwd()
    print(present_dir.split('\\')[-1])
    print(present_dir.split('\\')[-2])
    if present_dir.split('\\')[-2] == 'training_data':
        os.chdir('../')
    else:
        os.chdir('./training_data')
    os.mkdir(gesture)
    os.chdir(gesture)
    get_images()

def four_image_category_collection():
    for i in range(3):
        make_directory()




if __name__=="__main__":
    import os
    import cv2
    import time

    os.mkdir('training_data')
    
    four_image_category_collection()
        