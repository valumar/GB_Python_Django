# Урок 2

## Что реализовано

1. Всё общее вынесено в шаблон `_base.html`.
2. Реализовал циклы в шаблонах и списки словарей во вьюшках
3. Поправил меню (навбар). Добавил изменение класса li, по условию в шаблоне.
4. Создал виртуальное окружение.
5. Разместил проект на Гитхабе (https://github.com/valumar/GB_Python_Django)
6. Настроил Procfile для деплоя на Heroku
7. Настроил статику для корректного деплоя на Heroku

# Урок 3

## Что реализовано

1. Добавлены модели Work, Education
2. Таблицы моделей Work, Education заполнены данными через `.object.create()`
3. Модели зарегистрированы в админ-панели
4. Данные из моделей выгружены в `data.json` с помощью команды (https://docs.djangoproject.com/en/1.11/howto/initial-data/):

`python manage.py dumpdata about_app > about_app/fixtures/data.json`

5. Теперь исходные данные могут быть загружены через:

`python manage.py loaddata data`

