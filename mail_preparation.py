from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller
keyboard = Controller()

import time
import pyperclip
import datetime

from base_functions import mouse_pos_click



def start():
    with keyboard.pressed(Key.cmd):
        keyboard.press('d')
        keyboard.release('d')

    mouse_pos_click(413, 877)
    mouse_pos_click(70, 99)
    mouse_pos_click(993, 86)

    today = datetime.datetime.today()
    time.sleep(2)
    pyperclip.copy(f"sed@komus.net {today:%d}.{today:%m}")
    time.sleep(2)

    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')

    time.sleep(10)

    mouse_pos_click(203, 88)

    time.sleep(10)


