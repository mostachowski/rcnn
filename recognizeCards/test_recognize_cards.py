# import unittest
# import recognize_cards as rc
# import cv2
# from PokerDto import Card,Figure,Color
# import os


# class RecognizeCardsTest(unittest.TestCase):
  
#     def setUp(self) -> None:
#         self.TESTDATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')

#     def test_recognize_cards(self):

#         recon = rc.CardsRecon()
#         image = cv2.imread(self.TESTDATA_DIR + "/board.png")

#         print(image.shape)
#         result = recon.recognize_cards(image = image)
#         self.assertEqual(len(result),5)
#         self.assertEqual(any(x.Figure == Figure.King and x.Color == Color.Spade for x in result),True)
#         self.assertEqual(any(x.Figure == Figure.Nine and x.Color == Color.Heart for x in result),True)
#         self.assertEqual(any(x.Figure == Figure.Jack and x.Color == Color.Spade for x in result),True)
#         self.assertEqual(any(x.Figure == Figure.Four and x.Color == Color.Spade for x in result),True)
#         self.assertEqual(any(x.Figure == Figure.Two and x.Color == Color.Club for x in result),True)

#     # def test_recognize_button(self):
#     #     recon = rc.CardsRecon()
#     #     image = cv2.imread(self.TESTDATA_DIR + "/board.png")
#     #     result = recon.recognize_cards(image = image)
#     #     self.assertEqual(len(result),5)
#     #     self.assertEqual(any(x.Figure == Figure.King and x.Color == Color.Spade for x in result),True)
#     #     self.assertEqual(any(x.Figure == Figure.Nine and x.Color == Color.Heart for x in result),True)
#     #     self.assertEqual(any(x.Figure == Figure.Jack and x.Color == Color.Spade for x in result),True)
#     #     self.assertEqual(any(x.Figure == Figure.Four and x.Color == Color.Spade for x in result),True)
#     #     self.assertEqual(any(x.Figure == Figure.Two and x.Color == Color.Club for x in result),True)