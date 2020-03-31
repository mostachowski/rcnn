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
        if w>50 and h >50:
            w = 30
            h = 30
            x = x+1
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
            # cv2.imwrite(str(idx) + 'RESIZEDxxxx.png', small_img)
            # cv2.imwrite(str(idx) + 'BIGxxxx.png', big_img)
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

def get_candidates(image):
    train_images=[]
    train_labels=[]

    canny  = cv2.Canny(image,100,300)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh = 200
    black_image = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]
    _,contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    boundingBoxes= [cv2.boundingRect(c) for c in contours]
    
    boundingBoxes =sorted(boundingBoxes, key=lambda x: x[0])

    i = 1
    candindates = list()
    boundingBoxesCandidates = list()
    for (x,y,w,h) in boundingBoxes:
        if shapeInsideOther((x,y,w,h), boundingBoxesCandidates):
            continue
        boundingBoxesCandidates.append((x,y,w,h))
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
            print("boundinboxes in progress")
        candidate = np.zeros(shape=[30, 30, 1], dtype=np.uint8)
        crop_img = black_image[y:y+h, x:x+w]
        crop_img = crop_img.reshape(crop_img.shape[0],crop_img.shape[1],1)

        y_offset = int((30 - crop_img.shape[0]) /2)
        x_offset = int((30 - crop_img.shape[1]) /2)
        candidate[y_offset:y_offset+crop_img.shape[0], x_offset:x_offset+crop_img.shape[1]] = crop_img

        name = "rect" + str(i) + ".jpg"
        i = i+1
        cv2.imwrite(name,candidate)


        candindates.append(candidate)
    return candindates

def shapeInsideOther(contour, boundingBoxesCandidates):
    x= contour[0]
    y = contour[1]
    w=contour[2]
    h=contour[3]
    for (x_1,y_1,w_1,h_1) in boundingBoxesCandidates:
        if (x_1 <=x and y_1 <=y and (w_1+x_1) >=(w+x) and (h_1+y_1)>=(h+y)):
            return True
    return False