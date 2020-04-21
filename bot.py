import sys
sys.path.append('screen_watcher')
import screen_watcher.screen_watcher as sw
import board_reader
import time
import rx
import threading
import cv2
from PIL import Image
import numpy as np
import strategy6max as strategy
from PokerDto import Decision,TableAction,BetType
import clicker as clicker
import random

class bot:
    
    def __init__(self):
        self.i = 1
        self.board_reader = board_reader.BoardReader()
        self.strategy = strategy.Strategy6Max()
        self.clicker = clicker.Clicker()

    def do_smth(self, image):
        resized = self.board_reader.resize_if_needed(screen=image)
        # cv2.imwrite("9_resized.jpg",resized)
        print("got new image")
        self.i+=1
        cv2.imwrite("screenshots/" + str(self.i) + ".jpg",image)
        # 1. Is it my turn?
        if not self.board_reader.is_hero_acting(screen=resized):
            return
        
        
        # 2. Read board
        board = self.board_reader.get_board(screen = resized)

        # 3. Decide how to act

        decision = self.strategy.get_decision(situation=board)
        print("decision: ",decision.decision)
        
        # 4. act
        if decision.decision == Decision.RAISE:
            self.clicker.bet(betType=decision.betType, bet=decision.bet)
            board.add_action(6,bet = decision.bet,betType = decision.betType)
            
        else:   
            if decision.decision == Decision.CALL:
                self.clicker.call()
            else:
                if len(board.Board) == 0:
                    self.clicker.fold()
                else:    
                    if board.LastTableAction.value < TableAction.Raise.value:
                        self.clicker.call()
                    else:
                        self.clicker.fold()
        

bot = bot()

# watcher  = sw.screen_watcher() 
# watcher.on_new_screen.subscribe(lambda value: bot.do_smth(value))
# thread = threading.Thread(target=watcher.screenshotInLoop, args=())
# thread.start()

image = cv2.imread("screenshots/60.jpg")
bot.do_smth(image)

image = cv2.imread("screenshots/64.jpg")
bot.do_smth(image)


image = cv2.imread("screenshots/66.jpg")
bot.do_smth(image)


