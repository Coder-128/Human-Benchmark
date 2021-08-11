import pyautogui as p
import time as t
from PIL import Image

reg = (465,130,415,450)
levelReg = (643,70,60,40)
complete = False

a = 0
b = 0
while(a==0 and b==0):
    try:
        a,b = p.locateCenterOnScreen("Start.JPG",confidence=0.7, grayscale=True)
    except TypeError:
        pass

p.click(a,b)
p.moveTo(100,100)
t.sleep(1)

while True:
    complete = False
    screen1 = p.screenshot(region = reg)
    t.sleep(1)
    screen2 = p.screenshot(region = reg)
    level = p.screenshot(region = levelReg)
    
    for x in range(0,screen1.width,19):
        if complete == True:
            break
        
        for y in range(0,screen1.height,19):
            if complete == True:
                break
            
            if(screen1.getpixel((x,y)) != screen2.getpixel((x,y))):
                p.click(x+465,y+150)
                p.moveTo(100,100)
                t.sleep(.15)
                screen2 = p.screenshot(region = reg)

                try:
                    a,b = p.locateCenterOnScreen(level,confidence=0.7, grayscale=True, region = levelReg)
                except TypeError:
                    #print(str(t.time()) + "Level changed")
                    complete = True

    #print(str(t.time()) + "Pass complete")
    t.sleep(1.5)
    p.moveTo(100,100)

                
                

