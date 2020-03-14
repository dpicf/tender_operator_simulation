import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from bs4 import BeautifulSoup
from keywords import KEYWORDS_COMMENT
from lots_and_emails import letters


def sending_mail_reject(login, password, reject_reason, folder_lot_name):
    def check_comment():  # проверка комментария на стопслова
        frame = open(f"/LOTS/{folder_lot_name}/frame.html", encoding="utf8")
        soup = BeautifulSoup(frame, "html.parser")
        for keyword in KEYWORDS_COMMENT:
            if keyword in soup.text:
                return True

    def get_gp_emails():
        file = open(f"/LOTS/{folder_lot_name}/frame.html", encoding="utf8")
        soup = BeautifulSoup(file, "html.parser")
        gp_emails = soup.find('input', {'id': 'p[3837]'}).get('value')
        return gp_emails.split(';')

    def send_mail(list_receivers):
        for title in letters.keys():
            if folder_lot_name in title:
                message = MIMEMultipart()
                message['Subject'] = title
                part1 = MIMEText(reject_reason, 'plain')
                part2 = MIMEText(letters.get(title), 'html')
                message.attach(part1)
                message.attach(part2)
                smtpObj = smtplib.SMTP_SSL('smtp.komus.ru:***')
                smtpObj.login(login, password)
                smtpObj.auth_plain()
                smtpObj.sendmail(login, list_receivers, message.as_string())
                break

    if check_comment():
        send_mail(get_gp_emails())
    else:
        send_mail(["*******@komus.ru"])
