from PIL import Image
import pytesseract
import pathlib
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = ""

# Persion Pics Input
#for path in pathlib.Path(r"H:\My Life\Data\Example\image-to-text\Module\Text mining\Convert-type-text\farsi").iterdir():
for path in pathlib.Path(fr"farsi").iterdir():
    if path.is_file():
        img = path
        text += pytesseract.image_to_string(Image.open(img), lang="fas")
        text += 50 * "_"

# English Pics Input
for path in pathlib.Path(r"english").iterdir():
    if path.is_file():
        img = path
        eng = pytesseract.image_to_string(Image.open(img), lang="eng")
        
        text += 50 * "_"

# Create Persion Text File
with open("result/farsi.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Create English Text File
with open("result/english.txt", "w", encoding="utf-8") as f:
    f.write(eng)



