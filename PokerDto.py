from enum import Enum

class Figure(Enum):
    Two = 0
    Three = 1
    Four = 2
    Five = 3
    Six = 4
    Seven = 5
    Eight = 6
    Nine = 7
    Ten = 8
    Jack = 9
    Queen = 10
    King = 11
    Ace = 12
    Error = 13

class Color(Enum):
    Club = 0
    Diamond = 1
    Heart = 2
    Spade = 3
    Error = 4
      
class Card:

    def __init__(self, figure=Figure.Error, color=Color.Error):
        self.Figure = figure
        self.Color = color


class BetType(Enum):
    Min = 0
    FourtyThree = 1
    SixtySix = 2
    Pot = 3
    AllIn = 4

class Position(Enum):
    BU = 0
    SB = 1
    BB = 2
    UTG = 3
    HJ = 4
    CO = 5


class TableAction(Enum):
    NoAction = 0
    Check = 1
    Call = 2
    Raise = 3
    ReRaise = 4 
    ReReRaise = 5
class Player:
    def __init__(self,position,name=None,stack=None):
        self.Position = position
        self.Name = name
        self.Stack = stack

class Action:
    def __init__(self,player_number,bet):
        self.player_number = player_number
        self.bet = bet
        
class Decision(Enum):
    RAISE = 1
    CALL = 2
    FOLD = 3

class DecisionClass:
    def __init__(self,decision = Decision.FOLD, betType = BetType.Min, bet = 0):
        self.bet = bet
        self.betType = betType
        self.decision  = decision


class BoardPotential(Enum):
    Paired = 1
    TwoCardsFlushDraw = 2
    ThreeCardsFlushDraw = 3
    FourCardsFlushDraw = 4
    StraightDrawTwoInTheRow = 5
    StraightThreeInARow = 6
    StraightFourInTheRow = 7
    StraightOneGap = 8

class HandType(Enum):
    HighCard = 1
    SixthPair = 2
    FifthPair = 3
    FourthPair = 4
    ThirdPair = 5
    SecondPair = 6
    TopPair = 7
    OverPair = 8
    TwoPairsWithoutTop = 9
    TwoPairsWithTop = 10
    Trips = 11
    Set=12
    StraightOnBoard = 13
    Straight_from_bottom = 14
    Straight = 15
    NotNutsFlushWithFourBoardCards = 16
    Flush = 17
    NutsFlushWithFourBoardCards = 18
    FullHouseOnBoard = 19
    FullHouse = 20
    FourOfTheKindOnBoard =21
    FourOfKind = 22
    StraightFlush = 23

class HandPotential(Enum):
    FlashDraw = 1
    OneHighCardFlashDraw = 2
    OneCardFlashDraw = 3  
    TwoCardFlashBackdoor = 4
    Gutshot = 5
    StreightBackdoorTwoCards = 6
    OpenEnded = 7
    TwoOverCards = 8


