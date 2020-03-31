import unittest
import hand_type_evaluator as h
from PokerDto import Decision,Figure,Position,TableAction,Card, HandType,Color
import TableSituation as t

class HandTypeEvaluatorTests(unittest.TestCase):
  
    def setUp(self) -> None:
        self.situation = t.TableSituation()
        self.evaluator = h.HandTypeEvaluator()

    def test_should_recognize_third_pair(self):

        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.Three,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Four,color=Color.Spade))

        hand = self.evaluator.has_pair(situation=self.situation)
        self.assertEqual(hand, HandType.ThirdPair)

    def test_should_recognize_top_pair(self):

        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.King,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Queen,color=Color.Club))

        hand = self.evaluator.has_pair(situation=self.situation)
        self.assertEqual(hand, HandType.TopPair)

    def test_should_recognize_two_pairs_with_top(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.King,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.King,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Queen,color=Color.Club))

        hand = self.evaluator.has_two_pairs(situation=self.situation)
        self.assertEqual(hand, HandType.TwoPairsWithTop)

    def test_should_recognize_two_pairs_without_top(self):

        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.King,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.Ten,color=Color.Diamond))
        self.situation.Hand.append(Card(figure=Figure.Queen,color=Color.Club))

        hand = self.evaluator.has_two_pairs(situation=self.situation)
        self.assertEqual(hand, HandType.TwoPairsWithoutTop)
    
    def test_should_recognize_set(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.King,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.Ten,color=Color.Diamond))
        self.situation.Hand.append(Card(figure=Figure.Ten,color=Color.Heart))

        hand = self.evaluator.has_3_of_the_kind(situation=self.situation)
        self.assertEqual(hand, HandType.Set)

    def test_should_recognize_trips(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.King,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.Queen,color=Color.Diamond))
        self.situation.Hand.append(Card(figure=Figure.Ten,color=Color.Heart))

        hand = self.evaluator.has_3_of_the_kind(situation=self.situation)
        self.assertEqual(hand, HandType.Trips)

    def test_should_recognize_flush(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.King,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Spade))

        self.situation.Hand.append(Card(figure=Figure.King,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Two,color=Color.Spade))

        hand = self.evaluator.has_flush(situation=self.situation)
        self.assertEqual(hand, HandType.Flush)

    def test_should_recognize_four_card_flush_not_nuts(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Spade))

        self.situation.Hand.append(Card(figure=Figure.King,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Two,color=Color.Spade))

        hand = self.evaluator.has_flush(situation=self.situation)
        self.assertEqual(hand, HandType.NotNutsFlushWithFourBoardCards)

    def test_should_recognize_nuts_four_card_flush(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Four,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Ace,color=Color.Spade))

        self.situation.Hand.append(Card(figure=Figure.King,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Two,color=Color.Spade))

        hand = self.evaluator.has_flush(situation=self.situation)
        self.assertEqual(hand, HandType.NutsFlushWithFourBoardCards)
    
    def test_should_not_recognize_flush_when_cards_from_hand_not_used(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Nine,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Ace,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Eight,color=Color.Spade))

        self.situation.Hand.append(Card(figure=Figure.Seven,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Six,color=Color.Spade))

        hand = self.evaluator.has_flush(situation=self.situation)
        self.assertEqual(hand, None)

    def test_should_recognize_straight(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Three,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.King,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Spade))

        self.situation.Hand.append(Card(figure=Figure.Ace,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Jack,color=Color.Spade))

        hand = self.evaluator.has_straight(situation=self.situation)
        self.assertEqual(hand, HandType.Straight)

    def test_should_recognize_straight_from_bottom(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Jack,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.King,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Spade))

        self.situation.Hand.append(Card(figure=Figure.Nine,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Eight,color=Color.Spade))

        hand = self.evaluator.has_straight(situation=self.situation)
        self.assertEqual(hand, HandType.Straight_from_bottom)

    def test_should_recognize_straight_on_board(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Jack,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.King,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Ten,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Nine,color=Color.Heart))

        self.situation.Hand.append(Card(figure=Figure.Seven,color=Color.Spade))
        self.situation.Hand.append(Card(figure=Figure.Eight,color=Color.Spade))

        hand = self.evaluator.has_straight(situation=self.situation)
        self.assertEqual(hand, HandType.StraightOnBoard)

    def test_should_recognize_fullhouse(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Jack,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Nine,color=Color.Heart))

        self.situation.Hand.append(Card(figure=Figure.Jack,color=Color.Heart))
        self.situation.Hand.append(Card(figure=Figure.Jack,color=Color.Spade))

        hand = self.evaluator.has_fullhouse(situation=self.situation)
        self.assertEqual(hand, HandType.FullHouse)
    
    def test_should_recognize_fullhouse_on_board(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.Seven,color=Color.Heart))
        self.situation.Hand.append(Card(figure=Figure.Seven,color=Color.Spade))

        hand = self.evaluator.has_fullhouse(situation=self.situation)
        self.assertEqual(hand, HandType.FullHouseOnBoard)

    def test_should_recognize_quads(self):
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.Queen,color=Color.Heart))
        self.situation.Hand.append(Card(figure=Figure.Queen,color=Color.Spade))

        hand = self.evaluator.has_4_of_the_kind(situation=self.situation)
        self.assertEqual(hand, HandType.FourOfKind)

    def test_should_recognize_quads_on_board(self):
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Heart))
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Spade))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.Queen,color=Color.Heart))
        self.situation.Hand.append(Card(figure=Figure.Queen,color=Color.Spade))

        hand = self.evaluator.has_4_of_the_kind(situation=self.situation)
        self.assertEqual(hand, HandType.FourOfTheKindOnBoard)

    def test_should_recognize_straight_flush(self):
        self.situation.Board.append(Card(figure=Figure.Ace,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.King,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Queen,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Jack,color=Color.Diamond))
        self.situation.Board.append(Card(figure=Figure.Six,color=Color.Club))

        self.situation.Hand.append(Card(figure=Figure.Ten,color=Color.Diamond))
        self.situation.Hand.append(Card(figure=Figure.Queen,color=Color.Spade))

        hand = self.evaluator.has_flush_straight(situation=self.situation)
        self.assertEqual(hand, HandType.StraightFlush)