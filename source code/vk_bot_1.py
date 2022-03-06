import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

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

        if text == "hello":
            send_message(user_id, "Hello!")
