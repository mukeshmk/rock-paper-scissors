import cv2
import numpy as np
from random import choice
from tensorflow.keras.models import load_model

# custom pre-process techniques
# import this incase you want to resume the pre-processing techniques
# for the model creation and model predection while playing

#Importing the preprocess method from a different Jupyter notebook containing the entire preprocess and train code
from ipynb.fs.full.Preprocessing import preprocess  

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

def win(user,computer):
    if user == computer:
        return ('It''s a Tie')
    elif user == 'rock' and computer == 'paper':
        return ('Winner is: COMPUTER')
    elif user == 'rock' and computer == 'scissors':
        return ('Winner is: USER')
    elif user == 'paper' and computer == 'rock':
        return ('Winner is: USER')
    elif user == 'paper' and computer == 'scissors':
        return ('Winner is: COMPUTER')
    elif user == 'scissors' and computer == 'paper':
        return ('Winner is: USER')
    elif user == 'scissors' and computer == 'rock':
        return ('Winner is: COMPUTER')

def main():
    # note make sure the img_shape = (225, 225)
    # if you are changing this make sure to update the code in the model
    model = load_model("rock-paper-scissors-model.h5")

    cap = cv2.VideoCapture(0)
    last_move = None
    
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        
        cv2.rectangle(frame, (50,125), (450,525), (255,255,255), 2)   #User box
        cv2.rectangle(frame, (850,125), (1250,525), (255,255,255), 2)  #Computer box
        
        roi = frame[125:525,50:450]
        #img=cv2.resize(roi,(225,225))
        img = preprocess(roi)
 
        pred = model.predict(np.array([img]))
        move_made_by_you = mapper(np.argmax(pred[0]))

        if last_move != move_made_by_you:
            if move_made_by_you != 'empty':
                move_made_by_comp = choice(['rock','paper','scissors'])
                winner = win(move_made_by_you, move_made_by_comp)
            else:
                move_made_by_comp = 'empty'
                winner = 'Start Game'
        last_move = move_made_by_you

        if move_made_by_comp != 'empty':
            comp_img = cv2.imread('Comp_Images/{}.jpg'.format(move_made_by_comp)) #Images matching labels are read
            comp_img = cv2.resize(comp_img, (400,400))
            frame[125:525, 850:1250] = comp_img            
            
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame, 'USER: ' + move_made_by_you,(150,600), font, 1, (172,188,68), 2, cv2.LINE_AA)
        cv2.putText(frame, 'COMPUTER: ' + move_made_by_comp,(900,600), font, 1, (172,188,68), 2, cv2.LINE_AA)
        cv2.putText(frame, winner, (500,75),font, 1, (172,188,68), 2, cv2.LINE_AA)
        
        cv2.imshow('Rock, Paper, Scissors Game', frame)
        
        if cv2.waitKey(33) == 27:  #Press ESC Key to stop
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    # once you have written the code to play the game uncomment the below lines 
    # and place them where required so that the model can predict

main()