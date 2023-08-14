from ocr import extractText
from PIL import Image
import time
import pyperclip
import os

def is_valid_image(image_path):
    if image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        try:
            image = Image.open(image_path)
            image.verify()  # Verify the image integrity
            return True
        except (IOError, SyntaxError):
            return False

def main():
    source_folder = "~/.quickshot_temp/"
    source_folder = os.path.expanduser(source_folder)
    print(f"Watching: {source_folder}")
    while True:
        files = os.listdir(source_folder) 
        for file in files:
            full_path = os.path.join(source_folder, file)
            
            if is_valid_image(full_path):
                image = Image.open(full_path)
                text = extractText(full_path)
                if text != "":
                    print(f"{file} contains text: \n{text}")
                    pyperclip.copy(text)
                    print("Text copied to clipboard")
                    os.remove(full_path)
                    print("File deleted")
        time.sleep(0.5)

if __name__ == "__main__":
    main()