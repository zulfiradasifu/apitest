from reviews import receiveListOfReviews
from config import status200, status401, status404, status406


class TestReceiveListOfReviews:
    # TODO when https://growave.atlassian.net/browse/GROWK-6568 is done
    # def test_receiveAllReviews(self):
    #     r = receiveListOfReviews()
    #     res_json = r.json()
    #     print(res_json)

    def test_receiveListOfProductReviews(self):
        r = receiveListOfReviews()
        res_json = r.json()

    # def test_receiveListOfUsersReviews(self):
    #     assert receiveListOfUsersReviews(1).status_code == status200
    #
    # def test_receiveReviewsWithoutToken(self):
    #     assert receiveListOfReviews("").status_code == status401
    #
    # def test_receiveListOfProductReviews404(self):
    #     assert receiveListOfProductReviews(1).status_code == status404
    #
    # def test_receiveListOfUsersReviews404(self):
    #     assert receiveListOfUsersReviews(1).status_code == status404
