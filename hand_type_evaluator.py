from PokerDto import Decision,Figure,Position,TableAction,Card, HandType,Color
import TableSituation as t
import itertools


class HandTypeEvaluator:
    def get_hand_type(self, situation = t.TableSituation()):

        result = list()
        board = sorted(situation.Board,key=lambda x: x.Figure.value, reverse=True)

        #Pair in hand
        if situation.Hand[0].Figure == situation.Hand[1].Figure:
            if situation.Hand[0].Figure == Figure.Ace:
                result.append(HandType.OverPair)
            else:
                heroCard = int(situation.Hand[0].Figure)
                if heroCard > int(board[0].Figure):
                    result.append(HandType.OverPair)

                if heroCard > int(board[1].Figure):
                
                    result.append(HandType.SecondPair)
                
                if heroCard > int(board[2]).Figure:
                    result.append(HandType.ThirdPair)
                if len(board) >3 and heroCard >  int(board[3]).Figure:
                    result.append(HandType.FourthPair)
                if len(board) >4 and heroCard >  int(board[4]).Figure:
                    result.append(HandType.FifthPair)
                else:
                    if len(board) >4:
                        result.append(HandType.SixthPair)    
        
    def is_highest_available(self,heroCard = Figure.Ace, cardlist = list()):
        if heroCard == Figure.Ace:
            return True
        if heroCard == Figure.King:
            if cardlist[0].Figure == Figure.Ace:
                return True
        if heroCard == Figure.Queen:
            if cardlist[0].Figure == Figure.Ace and cardlist[1].Figure == Figure.King:
                return True
        if heroCard == Figure.Jack:
            if cardlist[0].Figure == Figure.Ace and cardlist[1].Figure == Figure.King and cardlist[2].Figure == Figure.Queen:
                return True
        return False


    def has_pair(self,situation=t.TableSituation()):
        board = sorted(situation.Board,key=lambda x: x.Figure.value, reverse=True)

        item = next((x for x in board if x.Figure == situation.Hand[0].Figure or x.Figure == situation.Hand[1].Figure),None)
        #TODO it doesnt work good when paired board
        if item != None:
            index  = board.index(item)
            if index == 0: 
                return HandType.TopPair
            if index == 1: 
                return HandType.SecondPair
            if index == 2: 
                return HandType.ThirdPair
            if index == 3: 
                return HandType.FourthPair
            if index == 4: 
                return HandType.FifthPair
        return None

    def has_two_pairs(self,situation=t.TableSituation()):
        board = sorted(situation.Board,key=lambda x: x.Figure.value, reverse=True)
        pair1 = next((x for x in board if x.Figure == situation.Hand[0].Figure),(None))
        pair2 = next((x for x in board if x.Figure == situation.Hand[1].Figure),(None))
        if (pair1 != None and pair2 != None):
            index1 = board.index(pair1)
            index2 = board.index(pair2)
            if index1 == 0 or index2 == 0:
                return HandType.TwoPairsWithTop
            return HandType.TwoPairsWithoutTop
        return None

    def has_3_of_the_kind(self,situation=t.TableSituation()):
        cards = situation.Hand
        cards = cards + situation.Board
        sum1 = sum(1 for x in cards if x.Figure == situation.Hand[0].Figure)
        sum2 = sum(1 for x in cards if x.Figure == situation.Hand[1].Figure)
        if sum1== 3 or sum2 == 3:
            if situation.Hand[0].Figure == situation.Hand[1].Figure:
                return HandType.Set
            return HandType.Trips
        return None

    def has_4_of_the_kind(self,situation=t.TableSituation()):
        cards = situation.Hand
        cards = cards + situation.Board
        cards = sorted(cards,key=lambda x: x.Figure.value,reverse=True)
        card_count = {}
        for  card in cards:
            if card.Figure.value in card_count:
                card_count[card.Figure.value] +=1
            else:
                 card_count[card.Figure.value] = 1
        for key,value in card_count.items():
            if value == 4:
                if key == situation.Hand[0].Figure.value or key == situation.Hand[1].Figure.value:
                    return HandType.FourOfKind
                return HandType.FourOfTheKindOnBoard
        return None

    def has_fullhouse(self,situation = t.TableSituation()):
        cards = situation.Hand
        cards = cards + situation.Board
        cards = sorted(cards,key=lambda x: x.Figure.value,reverse=True)
        card_count = {}
        for  card in cards:
            if card.Figure.value in card_count:
                card_count[card.Figure.value] +=1
            else:
                 card_count[card.Figure.value] = 1
        item_3 = next((x for x in card_count if card_count[x] == 3),None)
        item_2 = next((x for x in card_count if card_count[x] == 2),None)

        if item_3 == None or item_2 == None:
            return None
        
        if situation.Hand[0].Figure.value != item_3 and situation.Hand[1].Figure.value != item_3 and situation.Hand[0].Figure.value != item_2 and situation.Hand[1].Figure.value != item_2:
            return HandType.FullHouseOnBoard
        #TODO check if there are stronger full posiibilities
        
        return HandType.FullHouse

    def has_flush(self, situation = t.TableSituation()):
        cards = situation.Hand
        cards = cards + situation.Board
        sum1 = sum(1 for x in cards if x.Color == situation.Hand[0].Color)
        sum2 = sum(1 for x in cards if x.Color == situation.Hand[1].Color)
        
        if sum1 == 5 or sum2 == 5:
            if situation.Hand[0].Color == situation.Hand[1].Color:
                return HandType.Flush
            if sum1 >= sum2:
                color_cards = list(itertools.takewhile(lambda c: c.Color == situation.Hand[0].Color, cards))
                color_cards = sorted(color_cards,key=lambda x: x.Figure.value, reverse=True)
                if self.is_highest_available(situation.Hand[0].Figure,color_cards):
                    return HandType.NutsFlushWithFourBoardCards
                return HandType.NotNutsFlushWithFourBoardCards
            else:
                color_cards = list(itertools.takewhile(lambda c: c.Color == situation.Hand[1].Color, cards))
                color_cards = sorted(color_cards,key=lambda x: x.Figure.value, reverse=True)
                if self.is_highest_available(situation.Hand[1].Figure,color_cards):
                    return HandType.NutsFlushWithFourBoardCards
                return HandType.NotNutsFlushWithFourBoardCards
       
        if sum1 >5 or sum2 >5:
            card = None
            color_cards = list()
            if situation.Hand[0].Color == situation.Hand[1].Color:
                card = situation.Hand[0]
            if sum1 >= sum2:
                color_cards = list(itertools.takewhile(lambda c: c.Color == situation.Hand[0].Color, cards))
                color_cards = sorted(color_cards,key=lambda x: x.Figure.value, reverse=True)
                card = situation.Hand[0]
            else:
                color_cards = list(itertools.takewhile(lambda c: c.Color == situation.Hand[1].Color, cards))
                color_cards = sorted(color_cards,key=lambda x: x.Figure.value, reverse=True)
                card = situation.Hand[1]
            if self.is_highest_available(card,color_cards):
                return HandType.NutsFlushWithFourBoardCards
            color_cards = list(itertools.takewhile(lambda c: c.Color == card.Color, situation.Board))
            color_cards = sorted(color_cards,key=lambda x: x.Figure.value, reverse=False)
            print ("card.figure: ",card.Figure)
            print("board figure: ",color_cards[0].Figure)
            if card.Figure.value >color_cards[0].Figure.value:
                return HandType.NotNutsFlushWithFourBoardCards
            

        return None

    #return length of chain and the highest from chain
    def how_many_to_straight(self, int_list = list()):
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

    def has_straight(self, situation = t.TableSituation()):
        straight_candidate_cards = list()
        cards_numbers = list()
        cards = situation.Board
        for card in cards:
            cards_numbers.append(card.Figure.value)
            if card.Figure == Figure.Ace:
                cards_numbers.append(-1)
            cards_numbers.append(card.Figure.value)
        cards_numbers.sort()
        
        counter,highest_card = self.how_many_to_straight(cards_numbers)
        # if counter == 2:
        #     return None
        cards_numbers.append(situation.Hand[0].Figure.value)
        cards_numbers.append(situation.Hand[1].Figure.value)
        cards_numbers.sort()
        new_counter, new_highest_card = self.how_many_to_straight(cards_numbers)
        if counter <4 and new_counter == 5:
            return HandType.Straight
        if counter == 4 and new_counter >4:
            if(new_highest_card> highest_card):
                return HandType.Straight
            return HandType.Straight_from_bottom
        if counter >4:
            if new_highest_card > highest_card:
                return HandType.Straight
            return HandType.StraightOnBoard
        return None

    def has_flush_straight(self, situation = t.TableSituation()):
        flush = self.has_flush(situation=situation)
        if flush == None:
           return None
        cards = situation.Board
        cards.append(situation.Hand[0])
        cards.append(situation.Hand[1])
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
        
        cards_numbers = list()
        for card in new_cards:
            cards_numbers.append(card.Figure.value)
            if card.Figure == Figure.Ace:
                cards_numbers.append(-1)
            cards_numbers.append(card.Figure.value)
        cards_numbers.sort()

        counter, highest = self.how_many_to_straight(cards_numbers)
        if counter >4:
            return HandType.StraightFlush
        return None
