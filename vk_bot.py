import random

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from decouple import config
from intent_detector import detect_intent_texts


def reply(event, vk_api, project_id):
    vk_api.messages.send(
        user_id=event.user_id,
        message=detect_intent_texts(project_id, event.user_id, event.text, 'ru'),
        random_id=random.randint(1, 1000)
    )


def main():
    project_id = config("PROJECT_ID")
    vk_session = vk.VkApi(token=config("VK_TOKEN"))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reply(event, vk_api, project_id)


if __name__ == '__main__':
    main()
