from PokerDto import Action,TableAction,HandType,HandPotential,Position,BetType

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
        self.HighestFlopAction = TableAction.NoAction
        self.HighestPreflopAction = TableAction.NoAction
        self.HighestTurnAction = TableAction.NoAction
        self.HighestRiverAction = TableAction.NoAction

    def _calculate_bet(self,betType = BetType.Min):
        bet = 2.2
        if betType == BetType.Min:
                bet = 2.2
        if betType == BetType.FourtyThree:
            bet = 0.43 * self.Pot  + self.LastBet
        if betType == BetType.SixtySix:
            bet = 0.66 * self.Pot + self.LastBet
        if betType == BetType.Pot:
            bet  = self.Pot + self.LastBet
        if betType == BetType.AllIn:
            bet = 1000
        return bet

    def add_action(self,player_number,bet,betType = BetType.Min):
        need_update = False

        if player_number ==6:
            if bet is None or bet == 0:
                bet = self._calculate_bet(betType)
            need_update = True
            if self.LastTableAction.value < TableAction.Raise.value:
                    self.LastTableAction = TableAction.Raise
            else:
                if self.LastTableAction == TableAction.Raise:
                    self.LastTableAction = TableAction.ReRaise
                else:
                    self.LastTableAction = TableAction.ReReRaise
            
            


        if self.LastBet < bet and player_number !=6:
            self.LastBet = bet
            if bet <=1:
                if self.LastTableAction.value < TableAction.Raise.value:
                    self.LastTableAction = TableAction.Call
                    need_update = True
            else:
                need_update = True
                if self.LastTableAction.value < TableAction.Raise.value:
                    self.LastTableAction = TableAction.Raise
                else:
                    if self.LastTableAction == TableAction.Raise:
                        self.LastTableAction = TableAction.ReRaise
                    else:
                        self.LastTableAction = TableAction.ReReRaise


        if self.LastboardCardsCount==0:
            self.PreflopActions.append(Action(player_number=player_number,bet= bet))
            if need_update:
                self.HighestPreflopAction = self.LastTableAction
        if self.LastboardCardsCount==3:
            self.FlopActions.append(Action(player_number=player_number,bet= bet))
            if need_update:
                self.HighestFlopAction = self.LastTableAction
        if self.LastboardCardsCount==4:
            self.TurnActions.append(Action(player_number=player_number,bet= bet))
            if need_update:
                self.HighestTurnAction = self.LastTableAction
        if self.LastboardCardsCount==5:
            self.RiverActions.append(Action(player_number=player_number,bet= bet))
            if need_update:
                self.HighestRiverAction = self.LastTableAction
    
        self.Pot +=bet
        
    def set_board(self, cards):
        if len(self.Board) == len(cards):
            return
        self.LastBet = 0
        self.LastTableAction = TableAction.NoAction
        self.Board = cards
        self.LastboardCardsCount = len(self.Board)
        self.PlayersInPlay = list()
    def set_hand(self,hand):
        self.Hand = hand
        handType = [hand[0].Figure,hand[1].Figure,hand[0].Color==hand[1].Color]
        if hand[0].Figure.value > hand[1].Figure.value:
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

    def get_aggressor_on_flop(self):
        aggresor = -1
        lastbet = 0
        for action in self.FlopActions:
            if action.bet > lastbet:
                # TODO: if bet is to small, maybe its small all in and we should not change agressor
                aggresor = action.player_number
                lastbet = action.bet
        return aggresor

    def get_aggressor_on_turn(self):
        aggresor = -1
        lastbet = 0
        for action in self.TurnActions:
            if action.bet > lastbet:
                # TODO: if bet is to small, maybe its small all in and we should not change agressor
                aggresor = action.player_number
                lastbet = action.bet
        return aggresor

    def was_there_open(self, actions=list()):
        for action in actions:
            if float(action.bet) > 1.5:
                return True
        return False

    def get_hero_position(self):
       return Position(6 - int(self.ButtonPosition))

    def is_hero_in_poistion(self):
        hero_position = self.get_hero_position()
        if hero_position == Position.SB:
            return False
        if hero_position == Position.BB:
            if len(self.PlayersInPlay) >1:
                return False
            if PlayersInPlay[0].Position == 5:
                return True
            return False
    
        if hero_position == Position.UTG:
            item = next((x for x in self.PlayersInPlay if x.Position in {1,2,3}),None)
            return item == None
        if hero_position == Position.HJ:
            item = next((x for x in self.PlayersInPlay if x.Position in {1,2,3,4}),None)
            return item == None
        if hero_position == Position.CO:
            item = next((x for x in self.PlayersInPlay if x.Position in {1,2,3,5}),None)
            return item == None
        if hero_position == Position.BU:
            return True
        
    def was_3bet_preflop(self):
        last_bet = 0
        last_action_type = TableAction.NoAction
        for action in self.PreflopActions:
            if action.bet > last_bet:
                if last_bet == 0:
                    if action.bet == 1:
                        last_action_type = TableAction.Call
                    else: 
                        last_action_type = TableAction.Raise
                else:
                    if last_action_type.value < TableAction.ReReRaise.value:
                        last_action_type = TableAction(last_action_type.value+1)

                last_bet == action.bet
        return  last_action_type.value >2
            
