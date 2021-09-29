# [Vkontakte BOT (vk_api python) [1] | Настройка и структура.](https://www.youtube.com/watch?v=hhq4sPeQ5A8)
__Автор показывает как получить токен и начальную структуру кода при написании бота для ВК__

*Код:* Два основных импорта, второй импорт нужен для работы с `LongPoll` (длинный запрос). \
Иницилизируем класс в переменной `session`, создаем цикл, где будем получать значения из генератора.
Ставим условие `если тип события == новому сообщению и это адресовано мне, то`: создаем переменные: `user_id`, text, куда мы будем получать ID пользователя и его текст.

Создадим функцию `send_message`, в параметры передадим user_id, message, внутри функции воспользуемся методом `messages.send`, для того, чтобы отправить сообщение. \
Дальше в цикле ставим еще одно условие `если переменная текст == слову "hello", то`: вызываем функцию `send_message`, передаем туда переменную user_id и свой текст.
Тем самым, бот ответит на сообщение "hello".

```py
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

session = vk_api.VkApi(token="TOKEN")


def send_message(user_id, message):
	session.method("messages.send", 
		{
			"user_id": user_id,
			"message": message,
			"random_id": 0
		}
	)


for event in VkLongPoll(session).listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me:
		text = event.text.lower()
		user_id = event.user_id

		if text == "hello":
			send_message(user_id, "Hello!")
```
