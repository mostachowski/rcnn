import os,keras

def generate_data(direcotry_input,directory_output):

    from keras.preprocessing.image import ImageDataGenerator
    train_datagen = ImageDataGenerator(
        width_shift_range=0.3,
        height_shift_range=0.2,
        shear_range=0.2,
        horizontal_flip=False,rotation_range=0.2,zoom_range=0.3)
    i = 0
    for batch in train_datagen.flow_from_directory(directory=direcotry_input, batch_size=1, save_to_dir=directory_output,target_size=(32,32), save_format='png'):
        i+=1
        if i>4000:
            break
    
    import os
    import shutil
    for item in os.listdir(direcotry_input):
        new_dir = directory_output + "/" + item
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        prefix = "_" + item + "_"
        prefixed = [filename for filename in os.listdir(directory_output) if filename.startswith(prefix)]
        for filename in prefixed:
            shutil.move(directory_output + "/" + filename, new_dir)

generate_data("number_model","numbers_generated")