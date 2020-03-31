import os,keras
import glob

def generate_data(direcotry_input,directory_output):

    from keras.preprocessing.image import ImageDataGenerator
    train_datagen = ImageDataGenerator(
        width_shift_range=0.1,
        height_shift_range=0.1,
        rescale=0.3,
        horizontal_flip=False,rotation_range=0.0,zoom_range=0.4)
    i = 0
    for batch in train_datagen.flow_from_directory(directory=direcotry_input, batch_size=1, save_to_dir=directory_output,target_size=(32,32), save_format='png'):
        i+=1
        if i>20000:
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

# def prepare_data():

#     for filename in glob.iglob(direcotry + '**/*.png', recursive=True):
#         gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#         thresh = 170
#         black_image = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]

generate_data("number_model","numbers_generated")