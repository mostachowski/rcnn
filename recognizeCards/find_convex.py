import cv2
import numpy as np
import sys

def get_candidateImages(img):
    result = list()
    # convert image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray = read_file_as_numpy(file_path)
        
    # blur the image
    blur = cv2.blur(gray, (3, 3))

    # binary thresholding of the image
    ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)

    # find contours
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, \
            cv2.CHAIN_APPROX_SIMPLE)

    idx =0
    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        if w>3 and h>3:
            idx+=1
            big_img = np.ones((30,30,3),np.uint8) * 255

            small_img=img[y:y+h,x:x+w]
            # small_img = small_img[:, :, newaxis]

            x_offset=y_offset=0

            if small_img.shape[0]> 30 or small_img.shape[1]> 30:
                if (small_img.shape[0]>small_img.shape[1]):
                    small_img = image_resize(small_img, height=30)
                else:
                   small_img = image_resize(small_img, width=30)

            big_img = np.ones((30,30,3),np.uint8) * 255
            big_img[y_offset:0+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img
            # cv2.imwrite(str(idx) + 'xxxx.png', big_img)
            result.append(big_img)

    return result

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized
