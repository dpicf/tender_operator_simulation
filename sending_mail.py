from bs4 import BeautifulSoup
from keywords import keywords_comment


def check_comment(folder_name):  # проверка комментария на стопслова
    frame = open(f"/docs/{folder_name}/frame.html", encoding="utf8")
    soup = BeautifulSoup(frame, "html.parser")
    for keyword in keywords_comment:
        if keyword in soup.text:
            pass  # написать письмо с отказом в ГП и самому себе


def sending_mail_reject(rejection_reason, list_receivers):
    pass