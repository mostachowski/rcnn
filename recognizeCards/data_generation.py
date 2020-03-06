from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K


# dimensions of our images.
img_width, img_height = 30, 30

train_data_dir = 'C:/Projekty/nndemo/NNDemo/trainingset_small/train'
validation_data_dir = 'data/validation'
nb_train_samples = 4000
nb_validation_samples = 800
epochs = 50
batch_size = 16

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

train_datagen = ImageDataGenerator(
    width_shift_range=0.2,
    height_shift_range=0.05,
    shear_range=0.2,
    horizontal_flip=False)
i =0
for batch in train_datagen.flow_from_directory(directory='C:/Projekty/nndemo/NNDemo/tensorflow/data/train/x_button', batch_size=1, save_to_dir='C:/Projekty/nndemo/NNDemo/tensorflow/data/generated/x_button',target_size=(30,30), save_format='png'):
    i+=1
    if i>20:
        break