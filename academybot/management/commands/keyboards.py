from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from ...models import *


def Asosiy():
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton('Umumiy ro\'yxat', callback_data='all')],
        [InlineKeyboardButton('Guruhlar bo\'yicha', callback_data='groups')],
        [InlineKeyboardButton('Oylar bo\'yicha', callback_data='months')]
    ])
    return keyboard


def all_atudents():
    students = Student.objects.all()
    keys = []
    for i in students:
        keys.append([InlineKeyboardButton(f'{i.full_name}', callback_data=f'{i.id}')])

    keys.append([InlineKeyboardButton('◀️Back', callback_data='back')])
    keboard = InlineKeyboardMarkup(keys)
    return keboard


def courses_keyboard():
    courses = Courses.objects.all()
    keys = []
    for i in courses:
        keys.append([InlineKeyboardButton(f'{i.course_name}', callback_data=f'{i.id}')])
    keys.append([InlineKeyboardButton('◀️Back', callback_data='back')])
    keboard = InlineKeyboardMarkup(keys)
    return keboard


def students_by_courses(id):
    students = Student.objects.filter(course_id=id)
    keys = []
    for i in students:
        keys.append([InlineKeyboardButton(f'{i.full_name}', callback_data=f'{i.id}')])

    keys.append([InlineKeyboardButton('◀️Back', callback_data='back')])
    keboard = InlineKeyboardMarkup(keys)
    return keboard


def month_keyboards():
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton('January', callback_data='1'),
         InlineKeyboardButton('February', callback_data='2'),
         InlineKeyboardButton('March', callback_data='3'),
         InlineKeyboardButton('April', callback_data='04')],

        [InlineKeyboardButton('May', callback_data='5'),
         InlineKeyboardButton('June', callback_data='6'),
         InlineKeyboardButton('July', callback_data='7'),
         InlineKeyboardButton('August', callback_data='8')],

        [InlineKeyboardButton('September', callback_data='9'),
         InlineKeyboardButton('October', callback_data='10'),
         InlineKeyboardButton('November', callback_data='11'),
         InlineKeyboardButton('December', callback_data='12')],

        [InlineKeyboardButton("◀️Back", callback_data="back")]
    ])
    return keyboard


def payment_button(moth_id):
    payments = Payments.objects.all()
    keys = []
    for pay in payments:
        month = pay.payment_data.month
        if month == int(moth_id):
            keys.append([InlineKeyboardButton(f"{pay.student.full_name}  {pay.payment_data}", callback_data=f"{pay.id}" )])
    keys.append([InlineKeyboardButton("◀️Back", callback_data="back")])
    keboard = InlineKeyboardMarkup(keys)
    return keboard
