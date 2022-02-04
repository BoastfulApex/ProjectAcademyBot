from .keyboards import *


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Xush kelibsiz",
        reply_markup=Asosiy()
    )
    return 'substart'


def substart(update, context):
    query = update.callback_query
    query.answer()
    if query.data == "all":
        query.edit_message_text(
            text=f"Tanlang",
            reply_markup=all_atudents()
        )
        return 'students'
    elif query.data == "groups":
        query.edit_message_text(
            text=f"Tanlang",
            reply_markup=courses_keyboard()
        )
        return "courses"

    elif query.data == "months":
        query.edit_message_text(
            text=f"Tanlang",
            reply_markup=month_keyboards()
        )
    return "moth"


def payments_by_moth(update, context):
    query = update.callback_query
    query.answer()
    month_id = query.data
    if month_id != "back":
        query.edit_message_text(
            text=f"Tanlang",
            reply_markup=payment_button(month_id)
        )
        return "payments"
    else:
        query.edit_message_text(
            text="Xush kelibsiz",
            reply_markup=Asosiy()
        )
        return 'substart'


def pays(update, context):
    query = update.callback_query
    pay_id = query.data
    if pay_id != "back":
        payments = Payments.objects.get(id=pay_id)
        text = ""
        text += f"Course: {payments.course.course_name}\n" \
                f"Date: {payments.payment_data}\nStudent: {payments.student.full_name}" \
                f"\nAmount: {payments.amount}"
        context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)
    else:
        query.answer()
        query.edit_message_text(
            text="Xush kelibsiz",
            reply_markup=Asosiy()
        )
        return 'substart'


def group_list(update, context):
    query = update.callback_query
    query.answer()
    course_id = query.data
    if course_id != "back":
        query.edit_message_text(
        text=f"Tanlang",
        reply_markup=students_by_courses(course_id)
        )
        return "students"
    else:
        query.edit_message_text(
            text="Xush kelibsiz",
            reply_markup=Asosiy()
        )
        return 'substart'


def student_info(update, context):
    query = update.callback_query

    # query.answer() # <-- move it to `else:`

    if query.data != 'back':
        student_id = int(query.data)
        student = Student.objects.get(id=student_id)
        course = student.course
        remain = course.course_price - student.total_payment
        payments = Payments.objects.filter(student_id=student_id)
        text = ""
        text += f"{student.full_name}\n" \
                f"Course: {course.course_name}\n" \
                f"Duration: {course.begin_date} - {course.end_date}\nPrice: {course.course_price}"
        for i in payments:
            text += f"\n{i.payment_data} + {i.amount}"
        text += f"\nTotal: {student.total_payment}. Remain - {remain}"
        context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)
    else:
        query.answer()
        query.edit_message_text(
            text="Xush kelibsiz",
            reply_markup=Asosiy()
        )
        return 'substart'
