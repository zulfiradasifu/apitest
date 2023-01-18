import pytest
import requests
import json
from config import baseUrl, header


def test_own_service():
    req = requests.get(url="http://127.0.0.1:5000/")
    req_json = json.loads(req.text)
    if req_json["message"] == "ok":
        pass
    else:
        raise ValueError("Ожидали 'ok', получили {}".format(req_json))


def test_own_service_post():
    req = requests.post(url='http://127.0.0.1:5000/')
    print(req.text)

    assert req.status_code == 200
    print(req.text)


def test_receive_single_user():
    response = requests.get(url=baseUrl + "users/search?user_id=1", headers=header)
    req_json = json.loads(response.text)
    print(req_json)
    assert response.status_code == 200


def test_update_user_data():
    data = {
        "first_name": "Elon2",
        "last_name": "Musk",
        "about": "Entrepreneur, engineer, inventor, investor",
        "birthdate": "1971-06-28"
    }
    response = requests.put(url=baseUrl + "users/1", headers=header, json=data)
    print(json.loads(response.text))
    assert response.status_code == 201


def test_add_to_wishlist():
    response = requests.post(url=baseUrl + "wishlist?user_id=6&product_id=7963082654008", headers=header, params=data1)
    print(json.loads(response.text))
    assert response.status_code == 200


def test_remove_product_from_wl():
    response = requests.delete(url=baseUrl + "wishlist", headers=header, params=data1)
    print(json.loads(response.text))
    assert response.status_code == 200


def test_create_board():
    data1 = {
        'user_id': 6,
        'title': 'musthave'
    }
    response = requests.post(url=baseUrl + "wishlist/boards", headers=header, params=data1)
    req = json.loads(response.text)
    print(json.loads(response.text))
    actRes = req['data']['user_id']
    assert response.status_code == 200
    assert actRes == '6'
