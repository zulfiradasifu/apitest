from users import receiveSingleUser, listOfUsers, searchUser
from config import status200, status401, status404


class TestReceiveSingleUser:
    def test_receiveSingleUser(self):
        r = receiveSingleUser(42272)
        res_json = r.json()
        assert res_json["data"]["email"] == "jama.98.jk@gmail.com"
        assert res_json["message"] == "OK"
        assert r.status_code == status200

    def test_receiveSingleUser401(self):
        r = receiveSingleUser(42272, "")
        res_json = r.json()
        assert res_json["message"] == "Unauthorized"
        assert r.status_code == status401

    def test_receiveSingleUser404(self):
        r = receiveSingleUser(1)
        res_json = r.json()
        assert res_json["error_description"] == "User not found"
        assert res_json["message"] == "not_found: User not found"
        assert r.status_code == status404


class TestListOfUsers:
    def test_listOfUsers(self):
        r = listOfUsers()
        res_json = r.json()
        assert res_json["data"][0]["user_id"] == 42340
        assert res_json["message"] == "OK"
        assert r.status_code == status200

    def test_listOfUsers401(self):
        r = listOfUsers("")
        res_json = r.json()
        assert res_json["message"] == "Unauthorized"
        assert r.status_code == status401


class TestSearchUser:
    def test_searchUserByEmail(self):
        r = searchUser(1, "growavetest@gmail.com")
        res_json = r.json()
        assert res_json["data"]["first_name"] == "Peter"
        assert res_json["message"] == "OK"
        assert r.status_code == status200

    def test_searchUserByEmail401(self):
        r = searchUser(1, "growavetest@gmail.com", "")
        res_json = r.json()
        assert res_json["message"] == "Unauthorized"
        assert r.status_code == status401

    def test_searchUserByEmail404(self):
        r = searchUser(1, "example@gmail.com")
        res_json = r.json()
        assert res_json["message"] == "Customer not found"
        assert r.status_code == status404

    def test_searchUserByUserId(self):
        r = searchUser(2, 41179)
        res_json = r.json()
        assert res_json["data"]["first_name"] == "Peter"
        assert res_json["message"] == "OK"
        assert r.status_code == status200

    def test_searchUserByUserId401(self):
        r = searchUser(2, 41179, "")
        res_json = r.json()
        assert res_json["message"] == "Unauthorized"
        assert r.status_code == status401

    def test_searchUserByUserId404(self):
        r = searchUser(2, 1)
        res_json = r.json()
        assert res_json["message"] == "Customer not found"
        assert r.status_code == status404

    def test_searchUserByCustomerId(self):
        r = searchUser(3, 3420456845443)
        res_json = r.json()
        assert res_json["data"]["first_name"] == "Peter"
        assert res_json["message"] == "OK"
        assert r.status_code == status200

    def test_searchUserByCustomerId401(self):
        r = searchUser(3, 3420456845443, "")
        res_json = r.json()
        assert res_json["message"] == "Unauthorized"
        assert r.status_code == status401

    def test_searchUserByCustomerId404(self):
        r = searchUser(3, 1)
        res_json = r.json()
        assert res_json["message"] == "Customer not found"
        assert r.status_code == status404
