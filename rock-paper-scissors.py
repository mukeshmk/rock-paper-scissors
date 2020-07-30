import cv2
import numpy as np
import random 
from tensorflow.keras.models import load_model

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

   

def preprocess(img):
    
    #Image Resizing
    width = 225
    height = 225
    dimensions = (width,height)
    img = cv2.resize(img,dimensions,interpolation = cv2.INTER_LINEAR)
    img = cv2.GaussianBlur(img,(5,5),0)
    return img
def generate():
            while(True):
                ret,frame = cap.read()
                frame = cv2.rectangle(frame,(19,39),(492,392),(0,0,255),1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                frame = cv2.putText(frame,"Do Your Actions Here",(70,450),font,1,(255,0,0),2)
                cv2.imshow('Images',frame)
                start_row,start_col = int(40),int(20)
                end_row,end_col = int(390),int(490)
                frame = frame[start_row:end_row,start_col:end_col]
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    cv2.imwrite('C://Users//Manish Sehrawat//Downloads//training_data//test.jpg',frame)
                    break
            cap.release()
            cv2.destroyAllWindows() 
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
    
    your_score = 0
    pc_score  = 0
    while(True):
        generate()
        img = cv2.imread('C://Users//Manish Sehrawat//Downloads//training_data//test.jpg')
        img = preprocess(img)
        pred = model.predict(np.array([img]))
        move_made_by_you = mapper(np.argmax(pred[0]))
        choices = ['paper','scissors','rock']
        move_made_by_bot = random.choice(choices)
        print("Your Move Is  ",move_made_by_you)
        print("Computer's Move Is  ",move_made_by_bot)
        if move_made_by_you == 'scissors':
            if move_made_by_bot == 'scissors':
                print("Match Drawn")
            elif move_made_by_bot == 'paper':
                print("You Won")
                your_score = your_score+1
            elif move_made_by_bot == 'rock':
                print("You Lose")
                pc_score = pc_score +1
                
        if move_made_by_you == 'rock':
            if move_made_by_bot == 'rock':
                print("Match Drawn")
            elif move_made_by_bot == 'scissors':
                print("You Won")
                your_score = your_score+1
            elif move_made_by_bot == 'paper':
                print("You Lose")
                pc_score = pc_score +1
                
        if move_made_by_you == 'paper':
            if move_made_by_bot == 'paper':
                print("Match Drawn")
            elif move_made_by_bot == 'rock':
                print("You Won")
                your_score = your_score+1
            elif move_made_by_bot == 'scissors':
                print("You Lose")
                pc_score = pc_score +1
        if move_made_by_you == 'empty':
            print("Wrong Move Try Again")
        print("Press A if you want to play again\nPress Any Other Button If You Want To Exit")
        choice = input("Enter Your Choice\n")
        if choice == 'A' or choice =='a':
            continue
        else:
            break
            
    scores = {'Computer':pc_score,'Your_Score':your_score}
    print("Your Final Score",scores.get('Your_Score'))
    print("Computer Final Score",scores.get('Computer'))

main()


            

