import unittest
import hand_potential_evaluator as h
from PokerDto import Decision,Figure,Position,TableAction,Card, HandPotential,Color
import TableSituation as t

class HandTypeEvaluatorTests(unittest.TestCase):
  
    def setUp(self) -> None:
        self.situation = t.TableSituation()
        self.evaluator = h.HandPotentialEvaluator()

    def test_should_recognize_gutshot(self):

        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.King,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Ace,color=Color.Spade))

        hand = self.evaluator.has_gutshot(situation=self.situation)
        self.assertEqual(hand, HandPotential.Gutshot)

    def test_should_recognize_openended(self):

        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.King,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Jack,color=Color.Spade))

        hand = self.evaluator.has_openended(situation=self.situation)
        self.assertEqual(hand, HandPotential.OpenEnded)

    def test_should_recognize_openended_with_ace_as_bottom(self):

        self.situation.Board.append(Card(figure=Figure.Five,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.Four,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.King,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Two,color=Color.Spade))

        hand = self.evaluator.has_openended(situation=self.situation)
        self.assertEqual(hand, HandPotential.OpenEnded)