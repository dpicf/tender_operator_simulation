from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
import pyperclip


def mouse_pos_click(x, y):
    mouse.position = (x, y)
    time.sleep(2)
    mouse.click(Button.left, 1)
    time.sleep(2)


def begin_opening_lots():  # открытие списка всех лотов
    mouse_pos_click(351, 15)  # клик на вкладку СЭДа
    mouse_pos_click(66, 290)  # на Заявки
    mouse_pos_click(587, 140)  # на ДКРП
    mouse_pos_click(667, 156)  # на Работа с конкурсами
    mouse_pos_click(677, 177)  # на Реестр регистрации


def sed_error():  # Проверка вылета СЭД
    mouse.position = (190, 222); time.sleep(2)  # на "Регистрация"
    mouse.click(Button.left, 2); time.sleep(2)

    with keyboard.pressed(Key.ctrl):  # скопировать в буффер обмена
        keyboard.press('c')
        keyboard.release('c')

    value_error_sed = pyperclip.paste()

    if value_error_sed == 'Регистрация':
        return False
    else:
        return True


def lot_no_sed():  # Ошибка отсутствия лота в СЭД
    mouse.position = (621, 120); time.sleep(2)  # на Документ не найден
    mouse.click(Button.left, 2); time.sleep(2)

    with keyboard.pressed(Key.ctrl):  # скопировать в буффер обмена
        keyboard.press('c')
        keyboard.release('c')

    value_lot_no_sed = pyperclip.paste()

    if value_lot_no_sed == 'Документ':
        return True
    else:
        return False


def lot_opened_someone():
    mouse_pos_click(34, 305)  # на ссылку с номером лота

    time.sleep(7)  # Подождать пока прогрузится

    keyboard.press(Key.enter); keyboard.release(Key.enter)  # Enter

    time.sleep(7)  # Подождать пока прогрузится

