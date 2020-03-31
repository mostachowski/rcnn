import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import model_from_json
from PIL import Image
import numpy as np
import glob
import os
from random import shuffle
from sklearn.model_selection import train_test_split

###  get keras model. If model and weight paths are null 
###  the model will be built from scratch
def get_model_for_numbers(model_path="", weights_path=""):

    if len(model_path) == 0 and len(weights_path) == 0:
        num_classes = 13
        convolutions = 32
        img_rows = 32   
        img_cols = 32
        input_shape = (img_rows,img_cols,1) 

        model =  Sequential()
        model.add(Conv2D(convolutions,kernel_size=(3,3), activation='relu', input_shape=(input_shape)))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Conv2D(convolutions,kernel_size=(3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Flatten())

        model.add(Dense(400, activation='relu'))
        model.add(Dense(400, activation='relu'))
        model.add(Dropout(0.1))
        model.add(Dense(num_classes, activation='softmax'))
        model.summary()
        from keras.utils import plot_model 
        plot_model(model, to_file="model.png", show_shapes=True, show_layer_names=True)

        model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])
        train_model(model,"numbers_generated/", "model_numbers.json", "model_numbers.h5",num_classes,img_rows,img_cols)
    else:
        # load json and create model
        json_file = open(model_path, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights(weights_path)
        model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])

    return model

def train_model(model, data_path, save_model_path, save_weights_path, num_classes, img_rows,img_cols):
    batch_size = 20
    epochs = 15
    x_train,y_train, x_test, y_test  = getData(data_path)
    x_train = x_train.reshape(x_train.shape[0],img_rows, img_cols, 1)
    y_train = keras.utils.to_categorical(y_train,num_classes)
    x_test = x_test.reshape(x_test.shape[0],img_rows, img_cols, 1)
    y_test = keras.utils.to_categorical(y_test,num_classes)
    model.fit(x_train,y_train,batch_size=batch_size, epochs=epochs,verbose=1)

    validate = model.evaluate(x_test,y_test)
    print("\n\nTest loss: ",validate[0], "Test accuracy: ", validate[1])


    # serialize model to JSON
    model_json = model.to_json()
    with open(save_model_path, "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights(save_weights_path)
    print("Saved model to disk")

def read_file_as_numpy(filename):
    pill_im = Image.open(filename)

    pil_imgray = pill_im.convert('L')  
    res = np.array(pil_imgray)
    # res.resize((60,60))
    return res

# Prepare data to train and test. It reads given directory and assums that subdirectories will be the class names
def getData(direcotry):
    all_files = list()
    x_train = list()

    y_train = list()
    for filename in glob.iglob(direcotry + '**/*.png', recursive=True):
        all_files.append(filename)
    shuffle(all_files)
    print ("filename shape: ", len(all_files))
    for filename in all_files:
        x_train.append(read_file_as_numpy(filename))
        y_train.append(os.path.basename(os.path.dirname(filename)))
    print("x_train len: ",len(x_train))
    x, x_test,y, y_test = train_test_split(x_train,y_train,test_size=0.33,random_state=42)

    print("x[0] shape: ",x[0].shape)

    return np.asarray(x) ,y, np.asarray(x_test),y_test

# get_model_for_numbers()