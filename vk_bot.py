import random

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from decouple import config


def echo(event, vk_api):
    vk_api.messages.send(
        user_id=event.user_id,
        message=event.text,
        random_id=random.randint(1, 1000)
    )


def main():
    vk_session = vk.VkApi(token=config("VK_TOKEN"))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            print('Новое сообщение:')
            if event.to_me:
                print('Для меня от: ', event.user_id)
                echo(event, vk_api)


if __name__ == '__main__':
    main()
