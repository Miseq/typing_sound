from pynput import keyboard
import simpleaudio as sa




def on_press(key):
    try:
        if key.char >= 'a' and key.char <= 'z' and not wf.play().is_playing():
            wf.play()
    except AttributeError:
        pass
def on_release(key):
    pass

filename = "test.wav"
wf = sa.WaveObject.from_wave_file(filename)
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
