import re
import datetime


# Из словаря (ключ: значение) в словарь (ключ: тип ключа)
def string_data_to_dict(data, test=False):
    return {key: validation(value) for key, value in request_parse(data, test).items()}


# Из строки в словарь
def request_parse(data, test=False):
    """test=False: если данные пришли через POST запрос,
    то они приходят как байтовая строка, которую нужно декодировать,
    а при тестировании данные приходят как строка"""
    if not test:
        data = data.decode('utf-8')[3:-3]
    return dict([i.split('=') for i in data.split('&')])


def validation(field):
    if date_validation(field):
        return 'date'
    elif re.match(r'(\+7)\s\d{3}\s\d{3}\s\d{2}\s\d{2}', field):
        return 'phone'
    elif re.match(r'[^@]+@[^@]+\.[^@]+', field):
        return 'email'
    else:
        return 'text'


def date_validation(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        try:
            datetime.datetime.strptime(date, '%d.%m.%Y')
            return True
        except ValueError:
            return False
