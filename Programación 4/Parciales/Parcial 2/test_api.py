import unittest
from app import app

class APITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_all(self):
        response = self.client.get("/vacunas")
        self.assertEqual(response.status_code, 200)

    def test_get_year(self):
        response = self.client.get("/vacunas/2010")
        self.assertIn(response.status_code, [200, 404])

if __name__ == "__main__":
    unittest.main()