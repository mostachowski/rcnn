import win32gui
import pyautogui
import random
import scipy
import time
from scipy import interpolate
import math
import ctypes
import PokerDto as dto
import TablePositions6Max as tp

class Clicker:

    
    def __init__(self):
        self.betTypesRects = {
            dto.BetType.Min : tp.TablePositions6Max.BetMin,
            dto.BetType.FourtyThree : tp.TablePositions6Max.Bet43Rect,
            dto.BetType.SixtySix : tp.TablePositions6Max.Bet66Rect,
            dto.BetType.Pot : tp.TablePositions6Max.BetPotRect,
            dto.BetType.AllIn : tp.TablePositions6Max.BetAllInRect
        }
    
    def _get_random_point_from_rect(self,rect):
        x,y,w,h = rect
        x1 = random.randrange(x,x + w)
        y1 = random.randrange(y,y + h)
        return (x1,y1)

    def _rescale_if_needed(self, point):

        w = tp.TablePositions6Max.Width
        h = tp.TablePositions6Max.Height


        hwnd = win32gui.GetForegroundWindow()

        win32gui.SetForegroundWindow(hwnd)
        x, y, x1, y1 = win32gui.GetClientRect(hwnd)
        win32gui.ScreenToClient(hwnd,(x,y))

        x, y = win32gui.ClientToScreen(hwnd, (x, y))
        x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))

        w_proportion = x1 / w
        h_proportion = y1 / h
        

        return (int(point[0] * w_proportion) +x, int(point[1] * h_proportion) + y)


    def bet(self,betType = dto.BetType.FourtyThree,bet = 0 ):
        print("bettype: ",betType)
        betRect = tp.TablePositions6Max.BetButton
        point = self._get_random_point_from_rect(betRect)
        betPoint = self._rescale_if_needed(point)
        
        if bet>0:
            betStr = str(bet).replace('.',',')
            interval = random.uniform(0.05,0.2)
            pyautogui.write(betStr, interval=interval)

        else:
            rect = self.betTypesRects[betType]
            point = self._get_random_point_from_rect(rect)
            point = self._rescale_if_needed(point)
            self.move_cursor(point[0],point[1])
            pyautogui.click()


        self.move_cursor(betPoint[0],betPoint[1])
        pyautogui.click()


    def call(self):

        callRect = tp.TablePositions6Max.CallCheckButton
        point = self._get_random_point_from_rect(callRect)
        point = self._rescale_if_needed(point)
        self.move_cursor(point[0],point[1])
        pyautogui.click()

    def fold(self):
        callRect = tp.TablePositions6Max.FoldButton
        point = self._get_random_point_from_rect(callRect)
        point = self._rescale_if_needed(point)

        self.move_cursor(point[0],point[1])
        pyautogui.click()

    def move_cursor(self, x2,y2):

        cp = random.randint(3, 5)  # Number of control points. Must be at least 2.
        x1, y1 = pyautogui.position()  # Starting position

        # Distribute control points between start and destination evenly.
        x = scipy.linspace(x1, x2, num=cp, dtype='int')
        y = scipy.linspace(y1, y2, num=cp, dtype='int')

        # Randomise inner points a bit (+-RND at most).
        RND = 10
        xr = scipy.random.randint(-RND, RND, size=cp)
        yr = scipy.random.randint(-RND, RND, size=cp)
        xr[0] = yr[0] = xr[-1] = yr[-1] = 0
        x += xr
        y += yr

        # Approximate using Bezier spline.
        degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
                                        # Must be less than number of control points.
        tck, u = scipy.interpolate.splprep([x, y], k=degree)
        u = scipy.linspace(0, 1, num=max(pyautogui.size()))
        points = scipy.interpolate.splev(u, tck)

        # Any duration less than this is rounded to 0.0 to instantly move the mouse.
        pyautogui.MINIMUM_DURATION = 1  # Default: 0.1
        # Minimal number of seconds to sleep between mouse moves.
        pyautogui.MINIMUM_SLEEP = 1 # Default: 0.05
        # The number of seconds to pause after EVERY public function call.
        pyautogui.PAUSE = 0  # Default: 0.1

        # Move mouse.
        iterator = 0
        duration = 0.0001

        timeout = duration / len(points[0])
        for point in zip(*(i.astype(int) for i in points)):
            iterator +=1
            pyautogui.moveTo(*point)
            if iterator % 15 == 0:
                time.sleep(0.001)
        
    def random_movement(self, top_left_corner, bottom_right_corner, min_speed=100, max_speed=200):
        '''speed is in pixels per second'''

        x_bound = top_left_corner[0], bottom_right_corner[0]
        y_bound = top_left_corner[1], bottom_right_corner[1]

        pos = (random.randrange(*x_bound),
                        random.randrange(*y_bound))

        speed = min_speed + random.random()*(max_speed-min_speed)
        direction = 2*math.pi*random.random()

        def get_new_val(min_val, max_val, val, delta=0.01):
            new_val = val + random.randrange(-1,2)*(max_val-min_val)*delta
            if new_val<min_val or new_val>max_val:
                return get_new_val(min_val, max_val, val, delta)
            return new_val

        def move_mouse(pos):
            x_pos, y_pos = pos
            screen_size = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
            x = int(65536 * x_pos / screen_size[0] + 1)
            y = int(65536 * y_pos / screen_size[1] + 1)

    

            return ctypes.windll.user32.mouse_event(32769, x, y, 0, 0)

        steps_per_second = 200.0
        while True:
            move_mouse(pos)
            time.sleep(1.0/steps_per_second) 

            speed = get_new_val(min_speed, max_speed, speed)
            direction+=random.randrange(-1,2)*math.pi/5.0*random.random()

            new_pos = (int(round(pos[0]+speed*math.cos(direction)/steps_per_second)),
                int(round(pos[1]+speed*math.sin(direction)/steps_per_second)))

            while new_pos[0] not in range(*x_bound) or new_pos[1] not in range(*y_bound):
                direction  = 2*math.pi*random.random()
                new_pos = (int(round(pos[0]+speed*math.cos(direction)/steps_per_second)),
                int(round(pos[1]+speed*math.sin(direction)/steps_per_second)))
            pos=new_pos



if __name__ == "__main__":
   
    clicker = Clicker()
    # clicker.random_movement((300,300),(600,600))
    clicker.move_cursor(700,870)
