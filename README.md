## Подбор шаблона форм

###### Версия python 3.8.1

#### Для запуска тестовых скриптов:

1. Создайте виртуальное окружение в папке проекта с помощью команды: `python -m venv env`

2. Активируйте виртуальное окружение командой

на Windows: `.\env\Scripts\activate`

на Linux: `source env/bin/activate`

3. Установите зависимости командой: `pip install -r requirements.txt`

4. Запустите тесты командой 

на Windows: `.\env\Scripts\pytest app\test_app.py`

на Linux: ''

##### В качестве базы используется TinyDB
##### db.json - файл базы
##### Всего написано 4 теста, 2 с имеющимися в базе данными и 2 с отсутствующими.
