from users import receiveSingleUser, listOfUsers, searchUser
from config import status200, status401, status404


class TestReceiveSingleUser:
    def test_receiveSingleUser(self):
        assert receiveSingleUser(42272).status_code == status200

    def test_receiveSingleUser404(self):
        assert receiveSingleUser(1).status_code == status404

    def test_receiveSingleUser401(self):
        assert receiveSingleUser(1, '').status_code == status401


class TestListOfUsers:
    def test_listOfUsers(self):
        assert listOfUsers().status_code == status200

    def test_listOfUsers401(self):
        assert listOfUsers('').status_code == status401


class TestSearchUser:
    def test_searchUser(self):
        assert searchUser('growavetest@gmail.com').status_code == status200
        res = searchUser('growavetest@gmail.com').json()
        assert res['data']['first_name'] == 'Peter'

    def test_searchUser401(self):
        assert searchUser('growavetest@gmail.com', '').status_code == status401

    def test_searchUser404(self):
        assert searchUser('example@gmail.com').status_code == status404


