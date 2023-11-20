import logging

import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from decouple import config
from functools import partial

from logs_handler import MyLogsHandler
from intent_detector import detect_intent_texts


logger = logging.getLogger("tg_logger")


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text('Здравствуйте!')


def reply(update: Update, context: CallbackContext, project_id):
    reply_to_user = detect_intent_texts(project_id, str(update.effective_user.id), update.message.text, 'ru-Ru')
    if reply_to_user:
        update.message.reply_text(reply_to_user)


if __name__ == '__main__':
    dialogflow_project_id = config("GOOGLE_PROJECT_ID")
    tg_bot_token = config('TELEGRAM_BOT_TOKEN')
    tg_admin_bot_token = config('TELEGRAM_ADMIN_BOT_TOKEN')
    admin_chat_id = config('TG_ADMIN_CHAT_ID')

    bot = telegram.Bot(tg_bot_token)
    admin_bot = telegram.Bot(tg_admin_bot_token)

    logger.setLevel(logging.INFO)
    logger.addHandler(MyLogsHandler(admin_bot, admin_chat_id))
    logger.info("ТГ бот запущен")

    updater = Updater(tg_bot_token)
    dispatcher = updater.dispatcher

    while True:
        try:
            dispatcher.add_handler(CommandHandler("start", start))
            dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command,
                                                  partial(reply, project_id=dialogflow_project_id)))
            updater.start_polling()
            updater.idle()

        except Exception:
            logger.exception(Exception)
