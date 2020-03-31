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

class bot:
    
    def __init__(self):
        self.i = 1
        self.board_reader = board_reader.BoardReader()

    def do_smth(self, image):
        print("got new image")
        self.i+=1
        cv2.imwrite(str(self.i) + ".jpg",image)
        # 1. Is it my turn?
        if not self.board_reader.is_hero_acting(screen=image):
            return
        
        
        # 2. Read board
        board = self.board_reader.get_board(screen = image)

        # 3. Decide how to act

        
        # 4. act



bot = bot()


# watcher  = sw.screen_watcher() 
# watcher.on_new_screen.subscribe(lambda value: bot.do_smth(value))
# thread = threading.Thread(target=watcher.screenshotInLoop, args=())
# thread.start()

image = cv2.imread("sample8_resized.jpg")
bot.do_smth(image)

