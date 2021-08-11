import pyautogui as p
import time as t

a = 0
b = 0
while (a==0 and b==0):
    try:
        a,b = p.locateCenterOnScreen("Start.JPG", confidence = 0.7, grayscale = True)
    except TypeError:
        pass

p.click(a,b)

while True:
    t.sleep(1)
    screen1 = p.screenshot(region = (465,150,415,400))
    screen2 = p.screenshot(region = (465,150,415,400))
    for x in range(screen2.width):
        for y in range(screen2.height):
            if(screen1.pixel(x,y) != screen2.pixel(x,y)):
                click(x,y)
                screen2 = p.screenshot(region = (465,150,415,400))

        t.sleep(2)
        print("Pass complete")
