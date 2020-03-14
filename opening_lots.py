import time
import pyperclip

from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
from help_functions import mouse_pos_click


def opening_lot(num_lot):  # Открытие лота
    with keyboard.pressed(Key.cmd):  # свернуть все окна
        keyboard.press('d')
        keyboard.release('d')

    mouse_pos_click(271, 874)  # на браузер в панели инструментов
    mouse_pos_click(19, 234)  # на поиск лота (Номер = ...)

    pyperclip.copy(num_lot)

    with keyboard.pressed(Key.ctrl):  # вставить номер лота
        keyboard.press('v')
        keyboard.release('v')

    mouse_pos_click(463, 256)  # на Кнопку Установить 463 256
    time.sleep(12)  # Подождать пока прогрузится


def lot_performance():  # Исполнение лота (активно окно браузера)
    mouse_pos_click(1346, 141)  # Переместить курсор на кнопку Исполнить
    time.sleep(12)  # Подождать пока прогрузится

    keyboard.press(Key.enter); keyboard.release(Key.enter)
    time.sleep(2)  # Нажать Enter (на случай, если лот уже на исполнении)

    mouse_pos_click(34, 305)  # на ссылку с номером лота
    time.sleep(12)  # Подождать пока прогрузится





