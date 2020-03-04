import pyautogui
import time
from mss import mss

start_x = 300
start_y = 800

bbox = (start_x, start_y, start_x + 300, start_y + 1)


cord_x = [0, 100, 200, 299]


def test_time():
    with mass() as sct: 
        t1 = time.time()
        for i in range(1000):
            img = sct.grab(bbox)
            pyautogui,click (86, 300)
    t2 = time.time()
    print (t2 - t1)

def print_mouse_pos ():
        while True:
            print (pyautogui.position())

def start ():
    with mss() as sct:
        gg = 10
        while gg >= 1:
            img = sct.grab(bbox)
            for cord in cord_x:
                if img.pixel (cord, 0) [0] < 100:
                    pyautogui.click(start_x + cord, start_y)
                    print (pyautogui.position())
                    break

time.sleep (1)
start()