import json


class Checking:
    """Методы для проверки ответов наших запросов"""

    @staticmethod
    def check_status_cod(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, 'Ошибка, Статус код не совпадает'
        print(f'Успешно! Статус код = {result.status_code}')

    @staticmethod
    def check_json_token(result, expected_value):
        """Метод для проверки наличия обязательных полей в ответе запроса"""
        token = json.loads(result.text)
        assert list(token) == expected_value, 'Ошибка, Список полей не совпадает'
        print(list(token))
        print("Все поля на месте")

    @staticmethod
    def check_json_value(result,field_name, expected_value):
        """Метод для проверки значений обязательных полей в ответе запроса"""
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен !!!")

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        """Метод для проверки значений обязательных полей в ответе запроса по заданному словоу"""
        check = result.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f'Слово {search_word} в наличии !!!')
        else:
            print(f'Слово {search_word} не найдено')


