from utils.http_method import HttpMethod
from utils.config import BASE_URL_GOOGLE, KEY
"""Методы тестирования Google maps api"""

base_url = BASE_URL_GOOGLE  #Базовая URL
key = KEY #Параметр для всех запросов:


class GoogleMapsApi:

    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json" # Ресурс метода Post
        post_url = base_url + post_resource +key
        print(post_url)
        result_post = HttpMethod.post(post_url, json_for_create_new_place,headers=None)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    """Метод для проверки новой локации"""
    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json"  #Ресурс метода Get
        get_url = base_url +get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethod.get(get_url, headers=None)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Метод для изменения новой локации"""
    @staticmethod
    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json"  # Ресурс метода Put
        put_url = base_url+put_resource+key
        print(put_url)

        json_for_update_new_location = {

            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "name": "Veselie dubki",
            "key": "qaclick123"
        }
        result_put = HttpMethod.put(put_url,json_for_update_new_location,headers=None)
        print(result_put.text)
        return result_put

    """Метод для удаления новой локации"""
    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"  # Ресурс метода Put
        put_url = base_url+delete_resource+key
        print(put_url)

        json_for_delete_new_location = {

            "place_id": place_id,
        }
        result_delete = HttpMethod.delete(put_url,json_for_delete_new_location, headers=None)
        print(result_delete.text)
        return result_delete

    @staticmethod
    def get_new_ninja():
        url = "https://swapi.dev/api/people/4/"

        result_get = HttpMethod.get(url,headers=None)
        return result_get