import time
import glob
import os
import fitz
import docx2txt
from keywords import keywords_files
from bs4 import BeautifulSoup
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import pyperclip
import re
import requests


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
    file = open(f"/LOTS/{folder_name}/frame.html", encoding="utf8")
    soup = BeautifulSoup(file, "html.parser")
    for link in soup.find_all(attrs={"href": re.compile("^fdoc_")}):
        list_links.append(f"address//{link.get('href')}")


def download_docs(list_links):  # скачивание документов
    for link in list_links:
        file_name = link.rsplit('/')[-1]  # извлечение имени файла
        request = requests.get(link, allow_redirects=True)  # запрос содержимого файла
        open(file_name, 'wb').write(request.content)  # создание файла


def check_docs(folder_name):  # проверка файлов
    list_files = glob.glob(f"/LOTS/{folder_name}/*.*")

    def find_concurrence(text):
        for phrase in keywords_files:
            if phrase in text:
                pass  # написать письмо с отказом Наташе

    for file in list_files:
        if "pdf" in file:
            pdf = fitz.open(file)
            i_page = 0
            while i_page < pdf.pageCount:
                page = pdf.loadPage(i_page)
                page_text = page.getText("text")
                find_concurrence(page_text)
                i_page += 1

        elif "docx" in file:
            all_text = docx2txt.process(file)
            find_concurrence(all_text)

        elif "doc" in file and "docx" not in file:
            with open(file) as file_in:
                with open(f"{file}.txt", "w") as file_out:
                    for line in file_in:
                        file_out.write(line)
            txt_text = open(f"{file}.txt", encoding="cp1251")
            doc_text = txt_text.read()
            find_concurrence(doc_text)
