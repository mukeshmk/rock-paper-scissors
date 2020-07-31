import cv2
import numpy as np
from random import choice
from tensorflow.keras.models import load_model
from preprocessandtrain import preprocess
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

    test_list = ['paper','rock','scissors']
    computer_choice = choice(test_list)

    cap = cv2.VideoCapture(0)
    
    
    while(True):
        ret,frame = cap.read()
        if ret == True:
            frame = cv2.rectangle(frame,(100,100),(300,300),(0,0,255),5)
            cv2.imshow('user_input',frame)
            img = cv2.imwrite('img.jpg',frame[100:300,100:300])
            
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

    img = cv2.imread('img.jpg')
    img = preprocess(img)
    
    pred = model.predict(np.array([img]))
    move_made_by_you = mapper(np.argmax(pred[0]))
    #print(move_made_by_you)

    moves ={'rock':'scissors',
            'scissors':'paper',
            'paper' : 'rock',
            'empty': 'empty'}

    for key,val in moves.items():
        if move_made_by_you == key and computer_choice == val:
            print('You win')
            print('move_by_you',move_made_by_you)
            print('move of computer',computer_choice)
    # once you have written the code to play the game uncommend the below lines 
    # and place them where required so that the model can predict
    # pred = model.predict(np.array([img]))
    # move_made_by_you = mapper(np.argmax(pred[0]))

if __name__ == "__main__":
    main()