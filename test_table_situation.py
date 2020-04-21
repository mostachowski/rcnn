import unittest
import hand_type_evaluator as h
from PokerDto import Decision,Figure,Position,TableAction,Card, HandType,Color,Player
import TableSituation as t

class TableSituationTest(unittest.TestCase):
  
    def setUp(self) -> None:
                self.situation = t.TableSituation()

    def test_hero_should_not_be_in_position(self):

        self.situation.PlayersInPlay.append(Player(3))
        self.situation.ButtonPosition = 3

        result = self.situation.is_hero_in_poistion()
        self.assertEqual(result, False)

    def test_hero_should__be_in_position(self):

        self.situation.PlayersInPlay.append(Player(1))
        self.situation.PlayersInPlay.append(Player(2))
        self.situation.PlayersInPlay.append(Player(3))
        self.situation.PlayersInPlay.append(Player(4))
        self.situation.PlayersInPlay.append(Player(5))
        self.situation.ButtonPosition = 6

        result = self.situation.is_hero_in_poistion()
        self.assertEqual(result, True)