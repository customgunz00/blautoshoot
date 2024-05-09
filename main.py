from PIL import Image
import keyboard
import mss
import fade
import time
import os

os.system('title basketball legends autoshoot | made by customgunz00')
os.system('py ./cli.py')

def screenshot():
    with mss.mss() as sct:
        monitor = {"top": 367, "left": 901, "width": 1, "height": 1}
        img = sct.grab(monitor)

        img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
        img = img.convert("RGB")

        return img
    
while True:
    keyboard.wait('q')

    _time = time.time()

    keyboard.press('e')

    while True:
        img = screenshot()
        
        passed = 0

        for v in img.getpixel((0, 0)):
            if v >= 228:
                passed += 1

        if passed == 3:
            print(fade.purplepink(f"""\r- White detected... Releasing 'e' key
- Current time: {time.time()}
- Operation time: {time.time() - _time}"""))
            break

    keyboard.release('e')