from PokerDto import Decision,Figure,Position,TableAction,Card, HandType,Color, HandPotential,BoardPotential
import TableSituation as t
import itertools

class HandPotentialEvaluator:

# TODO: code copied from hand_type_evaluator. should use the same not a copu

    def how_many_to_straight(self, int_list = list()):
        """
        how_many_to_straight(self, int_list = list())

        return length of chain and the highest from chain

        """
      
      
        if len(int_list)== 0:
            return 0
        int_list.sort()
        counter = 1
        old_longest_counter = 0
        highest_card= 0
        for x in range(1, len(int_list)):
            diff = abs(int_list[x] - int_list[x-1])
            if diff ==0:
                continue
            if diff ==1:
                counter+=1
                if old_longest_counter <counter:
                    old_longest_counter = counter
                    highest_card = int_list[x]
            else:
                if old_longest_counter <counter:
                    old_longest_counter = counter
                    highest_card = int_list[x-1]
                    counter = 1
        return (old_longest_counter,highest_card)

    def change_cards_figures_into_numbers(self,cards = list()):
        cards_numbers = list()
        for card in cards:
            cards_numbers.append(card.Figure.value)
            if card.Figure == Figure.Ace:
                cards_numbers.append(-1)
            cards_numbers.append(card.Figure.value)
        cards_numbers.sort()
        return cards_numbers

    def find_nth_overlapping(self, haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+1)
            n -= 1
        return start

    def check_gutshot_chain(self,numbers = list()):

        number_chain = ""
        for x in range(1, len(numbers)):
            diff = abs(numbers[x] - numbers[x-1])
            if diff ==0:
                continue
            number_chain = number_chain + str(diff)
     
        # gutshot needs one of chains: 211, 121, 112
        if "211" in number_chain or "121" in number_chain or "112" in number_chain:
            return HandPotential.Gutshot    
        return None    

    def has_gutshot(self, situation = t.TableSituation()):
        board_numbers = self.change_cards_figures_into_numbers(situation.Board)
        cards_numbers =  self.change_cards_figures_into_numbers(situation.Board + situation.Hand)
        
        if self.check_gutshot_chain(board_numbers) == None:
            return self.check_gutshot_chain(cards_numbers)
        # gutshot on board we should check if we dont have higher gutshot...
        return None

    def has_openended(self, situation = t.TableSituation()):
        board_numbers = self.change_cards_figures_into_numbers(situation.Board)
        cards_numbers = self.change_cards_figures_into_numbers(situation.Board + situation.Hand)    
        board_chain_count,board_highest = self.how_many_to_straight(board_numbers)
        cards_chain_count,cards_highest = self.how_many_to_straight(cards_numbers)
        if board_chain_count == 4:
            return None
        if board_chain_count <4 and cards_chain_count ==4:
            #TODO: should recognize openended from bottom...
            return HandPotential.OpenEnded
        return None

    def has_flush_draw(self, situation = t.TableSituation()):
        board_draw = self.get_color_length(situation.Board)
        hand_draw =  self.get_color_length(situation.Board + situation.Hand)
        if hand_draw ==4:
            return board_draw != hand_draw
        return False
        


    def get_color_length(self,cards = list()):
        new_cards = list()
        hearts = list(filter(lambda x: x.Color == Color.Heart, cards))
        if len(hearts) > len(new_cards):
            new_cards = hearts
        clubs = list(filter(lambda x: x.Color == Color.Club, cards))
        if len(clubs) > len(new_cards):
            new_cards = clubs
        spades = list(filter(lambda x: x.Color == Color.Spade, cards))
        if len(spades) > len(new_cards):
            new_cards = spades
        diamonds = list(filter(lambda x: x.Color == Color.Diamond, cards))
        if len(diamonds) > len(new_cards):
            new_cards = diamonds
        return len(new_cards)

