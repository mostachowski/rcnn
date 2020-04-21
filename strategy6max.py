from PokerDto import Decision,Figure,Position,TableAction,HandType,BoardPotential,DecisionClass,BetType
import TableSituation
import hand_type_evaluator as h
import hand_potential_evaluator as p
import board_potential_evaluator as b
import random


#results are in tuples: (figure,figure,Is suited,percentage)
def get_hands_to_open_from_utg():
    result = list()

    result.append((Figure.Ace,Figure.Ace,False,1))
    result.append((Figure.King,Figure.King,False,1))
    result.append((Figure.Queen,Figure.Queen,False,1))
    result.append((Figure.Jack,Figure.Jack,False,1))
    result.append((Figure.Ten,Figure.Ten,False,1))
    result.append((Figure.Nine,Figure.Nine,False,1))
    result.append((Figure.Eight,Figure.Eight,False,1))
    result.append((Figure.Seven,Figure.Seven,False,1))
    result.append((Figure.Six,Figure.Six,False,1))
    result.append((Figure.Five,Figure.Five,False,1))
    result.append((Figure.Four,Figure.Four,False,1))
    result.append((Figure.Three,Figure.Three,False,1))
    result.append((Figure.Two,Figure.Two,False,1))

    result.append((Figure.Ace,Figure.King,True,1))
    result.append((Figure.Ace,Figure.King,False,1))
    result.append((Figure.Ace,Figure.Queen,True,1))
    result.append((Figure.Ace,Figure.Queen,False,1))
    result.append((Figure.Ace,Figure.Jack,True,1))
    result.append((Figure.Ace,Figure.Jack,False,1))
    result.append((Figure.Ace,Figure.Ten,True,1))
    result.append((Figure.Ace,Figure.Five,True,1))
    result.append((Figure.Ace,Figure.Four,True,1))
    result.append((Figure.Ace,Figure.Three,True,1))
    result.append((Figure.Ace,Figure.Two,True,1))
    result.append((Figure.King,Figure.Queen,True,1))
    result.append((Figure.King,Figure.Queen,False,1))
    return result

def get_hands_to_open_from_hj():
    result = get_hands_to_open_from_utg()
    result.append((Figure.Ace,Figure.Ten,False,1))
    result.append((Figure.Ace,Figure.Nine,True,1))
    result.append((Figure.Ace,Figure.Nine,False,1))
    result.append((Figure.Ace,Figure.Eight,True,1))
    result.append((Figure.King,Figure.Jack,True,1))
    result.append((Figure.King,Figure.Jack,False,1))
    return result


def get_hands_to_open_from_co():
    result = get_hands_to_open_from_hj()
    result.append((Figure.Ace,Figure.Eight,False,1))
    result.append((Figure.Ace,Figure.Seven,True,1))
    result.append((Figure.Ace,Figure.Six,True,1))
    result.append((Figure.King,Figure.Ten,True,1))
    result.append((Figure.King,Figure.Ten,False,1))
    result.append((Figure.Queen,Figure.Jack,True,1))
    result.append((Figure.Queen,Figure.Jack,False,1))
    result.append((Figure.Queen,Figure.Ten,True,1))
    result.append((Figure.Queen,Figure.Ten,False,1))
    result.append((Figure.Jack,Figure.Ten,True,1))
    result.append((Figure.Jack,Figure.Nine,True,1))
    result.append((Figure.Jack,Figure.Eight,True,1))

    result.append((Figure.Jack,Figure.Three,True,1))   #for testing. To be removed!

    result.append((Figure.Ten,Figure.Nine,True,1))
    result.append((Figure.Nine,Figure.Eight,True,1))
    result.append((Figure.Nine,Figure.Seven,True,1))
    result.append((Figure.Eight,Figure.Seven,True,1))
    result.append((Figure.Seven,Figure.Six,True,1))
    result.append((Figure.Seven,Figure.Five,True,1))
    result.append((Figure.Six,Figure.Five,True,1))
    return result

