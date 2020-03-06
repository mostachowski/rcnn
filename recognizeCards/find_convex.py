import cv2
import numpy as np
import sys
from Image_helper import CropImage

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

            if small_img.shape[0]> 31 or small_img.shape[1]> 31:
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

def ConvertToBlackAndWhite(image):
    # I assume that it is already grayscale.
    #TODO check shape and throw exception if not grayscale
    # grab the image dimensions
    h = image.shape[0]
    w = image.shape[1]
    # loop over the image, pixel by pixel
    for y in range(0, h):
        for x in range(0, w):
            # threshold the pixel
            T = 150
            image[y, x] = 255 if image[y, x] >= T else 0
    return image
    # cv2.imwrite("black_and_white.png", image)

def FindNeighbours(i,j,image,cutted_img):
    if  image[i, j] == 255:

        if cutted_img[i,j] == 255:
            return None
        cutted_img[i,j] = 255
        image[i,j]  = 0
        #go four dircetions
        if i >0:
            FindNeighbours(i-1,j,image,cutted_img)
        if j >0:
            FindNeighbours(i,j-1,image,cutted_img)
        if (i<image.shape[0]):
            FindNeighbours(i+1,j,image,cutted_img)
        if (j<image.shape[1]):
            FindNeighbours(i,j+1,image,cutted_img)
    return cutted_img

def FindMaxLeft(image):
        for y in range(0, image.shape[1]):
            for x in range(0, image.shape[0]):
                if image[x, y] == 255:
                    print("found max left in point: {0},{1}".format(x,y))

                    return y
        return image.shape[0]

def FindMaxTop(image):
        for x in range(0, image.shape[0]):
           for y in range(0, image.shape[1]):    

                if image[x, y] == 255:
                    print("found max top in point: {0},{1}".format(x,y))
                    return x
        return image.shape[1]

def FitIntoSmallImage(img):

    y = FindMaxLeft(img)
    x = FindMaxTop(img)
    cv2.imwrite("found_left_corner{0}-{1}.png".format(x,y),img)
    print("found min x,y={0},{1}".format(x,y))
    res =  CropImage(img, (y,x,20,20))
    print("shape:",res.shape)
    return res
    


# img =cv2.imread("bet.png")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# black = ConvertToBlackAndWhite(gray)
# cv2.imwrite("black.png",black)



# h = black.shape[0]
# w = black.shape[1]
# print(black.shape)


# for y in range(0, h):
#     for x in range(0, w):
#         # threshold the pixel
#         T = 150
#         if black[y, x] == 255:

#             newImage = np.zeros(shape=black.shape)
#             newImage = FindNeighbours(y,x,black,newImage)
#             newImage = FitIntoSmallImage(newImage)
#             name = "cutted{0}{1}.png".format(y,x)
#             cv2.imwrite(name,newImage)
#             break











