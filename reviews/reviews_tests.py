from reviews import receiveListOfReviews, receiveListOfUsersReviews, receiveListOfProductReviews
from config import status200, status401, status404


class TestReceiveListOfReviews:
    def test_receiveAllReviews(self):
        assert receiveListOfReviews().status_code == status200

    def test_receiveListOfProductReviews(self):
        assert receiveListOfProductReviews(0).status_code == status200

    def test_receiveListOfUsersReviews(self):
        assert receiveListOfUsersReviews(1).status_code == status200

    def test_receiveReviewsWithoutToken(self):
        assert receiveListOfReviews('').status_code == status401

    def test_receiveListOfProductReviews404(self):
        assert receiveListOfProductReviews(1).status_code == status404

    def test_receiveListOfUsersReviews404(self):
        assert receiveListOfUsersReviews(1).status_code == status404

