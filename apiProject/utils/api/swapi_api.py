# from utils.config import swapi_url
# from utils.http_method import HttpMethod
#
# class SwapiApi:
#     """Методы для тестирования сервиса Swapi.api"""
#     @staticmethod
#     def get_weider():
#         """Получение персонажа Дарт вейдера"""
#         url = swapi_url
#         print(url)
#         result_get = HttpMethod.get(url,headers=None)
#         check_get = result_get.json()
#         films_number = check_get.get("films")
#         print("Фильмы вейдера : " , films_number)
#         return result_get
#
#     def get_films(self, films_list):
#         """Получение списка фильмов где учавствовал Вейдер"""
#         for film_url in films_list:
#             response = HttpMethod.get(film_url, headers=None)
#             print(response.json().get("title"))
#
# SwapiApi.get_films(swapi.get_weider())



