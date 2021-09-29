# [Vkontakte API Python | Как работать с методами?](https://www.youtube.com/watch?v=gysqjgfLmBc)
__В ролике автор показывает начальную структуру кода для работы с методами в ВК-АПИ__

*Код:* импортируется основной класс `vk_api`, а также файл *config*, в нем хранится токен. Второй импорт необязателен, т.к. вы можете передать токен напрямую в коде. \
Создается две переменные: `session`, `vk`. В первой переменной иницилизируется класс `VkApi`, во второй переменной мы получаем *api*

Создается две функции: `get_user_status`, `set_user_status`, первая функция принимает на вход user_id. В переменной `friend` обращаемся к методу *friends.get*,
вторым аргументом передаем `user_id`, то есть мы получаем словарь со списком ID'ов друзей пользователя. \
Через цикл перебираем список, внутри цикла создаем две переменные: `user`, `status`, с помощью первой переменной, мы сможем получать дитальную информацию о пользователе,
а с помощью второй - статус.

Поставим условие: `если статус пользователя пустой то` мы пропускаем его, в ином случае выводим *print* в консоль.

Во второй функции можно обратиться к переменной `vk` и уже работать с методами по другому, выбирайте сами, каким способом удобней.
*Устанавливаем новый статус для своей страницы*

```py
import vk_api

from config import token

session = vk_api.VkApi(token=token)
vk = session.get_api()


def get_user_status(user_id):
	friends = session.method("friends.get", {"user_id": user_id})

	for friend in friends["items"]:
		user = session.method("users.get", {"user_ids": friend})
		status = session.method("status.get", {"user_id": friend})

		if status["text"] == "":
			continue
		else:
			print(f"{user[0]['first_name']} {user[0]['last_name']} | {status['text']}")


def set_user_status():
	vk.status.set(text="New text for my status")


get_user_status(1)
set_user_status()
```

### [Официальная документация VK-API](https://vk.com/dev/methods)
