import requests
from authentification import get_token
from config import baseURL

# r = requests.request(method=["GET"], url=baseURL, headers={}, cookies={})

def receiveListOfReviews(*args, access_token=get_token()):
    if args:
        r = requests.get(
            baseURL + "reviews/",
            headers={"Authorization": "Bearer {}".format(access_token)},
            params={args[0]: args[1]},
        )
    else:
        r = requests.get(
            baseURL + "reviews/",
            headers={"Authorization": "Bearer {}".format(access_token)},
        )
    return r
