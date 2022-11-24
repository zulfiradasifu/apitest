import requests
from authentification import get_token
from config import baseURL


def receiveSingleUser(user_id, access_token=get_token()):
    r = requests.get(
        baseURL + "users/" + str(user_id),
        headers={"Authorization": "Bearer {}".format(access_token)},
    )
    return r


def listOfUsers(access_token=get_token()):
    r = requests.get(
        baseURL + "users", headers={"Authorization": "Bearer {}".format(access_token)}
    )
    return r


def searchUser(param_name, arg, access_token=get_token()):
    r = requests.get(
        baseURL + "users/search",
        headers={"Authorization": "Bearer {}".format(access_token)},
        params={param_name: arg},
    )
    return r


# TODO add verify customer test
# TODO add update user data test
