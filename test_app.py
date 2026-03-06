import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):

    # Set up test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test home route
    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Welcome to the Flask Web Application!")

    # Test API route
    def test_hello_api(self):
        response = self.app.get('/api/hello')
        self.assertEqual(response.status_code, 200)

        json_data = response.get_json()
        self.assertEqual(json_data["message"], "Hello from Flask API")
        self.assertEqual(json_data["status"], "success")


if __name__ == '__main__':
    unittest.main()