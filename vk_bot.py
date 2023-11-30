import logging
import random

import telegram
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from decouple import config

from logs_handler import MyLogsHandler
from intent_detector import detect_intent_texts


logger = logging.getLogger("vk_logger")


def reply(event, vk_api, project_id):
    reply_to_user = detect_intent_texts(project_id, event.user_id, event.text, 'ru')
    if not reply_to_user.intent.is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=reply_to_user.fulfillment_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    project_id = config("GOOGLE_PROJECT_ID")
    vk_session = vk.VkApi(token=config("VK_BOT_TOKEN"))
    tg_admin_bot_token = config('TELEGRAM_ADMIN_BOT_TOKEN')
    admin_chat_id = config('TG_ADMIN_CHAT_ID')
    admin_bot = telegram.Bot(tg_admin_bot_token)

    logger.setLevel(logging.INFO)
    logger.addHandler(MyLogsHandler(admin_bot, admin_chat_id))
    logger.info("ВК бот запущен")

    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    reply(event, vk_api, project_id)
        except Exception:
            logger.exception(Exception)
