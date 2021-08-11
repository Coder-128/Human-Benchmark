import pyautogui as p
import time as t

pos1 = (545,215)
pos2 = (675,215)
pos3 = (800,215)
pos4 = (545,345)
pos5 = (675,345)
pos6 = (800,345)
pos7 = (545,485)
pos8 = (675,485)
pos9 = (800,485)

posList = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9]

sequence = ""
level = 1

def excecute(sequence):
    for x in range(len(sequence)):
        p.click(posList[int(sequence[x])][0],posList[int(sequence[x])][1])

def look():
    p.moveTo(100,100)
    for y in range(len(posList)):
        if p.pixelMatchesColor(posList[y][0],posList[y][1],(255,255,255)):
            return str(y)
        
a,b = 0,0
while(a == 0 and b == 0):
    try:
        a,b = p.locateCenterOnScreen("Start.JPG",confidence = 0.7)
    except TypeError:
        pass

p.click(a,b)

while True:
    t.sleep(.25)
    sequence = ""
    for x in range(level):
        addition = ""
        while(addition == "" or addition == None):
            addition = look()
        t.sleep(.15)
        while(p.pixelMatchesColor(posList[int(addition)][0],posList[int(addition)][1],(255,255,255))):
              pass
        sequence += addition
              
    excecute(sequence)
    level += 1
