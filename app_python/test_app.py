from app import app

from datetime import datetime

import pytz


class TestApp():
    def test_correct_url(self):
        client = app.test_client(self)
        response = client.get('/')

        assert response.status_code == 200

    def test_timeResponse(self):
        client = app.test_client(self)
        now = datetime.now(tz=pytz.timezone('Europe/Moscow')).strftime('%H:%M:%S')
        response = client.get('/')

        assert now in response.data.decode('utf-8')