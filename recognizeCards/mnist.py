import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import model_from_json
import cv2


def load_dataset():
    def donwload(filename, source='http://yann.lecun.com/exdb/mnist/'):
            print("Downloading ",filename)
            import urllib.request
            urllib.request.urlretrieve(source+filename,filename)
    import gzip
    import os
    def load_mnist_images(filename):
        if not os.path.exists(filename):
            donwload(filename)
        with gzip.open(filename,'rb') as f:
            data=np.frombuffer(f.read(),np.uint8, offset=16)
            data = data.reshape(-1,1,28,28)
            return data/np.float(256)
    def load_mnist_labels(filename):
        if not os.path.exists(filename):
            donwload(filename)
        with gzip.open(filename,'rb') as f:
            data = np.frombuffer(f.read(),np.uint8,offset=8)
        return data
    
    x_train = load_mnist_images('train-images-idx3-ubyte.gz')
    y_train = load_mnist_labels('train-labels-idx1-ubyte.gz')
    x_test = load_mnist_images('t10k-images-idx3-ubyte.gz')
    y_test = load_mnist_labels('t10k-labels-idx1-ubyte.gz')
    return x_train,y_train,x_test,y_test    

            
x_train, y_train, x_test, y_test = load_dataset()
from keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


print("shape:",x_train.shape)
print("shape y:",y_train.shape)
# import matplotlib.pyplot as plt 
# plt.show(plt.imshow(x_train[3][0]))

def build_NN():
    num_classes = 10
    convolutions = 32
    img_rows = 28
    img_cols = 28
    input_shape = (1,img_rows,img_cols) 

    model =  Sequential()
    model.add(Conv2D(convolutions,kernel_size=(3,3), activation='relu', input_shape=(input_shape), data_format='channels_first'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Conv2D(convolutions,kernel_size=(3,3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Flatten())

    model.add(Dense(100, activation='sigmoid'))
    model.add(Dense(100, activation='sigmoid'))
    model.add(Dropout(0.1))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])
    model.summary()
    return model

def build_model(model_path="model_mnist.json", weights_path="mnist_weights.h5"):
    model = build_NN()
    model.fit(x_train,y_train,batch_size=100, epochs=5,verbose=1)
    validate = model.evaluate(x_test,y_test)
    model_json = model.to_json()
    with open(model_path, "w") as json_file:
        json_file.write(model_json)
        # serialize weights to HDF5
    model.save_weights(weights_path)
    print("\n\nTest loss: ",validate[0], "Test accuracy: ", validate[1])

def get_model(model_path="model_mnist.json", weights_path="mnist_weights.h5"):
        json_file = open(model_path, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights(weights_path)
        model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])
        return model


test =cv2.imread("1_test.png")
test = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
test = cv2.resize(test,(28,28))
print(test.shape)
model = get_model()
resized = test.reshape(1,1,28,28)
result = model.predict_proba(resized)


print(result.argmax())

import matplotlib.pyplot as plt 
plt.show(plt.imshow(test))


