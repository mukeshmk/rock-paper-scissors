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
import sys

try:
	label_name = sys.argv[1]
	num_samples = int(sys.argv[2])
except:
	print('error,argument expected!')
	print(desc)
	exit(-1)

IMG_SAVE_PATH = 'image_data'
IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH,label_name)

try:
	os.mkdir(IMG_CLASS_PATH)

except FileExistsError:
	print('file already exists!')
	pass
 
try:
	os.mkdir(IMG_CLASS_PATH)
except FileExistsError:
	print('file already exists!')
	pass

# reading the image from camera:
cap = cv2.VideoCapture(0)
start=False
count=0

while True:
	ret,frame = cap.read()
	if not ret:
		continue
	
	if count == num_samples:
		break

	cv2.rectangle(frame,(60,60),(400,400),(255,255,255),2)

	if start:
		roi = frame[60:400,60:400]
		save_path = os.path.join(IMG_CLASS_PATH,'{}.jpg'.format(count+1))
		cv2.imwrite(save_path,roi)
		count+=1

	cv2.putText(frame,'collecting {}'.format(count),(5,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2,cv2.LINE_AA)
	cv2.imshow('collecting images',frame)

	k = cv2.waitKey(10)
	if k==ord('s'):
		start = not start

	if k==ord('q'):
		break

print('{} images saved to {}'.format(count,IMG_CLASS_PATH))
cap.release()
cv2.destroyALLWindows()
