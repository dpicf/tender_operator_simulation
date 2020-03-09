from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
from base_functions import mouse_pos_click
import time
import pyperclip


def current_lot_func():  # Получение номера текущего лота
    with keyboard.pressed(Key.cmd):  # свернуть все окна
        keyboard.press('d')
        keyboard.release('d')

    mouse_pos_click(413, 877)  # окно почты в панели инструментов

    mouse.position = (223, 87); time.sleep(2)  # на кнопку "Непрочитанные"
    mouse.click(Button.left, 1); time.sleep(10)  # два раза нажать ЛКМ
    mouse.click(Button.left, 1); time.sleep(10)

    mouse_pos_click(385, 154)  # на первое сверху письмо. Изначально (385, 134)

    mouse.position = (1010, 165); time.sleep(2)  # на номер Лота. Изначально (1010, 140)
    mouse.click(Button.left, 2); time.sleep(2)

    with keyboard.pressed(Key.ctrl):  # скопировать в буффер обмена
        keyboard.press('c')
        keyboard.release('c')

    number_lot = pyperclip.paste()

    return number_lot.replace("N", "")


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





