from PIL import Image
import time
import pyperclip
import pytesseract
import os

# Uses Tesseract (pytesseract) OCR to extract text from image and return without leading/trailing whitespace.
def extractText(imagePath):
    text = (pytesseract.image_to_string(Image.open(imagePath), lang='jpn+eng'))
    return text.strip()

# Returns true if file at `image_path` is a valid image, false otherwise.
def is_valid_image(image_path):
    if image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        try:
            image = Image.open(image_path)
            image.verify()  # Verify the image integrity
            return True
        except (IOError, SyntaxError):
            return False

# TODO: Make `source_folder` into command line argument.
# IMPORTANT: Use a dedicated folder for `source_folder`!
# Program will OCR and delete any images in `source_folder` that contain text.
source_folder = "~/.quickshot_temp/"

source_folder = os.path.expanduser(source_folder)
print(f"Watching: {source_folder}")
while True:
    # List filenames in source_folder.
    files = os.listdir(source_folder) 
    for file in files:
        full_path = os.path.join(source_folder, file)
        if is_valid_image(full_path):
            text = extractText(full_path)
            if text != "":
                print(f"{file} contains text: \n{text}")
                pyperclip.copy(text)
                print("Text copied to clipboard")
                os.remove(full_path)
                print("Temp image deleted: ", full_path)
    time.sleep(0.1)