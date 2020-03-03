import os,cv2,keras
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import pytesseract


print("hello from selective")

## count  intersection over union
def get_iou(bb1, bb2):
    assert bb1['x1'] < bb1['x2']
    assert bb1['y1'] < bb1['y2']
    assert bb2['x1'] < bb2['x2']
    assert bb2['y1'] < bb2['y2']
    x_left = max(bb1['x1'], bb2['x1'])
    y_top = max(bb1['y1'], bb2['y1'])
    x_right = min(bb1['x2'], bb2['x2'])
    y_bottom = min(bb1['y2'], bb2['y2'])
    if x_right < x_left or y_bottom < y_top:
        return 0.0
    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    bb1_area = (bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1'])
    bb2_area = (bb2['x2'] - bb2['x1']) * (bb2['y2'] - bb2['y1'])
    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
    assert iou >= 0.0
    assert iou <= 1.0
    return iou

def get_candidates(image):
    train_images=[]
    train_labels=[]

    canny  = cv2.Canny(image,100,300)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh = 200
    black_image = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 1
    candindates = list()
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        offset= 1
        if x + w + offset <=canny.shape[1]:
            w= w+offset
        if y + w < canny.shape[0]:
            h = h+offset
        if (x>0):
            x =x-offset
            w = w + offset
        if (y>0):    
            y = y -offset
            h = h + offset
        ratio = h/w
        if w >30 or h >30:
            continue
        
        candidate = np.zeros(shape=[32, 32, 1], dtype=np.uint8)
        crop_img = black_image[y:y+h, x:x+w]
        crop_img = crop_img.reshape(crop_img.shape[0],crop_img.shape[1],1)

        y_offset = int((32 - crop_img.shape[0]) /2)
        x_offset = int((32 - crop_img.shape[1]) /2)
        candidate[y_offset:y_offset+crop_img.shape[0], x_offset:x_offset+crop_img.shape[1]] = crop_img

        name = "rect" + str(i) + ".jpg"
        i = i+1
        cv2.imwrite(name,candidate)


        candindates.append(candidate)
    return candindates


def get_string(img_path):
    # Read image using opencv
    img = cv2.imread(img_path)

    # Extract the file name without the file extension
    file_name = os.path.basename(img_path).split('.')[0]
    file_name = file_name.split()[0]

    # Create a directory for outputs
    output_dir = "output"
    output_path = os.path.join(output_dir, file_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # Rescale the image, if needed.
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # Apply blur to smooth out the edges
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # Apply threshold to get image with only b&w (binarization)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
     # Save the filtered image in the output directory
    save_path = os.path.join(output_path, file_name + "_filter_"  + ".jpg")
    cv2.imwrite(save_path, img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(img,  config='--psm 6')
    return result

def add_offset(s_img):

    h = s_img.shape[0] + 50
    w = s_img.shape[1] + 50

    # s_img = np.expand_dims(s_img,axis=0)
    s_img = s_img.reshape(s_img.shape[0], s_img.shape[1], 1)

    l_img = np.zeros((h,w,1),np.int)
    x_offset=y_offset=25

    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

    return l_img


# add_background()
# generate_data("number_model","numbers_generated")










