from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
import pyperclip
import datetime
from base_functions import mouse_pos_click
import easyimap
import re


def get_list_lots():
    login = '********'
    password = '********'
    imapper = easyimap.connect('imap.*****.***', login, password)
    today = datetime.datetime.today()
    list_lots = []
    for mail_id in imapper.listids(limit=50):
        mail = imapper.mail(mail_id)
        if "Зарегистрирован" in mail.title and "************" in mail.title and f"{today:%d}.{today:%m}" in mail.title:
            title_list = mail.title.split()
            for iter in title_list:
                if re.match(r'N[0-9]{6}', iter):
                    num_lot = iter.replace("N", "")
                    list_lots.append(num_lot)

    return list_lots,