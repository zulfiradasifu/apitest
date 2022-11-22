import requests
from authentification import get_token
from config import baseURL


def receiveListOfReviews(access_token=get_token()):
    r = requests.get(
        baseURL + "reviews/",
        headers={"Authorization": "Bearer {}".format(access_token)},
    )
    return r


def receiveListOfProductReviews(product_id, access_token=get_token()):
    r = requests.get(
        baseURL + "reviews/",
        headers={"Authorization": "Bearer {}".format(access_token)},
        params={"product_id": product_id},
    )
    return r


def receiveListOfUsersReviews(user_id, access_token=get_token()):
    r = requests.get(
        baseURL + "reviews/",
        headers={"Authorization": "Bearer {}".format(access_token)},
        params={"user_id": user_id},
    )
    return r
