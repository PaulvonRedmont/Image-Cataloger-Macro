import time
import pyautogui
import pyperclip
import keyboard
import pytesseract
import re
import tkinter as tk
from datetime import datetime
from time import strftime
#import datetime

copied_text = None

number_of_screenshots = 0

number_of_books_catalogged = 0

tesseract_path = r'C:\Users\paule\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

#timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_image_path():
    global copied_text
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'c')
    copied_text = pyperclip.paste().strip('\"')
    print("Image File Path:", copied_text)

def ocr_it(image_path):
    # Use pytesseract for OCR
    text = pytesseract.image_to_string(image_path, lang='eng')

    # Print the OCR results
    print("+=============================================================")
    print("OCR Result:")
    print(text)
    print(f"The file path is: {copied_text}")
    print("+=============================================================")
    return text

def clean_text(raw_text):
    # Remove paragraph marks and extra whitespaces
    cleaned_text = re.sub(r'\n+', ' ', raw_text)
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text

def copy_it(cleaned_text, copied_text):
    # Combine and copy the text to clipboard
    combined_text = (f"{cleaned_text} FILE PATH: {copied_text}")
    pyperclip.copy(combined_text)
    print(f"Copied to clipboard: {combined_text}")
    
def take_screenshot():
    global number_of_screenshots
    screenshot = pyautogui.screenshot()
    number_of_screenshots += 1    
    screenshot_path = f"C:/Users/paul/Pictures/screenshot{number_of_screenshots}.png"
    screenshot.save(screenshot_path)
    print("Screenshot saved to", screenshot_path)



def run_program():
    global number_of_books_catalogged
    global copied_text
    take_screenshot()
    get_image_path()
    raw_text = ocr_it(copied_text)
    cleaned_text = clean_text(raw_text)
    copy_it(cleaned_text, copied_text)
    print("Cleaned OCR Result:")
    print(cleaned_text)
    print("+=============================================================+")
    number_of_books_catalogged += 1
    print(f"This OP macro has helped you catalog {number_of_books_catalogged} books, with (hopefully) flawless percision and grace")
    
keyboard.add_hotkey('F5', run_program)
keyboard.wait('esc')
