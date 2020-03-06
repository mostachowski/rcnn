import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import h5py
import cv2

from find_convex import get_candidateImages
from helper_functions import getData, rgb2gray, recognize_cards_in_picture, GetPlayerIfInHand, get_string_from_image
from cnn_helper import get_model, train_model

import TablePositions6Max
from Image_helper import CropImage
from TableSituation import TableSituation
from PokerDto import *


def recognize_cards(image):
    #Define the model
    model = get_model(model_path="model.json", weights_path="model.h5") #model_path= "model.json", weights_path="model.h5"

    # situation = TableSituation()

    # player = GetPlayerIfInHand(model,image, TablePositions6Max.TablePositions6Max.CardBack1Rect,1)
    # if  player is not None:
    #     situation.PlayersInPlay.append(player)
    # player = GetPlayerIfInHand(model,image, TablePositions6Max.TablePositions6Max.CardBack2Rect,2)
    # if  player is not None:
    #     situation.PlayersInPlay.append(player)
    # player = GetPlayerIfInHand(model,image, TablePositions6Max.TablePositions6Max.CardBack3Rect,3)
    # if  player is not None:
    #     situation.PlayersInPlay.append(player)
    # player = GetPlayerIfInHand(model,image, TablePositions6Max.TablePositions6Max.CardBack4Rect,4)
    # if  player is not None:
    #     situation.PlayersInPlay.append(player)
    # player = GetPlayerIfInHand(model,image, TablePositions6Max.TablePositions6Max.CardBack5Rect,5)
    # if  player is not None:
    #     situation.PlayersInPlay.append(player)

    # print(len(situation.PlayersInPlay))
    # candidates = get_candidateImages(image) 

    candidates = get_candidateImages(image) 
    result = list()
    for candidate in candidates:
        card  = recognize_cards_in_picture(model=model,picture=candidate)
        if card is not None and card.Figure != Figure.Error and card.Color != Color.Error:
            # situation.Hand.append(card)
            result.append(card)
            print("{0}  {1}".format(card.Figure, card.Color))
    return result







