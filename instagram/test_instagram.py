from instagram import receiveInstagramGalleries


class TestReceiveInstagramGalleries:
    def test_receiveInstagramGalleries(self):
        assert receiveInstagramGalleries().status_code == 200

    def test_receiveInstagramGalleries404(self):
        assert receiveInstagramGalleries().status_code == 404

    def test_receiveInstagramGalleries401(self):
        assert receiveInstagramGalleries("").status_code == 401
