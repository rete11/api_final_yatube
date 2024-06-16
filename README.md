# Проект «API для Yatube»

### Описание

* В проекте API для Yatube создано приложение posts с описанием моделей Yatube. В нём реализовано API для всех моделей приложения.
* API доступен только аутентифицированным пользователям. Используется аутентификация по токену TokenAuthentication.
* Логика API вынесена в отдельное приложение. 
* Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.

### Инструкция по запуску проекта

Клонировать репозиторий командой:

```
git clone https://github.com/rete11/api_final_yatube.git
```
перейти в него в командной строке:

```
cd api_final_yatube
```

Cоздать  виртуальное окружение:

```
python3 -m venv env
```

Активировать виртуальное окружение:

- Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

- Если у вас windows

    ```
    source env/Scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


Примеры работы с API для неавторизованных пользователей пользователей:

```
GET api/v1/posts/ - список публикаций
GET api/v1/posts/{id}/ - публикациия
GET api/v1/{post_id}/comments/ - список комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - комментарий к публикации
GET api/v1/groups/ - список сообществ
GET api/v1/groups/{id}/ - описание сообщества по id
```

Документация к API проекта Yatube будет доступна по ссылке:

```
http://127.0.0.1:8000/redoc/
```

### Автор проекта
#### Бранихин  Виталий
