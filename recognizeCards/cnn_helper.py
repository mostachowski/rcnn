import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import model_from_json
from helper_functions import getData



def get_model(model_path="", weights_path=""):

    # model =  Sequential()
    # model.add(Conv2D(16,kernel_size=(7,7), activation='relu', input_shape=(536,356,3)))
    # model.add(MaxPooling2D(pool_size=(2,2)))
    # model.add(Conv2D(16,kernel_size=(7,7), activation='relu'))
    # model.add(MaxPooling2D(pool_size=(2,2)))
    # model.add(Conv2D(16,kernel_size=(7,7), activation='relu'))
    # model.add(MaxPooling2D(pool_size=(2,2)))
    # model.add(Flatten())

    # model.add(Dense(19000, activation='sigmoid'))
    # model.add(Dense(19000, activation='sigmoid'))
    # model.add(Dropout(0.1))
    # model.add(Dense(2, activation='softmax'))
    # model.summary()


    if len(model_path) == 0 and len(weights_path) == 0:
     
        num_classes = 15
        convolutions = 32
        img_rows = 30
        img_cols = 30
        input_shape = (img_rows,img_cols,1) 

        model =  Sequential()
        model.add(Conv2D(convolutions,kernel_size=(3,3), activation='relu', input_shape=(input_shape)))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Conv2D(convolutions,kernel_size=(3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Flatten())

        model.add(Dense(400, activation='sigmoid'))
        model.add(Dense(400, activation='sigmoid'))
        model.add(Dropout(0.1))
        model.add(Dense(num_classes, activation='softmax'))
        model.summary()
        from keras.utils import plot_model 
        # plot_model(model, to_file="model.png", show_shapes=True, show_layer_names=True)


        model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])
        train_model(model,"C:/Projekty/nndemo/NNDemo/tensorflow/data/generated/", save_model_path="model.json", save_weights_path="model.h5")
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

def train_model(model, data_path, save_model_path, save_weights_path):
    x_train,y_train, x_test, y_test  = getData("C:/Projekty/nndemo/NNDemo/tensorflow/data/generated/")
    num_classes = 15
    batch_size = 20
    epochs = 20
    img_rows = 30
    img_cols = 30
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