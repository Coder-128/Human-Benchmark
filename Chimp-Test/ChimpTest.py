import pyautogui as p
import pytesseract
from PIL import Image
import PIL.ImageOps
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Tesseract-OCR\tesseract.exe'
import time as t

a,b = 0,0
while a==0 and b==0:
    try:
        a,b = p.locateCenterOnScreen("Start.JPG",confidence=0.7)
    except TypeError:
        pass

p.click(a,b)

columns = 8
rows = 5
squareSize = 88
numbers = 4

while True:
    t.sleep(1)
    p.moveTo(100,100)
    image = p.screenshot(region = (320, 96, columns * squareSize, rows * squareSize))
    image = image.convert("L")
    image = PIL.ImageOps.invert(image)
    pixels = image.load()
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if pixels[x,y] > 10:
                pixels[x,y] = 255
            else:
                pixels[x,y] = 0

    coords = [(0,0)] * numbers
    grid = []
    for y in range(rows):
        row = []
        for x in range(columns):
            digit = pytesseract.image_to_string(image.crop((x * squareSize, y * squareSize, (x+1) * squareSize, (y+1) * squareSize)), config="--psm 10 --oem 2 -c tessedit_char_whitelist=0123456789 classify_max_slope=20 classify_min_slope=0.2")
            digit = digit[:-2]
            if digit.isdigit():
                coords[int(digit)-1] = ((x+0.5)*squareSize,(y+0.5)*squareSize)
            row.append(digit)
            print("At " + str(x) + "," + str(y) + " pytesseract saw: " + digit)
            
        grid.append(row)

    print(grid)

    for z in range(numbers):
        p.click(coords[z][0]+320,coords[z][1]+96)    
    
    a,b = 0,0
    while a==0 and b==0:
        try:
            a,b = p.locateCenterOnScreen("Continue.JPG",confidence=0.7)
        except TypeError:
            pass

    p.click(a,b)
    numbers += 1

