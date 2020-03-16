from __future__ import absolute_import
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import h5py
import cv2

import find_convex as fc
from helper_functions import *
import cnn_helper
import TablePositions6Max
import Image_helper
import TableSituation
from PokerDto import Card,Figure,Color

class CardsRecon:

    def __init__(self):
        self.model = cnn_helper.get_model(model_path= "model.json", weights_path="model.h5") #model_path= "model.json", weights_path="model.h5"

    def recognize_cards(self, image):
        candidates = fc.get_candidateImages(image) 
        result = list()
        i =0
        for candidate in candidates:
            # i+=1
            # print("card no",i)
            card  = recognize_cards_in_picture(model=self.model,picture=candidate)
            if card is not None and card.Figure != Figure.Error and card.Color != Color.Error:
                # situation.Hand.append(card)
                result.append(card)
                # print("{0}  {1}".format(card.Figure, card.Color))
        return result

# image = cv2.imread("sample.jpg")
# recon = CardsRecon()
# recon.recognize_cards(image)
