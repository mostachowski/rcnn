import cv2
import sys
sys.path.append('recognizeCards')
import recognize_cards as rc
import TablePositions6Max as positions
from Image_helper import CropImage
import TableSituation
from helper_functions import GetPlayerIfInHand

# sys.path.append('recognizeCards')

class CardsRecon:
    def __init__(self):
        self.card_recognizer = rc.CardsRecon()

    def get_board(self,screen):
        board_rect = positions.TablePositions6Max.BoardCardsRect
        # image = cv2.imread("sample.jpg")
        board = CropImage(screen,board_rect)
        # cv2.imwrite("candidate.jpg",board)
        # print(board.shape)
        cards = self.card_recognizer.recognize_cards(board)
        for card in cards:
            print("{0}  {1}".format(card.Figure, card.Color))

        situation = TableSituation.TableSituation()

        player = GetPlayerIfInHand(self.card_recognizer.model,screen, positions.TablePositions6Max.CardBack1Rect,1)
        if  player is not None:
            situation.PlayersInPlay.append(player)
        player = GetPlayerIfInHand(self.card_recognizer.model,screen, positions.TablePositions6Max.CardBack2Rect,2)
        if  player is not None:
            situation.PlayersInPlay.append(player)
        player = GetPlayerIfInHand(self.card_recognizer.model,screen, positions.TablePositions6Max.CardBack3Rect,3)
        if  player is not None:
            situation.PlayersInPlay.append(player)
        player = GetPlayerIfInHand(self.card_recognizer.model,screen, positions.TablePositions6Max.CardBack4Rect,4)
        if  player is not None:
            situation.PlayersInPlay.append(player)
        player = GetPlayerIfInHand(self.card_recognizer.model, screen, positions.TablePositions6Max.CardBack5Rect,5)
        if  player is not None:
            situation.PlayersInPlay.append(player)
        print(situation.PlayersInPlay)

image = cv2.imread("sample.jpg")
recon = CardsRecon()
recon.get_board(screen = image)