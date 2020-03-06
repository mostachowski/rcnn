import cv2


def CropImage(image, rect):
    # TODO: check if image is not null
    crop_img = image[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]].copy()
    # cv2.imshow("cropped", crop_img)
    return crop_img