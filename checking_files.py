import time
import glob
import os
import fitz
import docx2txt
from keywords import keywords_comment
from bs4 import BeautifulSoup
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import pyperclip
import re
import requests


def check_comment(folder_name):  # проверка комментария на стопслова
    frame = open(f"/docs/{folder_name}/frame.html", encoding="utf8")
    soup = BeautifulSoup(frame, "html.parser")
    for keyword in keywords_comment:
        if keyword in soup.text:
            pass  # написать письмо с отказом в ГП и самому себе


def opening_frame():  # открытие фрейма
    mouse.position = (1184, 482); time.sleep(2)  # ПК на пустое поле в СЭД
    mouse.click(Button.right, 1); time.sleep(2)

    i = 0
    while i < 8:
        i += 1
        keyboard.press(Key.down.value); keyboard.release(Key.down.value); time.sleep(2)  # просмотр кода фрейма

    keyboard.press(Key.enter.value); keyboard.release(Key.enter.value); time.sleep(2)


def create_list_links(folder_name):  # извлечение линков и запись их в массив
    opening_frame()

    mouse.position = (710, 17); time.sleep(2)  # закрытие вкладки с кодом
    mouse.click(Button.left, 1); time.sleep(2)

    opening_frame()

    with keyboard.pressed(Key.ctrl):  # выделить всё
        keyboard.press('a'); keyboard.release('a')
    time.sleep(2)

    with keyboard.pressed(Key.ctrl):  # скопировать содержимое
        keyboard.press('c'); keyboard.release('c')
    time.sleep(2)

    # создание файла с кодом из фрейма
    os.mkdir(f"/LOTS/{folder_name}")  # создать папку с номером лота
    frame = open(f"/LOTS/{folder_name}/frame.html", "w+")  # открыть файл с кодом страницы
    frame.write(pyperclip.paste())  # вставить в него код
    frame.close()  # сохранить файл

    # извлечение ссылок с документами и запись их в массив
    list_links = []
    file = open("/LOTS/{folder_name}/frame.html", encoding="utf8")
    soup = BeautifulSoup(file, "html.parser")
    for link in soup.find_all(attrs={"href": re.compile("^fdoc_")}):
        list_links.append(f"address//{link.get('href')}")


def download_docs(list_links):  # скачивание документов
    for link in list_links:
        file_name = link.rsplit('/')[-1]  # извлечение имени файла
        request = requests.get(link, allow_redirects=True)  # запрос содержимого файла
        open(file_name, 'wb').write(request.content)  # создание файла

