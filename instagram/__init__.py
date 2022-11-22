import requests
from authentification import get_token
from config import baseURL


def receiveInstagramGalleries(access_token=get_token()):
    r = requests.get(
        baseURL + "reviews/",
        headers={"Authorization": "Bearer {}".format(access_token)},
    )
    return r
