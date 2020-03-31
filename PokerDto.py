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


class HandType(Enum):
    HighCard = 1
    OverPair = 2
    TopPair = 3
    SecondPair = 4
    ThirdPair = 5
    FourthPair = 6
    FifthPair = 7
    SixthPair = 8
    TwoPairsWithTop = 9
    TwoPairsWithoutTop = 10
    Set=11
    Trips = 12
    Straight = 13
    Straight_from_bottom = 13
    StraightOnBoard = 14
    Flush = 15
    NutsFlushWithFourBoardCards = 16
    NotNutsFlushWithFourBoardCards = 17
    FullHouse = 18
    FullHouseOnBoard = 19
    FourOfKind = 20
    FourOfTheKindOnBoard =21
    StraightFlush = 22

class HandPotential(Enum):
    FlashDraw = 1
    OneHighCardFlashDraw = 2
    OneCardFlashDraw = 3  
    TwoCardFlashBackdoor = 4
    Gutshot = 5
    StreightBackdoorTwoCards = 6
    OpenEnded = 7
    TwoOverCards = 8