def get_hands_to_open_from_button():
    result = get_hands_to_open_from_co()

    result.append((Figure.Ace,Figure.Seven,False,1))
    result.append((Figure.Ace,Figure.Six,False,1))
    result.append((Figure.Ace,Figure.Five,False,1))
    result.append((Figure.Ace,Figure.Four,False,1))
    result.append((Figure.Ace,Figure.Three,False,1))
    result.append((Figure.Ace,Figure.Two,False,1))

    result.append((Figure.King,Figure.Nine,True,1))
    result.append((Figure.King,Figure.Nine,False,1))
    result.append((Figure.King,Figure.Eight,True,1))
    result.append((Figure.King,Figure.Eight,False,1))
    result.append((Figure.King,Figure.Seven,True,1))
    result.append((Figure.King,Figure.Seven,False,1))
    result.append((Figure.King,Figure.Six,True,1))
    result.append((Figure.King,Figure.Five,True,1))

    result.append((Figure.Queen,Figure.Nine,True,1))
    result.append((Figure.Queen,Figure.Eight,True,1))
    result.append((Figure.Queen,Figure.Seven,True,1))
    result.append((Figure.Jack,Figure.Nine,False,1))
    result.append((Figure.Jack,Figure.Seven,True,1))

    result.append((Figure.Ten,Figure.Nine,False,1))  
    result.append((Figure.Ten,Figure.Eight,False,1))  
    result.append((Figure.Ten,Figure.Seven,True,1))  
    result.append((Figure.Ten,Figure.Six,True,1)) 
    result.append((Figure.Nine,Figure.Eight,False,1)) 
    result.append((Figure.Nine,Figure.Seven,False,1)) 
    result.append((Figure.Eight,Figure.Seven,False,1)) 
    result.append((Figure.Seven,Figure.Six,False,1)) 
    return result

def get_hands_to_open_from_sb():
    result = get_hands_to_open_from_hj()
    return result

def get_hands_to_open_from_bb():
    result = get_hands_to_open_from_hj()
    return result

def get_hands_to_3bet_preflop():
    result = list()
    result.append((Figure.Ace,Figure.Ace,False,1))
    result.append((Figure.King,Figure.King,False,1))
    result.append((Figure.Queen,Figure.Queen,False,1))
    result.append((Figure.Jack,Figure.Jack,False,1))
    result.append((Figure.Ten,Figure.Ten,False,1))

    result.append((Figure.Ace,Figure.King,True,1))
    result.append((Figure.Ace,Figure.King,False,1))
    result.append((Figure.Ace,Figure.Queen,True,1))
    result.append((Figure.Ace,Figure.Queen,False,1))
    result.append((Figure.Ace,Figure.Jack,True,1))
    result.append((Figure.Ace,Figure.Jack,False,1))
    result.append((Figure.King,Figure.Queen,True,1))
    return result

def get_hands_to_4bet_preflop():
    result = list()
    result.append((Figure.Ace,Figure.Ace,False,0.7))
    result.append((Figure.King,Figure.King,False,0.7))
    result.append((Figure.Queen,Figure.Queen,False,0.8))

    result.append((Figure.Ace,Figure.King,True,0.4))
    result.append((Figure.Ace,Figure.King,False,0.2))
    result.append((Figure.King,Figure.Queen,True,0.2))
    return result

def get_hands_to_5bet_preflop():
    result = list()
    result.append((Figure.Ace,Figure.Ace,False,0.7))
    result.append((Figure.King,Figure.King,False,0.7))
    result.append((Figure.Queen,Figure.Queen,False,0.5))
    result.append((Figure.Ace,Figure.King,True,0.4))
    return result

def should_call_open_from_utg(situation = TableSituation.TableSituation()):
    return list()

