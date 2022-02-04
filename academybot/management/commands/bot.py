from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from .conversation import *
from django.core.management.base import BaseCommand
from telegram.utils.request import Request
from telegram import Bot
from django.conf import settings


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'xatolik: {e}'
            print(error_message)
            raise e

    return inner


@log_errors
def do_echo(update, context):
    chat_id = update.message.chat_id
    text = update.message.text

    reply_text = f"Sizning ID raqamingiz: {chat_id}\n{text}"
    update.message.reply_text(
        text=reply_text
    )


class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=0.6
        )
        bot = Bot(
            request=request,
            token='5055509145:AAHjm3thE181NROAf7qILO7PIrhr2uOdQEA',
        )
        print(bot.get_me())

        updater = Updater(
            bot=bot,
            use_context=True
        )
        updater = Updater(token='5055509145:AAHjm3thE181NROAf7qILO7PIrhr2uOdQEA', use_context=True)
        dispatcher = updater.dispatcher
        handler = ConversationHandler(
            entry_points=[MessageHandler(Filters.text, start)],
            states={
                'substart': [CallbackQueryHandler(substart)],
                'students': [CallbackQueryHandler(student_info)],
                'courses': [CallbackQueryHandler(group_list)],
                'moth': [CallbackQueryHandler(payments_by_moth)],
                'payments': [CallbackQueryHandler(pays)],
            },
            fallbacks=[],
        )
        dispatcher.add_handler(handler)
        updater.start_polling()
