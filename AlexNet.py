# import the necessary packages
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras.layers import Dropout
from keras import backend as K


class AlexNet:
    @staticmethod
    def build(width, height, depth, classes):
        # initialize the model
        model = Sequential()
        inputShape = (height, width, depth)

        # if we are using "channels first", update the input shape
        if K.image_data_format() == "channels_first":
            inputShape = (depth, height, width)
            # first set of CONV => RELU => POOL layers
        model.add(Conv2D(filters=20, padding="valid",kernel_size=(5,5),
                         input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2),padding="valid"))
        # second set of CONV => RELU => POOL layers
        model.add(Conv2D(50, (11,11), padding="valid",strides=(1,1)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2),padding="valid"))
        # third set of CONV => RELU => POOL layers
        model.add(Conv2D(100, (3,3), padding="valid",strides=(1,1)))
        model.add(Activation("relu"))
        # fourth set of CONV => RELU => POOL layers
        model.add(Conv2D(100, (3,3), padding="valid",strides=(1,1)))
        model.add(Activation("relu"))
        # fifth set of CONV => RELU => POOL layers
        model.add(Conv2D(50, (5,5), padding="valid",strides=(1,1)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2),padding="valid"))
        # first (and only) set of FC => RELU layers


        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))
        model.add(Dropout(0.4))

        # softmax classifier
        model.add(Dense(classes))
        model.add(Activation("softmax"))

        # return the constructed network architecture
        return model