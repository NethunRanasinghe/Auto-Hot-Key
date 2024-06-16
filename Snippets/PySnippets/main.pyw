import time
from datetime import datetime
from pynput.keyboard import Key, Controller, Listener

# Define the snippet dictionary
SNIPPETS = {
    'hh1': '# ',
    'hh2': '## ',
    'hh3': '### ',
    'hh4': '#### ',
    '!note': '> [!note]',
    '!tldr': '> [!tldr]',
    '!tip': '> [!tip]',
    '!success': '> [!success]',
    '!question': '> [!question]',
    '!fail': '> [!fail]',
    '!error': '> [!error]',
    '!bug': '> [!bug]',
    '!example': '> [!example]',
    '!quote': '> [!quote]',
    '!all': '> [!note]\n\n> [!tldr]\n\n> [!tip]\n\n> [!success]\n\n> [!question]\n\n> [!fail]\n\n> [!error]\n\n> [!bug]\n\n> [!example]\n\n> [!quote]\n\n'
}

typing_word = []

# Logger function
def log_exception(exception_message):
    with open('log', 'a') as file:
        file.write(f'{exception_message}\n')

# Function to replace typed word with snippet
def replace_word(key, snippet):
    try:
        # Delete the typed key
        for _ in range(len(key) + 1):
            time.sleep(0.05)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        
        # Type the snippet
        keyboard.type(snippet)
    except Exception as ex:
        exception_message = f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} : {ex}'
        log_exception(exception_message)

# Function to check if typed word is a snippet
def is_snippet(typed_word):
    return typed_word in SNIPPETS

# Listener event for key press
def on_press(key):
    try:
        typing_word.append(key.char)
    except AttributeError:
        if key == Key.backspace and typing_word:
            typing_word.pop()
        if key == Key.enter:
            typing_word.clear()

# Listener event for key release
def on_release(key):
    if key == Key.space:
        # Convert the list of characters to a string
        typed_word = ''.join(typing_word)
        
        if is_snippet(typed_word):
            replace_word(typed_word, SNIPPETS[typed_word])
        typing_word.clear()

    if key in (Key.backspace, Key.enter):
        typing_word.clear()

# Initialize the keyboard controller
keyboard = Controller()

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
