import pyautogui as p
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

from PIL import Image
import time as t

wordList = []
reg = (430,270,500,100)
seenPos = (600,400)
newPos = (740,400)

a,b = 0,0
while(a==0 and b==0):
    try:
        a,b = p.locateCenterOnScreen("Start.JPG", confidence = 0.65)
    except TypeError:
        pass
    
p.click(a,b)

while True:
    wordImage = p.screenshot(region = reg)
    word = pytesseract.image_to_string(wordImage)

    if(word in wordList):
        p.click(seenPos)
    else:
        wordList.append(word)
        p.click(newPos)
