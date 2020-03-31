from PokerDto import Decision,Figure,Position,TableAction
import TableSituation
import hand_type_evaluator as h


#results are in tuples: (figure,figure,Is suited,percentage)
def get_hands_to_open_from_utg():
    result = list()

    reuslt.append((Figure.Ace,Figure.Ace,False,1))
    reuslt.append((Figure.King,Figure.King,False,1))
    reuslt.append((Figure.Queen,Figure.Queen,False,1))
    reuslt.append((Figure.Jack,Figure.Jack,False,1))
    reuslt.append((Figure.Ten,Figure.Ten,False,1))
    reuslt.append((Figure.Nine,Figure.Nine,False,1))
    reuslt.append((Figure.Eight,Figure.Eight,False,1))
    reuslt.append((Figure.Seven,Figure.Seven,False,1))
    reuslt.append((Figure.Six,Figure.Six,False,1))
    reuslt.append((Figure.Five,Figure.Five,False,1))
    reuslt.append((Figure.Four,Figure.Four,False,1))
    reuslt.append((Figure.Three,Figure.Three,False,1))
    reuslt.append((Figure.Two,Figure.Two,False,1))

    reuslt.append((Figure.Ace,Figure.King,True,1))
    reuslt.append((Figure.Ace,Figure.King,False,1))
    reuslt.append((Figure.Ace,Figure.Queen,True,1))
    reuslt.append((Figure.Ace,Figure.Queen,False,1))
    reuslt.append((Figure.Ace,Figure.Jack,True,1))
    reuslt.append((Figure.Ace,Figure.Jack,False,1))
    reuslt.append((Figure.Ace,Figure.Ten,True,1))
    reuslt.append((Figure.Ace,Figure.Five,True,1))
    reuslt.append((Figure.Ace,Figure.Four,True,1))
    reuslt.append((Figure.Ace,Figure.Three,True,1))
    reuslt.append((Figure.Ace,Figure.Two,True,1))
    reuslt.append((Figure.King,Figure.Queen,True,1))
    reuslt.append((Figure.King,Figure.Queen,False,1))
    return result

def get_hands_to_open_from_hj():
    result = get_hands_to_open_from_utg()
    reuslt.append((Figure.Ace,Figure.Ten,False,1))
    reuslt.append((Figure.Ace,Figure.Nine,True,1))
    reuslt.append((Figure.Ace,Figure.Nine,False,1))
    reuslt.append((Figure.Ace,Figure.Eight,True,1))
    reuslt.append((Figure.King,Figure.Jack,True,1))
    reuslt.append((Figure.King,Figure.Jack,False,1))
    return result


def get_hands_to_open_from_co():
    result = get_hands_to_open_from_hj()
    reuslt.append((Figure.Ace,Figure.Eight,False,1))
    reuslt.append((Figure.Ace,Figure.Seven,True,1))
    reuslt.append((Figure.Ace,Figure.Six,True,1))
    reuslt.append((Figure.King,Figure.Ten,True,1))
    reuslt.append((Figure.King,Figure.Ten,False,1))
    reuslt.append((Figure.Queen,Figure.Jack,True,1))
    reuslt.append((Figure.Queen,Figure.Jack,False,1))
    reuslt.append((Figure.Queen,Figure.Ten,True,1))
    reuslt.append((Figure.Queen,Figure.Ten,False,1))
    reuslt.append((Figure.Jack,Figure.Ten,True,1))
    reuslt.append((Figure.Jack,Figure.Nine,True,1))
    reuslt.append((Figure.Jack,Figure.Eight,True,1))
    reuslt.append((Figure.Ten,Figure.Nine,True,1))
    reuslt.append((Figure.Nine,Figure.Eight,True,1))
    reuslt.append((Figure.Nine,Figure.Seven,True,1))
    reuslt.append((Figure.Eight,Figure.Seven,True,1))
    reuslt.append((Figure.Seven,Figure.Six,True,1))
    reuslt.append((Figure.Seven,Figure.Five,True,1))
    reuslt.append((Figure.Six,Figure.Five,True,1))
    return result

