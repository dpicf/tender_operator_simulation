import datetime
import easyimap
import re


list_lots = []
letters = {}


def create_lots_and_emails(login, password):
    imapper = easyimap.connect('imap.komus.ru', login, password)
    today = datetime.datetime.today()
    for mail_id in imapper.listids(limit=50):
        mail = imapper.mail(mail_id)
        if "Зарегистрирован" in mail.title and f"{today:%d}.{today:%m}" in mail.title:
            num_lot = re.findall(r'N[0-9]{6}', mail.title)
            num_lot = num_lot[0].replace("N", "")
            if num_lot not in list_lots:
                list_lots.append(num_lot)
                letters[mail.title] = mail.body


def get_current_lot():  # Получение номера текущего лота
    return list_lots.pop()