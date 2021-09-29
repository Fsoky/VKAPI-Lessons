# [Vkontakte BOT (vk_api python) [2] | Клавиатура, кнопочки.](https://www.youtube.com/watch?v=pHESBypF9mo
__Здесь не будет описано все, предыдущее смотреть [здесь](https://github.com/Fsoky/VKAPI-Lessons/blob/main/tutorial/vk_bot_1.md)__

Импортируем классы `VkKeyboard`, `VkKeyboardColor` из пакета `vk_api.keyboard`

Чтобы создать клавиатуру нужно обратиться к классу `VkKeyboard`, чтобы добавить кнопку нужно обратиться к методу `add_button("сюда передать текст кнопки", а сюда цвет)` \
Чтобы прикрепить клавиатуру к сообщению нужно отправить сообщение с параметром `keyboard`, и воспользоваться методом `get_keyboard` у класса VkKeyboard.

Также у клавиатуры есть другие кнопки, почитать можете в [оф. документации модуля vk_api](https://vk-api.readthedocs.io/en/latest/keyboard.html), а лучше воспользоваться простым способом создания клавиатуры
с помощью модуля [vktools](https://github.com/Fsoky/vktools) 

```py
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

session = vk_api.VkApi(token="TOKEN")


def send_message(user_id, message, keyboard=None):
	post = {
		"user_id": user_id,
		"message": message,
		"random_id": 0
	}

	if keyboard is not None:
		post["keyboard"] = keyboard.get_keyboard()

	session.method("messages.send", post)


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

			send_message(user_id, "My Keyboard", keyboard)

		elif text == "blue":
			send_message(user_id, "BLUE")
```
