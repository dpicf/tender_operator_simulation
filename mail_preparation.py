from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
import pyperclip
import datetime
from base_functions import mouse_pos_click


def start():
    with keyboard.pressed(Key.cmd):  # свернуть все окна
        keyboard.press('d')
        keyboard.release('d')

    mouse_pos_click(413, 877)  # переместить курсор на почтовый клиент
    mouse_pos_click(70, 99)  # на входящие письма
    mouse_pos_click(993, 86)  # на быстрый фильтр сообщений

    today = datetime.datetime.today()
    time.sleep(2)
    pyperclip.copy(f"sed@komus.net {today:%d}.{today:%m}")  # скопировать в буфер строку с датой
    time.sleep(2)

    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')

    time.sleep(10)

    mouse_pos_click(203, 88)  # на кнопку Непрочитанные

    time.sleep(10)


