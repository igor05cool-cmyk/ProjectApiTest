from utils.http_method import HttpMethod
from utils.config import REQRES_URL,REQRES_API_KEY

class ReqResApi:
    """Методы для тестирования сервиса reqres.in"""
    @staticmethod
    def create_user():
        """Создание пользователя"""
        url = REQRES_URL+'/api/users'
        headers = {
            "x-api-key": REQRES_API_KEY
        }
        json_post = {
            "name": "morpheus",
            "job": "leader"
        }

        print(url)
        result_post = HttpMethod.post(url, json_post, headers)
        chek_post = result_post.json()
        print(f'ID морфеуса : {chek_post.get('id')}')
        print(f"Статус код : {result_post.status_code}")

        return result_post

    @staticmethod
    def register_user():
        """Регистрация пользователя"""
        url = REQRES_URL+"/api/register"
        headers = {
            "x-api-key": REQRES_API_KEY
        }
        json_post = {
            "email": "eve.holt@re"
                     "qres.in",
            "password": "pistol"
        }

        print(url)
        result_post = HttpMethod.post(url, json_post, headers)
        print(result_post.json())
        print(f'Статус код : {result_post.status_code}')

        return result_post

    @staticmethod
    def get_user():
        """Получение пользователя"""
        url = REQRES_URL + "/api/unknown/2"
        headers = {
            "x-api-key": REQRES_API_KEY
        }
        print(url)
        result_get = HttpMethod.get(url,headers=headers)
        print(result_get.json())
        print(f'Статус код : {result_get.status_code}')
        check_get = result_get.json()
        count_check_get = len(check_get['data'].keys())
        print(count_check_get)
        return result_get

    @staticmethod
    def update_user():
        url = REQRES_URL + "/api/users/3"
        headers = {
            "x-api-key": REQRES_API_KEY
        }
        json_put =[
            {
                "name": "morpheus",
                "job": "zion resident"
            }
        ]
        print(url)
        result_put = HttpMethod.put(url,json_put,headers=headers)
        print(result_put.json())
        return result_put

    @staticmethod
    def delete_user():
        url = REQRES_URL +"/api/users/2"
        headers = {
            "x-api-key": REQRES_API_KEY
        }
        print(url)
        result_delete = HttpMethod.delete(url,headers=headers,body=None)
        print(result_delete.status_code)
        return result_delete


