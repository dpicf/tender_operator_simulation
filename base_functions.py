#тестовое измнение

from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller
keyboard = Controller()

import time
import pyperclip
import datetime


false_error_sed = 'Регистрация'


def mouse_pos_click(x, y):
    mouse.position = (x, y)
    time.sleep(2)
    mouse.click(Button.left, 1)
    time.sleep(2)



def begin_opening_lots(): #открытие списка всех лотов
    mouse_pos_click(351, 15) #клик на вкладку СЭДа
    mouse_pos_click(66, 290) #ПК на Заявки
    mouse_pos_click(587, 140) #ПК на ДКРП
    mouse_pos_click(667, 156) #ПК на Работа с конкурсами
    mouse_pos_click(677, 177) #ПК на Реестр регистрации



def sed_error(): #Проверка вылета СЭД
    mouse.position = (190, 222); time.sleep(2) #ПК на "Регистрация"
    mouse.click(Button.left, 2); time.sleep(2)

    with keyboard.pressed(Key.ctrl): #скопировать в буффер обмена
        keyboard.press('c')
        keyboard.release('c')

    value_error_sed = pyperclip.paste()

    if value_error_sed == false_error_sed:
        return False
    else:
        return True
