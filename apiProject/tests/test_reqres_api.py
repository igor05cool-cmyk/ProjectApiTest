from utils.api.reqres_api import ReqResApi #импорт данных из файла reqres_api класс ReqResApi

class TestReqRes:

    def test_create_user(self):
        """Запуск проверки Создания юзера"""
        response = ReqResApi.create_user()

        print(response.text)
        assert response.status_code == 201
        assert response.json()["name"] == "morpheus"

    def test_register_user(self):
        """Запуск проверки Регистрации пользователя"""
        response = ReqResApi.register_user()

        print(response.text)
        assert response.status_code == 200
        assert "id" in response.json()
        assert "token" in response.json()

    def test_get_user(self):
        response = ReqResApi.get_user()

    def test_put_user(self):
        response = ReqResApi.update_user()

    def test_delete_user(self):
        response =ReqResApi.delete_user()


    # def test_login_user(self):
    #     response = ReqResApi.login_user()
    #
    #     print(response.text)
    #     assert response.status_code == 200
    #     assert "id" in response.json()
    #     assert "token" in response.json()