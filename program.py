from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
from base_functions import mouse_pos_click, begin_opening_lots, sed_error, lot_no_sed, lot_opened_someone
from mail_preparation import get_list_lots
from opening_lots import current_lot_func, opening_lot, lot_performance


def iteration_sed_error():
    if sed_error():  # Проверка вылета СЭД
        time.sleep(30)
        keyboard.press(Key.f5); keyboard.release(Key.f5)  # обновить страницу
        begin_opening_lots()
        opening_lot(current_lot)
        lot_performance()


list_completed_lots = []

time.sleep(3)

with keyboard.pressed(Key.cmd):  # свернуть все окна
    keyboard.press('d')
    keyboard.release('d')
    
mouse_pos_click(271, 874)  # на браузер в панели инструментов. КЛКМ

begin_opening_lots(); time.sleep(2)
get_list_lots(); time.sleep(2)

current_lot = current_lot_func()
while current_lot in list_completed_lots:  # если лот есть в списке, брать из почты новый лот
    current_lot = current_lot_func()
time.sleep(2)

list_completed_lots.append(current_lot); time.sleep(2)

opening_lot(current_lot); time.sleep(2)
if lot_no_sed():  # Ошибка отсутствия лота в СЭД
    quit()
lot_opened_someone()
lot_opened_someone()
lot_opened_someone()
iteration_sed_error()

lot_performance(); time.sleep(2)
iteration_sed_error()

