from PIL import Image
import pytesseract

def extractText(imagePath):
    text = (pytesseract.image_to_string(Image.open(imagePath), lang='jpn+eng'))
    return text.strip()
