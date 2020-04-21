from PokerDto import Decision,Figure,Position,TableAction,Card, HandType,Color, HandPotential,BoardPotential
import TableSituation as t
import itertools

class BoardPotentialEvaluator:

    def is_flush_draw(self, situation = t.TableSituation()):
        new_cards = list()
        hearts = list(filter(lambda x: x.Color == Color.Heart, situation.Board))
        if len(hearts) > len(new_cards):
            new_cards = hearts
        clubs = list(filter(lambda x: x.Color == Color.Club, situation.Board))
        if len(clubs) > len(new_cards):
            new_cards = clubs
        spades = list(filter(lambda x: x.Color == Color.Spade, situation.Board))
        if len(spades) > len(new_cards):
            new_cards = spades
        diamonds = list(filter(lambda x: x.Color == Color.Diamond, situation.Board))
        if len(diamonds) > len(new_cards):
            new_cards = diamonds
        if len(new_cards) == 2:
            return BoardPotential.TwoCardsFlushDraw
        if len(new_cards) == 3:
            return BoardPotential.ThreeCardsFlushDraw
        if len(new_cards) == 4:
            return BoardPotential.FourCardsFlushDraw
        return None

    def is_board_paired(self,situation = t.TableSituation()):

        cards = {}
        for card in situation.Board:
            if card.Figure in cards:
                cards[card.Figure] +=1
            else:
                cards[card.Figure] =1 
       
        for item in cards:
           if cards[item] ==2:
               return True
        return False

    def change_cards_figures_into_numbers(self,cards = list()):
        cards_numbers = list()
        for card in cards:
            cards_numbers.append(card.Figure.value)
            if card.Figure == Figure.Ace:
                cards_numbers.append(-1)
            cards_numbers.append(card.Figure.value)
        cards_numbers.sort()
        return cards_numbers

    def is_straight_draw(self,situation = t.TableSituation()):
        numbers = self.change_cards_figures_into_numbers(situation.Board)
        number_chain = ""
        for x in range(1, len(numbers)):
            diff = abs(numbers[x] - numbers[x-1])
            if diff ==0:
                continue
            number_chain = number_chain + str(diff)
        if "111" in number_chain:
            return BoardPotential.StraightFourInTheRow
        # gutshot needs one of chains: 211, 121, 112, 
        if "211" in number_chain or "121" in number_chain or "112" in number_chain:
            return BoardPotential.StraightOneGap
        if "11" in number_chain:
            return BoardPotential.StraightThreeInARow
        # if "12" in number_chain or "21" in number_chain:
        #     return BoardPotential.   
        if "1" in number_chain:
            return BoardPotential.StraightDrawTwoInTheRow
        return None 