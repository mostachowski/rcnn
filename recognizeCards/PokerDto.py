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
    Figure
    Color 
    def __init__(self, figure=Figure.Error, color=Color.Error):
        self.Figure = figure
        self.Color = color

class Position(Enum):
    SB = 1
    BB = 2
    UTG = 3
    MP = 4
    CO = 5
    BTN = 6

class TableAction(Enum):
    Check = 0
    Call = 1
    Raise = 2
    ReRaise = 3
class Player:
    def __init__(self,position,name=None,stack=None):
        self.Position = position
        self.Name = name
        self.Stack = stack
