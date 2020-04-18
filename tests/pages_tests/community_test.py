
from app_main import app
from tests import OhmTestCase


class CommunityTest(OhmTestCase):
    def test_get(self):
        with app.test_client() as c:
            response = c.get('/community')
            assert "5 Most Recent Users" in response.data
