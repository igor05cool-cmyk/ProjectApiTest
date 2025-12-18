from utils.api.petstore_api import PetStoreApi

"Создание, изменение и удаление новой локации"
class TestCreateUser:

    def test_create_new_user_pet(self):

        print("Метод POST")
        result_post = PetStoreApi.create_user_pet()
        print(result_post.text)
        assert result_post.status_code == 200
        check_post = result_post.json()
        pet_id = check_post.get("id")

        print("Метод Put")
        result_put = PetStoreApi.update_user_pet()

        print("Метод Delete")
        result_delete = PetStoreApi.delete_user_pet()


