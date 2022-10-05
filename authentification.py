import requests
from config import secret, client


def get_token(client_id=client, client_secret=secret):
    scope = 'read_user write_user read_wishlist write_wishlist read_review ' \
            'write_review read_gallery read_reward write_reward app_install'
    r = requests.post('https://api.growave.io/api/access_token', data={'client_id': client_id,
                                                                       'client_secret': client_secret,
                                                                       'grant_type': 'client_credentials',
                                                                       'scope': scope})
    response = r.json()
    return response["access_token"]





# репликаловка работающая с майскл ставлю инстанс и делаю слайс с прода
# слони
