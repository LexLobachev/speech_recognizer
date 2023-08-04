import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from decouple import config

from intent_detector import detect_intent_texts

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text('Здравствуйте!')


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Help!')


def reply(update: Update, context: CallbackContext):
    update.message.reply_text(detect_intent_texts(project_id, session_id, update.message.text, 'ru-Ru'))


def main():
    updater = Updater(config("TG_BOT_TOKEN"))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    project_id = config("PROJECT_ID")
    session_id = config("YOUR_TELEGRAM_ID")
    main()
