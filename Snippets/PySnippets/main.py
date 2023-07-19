from pynput import keyboard
import time

Snippets = {
    'hh1': '# ',
    'hh2': '## ',
    'hh3': '### ',
    'hh4': '#### '
}

typing_word = []


def replace_word(key, snippet):
    try:
        # Delete Key
        for e in range (len(key) + 1):
            time.sleep(0.05)
            keyboard.Controller().press(keyboard.Key.backspace)

        keyboard.Controller().release(keyboard.Key.backspace)

        # Enter snippet
        keyboard.Controller().type(snippet)

    except Exception as ex:
        print(ex)


def check_for_snippet(typedword):
    if typedword in Snippets.keys():
        return True


def on_press(key):
    try:
        typing_word.append(key.char)
    except AttributeError:
        if key == keyboard.Key.backspace:
            if(len(typing_word) > 0):
                typing_word.pop()


def on_release(key):
    if key == keyboard.Key.space:
        # Check for any matching snippets
        typed_word = ''.join([str(letter) for letter in typing_word])
        print(typed_word)

        if check_for_snippet(typed_word):
            replace_word(typed_word, Snippets[typed_word])
            typing_word.clear()
    
        else:
            typing_word.clear()

    if key == keyboard.Key.backspace:
        if(len(typing_word) > 0):
            typing_word.pop()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
