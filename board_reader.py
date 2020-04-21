import cv2
import sys
sys.path.append('recognizeCards')
sys.path.append('recognizeNumbers')
import recognize_cards as rc
import recognize_numbers as rn
import TablePositions6Max as positions
from Image_helper import CropImage
import TableSituation
from helper_functions import GetPlayerIfInHand,get_string_from_image
import find_convex as fc
from helper_functions import get_string_from_image

# sys.path.append('recognizeCards')

class BoardReader:
    def __init__(self):
        self.card_recognizer = rc.CardsRecon()
        self.number_recognizer = rn.number_recognizer()

        self.hands = {}

    def get_hand_number(self, screen):

        rect = positions.TablePositions6Max.HandNumberRect
        image = CropImage(screen,rect)
        # bet = self.number_recognizer.getNumber(image = image)
        bet = get_string_from_image(image)
        bet = bet[1:]
        bet = bet.replace(" ","")
        return bet

    def _get_situation(self, hand_number):
        if hand_number in self.hands:
            return self.hands[hand_number]
        situation = TableSituation.TableSituation()
        self.hands[hand_number] = situation
        return situation

    def get_board(self,screen):

        hand_number = self.get_hand_number(screen)

        situation = self._get_situation(hand_number)
        #1 read cards on the board

        board_rect = positions.TablePositions6Max.BoardCardsRect
        # image = cv2.imread("sample.jpg")
        board = CropImage(screen,board_rect)
        # cv2.imwrite("candidate.jpg",board)
        cards = self.card_recognizer.recognize_cards(board)
        for card in cards:
            print("{0}  {1}".format(card.Figure, card.Color))
        situation.set_board(cards)

        #2 Read hero cards if needed
        if len(situation.Hand) == 0:
            rect = positions.TablePositions6Max.HeroCardsRect
            hero_cards_image = CropImage(screen,rect)
            cv2.imwrite("hero.jpg",hero_cards_image)
            situation.set_hand(self.card_recognizer.recognize_cards(hero_cards_image))



        # #3 read pot  (not sure if needed... maybe just increment pot in add_action method)
        # pot_rect = positions.TablePositions6Max.PotRect
        # pot_image = CropImage(screen,pot_rect)
        # cv2.imwrite("pot_candidate.jpg",pot_image)
        # situation.Pot = self.number_recognizer.getNumber(pot_image)
        # print("pot: ",situation.Pot)

        #4 read button position
        situation.ButtonPosition = self.get_button(screen)

        #5 read actions 
        player = GetPlayerIfInHand(self.card_recognizer.model,screen, positions.TablePositions6Max.CardBack1Rect,1)
        if  player is not None:
            situation.PlayersInPlay.append(player)

            rect = positions.TablePositions6Max.Position1BetRect
            image = CropImage(screen,rect)
            bet = self.number_recognizer.getNumber(image = image)
            # cv2.imwrite("pot1.jpg",image)
            # print("bet1: ",bet)
            if bet != None:
                situation.add_action(player_number = 1, bet = bet)

        player = GetPlayerIfInHand(self.card_recognizer.model,screen, positions.TablePositions6Max.CardBack2Rect,2)
        if  player is not None:
            situation.PlayersInPlay.append(player)

            rect = positions.TablePositions6Max.Position2BetRect
            image = CropImage(screen,rect)
            bet = self.number_recognizer.getNumber(image = image)
            # cv2.imwrite("pot2.jpg",image)
            # print("bet2: ",bet)
            if bet != None:
                situation.add_action(player_number = 2, bet = bet)

        player = GetPlayerIfInHand(self.card_recognizer.model,screen, positions.TablePositions6Max.CardBack3Rect,3)
        if  player is not None:
            situation.PlayersInPlay.append(player)

            rect = positions.TablePositions6Max.Position3BetRect
            image = CropImage(screen,rect)
            bet = self.number_recognizer.getNumber(image= image)
            
            # cv2.imwrite("pot3.jpg",image)
            # print("bet3: ",bet)
            if bet != None:
                situation.add_action(player_number = 3, bet = bet)

        player = GetPlayerIfInHand(self.card_recognizer.model,screen, positions.TablePositions6Max.CardBack4Rect,4)
        if  player is not None:
            situation.PlayersInPlay.append(player)

            rect = positions.TablePositions6Max.Position4BetRect
            bet = self.number_recognizer.getNumber(image = CropImage(screen,rect))
            # print("bet4: ",bet)
            if bet != None:
                situation.add_action(player_number = 4, bet = bet)

        player = GetPlayerIfInHand(self.card_recognizer.model, screen, positions.TablePositions6Max.CardBack5Rect,5)
        if  player is not None:
            situation.PlayersInPlay.append(player)

            rect = positions.TablePositions6Max.Position5BetRect
            bet = self.number_recognizer.getNumber(image = CropImage(screen,rect))

            # print("bet5: ",bet)
            if bet != None:
                situation.add_action(player_number = 5, bet = bet)


        return situation


    def get_button(self,screen):
        button_candidate =  CropImage(screen,positions.TablePositions6Max.Button1)
        res = self.card_recognizer.get_classess_from_image(button_candidate)
        if any(x == 14 for x in res):
            return 1
        button_candidate =  CropImage(screen,positions.TablePositions6Max.Button2)
        res = self.card_recognizer.get_classess_from_image(button_candidate)
        if any(x == 14 for x in res):
            return 2
        button_candidate =  CropImage(screen,positions.TablePositions6Max.Button3)
        res = self.card_recognizer.get_classess_from_image(button_candidate)
        if any(x == 14 for x in res):
            return 3
        button_candidate =  CropImage(screen,positions.TablePositions6Max.Button4)
        res = self.card_recognizer.get_classess_from_image(button_candidate)
        if any(x == 14 for x in res):
            return 4
        button_candidate =  CropImage(screen,positions.TablePositions6Max.Button5)
        res = self.card_recognizer.get_classess_from_image(button_candidate)
        if any(x == 14 for x in res):
            return 5
        button_candidate =  CropImage(screen,positions.TablePositions6Max.Button6)
        res = self.card_recognizer.get_classess_from_image(button_candidate)
        if any(x == 14 for x in res):
            return 6
        
    def resize_if_needed(self, screen):
        dsize = (positions.TablePositions6Max.Width,positions.TablePositions6Max.Height)
        return cv2.resize(screen,dsize)
            
    def is_hero_acting(self, screen):
        candidate =  CropImage(screen,positions.TablePositions6Max.FoldButton)
        return get_string_from_image(candidate).lower() == "fold"


# image = cv2.imread("sample9.jpg")
# recon = BoardReader()
# if recon.is_hero_acting(screen = image):
#     print("ready to act")
# else:
#     print("not ready")
# image = recon.resize_if_needed(screen=image)
# cv2.imwrite("resized.jpg",image)
# print("button pos: ",recon.get_button(screen=image))
# recon.get_board(screen = image)
# # fc.get_candidates(img= image)

if __name__ == "__main__":
    image = cv2.imread("resized.jpg")
    recon = BoardReader()  
    recon.get_hand_number(image) 
