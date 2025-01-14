import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

from_address = "LiMBtsk@yandex.ru"
to_address = "LiMBtsk@yandex.ru"
subject = "Приглашение!"

template = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на %website%?

→ Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → %website%
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

friend_name = "Маргарита"
my_name = "Виктор"
website = "https://dvmn.org/profession-ref-program/limb_rap/njVWG/"

letter_body = template.replace("%friend_name%", friend_name).replace("%my_name%", my_name).replace("%website%", website)

letter = """From: {from_address}
To: {to_address}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

{letter_body}""".format(
    from_address=from_address,
    to_address=to_address,
    subject=subject,
    letter_body=letter_body
)

encoded_letter = letter.encode('utf-8')

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail(from_address, to_address, encoded_letter)
server.quit()

print("отправлено")
