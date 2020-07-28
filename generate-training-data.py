import os
import cv2

cap = cv2.VideoCapture(0)
count = 1
folder = str(input("Enter The Folder Name in which you want to save the images\n1 rock\n2 empty\n3 scissors\n4 paper\n"))

while(True):
     ret,frame = cap.read()
     print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
     print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
     frame = cv2.rectangle(frame,(19,39),(402,302),(0,0,255),1)
     font = cv2.FONT_HERSHEY_SIMPLEX
     frame = cv2.putText(frame,"Do Your Actions Here",(40,330),font,1,(255,0,0),2)
     cv2.imshow('Images',frame)
     start_row,start_col = int(40),int(20)
     end_row,end_col = int(300),int(400)
     frame = frame[start_row:end_row,start_col:end_col]
     cv2.imwrite('C://Users//Manish Sehrawat//Downloads//training_data//'+folder+'//image'+str(count)+'.jpg',frame)
     count = count + 1
     if count > 100:
         break
     if cv2.waitKey(10) & 0xFF == ord('q'):
         break
cap.release()
cv2.destroyAllWindows()
#this is my code
     
