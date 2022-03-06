"""VkTools
Модуль обновился, смотрите здесь https://github.com/Fsoky/vktools
pip install vktools -U

"""

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from vktools import Keyboard, ButtonColor, Text, OpenLink, Location, Carousel, Element

session = vk_api.VkApi(token="TOKEN")
api = session.get_api()


def send_message(user_id, message, **kwargs):
    api.messages.send(
        user_id=user_id,
        message=message,
        random_id=0,
        **kwargs
    )


for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id

        if text == "start":
            keyboard = Keyboard(
                [
                    [
                        Text("RED", ButtonColor.NEGATIVE),
                        Text("GREEN", ButtonColor.POSITIVE),
                        Text("BLUE", ButtonColor.PRIMARY),
                        Text("WHITE")
                    ],
                    [
                        OpenLink("YouTube", "https://youtube.com/c/Фсоки"),
                        Location()
                    ]
                ]
            )

            send_message(user_id, "New Keyboard", keyboard=keyboard.add_keyboard())
        elif text == "test":
            carousel = Carousel(
                [
                    Element(
                        "Title 1",
                        "Description 1",
                        "-203980592_457239030",
                        "https://vk.com/fsoky",
                        [Text("Button 1", ButtonColor.NEGATIVE)]
                    ),
                    Element(
                        "Title 2",
                        "Description 2",
                        "-203980592_457239030",
                        "https://vk.com/fsoky",
                        [Text("Button 2", ButtonColor.PRIMARY)]
                    )     
                ]
            )

            send_message(user_id, "Carousel", template=carousel.add_carousel())
