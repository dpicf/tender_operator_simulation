from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
from base_functions import mouse_pos_click, begin_opening_lots
from mail_preparation import start
from opening_lots import current_lot_func, opening_lot, lot_perfomance


list_lots = []

time.sleep(5)

with keyboard.pressed(Key.cmd): #свернуть все окна
    keyboard.press('d')
    keyboard.release('d')
    
mouse_pos_click(271, 874) #на браузер в панели инструментов. КЛКМ

begin_opening_lots(); time.sleep(2)
start(); time.sleep(2)

current_lot = current_lot_func()
while(current_lot in list_lots): #если лот есть в списке, брать из почты новый лот
    current_lot = current_lot_func()
time.sleep(2)

list_lots.append(current_lot); time.sleep(2)

opening_lot(current_lot); time.sleep(2)

lot_perfomance(); time.sleep(2)


