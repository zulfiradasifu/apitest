from reviews import receiveListOfReviews
from config import status200, status401, status404


class TestReceiveListOfReviews:
    def test_receiveAllReviews(self):
        assert receiveListOfReviews(0, 1).status_code == status200

    def test_receiveReviewsOfProduct(self):
        assert receiveListOfReviews(0, 1).status_code == status200

    def test_receiveReviewsFromUser(self):
        assert receiveListOfReviews(0, 1).status_code == status200

    def test_receiveReviewsWithoutToken(self):
        assert receiveListOfReviews(0, 1, '').status_code == status401

    def test_receiveReviews404Product(self):
        assert receiveListOfReviews(0, 1).status_code == status404

    def test_receiveReviews404User(self):
        assert receiveListOfReviews(0, 1).status_code == status404

