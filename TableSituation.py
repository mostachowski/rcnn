from PokerDto import Action,TableAction,HandType,HandPotential

class TableSituation:
    def __init__(self):
        self.TableName = None
        self.Hand = list()
        self.Board = list()
        self.PreflopActions = list()
        self.FlopActions = list()
        self.TurnActions = list()
        self.RiverActions = list()
        self.ButtonPosition = 0
        self.HeroStack = 0
        self.TableActions = list()
        self.PlayersInPlay = list()
        self.Pot = 0
        self.LastBet = 0
        self.LastboardCardsCount = 0
        self.HeroHandType = None
        self.LastTableAction = TableAction.NoAction

    def add_action(self,player_number,bet):
        print("action. Bet: ",str(bet))
        if self.LastboardCardsCount==0:
            self.PreflopActions.append(Action(player_number=player_number,bet= bet))
        if self.LastboardCardsCount==3:
            self.FlopActions.append(Action(player_number=player_number,bet= bet))
        if self.LastboardCardsCount==4:
            self.TurnActions.append(Action(player_number=player_number,bet= bet))
        if self.LastboardCardsCount==5:
            self.RiverActions.append(Action(player_number=player_number,bet= bet))
        if self.LastBet < bet:
            self.LastBet = bet
            if self.LastTableAction != TableAction.ReReRaise: 
                self.LastTableAction  = TableAction((int(self.LastTableAction) +1))
        
        self.Pot +=bet
    def set_board(self, cards):
        if len(self.Board) == len(cards):
            return
        self.LastBet = 0
        self.LastTableAction = TableAction.NoAction
        self.Board = cards
        self.LastboardCardsCount = len(self.Board)
    def set_hand(self,hand):
        self.Hand = hand
        handType = (None,None,hand[0].Color==hand[1].Color)
        if int(hand[0].Figure)> int(hand[1].Figure):
            handType[0] = hand[0].Figure
            handType[1] = hand[1].Figure
        else:
            handType[0] = hand[1].Figure
            handType[1] = hand[0].Figure
        self.HeroHandType = handType

    def is_hero_preflop_agressor(self):
        aggresor = 0
        lastbet = 0
        for action in self.PreflopActions:
            if action.bet > lastbet:
                # TODO: if bet is to small, maybe its small all in and we should not change agressor
                aggresor = action.player_number
                lastbet = action.bet
        return aggresor == 6

    def get_hero_position(self):
       return Position(6 - int(self.ButtonPosition))




    
