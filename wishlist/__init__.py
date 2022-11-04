import requests
from authentification import get_token
from config import baseURL


def receiveSingleUser(user_id, access_token=get_token()):
    r = requests.get(baseURL+'users/'+str(user_id),
                     headers={'Authorization': 'Bearer {}'.format(access_token)})
    return r
