import pytesseract
from PIL import Image


im=Image.open("b.png")
print(im)
s=pytesseract.image_to_string(im)
print(s)