import requests
from authentification import get_token
from config import baseURL


def receiveListOfReviews(product_id, user_id, access_token=get_token()):
    r = requests.get(baseURL+'reviews/',
                     headers={'Authorization': 'Bearer {}'.format(access_token)},
                     params={'product_id': product_id, 'user_id': user_id})
    return r
