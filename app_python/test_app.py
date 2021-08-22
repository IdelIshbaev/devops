from app import app


class TestApp():
    def test_correct_url(self):
        client = app.test_client(self)
        response = client.get('/')

        assert response.status_code == 200