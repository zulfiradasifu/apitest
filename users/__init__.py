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


def searchUser(choice, arg, access_token=get_token()):
    match choice:
        case 1:  # search by email
            r = requests.get(
                baseURL + "users/search",
                headers={"Authorization": "Bearer {}".format(access_token)},
                params={"email": arg},
            )
        case 2:  # search by user_id
            r = requests.get(
                baseURL + "users/search",
                headers={"Authorization": "Bearer {}".format(access_token)},
                params={"user_id": arg},
            )
        case 3:  # search by customer_id
            r = requests.get(
                baseURL + "users/search",
                headers={"Authorization": "Bearer {}".format(access_token)},
                params={"customer_id": arg},
            )
    return r

# TODO add verify customer test
