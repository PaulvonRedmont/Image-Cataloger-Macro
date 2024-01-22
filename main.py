import time
import pyautogui
import pyperclip
import keyboard
import pytesseract
import re
#import datetime

copied_text = None

tesseract_path = r'C:\Users\paule\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

#timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_image_path():
    global copied_text
    time.sleep(1)
    pyautogui.keyDown('shift')
    pyautogui.rightClick()
    pyautogui.keyUp('shift')
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
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
    

def run_program():
    global copied_text
    get_image_path()
    raw_text = ocr_it(copied_text)
    cleaned_text = clean_text(raw_text)
    copy_it(cleaned_text, copied_text)
    print("Cleaned OCR Result:")
    print(cleaned_text)
    print("+=============================================================+")

keyboard.add_hotkey('F5', run_program)
keyboard.wait('esc')

