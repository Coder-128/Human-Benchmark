import pyautogui as p
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

import time as t
from PIL import Image

reg = (200,290,950,160)


t.sleep(3)
p.moveTo(100,100)
t.sleep(.2)
image = p.screenshot(region = reg)
text = pytesseract.image_to_string(image)
text = text.replace("\n", " ")
text = text.replace("|", "I")
p.click(250,350)
t.sleep(1)
p.write(text)

