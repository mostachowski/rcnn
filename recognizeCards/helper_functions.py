import numpy as np
from PIL import Image
import glob
import os
from random import shuffle
from sklearn.model_selection import train_test_split
from PokerDto import Figure,Color, Card
from Image_helper import CropImage
import TablePositions6Max
from find_convex import get_candidateImages
import cv2
from PokerDto import *
import pytesseract

def get_string_from_image(img):
    # img = cv2.imread(img_path)

    # # Extract the file name without the file extension
    # file_name = os.path.basename(img_path).split('.')[0]
    # file_name = file_name.split()[0]

    # # Create a directory for outputs
    # output_path = os.path.join(output_dir, file_name)
    
    # if not os.path.exists(output_path):
    #     os.makedirs(output_path)
        # Rescale the image, if needed.
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    # img = cv2.erode(img, kernel, iterations=1)
    # Apply blur to smooth out the edges
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # Apply threshold to get image with only b&w (binarization)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    cv2.imwrite("card_back_processed.png", img)
    result = pytesseract.image_to_string(img, lang="eng", config='-psm 6')
    return result

def read_file_as_numpy(filename):
    pill_im = Image.open(filename)
    area=(0,0,30,30)

    pil_imgray = pill_im.convert('L')
    res = np.array(pil_imgray.crop(area))
    return res

# Prepare data to train and test. It reads given directory and assums that subdirectories will be the class names
def getData(direcotry):
    all_files = list()
    x_train = list()

    y_train = list()
    for filename in glob.iglob(direcotry + '**/*.png', recursive=True):
        all_files.append(filename)
    shuffle(all_files)
    for filename in all_files:
        x_train.append(read_file_as_numpy(filename))
        y_train.append(convert_class_to_number(os.path.basename(os.path.dirname(filename))))
    x, x_test,y, y_test = train_test_split(x_train,y_train,test_size=0.33,random_state=42)

    return np.asarray(x) ,y, np.asarray(x_test),y_test

def convert_class_to_number(filename):
    letter = os.path.basename(filename)[0]
    if letter == '2':
        return 0
    if letter == '3':
        return 1
    if letter == '4':
        return 2
    if letter == '5':
        return 3
    if letter == '6':
        return 4
    if letter == '7':
        return 5
    if letter == '8':
        return 6
    if letter == '9':
        return 7
    if letter == 't':
        return 8
    if letter == 'j':
        return 9
    if letter == 'q':
        return 10
    if letter == 'k':
        return 11
    if letter == 'a':
        return 12
    if os.path.basename(filename) == "x_cardback":
        return 13
    return 14

def convert_numer_to_class(number):
    if number < 13:
        return Figure(number)
    return Figure.Error

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def get_card_color(picture):
    
    accepted_difference = 25
    rd = 41
    gd = 107
    bd = 168

    rs = 0
    gs = 0
    bs = 0

    rh = 211
    gh = 18
    bh = 39

    rc = 90
    gc = 172
    bc = 96    

    do = True
    x = 0
    y = 0
    diamond_count = 0
    spade_count = 0
    heart_count = 0
    club_count = 0
    while do:
        if abs(int(picture[x][y][0]) - bd)  < accepted_difference and abs(int(picture[x][y][1]) - gd) <accepted_difference and  abs(int(picture[x][y][2]) - rd) < accepted_difference:
            diamond_count = diamond_count +1
        if diamond_count >10:
            return Color.Diamond

        if abs(int(picture[x][y][0]) - bs)  < accepted_difference and abs(int(picture[x][y][1]) - gs) <accepted_difference and  abs(int(picture[x][y][2]) - rs) < accepted_difference:
            spade_count = spade_count +1
        if spade_count >10:
            return Color.Spade

        if abs(int(picture[x][y][0]) - bh)  < accepted_difference and abs(int(picture[x][y][1]) - gh) <accepted_difference and  abs(int(picture[x][y][2]) - rh) < accepted_difference:
            heart_count = heart_count +1
        if heart_count >10:
            return Color.Heart

        if abs(int(picture[x][y][0]) - bc)  < accepted_difference and abs(int(picture[x][y][1]) - gc) <accepted_difference and  abs(int(picture[x][y][2]) - rc) < accepted_difference:
            club_count = club_count +1
        if club_count >10:
            return Color.Club
        
        if x == 29:
            x = 0
            y = y +1
        else:
            x = x+1
        if y == 29:
            return Color.Error   
    return Color.Error

def recognize_cards_in_picture(model, picture):

    img_rows = 30
    img_cols = 30
    sample = rgb2gray(picture).reshape(1,img_rows, img_cols, 1)
    result = model.predict(sample)
    y_class = result.argmax()
    if y_class <13 and result[0][y_class] > 0.98:  # classes 0-12 are cards 
        color = get_card_color(picture) 
        return Card(color=color, figure=convert_numer_to_class(y_class))
    return None


def GetPlayerIfInHand(model,picture, rectangle, position):
    img_rows = 30
    img_cols = 30
    result  = None
    cardBack1 = CropImage(picture, rectangle)
    cv2.imwrite("card_back_candidate.png", cardBack1)

    candidates = get_candidateImages(cardBack1) 
    cardbackCount = 0
    for candidate in candidates:
        sample = rgb2gray(candidate).reshape(1,img_rows, img_cols, 1)
        result = model.predict(sample)

        y_class = result.argmax()
        if y_class == 13:
            cardbackCount +=1
    if cardbackCount >=2:
        result = Player(position)
        print(get_string_from_image(cardBack1))
    return result

