from instagram import receiveInstagramGalleries
from config import status200, status401, status404


class TestReceiveInstagramGalleries:
    def test_receiveInstagramGalleries(self):
        assert receiveInstagramGalleries().status_code == status200

    def test_receiveInstagramGalleries404(self):
        assert receiveInstagramGalleries().status_code == status404

    def test_receiveInstagramGalleries401(self):
        assert receiveInstagramGalleries('').status_code == status401

