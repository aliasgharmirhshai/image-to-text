from PIL import Image
import pytesseract
import pathlib

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = ""

# Persion Pics Input
for path in pathlib.Path(r"H:\My Life\Data\Example\convert\farsi").iterdir():
    if path.is_file():
        img = path
        text += pytesseract.image_to_string(Image.open(img), lang="fas")
        text += 50 * "_"

# English Pics Input
for path in pathlib.Path(r"H:\My Life\Data\Example\convert\english").iterdir():
    if path.is_file():
        img = path
        eng = pytesseract.image_to_string(Image.open(img), lang="eng")
        
        text += 50 * "_"

# Create Persion Text File
with open("farsi.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Create English Text File
with open("english.txt", "w", encoding="utf-8") as f:
    f.write(eng)


