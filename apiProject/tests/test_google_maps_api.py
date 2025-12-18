from utils.api.google_maps_api import GoogleMapsApi
from utils.cheking import Checking
import json

"Создание, изменение и удаление новой локации"
class TestCreatePlace:

    def test_create_new_place(self):

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_cod(result_post, 200)
        Checking.check_json_token(result_post,['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', "OK")
        print()

        # token = json.loads(result_post.text)
        # print(list(token))


        print("Метод GET")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_cod(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', "29, side layout, cohen 09")
        print()

        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_cod(result_put, 200)
        Checking.check_json_token(result_put,["msg"])
        Checking.check_json_value(result_put, 'msg', "Address successfully updated")
        print()

        print("Метод GET_PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_cod(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        Checking.check_json_value(result_get, 'address', "100 Lenina street, RU")
        print()

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_cod(result_delete, 200)
        Checking.check_json_token(result_delete, ["status"])
        Checking.check_json_value(result_delete, 'status', "OK")
        print()

        print("Метод GET_DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_cod(result_get, 404)
        Checking.check_json_token(result_get, ["msg"])
        #Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        Checking.check_json_search_word_in_value(result_get,'msg',"place_id")
        print()

        print("Метод ниндзя")
        result_get_ninja = GoogleMapsApi.get_new_ninja()
        check_get = result_get_ninja.json()

        print(check_get)


        print("Тестирование создания, изменения и удаление новой локации прошло успешно!!!")



