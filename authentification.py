import pytest
import requests
from config import secret, client, baseURL

# @pytest.fixture(scope='session')
# def req():
#     s = requests.Session()
# #
# #
# #
#     return s
# def test_1(req):
#     req.request(method="GET", url="qwe")


# @pytest.fixture(scope='session')
# def get_token():
#     scope = (
#         "read_user write_user read_wishlist write_wishlist read_review "
#         "write_review read_gallery read_reward write_reward app_install"
#     )
#     r = requests.Session().post(
#         baseURL + "access_token",
#         data={
#             "client_id": client,
#             "client_secret": secret,
#             "grant_type": "client_credentials",
#             "scope": scope,
#         },
#     )
#     response = r.json()
#     print(response["access_token"])
#     return response["access_token"]

def get_token():
    scope = (
        "read_user write_user read_wishlist write_wishlist read_review "
        "write_review read_gallery read_reward write_reward app_install"
    )
    r = requests.post(
        baseURL + "access_token",
        data={
            "client_id": client,
            "client_secret": secret,
            "grant_type": "client_credentials",
            "scope": scope,
        },
    )
    response = r.json()
    return response["access_token"]


# репликаловка работающая с майскл ставлю инстанс и делаю слайс с прода
# слони
