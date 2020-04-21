import unittest
import hand_type_evaluator as h
from PokerDto import Decision,Figure,Position,TableAction,Card, HandType,Color
import strategy6max as s
import TableSituation as t

class Strategy6maxTests(unittest.TestCase):
  
    def setUp(self) -> None:
        self.situation = t.TableSituation()
        self.startegy = s.Strategy6Max()

    def test_should_open_AK_preflop_from_CO(self):
      
        hand = list()
        hand.append(Card(figure=Figure.Ace,color=Color.Spade))
        hand.append(Card(figure=Figure.King,color=Color.Spade))
        self.situation.set_hand(hand)

        self.situation.ButtonPosition = 1
    
        decision = self.startegy.get_decision(situation=self.situation)

        self.assertEqual(decision.decision, Decision.RAISE)

    def test_should_call_open_99_preflop(self):
        hand = list()
        hand.append(Card(figure=Figure.Nine,color=Color.Spade))
        hand.append(Card(figure=Figure.Nine,color=Color.Club))
        self.situation.set_hand(hand)

        self.situation.ButtonPosition = 1
        self.situation.add_action(2, 0.5)
        self.situation.add_action(3, 1)
        self.situation.add_action(4, 2.4)

    
        decision = self.startegy.get_decision(situation=self.situation)

        self.assertEqual(decision.decision, Decision.CALL)


    def test_should_fold_to_3bet_88_preflop(self):
        hand = list()
        hand.append(Card(figure=Figure.Eight,color=Color.Spade))
        hand.append(Card(figure=Figure.Eight,color=Color.Club))
        self.situation.set_hand(hand)

        self.situation.ButtonPosition = 1
        self.situation.add_action(2, 0.5)
        self.situation.add_action(3, 1)
        self.situation.add_action(6, 2.4)
        self.situation.add_action(3, 8)        

    
        decision = self.startegy.get_decision(situation=self.situation)

        self.assertEqual(decision.decision, Decision.FOLD)

    def test_should_call_AQ_on_flop_after_calling_3bet_pre_when_having_flush_draw(self):

        hand = list()
        hand.append(Card(figure=Figure.Ace,color=Color.Spade))
        hand.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.set_hand(hand)

        self.situation.ButtonPosition = 1
        self.situation.add_action(2, 0.5)
        self.situation.add_action(3, 1)
        self.situation.add_action(6, 2.4)
        self.situation.add_action(3, 8)    
        
        board = list()
        board.append(Card(figure=Figure.King,color=Color.Spade))
        board.append(Card(figure=Figure.Three,color=Color.Spade))
        board.append(Card(figure=Figure.Seven,color=Color.Club))


        self.situation.set_board(board)

        self.situation.add_action(3, 7)    
      
        decision = self.startegy.get_decision(situation=self.situation)

        self.assertEqual(decision.decision, Decision.CALL)


    def test_should_fold_AQ_on_flop_after_calling_3bet_pre_when_having_high_card(self):

        hand = list()
        hand.append(Card(figure=Figure.Ace,color=Color.Spade))
        hand.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.set_hand(hand)

        self.situation.ButtonPosition = 1
        self.situation.add_action(2, 0.5)
        self.situation.add_action(3, 1)
        self.situation.add_action(6, 2.4)
        self.situation.add_action(3, 8)    
        
        board = list()
        board.append(Card(figure=Figure.King,color=Color.Spade))
        board.append(Card(figure=Figure.Three,color=Color.Diamond))
        board.append(Card(figure=Figure.Seven,color=Color.Club))


        self.situation.set_board(board)

        self.situation.add_action(3, 7)    
      
        decision = self.startegy.get_decision(situation=self.situation)

        self.assertEqual(decision.decision, Decision.FOLD)


    def test_should_bet_turn_with_top_pair(self):
        hand = list()
        hand.append(Card(figure=Figure.Ace,color=Color.Spade))
        hand.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.set_hand(hand)

        self.situation.ButtonPosition = 1
        self.situation.add_action(2, 0.5)
        self.situation.add_action(3, 1)
        self.situation.add_action(6, 2.4) 
        
        board = list()
        board.append(Card(figure=Figure.King,color=Color.Spade))
        board.append(Card(figure=Figure.Three,color=Color.Diamond))
        board.append(Card(figure=Figure.Seven,color=Color.Club))

        self.situation.set_board(board)

        self.situation.add_action(6, 3)
        board.append(Card(figure=Figure.Ace,color=Color.Heart)) 

        self.situation.set_board(board)

        decision = self.startegy.get_decision(situation=self.situation)

        self.assertEqual(decision.decision, Decision.RAISE)

    def test_should_fold_turn_with_top_pair_with_4_to_color(self):
        hand = list()
        hand.append(Card(figure=Figure.Ace,color=Color.Spade))
        hand.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.set_hand(hand)

        self.situation.ButtonPosition = 1
        self.situation.add_action(2, 0.5)
        self.situation.add_action(3, 1)
        self.situation.add_action(6, 2.4) 
        
        board = list()
        board.append(Card(figure=Figure.King,color=Color.Diamond))
        board.append(Card(figure=Figure.Three,color=Color.Diamond))
        board.append(Card(figure=Figure.Seven,color=Color.Diamond))

        self.situation.set_board(board)

        self.situation.add_action(6, 3)

        turn = list()
        turn.append(Card(figure=Figure.King,color=Color.Diamond))
        turn.append(Card(figure=Figure.Three,color=Color.Diamond))
        turn.append(Card(figure=Figure.Seven,color=Color.Diamond))
        turn.append(Card(figure=Figure.Ace,color=Color.Diamond)) 

        self.situation.set_board(turn)

        self.situation.add_action(3, 7)

        decision = self.startegy.get_decision(situation=self.situation)

        self.assertEqual(decision.decision, Decision.FOLD)
        
    def test_should_fold_river_with_tp_when_bet_bet_bet(self):
        
        hand = list()
        hand.append(Card(figure=Figure.Ace,color=Color.Spade))
        hand.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.set_hand(hand)

        self.situation.ButtonPosition = 1
        self.situation.add_action(2, 0.5)
        self.situation.add_action(3, 1)
        self.situation.add_action(6, 2.4) 
        
        board = list()
        board.append(Card(figure=Figure.King,color=Color.Heart))
        board.append(Card(figure=Figure.Three,color=Color.Diamond))
        board.append(Card(figure=Figure.Seven,color=Color.Club))

        self.situation.set_board(board)

        self.situation.add_action(3, 3)

        turn = list()
        turn.append(Card(figure=Figure.King,color=Color.Heart))
        turn.append(Card(figure=Figure.Three,color=Color.Diamond))
        turn.append(Card(figure=Figure.Seven,color=Color.Club))
        turn.append(Card(figure=Figure.Ace,color=Color.Spade)) 

        self.situation.set_board(turn)

        self.situation.add_action(3, 7)

        river = list()
        river.append(Card(figure=Figure.King,color=Color.Heart))
        river.append(Card(figure=Figure.Three,color=Color.Diamond))
        river.append(Card(figure=Figure.Seven,color=Color.Club))
        river.append(Card(figure=Figure.Ace,color=Color.Heart)) 
        river.append(Card(figure=Figure.Four,color=Color.Heart)) 

        self.situation.set_board(river)

        self.situation.add_action(3, 7)

        decision = self.startegy.get_decision(situation=self.situation)

        self.assertEqual(decision.decision, Decision.FOLD)


    def test_should_call_river_with_tp_when_only_bet_on_river(self):
        
        hand = list()
        hand.append(Card(figure=Figure.Ace,color=Color.Spade))
        hand.append(Card(figure=Figure.Queen,color=Color.Spade))
        self.situation.set_hand(hand)

        self.situation.ButtonPosition = 1
        self.situation.add_action(2, 0.5)
        self.situation.add_action(3, 1)
        self.situation.add_action(6, 2.4) 
        
        board = list()
        board.append(Card(figure=Figure.King,color=Color.Heart))
        board.append(Card(figure=Figure.Three,color=Color.Diamond))
        board.append(Card(figure=Figure.Seven,color=Color.Club))

        self.situation.set_board(board)

        # self.situation.add_action(3, 3)

        turn = list()
        turn.append(Card(figure=Figure.King,color=Color.Heart))
        turn.append(Card(figure=Figure.Three,color=Color.Diamond))
        turn.append(Card(figure=Figure.Seven,color=Color.Club))
        turn.append(Card(figure=Figure.Ace,color=Color.Spade)) 

        self.situation.set_board(turn)

        # self.situation.add_action(3, 7)

        river = list()
        river.append(Card(figure=Figure.King,color=Color.Heart))
        river.append(Card(figure=Figure.Three,color=Color.Diamond))
        river.append(Card(figure=Figure.Seven,color=Color.Club))
        river.append(Card(figure=Figure.Ace,color=Color.Heart)) 
        river.append(Card(figure=Figure.Four,color=Color.Heart)) 

        self.situation.set_board(river)

        self.situation.add_action(3, 7)

        decision = self.startegy.get_decision(situation=self.situation)

        self.assertEqual(decision.decision, Decision.CALL)