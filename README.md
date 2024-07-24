# Проект сервис API_yatube

Стек: Django, REST API, Djoser, JWT, Pillow.

## Описание

Проект содержит сервис API для работы с приложением Yatube. Приложение Yatube - место, где люди делятся своими историями. Посты состоят из следующих полей: текст поста, автор, группа, иллюстрация к посту, дата публикации. Также можно оставлять комментарии под любыми постами, подписываться на любимых авторов. Главное не забудьте зарегистрироваться, а иначе сможете только читать.

## Как запустить проект:

Клонировать репозиторий

```
git clone git@github.com:AlehAkbashev/api_final_yatube.git
```

Установить локальное окружение

```
python3 -m venv venv
```

Активировать локальное окружение

```
source venv/bin/activate
```

Установить все зависимости из файла requirements.txt

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции

```
python manage.py makemigrations
```
```
python manage.py migrate
```

Запустить сервер

```
python manage.py runserver
```

## Примеры запросов и ответов

Endpoints

* api/v1/jwt/create/  
* api/v1/jwt/refresh/
* api/v1/jwt/verify/
* api/v1/groups/
* api/v1/groups/<group_id>/
* api/v1/posts/
* api/v1/posts/<post_id>/
* api/v1/posts/api/v1/posts/<post_id>/comments/
* api/v1/posts/api/v1/posts/<post_id>/comments/<comment_id>
* api/v1/follow/
* api/v1/follow/?search

### Регистрация пользователя: **api/v1/jwt/create/**


Запрос:
```
{
    "username": "user",
    "password": "password"
}
```

Ответ:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJh",
    "access": "eyJ0eXAiOiJKV1QiLCJ"
}
```

### Получение публикаций: **api/v1/posts/**


Ответ:

```
[
    {
        "id": 1,
        "author": "regular_user",
        "image": null,
        "text": "Пост зарегистрированного пользователя.",
        "pub_date": "2023-10-14T16:26:12.761111Z",
        "group": null
    },
    {
        "id": 2,
        "author": "regular_user",
        "image": null,
        "text": "Пост с группой",
        "pub_date": "2023-10-14T16:26:16.750532Z",
        "group": 1
    }
]
```

### Создать пост: **api/v1/posts/**

Запрос: (поле group необязательное)

```
{
    "text": "Пост",
    "group": group_id
}
```
Ответ:
```
{
    "id": 1,
    "author": "user",
    "image": null,
    "text": "Пост",
    "pub_date": "2023-10-15T01:15:54.104260Z",
    "group": 1
}
```
