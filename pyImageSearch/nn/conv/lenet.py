from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.core import Activation,Flatten,Dense
from keras.layers import MaxPooling2D
from keras import backend as K 



class LeNet:
    @staticmethod
    def build(width,height,depth,classes):

        model = Sequential()
        input_shape = (width,height,depth)

        if K.image_data_format() =="channel_first":
            input_shape=(depth,width,height)
        
        model.add(Conv2D(20,(5,5),padding="same",input_shape=input_shape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))

        model.add(Conv2D(20,(5,5),padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))


        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))

        model.add(Dense(classes))
        model.add(Activation("softmax"))

        return model

