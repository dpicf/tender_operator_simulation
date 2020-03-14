import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
from help_functions import begin_opening_lots, sed_error, lot_no_sed, lot_opened_someone
from lots_and_emails import create_lots_and_mails, get_current_lot
from opening_lots import opening_lot, lot_performance
from checking_files import check_docs_keywords
from sending_mail import sending_mail_reject


list_completed_lots = []
login = "********"
password = "********"


def program():
    def part_2(current_lot):
        def iteration_sed_error():
            if sed_error():  # Проверка вылета СЭД
                time.sleep(30)
                keyboard.press(Key.f5); keyboard.release(Key.f5)  # обновить страницу
                begin_opening_lots()
                opening_lot(current_lot)
                lot_performance()

        lot_opened_someone()
        lot_opened_someone()
        lot_opened_someone()
        iteration_sed_error()

        lot_performance(); time.sleep(2)
        iteration_sed_error()

        reject_reason = check_docs_keywords(current_lot)
        if reject_reason:
            sending_mail_reject(login, password, reject_reason, current_lot)

        part_1()

    def part_1():
        create_lots_and_mails(login, password)

        try:
            current_lot = get_current_lot()
            while current_lot in list_completed_lots:  # если лот есть в списке, брать из почты новый лот
                current_lot = get_current_lot()
            list_completed_lots.append(current_lot)

            opening_lot(current_lot); time.sleep(2)

            if lot_no_sed():  # Ошибка отсутствия лота в СЭД
                part_1()
            else:
                part_2(current_lot)

        except "list_lots_empty":
            quit()


program()
