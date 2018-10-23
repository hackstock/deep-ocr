import numpy as np
import cv2
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
from keras.utils import to_categorical

class NeuralNet(object):

    def __init__(self):
        # loading mnist data
        (X_train,y_train), (X_test,y_test) = mnist.load_data()

        # feature scaling and normalization
        self.training_images = X_train.reshape((60000, 28 * 28)).astype('float32') / 255
        self.training_targets = to_categorical(y_train,10)

        self.test_images = X_test.reshape((10000, 28 * 28)).astype('float32') / 255
        self.test_targets = to_categorical(y_test,10)

        self.input_shape = (self.training_images.shape[1],)

        # building the model
        self.model = Sequential()
        self.model.add(Dense(512, activation='relu', input_shape=self.input_shape))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dropout(0.25))
        self.model.add(Dense(10, activation='softmax'))

        self.model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])
        self.model.fit(self.training_images, self.training_targets, validation_split=0.3, callbacks=[EarlyStopping(patience=2)], epochs=50)

    def predict(self, image):
        input = cv2.resize(image, (28 , 28)).reshape((28 * 28,)).astype('float32') / 255
        return self.model.predict_classes(np.array([input]))

        