def should_call_open_from_hj(situation = TableSituation.TableSituation()):
    result = list()
    result.append((Figure.Nine,Figure.Nine,False,1))
    result.append((Figure.Eight,Figure.Eight,False,1))
    result.append((Figure.Seven,Figure.Seven,False,1))
    result.append((Figure.Six,Figure.Six,False,1))
    result.append((Figure.Five,Figure.Five,False,1))
    result.append((Figure.Four,Figure.Four,False,1))
    result.append((Figure.Three,Figure.Three,False,1))
    result.append((Figure.Two,Figure.Two,False,1))

    return result

def should_call_open_from_co(situation = TableSituation.TableSituation()):
    result = list()
    result.append((Figure.Nine,Figure.Nine,False,1))
    result.append((Figure.Eight,Figure.Eight,False,1))
    result.append((Figure.Seven,Figure.Seven,False,1))
    result.append((Figure.Six,Figure.Six,False,1))
    result.append((Figure.Five,Figure.Five,False,1))
    result.append((Figure.Four,Figure.Four,False,1))
    result.append((Figure.Three,Figure.Three,False,1))
    result.append((Figure.Two,Figure.Two,False,1))

    result.append((Figure.King,Figure.Queen,False,1))
    result.append((Figure.Queen,Figure.Jack,True,1))

    return result    

def should_call_open_from_bu(situation = TableSituation.TableSituation()):
    result = list()
    result.append((Figure.Nine,Figure.Nine,False,1))
    result.append((Figure.Eight,Figure.Eight,False,1))
    result.append((Figure.Seven,Figure.Seven,False,1))
    result.append((Figure.Six,Figure.Six,False,1))
    result.append((Figure.Five,Figure.Five,False,1))
    result.append((Figure.Four,Figure.Four,False,1))
    result.append((Figure.Three,Figure.Three,False,1))
    result.append((Figure.Two,Figure.Two,False,1))

    result.append((Figure.King,Figure.Queen,False,1))
    result.append((Figure.Queen,Figure.Jack,True,1))
    result.append((Figure.Jack,Figure.Ten,True,1))
    result.append((Figure.Ten,Figure.Nine,True,1))

    return result     

def should_call_open_from_sb(situation = TableSituation.TableSituation()):
    result = list()
    result.append((Figure.Nine,Figure.Nine,False,1))
    result.append((Figure.Eight,Figure.Eight,False,1))
    result.append((Figure.Seven,Figure.Seven,False,1))
    result.append((Figure.Six,Figure.Six,False,1))
    result.append((Figure.Five,Figure.Five,False,1))
    result.append((Figure.Four,Figure.Four,False,1))
    result.append((Figure.Three,Figure.Three,False,1))
    result.append((Figure.Two,Figure.Two,False,1))

    result.append((Figure.King,Figure.Queen,False,1))
    result.append((Figure.Queen,Figure.Jack,True,1))

    return result    

def should_call_open_from_bb(situation = TableSituation.TableSituation()):
   
    result = list()
    result.append((Figure.Nine,Figure.Nine,False,1))
    result.append((Figure.Eight,Figure.Eight,False,1))
    result.append((Figure.Seven,Figure.Seven,False,1))
    result.append((Figure.Six,Figure.Six,False,1))
    result.append((Figure.Five,Figure.Five,False,1))
    result.append((Figure.Four,Figure.Four,False,1))
    result.append((Figure.Three,Figure.Three,False,1))
    result.append((Figure.Two,Figure.Two,False,1))

    result.append((Figure.King,Figure.Queen,False,1))
    result.append((Figure.Queen,Figure.Jack,True,1))


    if situation.LastBet <=2.5:
        result.append((Figure.King,Figure.Jack,False,1))
        result.append((Figure.King,Figure.Jack,True,1))
        result.append((Figure.Queen,Figure.Jack,False,1))
        result.append((Figure.Jack,Figure.Ten,True,1))
        result.append((Figure.Ten,Figure.Nine,True,1))
        result.append((Figure.Jack,Figure.Ten,False,1))
        result.append((Figure.Ten,Figure.Nine,False,1))
    return result

