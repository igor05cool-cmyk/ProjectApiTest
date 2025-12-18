import requests

"""Список шаблонов HTTP методов"""

class HttpMethod:

    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url,headers):
        headers = headers or HttpMethod.headers
        result = requests.get(url, headers=headers, cookies=HttpMethod.cookie)
        return  result

    @staticmethod
    def post(url, body, headers):
        headers = headers or HttpMethod.headers
        result = requests.post(url, json=body, headers=headers, cookies=HttpMethod.cookie)
        return result

    @staticmethod
    def put(url, body,headers):
        headers = headers or HttpMethod.headers
        result = requests.put(url, json=body, headers=headers, cookies=HttpMethod.cookie)
        return result

    @staticmethod
    def delete(url, body,headers):
        headers = headers or HttpMethod.headers
        result = requests.delete(url, json=body, headers=headers, cookies=HttpMethod.cookie)
        return result