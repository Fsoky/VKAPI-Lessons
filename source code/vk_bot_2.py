import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

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
            keyboard = VkKeyboard()
            keyboard.add_location_button()
            keyboard.add_line()

            buttons = ["blue", "red", "white", "green"]
            button_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.NEGATIVE,
                                VkKeyboardColor.SECONDARY, VkKeyboardColor.POSITIVE]

            for btn, btn_color in zip(buttons, button_colors):
                keyboard.add_button(btn, btn_color)

            send_message(user_id, "My Keyboard", keyboard=keyboard.get_keyboard())

        elif text == "blue":
            send_message(user_id, "BLUE")
