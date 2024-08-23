mails = {".com", ".ru", ".net"}
university_help_mail = 'university.help@gmail.com'

def find_mail(mail):
    for i in mails:
        if mail.find(i) != -1:
            return True
    return False

def send_email(message, recipient, *,sender = university_help_mail):
    if recipient.find('@') == -1 or sender.find('@') == -1:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if find_mail(recipient) == False or find_mail(sender) == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == university_help_mail:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
