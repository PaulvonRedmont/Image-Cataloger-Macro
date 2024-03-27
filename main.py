import pyautogui
import pyperclip
import keyboard
import pytesseract
import re
from colorama import Fore
from datetime import datetime

end_of_book_file_path = None

tesseract_path = r'C:\Users\paule\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Import functions for handling book count
def write_book_count(count):
    with open(r'C:\Users\paule\Downloads\Auto Cataloger Backend Data.txt', 'w') as file:
        file.write(str(count))

def read_book_count():
    try:
        with open(r'C:\Users\paule\Downloads\Auto Cataloger Backend Data.txt', 'r') as file:
            content = file.read().strip()
        if content:
            return int(content)
        else:
            return 0
    except FileNotFoundError:
        return 0

def increment_book_count():
    count = read_book_count()
    count += 1
    write_book_count(count)

def get_book_count():
    return read_book_count()

# Initialize variables
use_ascii = True
text_colour = Fore.RED
copied_text = None
number_of_books_cataloged = get_book_count()  # Initialize book count

# Update the file path
file_path = r'C:\Users\paule\Downloads\Auto Cataloger Log.txt'

# Function to write cataloged book information to a text file
def write_to_file(info):
    with open(file_path, 'a') as file:
        file.write(info + '\n')

def get_image_path():
    global copied_text
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
    # Convert text to lowercase and capitalize the first letter of each word
    cleaned_text = raw_text.lower()
    cleaned_text = ' '.join(word.capitalize() for word in cleaned_text.split())
    return cleaned_text

def copy_it(cleaned_text, copied_text):
    # Combine and copy the text to clipboard
    combined_text = (f"{cleaned_text} FILE PATH: {copied_text}")
    pyperclip.copy(combined_text)
    print(f"Copied to clipboard: {combined_text}")


def print_end_of_book():
    global end_of_book_file_path
    pyautogui.hotkey('ctrl', 'shift', 'c')
    end_of_book_file_path = pyperclip.paste().strip('\"')
    print("End of book file path:", end_of_book_file_path)

def run_program():
    global number_of_books_cataloged
    global copied_text
    global end_of_book_file_path
    get_image_path()
    raw_text = ocr_it(copied_text)
    cleaned_text = clean_text(raw_text)
    copy_it(cleaned_text, copied_text)
    print("Cleaned OCR Result:")
    print(cleaned_text)
    print("+=============================================================+")
    number_of_books_cataloged += 1
    print(f"This OP macro has helped you catalog {number_of_books_cataloged} books total, with (hopefully) flawless precision and grace")

    # Create a string containing book information and current date and time
    book_info = f"""
=================================================================================================================== 
Book number {number_of_books_cataloged} catalogged: {cleaned_text}
    
File Path: {copied_text} 
    
Date & Time of book cataloged: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

This book ends at: {end_of_book_file_path}
===================================================================================================================
"""

    # Write the information to the file
    write_to_file(book_info)

    # Increment the book count after cataloging
    increment_book_count()

def run_macro():
    keyboard.add_hotkey('b', run_program)  # Run the program when 'b' is pressed
    keyboard.add_hotkey('e', print_end_of_book)  # Print end of book when 'e' is pressed
    keyboard.wait('esc')

run_macro()
