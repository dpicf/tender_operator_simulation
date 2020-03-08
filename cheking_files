import time
import glob
import os
import fitz
import docx2txt
from keywords import keywords_comment
from bs4 import BeautifulSoup


def check_comment(): #проверка комментария на стопслова
    frame = open("C:/docs/frame3.html", encoding="utf8")
    soup = BeautifulSoup(frame, "html.parser")
    for keyword in keywords_comment:
        if keyword in soup.text:
            #отправить письмо