class Strategy6Max:
    def __init__(self):
        self.preflop_open = {
            Position.UTG: get_hands_to_open_from_utg,
            Position.HJ: get_hands_to_open_from_hj,
            Position.CO: get_hands_to_open_from_co,
            Position.BU: get_hands_to_open_from_button,
            Position.SB: get_hands_to_open_from_sb,
            Position.BB: get_hands_to_open_from_bb
        }
        self.preflop_raise ={
            TableAction.Raise: get_hands_to_3bet_preflop,
            TableAction.ReRaise: get_hands_to_4bet_preflop,
            TableAction.ReReRaise: get_hands_to_5bet_preflop
        }

        self.should_preflop_call_open ={
            Position.UTG:should_call_open_from_utg,
            Position.HJ: should_call_open_from_hj,
            Position.CO: should_call_open_from_co,
            Position.BU: should_call_open_from_bu,
            Position.SB: should_call_open_from_sb,
            Position.BB: should_call_open_from_bb
        }


        self.hand_evaluator = h.HandTypeEvaluator()
        self.hand_potential_evaluator = p.HandPotentialEvaluator()
        self.board_evaluator = b.BoardPotentialEvaluator()
   

    def get_decision(self, situation):
        result = DecisionClass(decision=Decision.FOLD)
        decision = self.should_bet(situation)
        if decision != None :
            return decision
        
        call_value = self.should_call(situation)
        if call_value != None:
            if call_value > random.uniform(0,1):
                result.decision = Decision.CALL
        return result

    def should_call(self, situation):
        cards_on_board = len(situation.Board)
        if cards_on_board == 0:
            return self.should_call_preflop(situation)
        if cards_on_board == 3:
            return self.should_call_flop(situation)
        if cards_on_board == 4:
            return self.should_call_turn(situation)
        if cards_on_board == 5:
            return self.should_call_river(situation)

    def should_call_preflop(self, situation = TableSituation.TableSituation()):
        if situation.LastTableAction == TableAction.Raise:
            _range = self.should_preflop_call_open[situation.get_hero_position()](situation)
            item = next((x for x in _range if x[0] == situation.HeroHandType[0] and x[1] == situation.HeroHandType[1] and x[2] == situation.HeroHandType[2]),None)
            if item == None:
                return False
            return True

        if situation.LastTableAction == TableAction.ReRaise:
            return self.should_call_3bet_pre(situation)
        return self.should_call_all_in_preflop(situation)

    def should_call_flop(self, situation = TableSituation.TableSituation()):

        tableAction = situation.LastTableAction
        oponents = len(situation.PlayersInPlay)
        handType = self.get_hand_value(situation = situation)
        has_color_draw = self.hand_potential_evaluator.has_flush_draw(situation = situation)
        is_straight_draw  = self.hand_potential_evaluator.has_openended(situation)
        has_gutshot = self.hand_potential_evaluator.has_gutshot(situation)
        denominator = (situation.Pot + 2 * situation.LastBet)
        percentage = 0
        if denominator != 0:
            percentage = situation.LastBet / (situation.Pot + 2 * situation.LastBet)


        if situation.LastBet <1.3:
            return True
        if tableAction == TableAction.Raise:
            if oponents == 1:
                return handType.value > HandType.ThirdPair.value or (percentage <0.7 and ( has_color_draw or is_straight_draw )) or (percentage <0.3 and has_gutshot )          

            return handType.value > HandType.SecondPair.value or (percentage <0.7 and ( has_color_draw or is_straight_draw )) or (percentage <0.3 and has_gutshot )          

        return handType.value >= HandType.TwoPairsWithTop or (percentage <0.4 and ( has_color_draw or is_straight_draw ))
    
    def should_call_turn(self, situation = TableSituation.TableSituation()):

        tableAction = situation.LastTableAction
        oponents = len(situation.PlayersInPlay)
        handType = self.get_hand_value(situation = situation)
        board_draw = self.board_evaluator.is_flush_draw(situation=situation)
        board_straight = self.board_evaluator.is_straight_draw(situation=situation)
        has_color_draw = self.hand_potential_evaluator.has_flush_draw(situation = situation)
        is_straight_draw  = self.hand_potential_evaluator.has_openended(situation)
        has_gutshot = self.hand_potential_evaluator.has_gutshot(situation)
        percentage = situation.LastBet / (situation.Pot + 2 * situation.LastBet)


        if situation.LastBet <1.1:
            return True
        if board_draw != None and board_draw.value > BoardPotential.ThreeCardsFlushDraw.value:
            if percentage <0.2:
                return handType.value >= HandType.NotNutsFlushWithFourBoardCards.value
            return handType.value > HandType.NotNutsFlushWithFourBoardCards.value 
        if  board_straight != None and board_straight.value > BoardPotential.StraightThreeInARow.value:
            return handType.value >= HandType.Straight_from_bottom.value
        if tableAction == TableAction.Raise:
            return handType.value > HandType.SecondPair.value or (percentage <0.3 and ( has_color_draw or is_straight_draw ))           

        return handType.value >= HandType.Trips or (percentage <0.3 and ( has_color_draw or is_straight_draw ))

    def get_street_count_with_action(self, situation = TableSituation.TableSituation()):
        result = 0
        if len(situation.FlopActions) > 0:
            result += 1
        if len(situation.TurnActions) > 0:
            result += 1
        if len(situation.RiverActions) >0:
            result += 1
        return result    

    def was_there_aggression(self, situation = TableSituation.TableSituation()):
        return situation.HighestFlopAction.value > TableAction.Raise.value or situation.HighestTurnAction.value > TableAction.Raise.value or situation.HighestRiverAction.value > TableAction.Raise.value

    def should_call_river(self, situation = TableSituation.TableSituation()):
            tableAction = situation.LastTableAction
            oponents = len(situation.PlayersInPlay)
            handType = self.get_hand_value(situation = situation)
            is_board_paired = self.board_evaluator.is_board_paired(situation=situation)

            is_color_possible = (self.board_evaluator.is_flush_draw(situation = situation).value >BoardPotential.TwoCardsFlushDraw.value)
            is_straight_possible = self.board_evaluator.is_straight_draw(situation =situation).value > BoardPotential.StraightDrawTwoInTheRow.value
            percentage = situation.LastBet / (situation.Pot + 2 * situation.LastBet)

            was_there_aggresion = self.was_there_aggression(situation)
            how_many_streets_were_bets = self.get_street_count_with_action(situation)

            if situation.LastTableAction == TableAction.Raise:
                if was_there_aggresion or how_many_streets_were_bets > 1:
                    if is_color_possible or is_straight_possible:
                        return handType.value >= HandType.Straight_from_bottom.value
                    return handType.value >= HandType.Trips.value
                return handType.value > HandType.SecondPair.value

            if is_color_possible or is_straight_draw:
                        return handType.value >= HandType.Straight
        
            if is_board_paired:
                return handType.value >= HandType.FullHouse
            return handType.value >= HandType.TwoPairsWithTop

    def should_bet(self, situation):
        cards_on_board = len(situation.Board)
        if cards_on_board == 0:
            return self.should_bet_preflop(situation)
        if cards_on_board == 3:
            return self.should_bet_flop(situation)
        if cards_on_board == 4:
            return self.should_bet_turn(situation)
        if cards_on_board == 5:
            return self.should_bet_river(situation)
   
    def should_bet_preflop(self, situation):
        result = DecisionClass(decision=Decision.RAISE)
        result = list()
        if situation.LastBet <=1:
            #should I open with my hand
          
            _range = self.preflop_open[situation.get_hero_position()]()
            item = next((x for x in _range if x[0] == situation.HeroHandType[0] and x[1] == situation.HeroHandType[1] and x[2] == situation.HeroHandType[2]),None)
            if item == None:
                return None
            if item[3]> random.uniform(0,1):
                return self.calculate_open(situation)
        _range = self.preflop_raise[situation.LastTableAction]()
        item = next((x for x in _range if x[0] == situation.HeroHandType[0] and x[1] == situation.HeroHandType[1] and x[2] == situation.HeroHandType[2]),None)
        if item == None:
                return None
        if item[3]> random.uniform(0,1):
            return self.calculate_open(situation)
        return None

    def should_bet_flop(self, situation = TableSituation.TableSituation()):
        was_hero_agressor_pre = situation.is_hero_preflop_agressor()
        last_open = (situation.FlopActions or [None])[-1]
        was_there_open = situation.was_there_open(actions=situation.FlopActions)
        

        if  was_hero_agressor_pre:
            if not was_there_open:
                return self.should_cbet_flop(situation)
            return self.should_reraise_donkbet_flop(situation)
        if not was_there_open:
            if situation.is_hero_in_poistion():
                return self.should_open_flop_after_checks(situation)
            return self.should_donkbet_flop(situation)
        if situation.LastTableAction == TableAction.Raise and self.should_reraise_flop(situation = situation):
            return self.calculate_open(situation)
        if situation.LastTableAction == TableAction.ReRaise and self.should_rereraise(situation):
            return self.calculate_open(situation)
        if situation.LastTableAction == TableAction.ReReRaise and self.should_go_all_in_on_flop():
            return self.calculate_open(situation)

    def should_bet_turn(self,situation=TableSituation.TableSituation()):
        was_there_open = situation.was_there_open(situation.TurnActions)
        aggressor_flop = situation.get_aggressor_on_flop()
        is_hero_aggressor_preflop = situation.is_hero_preflop_agressor()

        if not was_there_open:
            if (situation.is_hero_in_poistion() or aggressor_flop == 6 or (aggressor_flop == -1 and is_hero_aggressor_preflop )) and self.should_open_turn(situation):
                return self.calculate_open(situation)
            return None
        if situation.LastTableAction == TableAction.Raise and self.should_reraise_turn(situation = situation):
            return self.calculate_open(situation)
        if situation.LastTableAction == TableAction.ReRaise and self.should_rereraise(situation):
            return self.calculate_open(situation)
        if situation.LastTableAction == TableAction.ReReRaise and self.should_go_all_in_on_flop():
            return self.calculate_open(situation)
        return None      

    def should_bet_river(self, situation=TableSituation.TableSituation()):
        was_there_open = situation.was_there_open(situation.RiverActions)
        # aggressor_flop = situation.get_aggressor_on_flop()
        aggressor_turn = situation.get_aggressor_on_turn()
        if not was_there_open:
            if self.should_open_river(situation):
                return self.calculate_open(situation)
            return None
        if situation.LastTableAction == TableAction.Raise and self.should_reraise_river(situation = situation):
            return self.calculate_open(situation)
        if situation.LastTableAction == TableAction.ReRaise and self.should_reraise_river(situation):
            return self.calculate_open(situation)
        if situation.LastTableAction == TableAction.ReReRaise and self.should_reraise_river():
            return self.calculate_open(situation)
        return None      

    def should_call_3bet_pre(self, situation=TableSituation.TableSituation()):
        result = list()
        result.append((Figure.Ace,Figure.Ace,False,1))
        result.append((Figure.King,Figure.King,False,1))
        result.append((Figure.Queen,Figure.Queen,False,1))
        result.append((Figure.Jack,Figure.Jack,False,1))
        result.append((Figure.Ten,Figure.Ten,False,1))
        result.append((Figure.Nine,Figure.Nine,False,1))

        result.append((Figure.Ace,Figure.King,True,1))
        result.append((Figure.Ace,Figure.Queen,True,1))
        result.append((Figure.Ace,Figure.King,False,1))

        item = next((x for x in result if x[0] == situation.HeroHandType[0] and x[1] == situation.HeroHandType[1] and x[2] == situation.HeroHandType[2]),None)
        if item == None:
            return False
        return True

    def should_call_all_in_preflop(self, situation = TableSituation.TableSituation()):
        result = list()
        result.append((Figure.Ace,Figure.Ace,False,1))
        result.append((Figure.King,Figure.King,False,1))
        result.append((Figure.Queen,Figure.Queen,False,1))
      
        result.append((Figure.Ace,Figure.King,True,1))
        result.append((Figure.Ace,Figure.King,False,1))

        item = next((x for x in result if x[0] == situation.HeroHandType[0] and x[1] == situation.HeroHandType[1] and x[2] == situation.HeroHandType[2]),None)
        if item == None:
            return False
        return True

    def should_open_river(self, situation = TableSituation.TableSituation()):
        oponents_count = len(situation.PlayersInPlay)
        handType = self.get_hand_value(situation = situation)
        handTypeValue = handType.value
        has_color_draw = self.board_evaluator.is_flush_draw(situation = situation)
        is_straight  = self.board_evaluator.is_straight_draw(situation)

        if oponents_count>1:
            #cbet at least TP
            if is_straight >BoardPotential.StraightDrawTwoInTheRow.value or has_color_draw > BoardPotential.TwoCardsFlushDraw.value:
                return handType > 12
        return handType >= HandType.TwoPairsWithoutTop.value

        if handTypeValue > HandType.TopPair.value:
            return True
        return False

    def should_open_turn(self,situation = TableSituation.TableSituation()):
        oponents_count = len(situation.PlayersInPlay)
        handType = self.get_hand_value(situation = situation)
        handTypeValue = handType.value
        has_color_draw = self.board_evaluator.is_flush_draw(situation = situation)
        is_straight  = self.board_evaluator.is_straight_draw(situation)


        if has_color_draw != None and has_color_draw.value > BoardPotential.ThreeCardsFlushDraw.value: 
            return handTypeValue >= HandType.NutsFlushWithFourBoardCards.value
        if is_straight != None and is_straight.value > BoardPotential.StraightDrawTwoInTheRow.value:
            return handTypeValue >= HandType.Straight.value
        
        return handTypeValue >= HandType.TopPair.value


    def should_reraise_river(self, situation = TableSituation.TableSituation()):
        hand_type = self.get_hand_value(situation)
        is_color_draw = self.board_evaluator.is_flush_draw(situation = situation)
        is_straight  = self.board_evaluator.is_straight_draw(situation)
        
        if (is_straight == None or is_straight.value < 6) and (is_color_draw == None or is_color_draw.value <3):
            return hand_type.value > HandType.Set.value

        if is_color_draw == None or is_color_draw.value <3 :
            return hand_type.value > HandType.Straight_from_bottom.value
        return hand_type.value >= HandType.Flush.value

    def should_reraise_turn(self, situation = TableSituation.TableSituation()):
        hand_type = self.get_hand_value(situation)
        is_color_draw = self.board_evaluator.is_flush_draw(situation = situation)

        is_straight  = self.board_evaluator.is_straight_draw(situation)
        if (is_straight == None or is_straight.value < 6) and (is_color_draw == None or is_color_draw.value <3):
            return hand_type.value > HandType.Set.value

        if is_color_draw == None or is_color_draw.value <3 :
            return hand_type.value >= HandType.Straight_from_bottom.value
        return hand_type.value >= HandType.Flush.value

    def get_hand_value(self,situation):
        result  = None
        if self.hand_evaluator.has_straight_flush(situation) != None:
            return HandType.StraightFlush

        if self.hand_evaluator.has_4_of_the_kind(situation) == HandType.FourOfKind:
            return HandType.FourOfKind
        if self.hand_evaluator.has_fullhouse(situation=situation) == HandType.FullHouse:
            return HandType.FullHouse
        result = self.hand_evaluator.has_flush(situation=situation)
        if result != None:
            return result
        result = self.hand_evaluator.has_straight(situation=situation)
        if result != None:
            return result
        result = self.hand_evaluator.has_3_of_the_kind(situation=situation)
        if result != None:
            return result
        result = self.hand_evaluator.has_two_pairs(situation=situation)
        if result != None:
            return result
        result = self.hand_evaluator.has_pair(situation=situation)
        if result != None:
            return result
        return HandType.HighCard

    def should_cbet_flop(self,situation = TableSituation.TableSituation()):
        oponents_count = len(situation.PlayersInPlay)
        handType = self.get_hand_value(situation = situation)
        handTypeValue = handType.value
        is_openended = self.hand_potential_evaluator.has_openended(situation = situation)
        is_flush_draw = self.hand_potential_evaluator.has_flush_draw(situation=situation)
        if oponents_count>1:
            #cbet at least TP
            if handTypeValue  > HandType.SecondPair.value:
                return self.calculate_open(situation)
        
        if handTypeValue > HandType.ThirdPair.value  or is_flush_draw or is_openended:
            return self.calculate_open(situation)
        if situation.Board[0].Figure == Figure.Ace or situation.Board[1].Figure == Figure.Ace or situation.Board[2] == Figure.Ace:
            ## should check if board is not to drawy?
            return self.calculate_open(situation)
        return None
            
    def should_reraise_donkbet_flop(self, situation):

        hand_value  = self.get_hand_value(self, situation=situation)
        if hand_value >8:
            return self.calculate_open(situation)
        return None

    def should_open_flop_after_checks(self, situation= TableSituation.TableSituation()):
        hand_type = self.get_hand_value(situation)
        if situation.was_3bet_preflop():
            return hand_type.value > HandType.TopPair.value
        return hand_type.value > HandType.ThirdPair

    def should_open_flop_after_checks(self, situation = TableSituation.TableSituation()):
        hand_type = self.get_hand_value(situation)
        if situation.was_3bet_preflop():
            is_openended = self.hand_potential_evaluator.has_openended(situation = situation)
            is_flush_draw = self.hand_potential_evaluator.has_flush_draw(situation=situation)
            if hand_type.value >= HandType.TopPair.value:
                return self.calculate_open(situation)
            return None
        if hand_type.value >= HandType.SecondPair or is_flush_draw or is_openended:
            if item[3]> random.random(0,1):
                return self.calculate_open(situation)
        return None

    def should_donkbet_flop(self, situation = TableSituation.TableSituation()):
        #TODO
        return None

    def should_reraise_flop(self,situation = TableSituation.TableSituation()):
        hand_type = self.get_hand_value(situation)
        
        return hand_type.value >= HandType.TwoPairsWithTop.value

    def should_rereraise(self, situation = TableSituation.TableSituation()):
        hand_type = self.get_hand_value(situation)
        has_color_draw = self.board_evaluator.is_flush_draw(situation = situation)

        is_straight  = self.board_evaluator.is_straight_draw(situation)
        if (is_straight == None or is_straight.value < 6) and (has_color_draw == None or has_color_draw.value <3):
            return hand_type.value > HandType.Set.value

        if has_color_draw == None or has_color_draw.value <3 :
            return hand_type.value >= HandType.Straight_from_bottom.value
        return hand_type.value >= HandType.Flush.value

    def should_go_all_in_on_flop(self,situation): 
        
        # #todo all in with set when no mono board or straight
        # hand_type = self.get_hand_value(situation)
        # return hand_type.value >= HandType.Straight_from_bottom.value
        return self.should_rereraise(situation=situation)

    def calculate_open(self, situation = TableSituation.TableSituation()):
        result = DecisionClass(decision=Decision.RAISE)
        if situation.LastTableAction.value < TableAction.Raise.value:
            if len(situation.Board) ==0:
                if situation.Pot <= 1.5:
                    result.betType = BetType.Min
                else:
                    result.bet = situation.Pot + 1
                return result
            result.betType = BetType(random.randrange(1,4))
            return result         
        result.betType =  BetType.Pot
        return result
    