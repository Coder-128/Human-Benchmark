import pyautogui as p
import time

for x in range(5):
    while p.pixelMatchesColor(244,356,(75, 219, 106)) == False:
          pass

    p.click(244,356)
    time.sleep(0.1)
    p.click(244,356)
