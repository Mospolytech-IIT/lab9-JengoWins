Для данной работы была выбрана MySql 
Для создания таблиц, существует запрос /DBCreateTable, написанный вручную

Далее, идет Часть 2: Взаимодействие с базой данных

Добавление данных:
/DBCreateUser - POST запрос, который добавляет записи в Users
/DBCreatePost - POST запрос, который добавляет записи в Posts (в последнем поле указите внешний ключ (связь) с Users)

Извлечение данных:
/DBSelectUser - GET запрос, который выводит все записи Users
/DBSelectPosts - GET запрос, который выводит все записи Posts
/DBSelectPostsOneUsers/{username} - GET запрос, который выводит записи Posts, по имени пользователя Users

Обновление данных:
/DBUpdateUsers/{username}&{email} - PUT запрос, изменение почты пользователя по имени
/DBUpdatePosts/{title}&{content} - PUT запрос, изменение контента по его титульнику

Удаление данных:
/DBDeletePost/{title} - DELETE запрос, удаляет один из постов
/DBDeleteUser/{username} - Delete ЗАПРОС, удаляющий пользователя и все его посты

Для удобной работы были использованы такие данные вида JSON

[
  {
    "id": 1,
    "username": "Longer",
    "email": "Longer@mail.ru",
    "password": 1111
  },
  {
    "id": 2,
    "username": "Jengo",
    "email": "Jengo@mail.ru",
    "password": 5555
  }
]

[
  {
    "id": 1,
    "title": "Heading",
    "content": "Growing",
    "user_id": 1
  },
  {
    "id": 2,
    "title": "Logikal",
    "content": "Dmitry Labots",
    "user_id": 1
  },
  {
    "id": 3,
    "title": "LogAway",
    "content": "Laboratories",
    "user_id": 2
  }
]

Для Части 3: Базовые операции с базой данных в веб-приложении

Были созданы страницы для создания и вывода информации на HTML страницы
Были попытки реализации удаление по кнопке, но со стороны клиента запросы записаны некорректно, поэтому методы не могут сработать
Страницы редактирования не были реализованы.
Для всех манипуляций с Веб-Приложением, было создан отдельный файл с методами, описанные ранее во второй части, но подстроеные на работы со страницами
