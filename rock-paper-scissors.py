import cv2
import numpy as np
from random import choice
from tensorflow.keras.models import load_model

# custom pre-process techniques
# import this incase you want to resume the pre-processing techniques
# for the model creation and model predection while playing
# import preprocess

# DO NOT MODIFY THIS
REV_CLASS_MAP = {
    0: "empty",
    1: "rock",
    2: "paper",
    3: "scissors"
}

# DO NOT MODIFY THIS
def mapper(value):
    return REV_CLASS_MAP[value]

def main():
    # note make sure the img_shape = (225, 225)
    # if you are chaning this make sure to update the code in the model
    model = load_model("rock-paper-scissors-model.h5")
#_________________________________
    # once you have written the code to play the game uncommend the below lines 
    # and place them where required so that the model can predict
    # pred = model.predict(np.array([img]))
    # move_made_by_you = mapper(np.argmax(pred[0]))
   # ______________________
    cap = cv2.VideoCapture(0)
    prev_move = None
    while True:
        ret,frame = cap.read()
        if not ret:
            continue
        
        cv2.rectangle(frame,(100,100),(500,500),(255,255,255),2) #user
        cv2.rectangle(frame, (800, 100), (1200, 500), (255, 255, 255), 2) #computer
        
        roi = frame[100:500,100:500]
        img = cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)
        img = cv2.GaussianBlur(img,(5,5),0)
        img = cv2.Canny(img,50,60)
        img = cv2.resize(img,(255,255))
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = cv2.resize(img,(255,255))
        
        pred = model.predict(np.array([img]))
        user_move = mapper(np.argmax(pred[0])) 
        
        # ..and the winner is:
        if prev_move != user_move:
            if user_move != 'empty':
                computer_move = choice(['rock','paper','scissor'])
                winner = find_winner(user_move,computer_move)
            else:
                computer_move = 'empty'
                winner = 'waiting...'
        
        prev_move = user_move
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Your Move: " + user_move,
                (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "Computer's Move: " + computer_move,
                (750, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "Winner: " + winner,
                (400, 600), font, 2, (0, 0, 255), 4, cv2.LINE_AA)
        
        if computer_move != 'empty':
            computer_img = cv2.imread('E:/Projects/RPS/computer_images/{}.jpg'.format(computer_move))
            computer_img = cv2.resize(computer_img,(400,400))
            frame[100:500,800:1200] = computer_img
            
        cv2.imshow("rock paper scissor",frame)
        
        k = cv2.waitKey(10)
        if k == ord('q'):
            break
    
    cap.release()
    cv2.destroyALLWindows()
        
