import pyautogui as p
import time as t
import pytesseract
from PIL import Image
import PIL.ImageOps
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

a,b = 0,0
while a==0 and b==0:
    try:
        a,b = p.locateCenterOnScreen("Start.JPG",confidence=0.7)
    except TypeError:
        pass

p.click(a,b)

while True:
    t.sleep(1)
    image = p.screenshot(region=(10,260,1346,100))
    image = image.convert("L")
    image = PIL.ImageOps.invert(image)
    pixels = image.load()
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if pixels[x,y] > 10:
                pixels[x,y] = 255
            else:
                pixels[x,y] = 0
    
    number = pytesseract.image_to_string(image, config="--psm 8] --oem 1 -c tessedit_char_whitelist=0123456789 classify_max_slope=20 classify_min_slope=0.2 textord_tabfind_vertical_text=0 language_model_penalty_non_dict_word=0 language_model_penalty_non_freq_dict_word")
    print(number)
    
    a,b = 0,0
    while a==0 and b==0:
        try:
            a,b = p.locateCenterOnScreen("Submit.JPG",confidence=0.7)
        except TypeError:
            pass

    t.sleep(.2)
    p.write(number)
    for x in range(2):
        p.press("enter")
    
    
