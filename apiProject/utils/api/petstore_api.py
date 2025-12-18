from utils.http_method import HttpMethod
from utils.config import PETSTORE_URL

class PetStoreApi:

    @staticmethod
    def create_user_pet():
        url = PETSTORE_URL+'/v2/user/createWithArray'
        json_post = [{
          "id": 12,
          "username": "testUserAndre",
          "firstName": "Timi",
          "lastName": "Timson",
          "email": "titmi@email.com",
          "password": "87654321",
          "phone": "8-800-555-35-35",
          "userStatus": 1
        }]

        print(url)
        result_post = HttpMethod.post(url, json_post, headers=None)
        chek_post = result_post.json()
        print(f"Статус код : {result_post.status_code}")
        print(result_post.json())
        return result_post

    @staticmethod
    def update_user_pet():
        url = PETSTORE_URL + '/v2/pet'
        json_put =[{
                "id": 1,
                "category": {
                    "id": 1,
                    "name": "Bobik"
                },
                "name": "doggie",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": "1",
                        "name": "Bob"
                    }
                ],
                "status": "available"
            }]
        print(url)
        result_put = HttpMethod.put(url, json_put,headers=None)
        chek_put = result_put.json()
        print(f"Статус код : {result_put.status_code}")
        print(chek_put)
        return result_put

    @staticmethod
    def delete_user_pet():
        url = PETSTORE_URL + '/v2/store/order/1'
        print(url)
        result_delete = HttpMethod.delete(url,body=None)
        check_delete = result_delete.json()
        print(check_delete)
        return result_delete


