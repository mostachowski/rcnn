import pyautogui
import win32gui
import cv2
import time
import rx.subject 
import numpy

class screen_watcher:
    def __init__(self):
        self.i = 0
        self.on_new_screen = rx.subject.Subject()

    def screenshot(self, ):
        hwnd = win32gui.GetForegroundWindow()
        if hwnd:

            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)

            win32gui.ScreenToClient(hwnd,(x,y))

            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))

            print("x = ",x)
            print("y = ",y)
            print("x1 = ", x1)
            print("y1 = ",y1)


            im = pyautogui.screenshot(region=(x, y, x1, y1))
            im = im.convert('RGB')

            im = numpy.array(im)
            im = im[:, :, ::-1].copy() 
            self.i+=1
            # im.save(str(self.i) + ".jpg","JPEG")
            return im
        else:
            print('Window not found!')

    def screenshotInLoop(self):
        do = True
        while do:
            time.sleep(2)
            img  = self.screenshot()
            self.on_new_screen.on_next(img)


# sw = screen_watcher()
# sw.screenshotInLoop()

    