def get_hands_to_open_from_button():
    result = get_hands_to_open_from_co()

    reuslt.append((Figure.Ace,Figure.Seven,False,1))
    reuslt.append((Figure.Ace,Figure.Six,False,1))
    reuslt.append((Figure.Ace,Figure.Five,False,1))
    reuslt.append((Figure.Ace,Figure.Four,False,1))
    reuslt.append((Figure.Ace,Figure.Three,False,1))
    reuslt.append((Figure.Ace,Figure.Two,False,1))

    reuslt.append((Figure.King,Figure.Nine,True,1))
    reuslt.append((Figure.King,Figure.Nine,False,1))
    reuslt.append((Figure.King,Figure.Eight,True,1))
    reuslt.append((Figure.King,Figure.Eight,False,1))
    reuslt.append((Figure.King,Figure.Seven,True,1))
    reuslt.append((Figure.King,Figure.Seven,False,1))
    reuslt.append((Figure.King,Figure.Six,True,1))
    reuslt.append((Figure.King,Figure.Five,True,1))

    reuslt.append((Figure.Queen,Figure.Nine,True,1))
    reuslt.append((Figure.Queen,Figure.Eight,True,1))
    reuslt.append((Figure.Queen,Figure.Seven,True,1))
    reuslt.append((Figure.Jack,Figure.Nine,False,1))
    reuslt.append((Figure.Jack,Figure.Seven,True,1))

    reuslt.append((Figure.Ten,Figure.Nine,False,1))  
    reuslt.append((Figure.Ten,Figure.Eight,False,1))  
    reuslt.append((Figure.Ten,Figure.Seven,True,1))  
    reuslt.append((Figure.Ten,Figure.Six,True,1)) 
    reuslt.append((Figure.Nine,Figure.Eight,False,1)) 
    reuslt.append((Figure.Nine,Figure.Seven,False,1)) 
    reuslt.append((Figure.Eight,Figure.Seven,False,1)) 
    reuslt.append((Figure.Seven,Figure.Six,False,1)) 

def get_hands_to_open_from_sb():
    result = get_hands_to_open_from_hj()
    return result

def get_hands_to_open_from_bb():
    result = get_hands_to_open_from_hj()
    return result

def get_hands_to_3bet_preflop():
    result = list()
    reuslt.append((Figure.Ace,Figure.Ace,False,1))
    reuslt.append((Figure.King,Figure.King,False,1))
    reuslt.append((Figure.Queen,Figure.Queen,False,1))
    reuslt.append((Figure.Jack,Figure.Jack,False,1))
    reuslt.append((Figure.Ten,Figure.Ten,False,1))

    reuslt.append((Figure.Ace,Figure.King,True,1))
    reuslt.append((Figure.Ace,Figure.King,False,1))
    reuslt.append((Figure.Ace,Figure.Queen,True,1))
    reuslt.append((Figure.Ace,Figure.Queen,False,1))
    reuslt.append((Figure.Ace,Figure.Jack,True,1))
    reuslt.append((Figure.Ace,Figure.Jack,False,1))
    reuslt.append((Figure.King,Figure.Queen,True,1))

def get_hands_to_4bet_preflop():
    result = list()
    reuslt.append((Figure.Ace,Figure.Ace,False,0.7))
    reuslt.append((Figure.King,Figure.King,False,0.7))
    reuslt.append((Figure.Queen,Figure.Queen,False,0.8))

    reuslt.append((Figure.Ace,Figure.King,True,0.4))
    reuslt.append((Figure.Ace,Figure.King,False,0.2))
    reuslt.append((Figure.King,Figure.Queen,True,0.2))

def get_hands_to_5bet_preflop():
    result = list()
    reuslt.append((Figure.Ace,Figure.Ace,False,0.7))
    reuslt.append((Figure.King,Figure.King,False,0.7))
    reuslt.append((Figure.Queen,Figure.Queen,False,0.5))
    reuslt.append((Figure.Ace,Figure.King,True,0.4))


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
        self.hand_evaluator = h.HandTypeEvaluator()
    def get_decision(self, situation):
        if should_bet(situation):
            return Decision.RAISE
        if should_call(situation):
            return Decision.CALL
        return Decision.FOLD

    def should_bet(self, situation):
        cards_on_board = len(situation.Board)
        if cards_on_board == 0:
            return should_bet_preflop(situation)
        if cards_on_board == 3:
            return should_bet_flop(situation)
        if cards_on_board == 4:
            return should_bet_turn(situation)
        if cards_on_board == 5:
            return should_bet_river(situation)
   
    def should_bet_preflop(self, situation):
        result = list()
        if situation.LastBet <=1:
            #should I open with my hand
            _range = self.preflop_open[situation.get_hero_position()]()
            item = next(x for x in _range if x[0].Figure == situation.HeroHandType[0] and x[1].Figure == situation.HeroHandType[1] and x[2].Figure == situation.HeroHandType[2],None):
            if item == None:
                return 0
            return item[3]
        _range = self.preflop_raise[situation.LastTableAction]()
         item = next(x for x in _range if x[0].Figure == situation.HeroHandType[0] and x[1].Figure == situation.HeroHandType[1],(None))
            if item == None:
                return 0
            return item[3]

    def should_cbet_flop(self.situation):
        has_srtaight() or has

    def should_bet_flop(self, situation):
        if  situation.is_hero_preflop_agressor():
            return should_cbet_flop(situation)


    