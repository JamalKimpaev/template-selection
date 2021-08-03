from tinydb import Query
from app import db
from utils import string_data_to_dict

from request_data import request_data
from db_data import db_data

import requests
import json
import pytest


REQUEST_URL = 'http://127.0.0.1:5000/get_form'


@pytest.fixture(scope='module', autouse=True)
def init_db():
    db.insert_multiple(db_data)
    yield init_db
    db.truncate()


def test_correct_data_1():
    data = request_data['correct_data1']
    template = send_test_data(data)
    make_assertions(data, template)


def test_correct_data_2():
    data = request_data['correct_data2']
    template = send_test_data(data)
    make_assertions(data, template)


def test_wrong_data_1():
    data = request_data['wrong_data1']
    template = send_test_data(data)
    # template должен быть пустым списком
    assert not template


def test_wrong_data_2():
    data = request_data['wrong_data2']
    template = send_test_data(data)
    assert not template


def send_test_data(data):
    response = requests.post(REQUEST_URL, json=json.dumps(data))
    Template = Query()
    template = db.search(Template.name == response.text)
    return template


def make_assertions(data, template):
    correct_data = string_data_to_dict(data, test=True)
    if 'name' in correct_data:
        correct_data['person_name'] = correct_data['name']
    fields = template[0]
    del fields['name']
    for key, value in fields.items():
        assert key in correct_data, 'Отсутствует поле'
        assert correct_data[key] == value, 'Неверный тип поля'


