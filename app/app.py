from flask import Flask, request
from utils import string_data_to_dict
from database import db

app = Flask(__name__)


@app.route('/get_form', methods=['POST'])
def get_form():
    data = string_data_to_dict(request.data)  # Словарь (имя поля: тип поля)

    # Поле name заменяется на person_name, так как в шаблонах оно занято именем шаблона
    correct_data = data
    if 'name' in correct_data:
        correct_data['person_name'] = data['name']

    all_templates = db.all()
    best_fit_template_name = ''
    max_fields_count = 0
    for template in all_templates:
        fields_count = 0
        name = template['name']
        del template['name']
        for key, value in template.items():
            if (key not in correct_data) or (correct_data[key] != value):
                break
            fields_count += 1
        else:
            if fields_count > max_fields_count:
                best_fit_template_name = name
                max_fields_count = fields_count

    if best_fit_template_name:
        return best_fit_template_name
    return data


if __name__ == '__main__':
    app.run()
