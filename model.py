# NO NOT MODIFY THE CONTENTS OF THIS FILE UNLESS REQUIRED

import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

CLASS_MAP = {
    "empty": 0,
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

def mapper(value):
    return CLASS_MAP[value]

def create_model(input_shape, num_classes):
#     model = keras.models.Sequential([
#         # NOTE the input shape is the desired size of the image with 3 bytes color
#         # This is the first convolution
#         # With 64 filters and a kernel_size of (3, 3)
#         # DOCS: https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D
#         keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=input_shape),
#         keras.layers.MaxPooling2D(2, 2),
#         # The second convolution
#         keras.layers.Conv2D(64, (3,3), activation='relu'),
#         keras.layers.MaxPooling2D(2,2),
#         # The third convolution
#         keras.layers.Conv2D(128, (3,3), activation='relu'),
#         keras.layers.MaxPooling2D(2,2),
#         # The fourth convolution
#         keras.layers.Conv2D(128, (3,3), activation='relu'),
#         keras.layers.MaxPooling2D(2,2),
#         # The fifth convolution
#         keras.layers.Conv2D(128, (3,3), activation='relu'),
#         keras.layers.MaxPooling2D(2,2),
#         # Flatten the results to feed into a DNN
#         keras.layers.Flatten(),
#         keras.layers.Dropout(0.5),
#         # 512 neuron hidden layer
#         keras.layers.Dense(512, activation='relu'),
#         keras.layers.Dense(num_classes, activation='softmax')
#     ])
    base_model = VGG16(weights='imagenet',include_top=False,input_shape=(255,255,3))
    base_model.trainable = False
    model = tf.keras.models.Sequential([
        base_model,
        keras.layers.GlobalAveragePooling2D(),
        keras.layers.Dense(512,activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(4,activation='softmax')
    return model

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get("accuracy") >= 0.99):
            print("Reached 99% accuracy, cancelling training!")
            self.model.stop_training = True
            
def generate_model(X, y):

    dataset, labels = X, y

    # label encode the classes
    labels = list(map(mapper, labels))

    input_shape = (225, 225, 3)
    model = create_model(input_shape, len(CLASS_MAP))

    with tf.device('/device:CPU:0'):

        model.compile(loss='sparse_categorical_crossentropy',
                      optimizer=keras.optimizers.Adam(1e-3, amsgrad=True),
                      metrics=['accuracy'])

        model.summary()
        callback = myCallback()
        # start training
        model.fit(np.array(dataset), np.array(labels), epochs=15,callbacks=[callback])

        # save the model for later use
        model.save("rock-paper-scissors-model.h5")
