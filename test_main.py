import hug
import main
from unittest import TestCase


class Test(TestCase):
    HTTP_200 = '200 OK'

    def test_get_goal(self):
        expected_response = [
            {'date': '2024-05-10T00:00:00', 'goal': 'asd', 'timeframe': 'week'},
            {'date': '2024-05-10T00:00:00', 'goal': 'asd', 'timeframe': 'week'}
        ]

        response = hug.test.get(
            main,
            'goal',
            {"timeframe": "week"}
        )
        assert response.status == self.HTTP_200
        assert response.data is not None
        assert response.data == expected_response
