import os
import cv2
from model import generate_model

TRAINING_DATA_DIR = "training_data"

# here write code to pre process the images as required
# but make sure to have a copy of the original training data
# or that you write your code in such a way that you pre-process on the fly
# pre-processing on the fly is possible because this is small project and
# not a lot of images will be there as well.
def preprocess(img):
    # your code goes here
    scale_percent = 40  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    img_resize = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    # Converting color image to grayscale image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Gaussian_blurred_img=np.hstack([cv2.GaussianBlur(img_resize,(9,9),0)])

    # Creating our sharpening filter
    filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    # Applying cv2.filter2D function on our image
    final_img = cv2.filter2D(gray_img, -1, filter)
    return  final_img

# NOTE: This method will only work if you have followed the same folder strucutre as I mentioned
# if not update this code below
def get_dataset():
    # load images from the training data directory
    dataset = []
    for label_dir in os.listdir(TRAINING_DATA_DIR):
        # iterating each item in the training data directory
        path = os.path.join(TRAINING_DATA_DIR, label_dir)
        if not os.path.isdir(path):
            continue
        # iterating threw each file in the sub directory
        for image_file in os.listdir(path):
            # loading each image
            img = cv2.imread(os.path.join(path, image_file))
            img = preprocess(img)           
            # adding them to the dataset
            dataset.append([img, label_dir])
    
    return zip(*dataset)

def main():
    # this line will get the data pre-process the image
    # as per preprocess() method and store the results in X, y
    # which will be used in model generation
    X, y = get_dataset()
    # this line will generate a tensorflow model and save it as rock-paper-scissors-model.h5 file
    generate_model(X, y)

if __name__ == "__main__":
    main()
