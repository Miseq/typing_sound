from pynput import keyboard

def on_press(key):
    try:
        print(f'pressed key {key}')
    except AttributeError:
        print('Attribute Error')

def on_release(key):
    try:
        print('klick')
    except AttributeError:
        print('Attribute Error on realese')


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
