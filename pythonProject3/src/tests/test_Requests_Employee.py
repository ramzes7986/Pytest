import requests

from jsonschema import validate
from src.authorization.auth import Test
from src.venv.configuration import *
from src.schemas.post import POST_SCHEMA
from src.enums.global_enums import *

def test_post_employee_add():

    json = {
            "departments": [
                5
            ],
            "id": 99,
            "name": "PytestCreatingEmployee",
            "password": "QwertyQwerty",
            "phone": "87775832571",
            "roleId": 2
    }

    headers = {"Content-Type": "application/json", "TOKEN": f"Bearer {Test.test(Test)}"}
    post_response = requests.post(url=SERVICE_URL_POST, json=json, headers=headers)
    received_posts = post_response.json()
    print(received_posts)
    #assert post_response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    #assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_NUMBER.value
    validate(received_posts, POST_SCHEMA)

def test_get_employee_update():

    headers = {"Content-Type": "application/json", "TOKEN": f"Bearer {Test.test(Test)}"}
    get_response = requests.get(url=SERVICE_URL_GET + "99", headers=headers)
    received_get = get_response.json()
    print(received_get)

def test_put_employee_add():

    json = {
            "departments": [
                5
            ],
            "id": 99,
            "name": "PytestCreatingEmployee2",
            "password": "QwertyQwerty",
            "phone": "87775832571",
            "roleId": 2
    }

    headers = {"Content-Type": "application/json", "TOKEN": f"Bearer {Test.test(Test)}"}
    put_response = requests.put(url=SERVICE_URL_PUT, json=json, headers=headers)
    received_put = put_response.json()
    print(received_put)

def test_get_employee_update():

    headers = {"Content-Type": "application/json", "TOKEN": f"Bearer {Test.test(Test)}"}
    delete_response = requests.delete(url=SERVICE_URL_DELETE + "99", headers=headers)
    received_delete = delete_response.json()
    print(received_delete)