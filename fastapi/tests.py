import unittest
from main import app
from fastapi.testclient import TestClient
import json


class FastapiTests(unittest.TestCase):

    def setUp(self):
        self.app = TestClient(app)

    def test_get_hello_endpoint(self):
        res = self.app.get('/')
        self.assertEqual(res.body, b'Hello World!')

    def test_post_hello_endpoint(self):
        res = self.app.post('/')
        self.assertEqual(res.status_code, 405)

    def test_get_api_endpoint(self):
        res = self.app.get('/api')
        self.assertEqual(res.json(), {'status': 'test'})

    def test_correct_post_api_endpoint(self):
        res = self.app.post(
            '/api',
            headers={'Content-Type': 'application/json'},
            json={'name': 'Den', 'age': 100}
        )
        self.assertEqual(res.json(), {'status': 'OK'})
        self.assertEqual(res.status_code, 200)

        res = self.app.post(
            '/api',
            headers={'Content-Type': 'application/json'},
            json={'name': 'Den'}
        )
        self.assertEqual(res.json(), {'status': 'OK'})
        self.assertEqual(res.status_code, 200)

    def test_not_dict_post_api_endpoint(self):
        res = self.app.post(
            '/api',
            headers={'Content-Type': 'application/json'},
            json=[{'name': 'Den'}]
        )
        self.assertEqual(res.json(), {'error': 'JSON is not present'})
        self.assertEqual(res.status_code, 400)

    def test_no_name_post_api_endpoint(self):
        res = self.app.post(
            '/api',
            headers={'Content-Type': 'application/json'},
            json={'age': 100}
        )
        self.assertEqual(res.json(), {'error': 'name field is required and must be of type string'})
        self.assertEqual(res.status_code, 422)

    def test_bad_age_post_api_endpoint(self):
        res = self.app.post(
            '/api',
            headers={'Content-Type': 'application/json'},
            json={'name': 'Den', 'age': '100'}
        )
        self.assertEqual(res.json(), {'error': 'age field must be of type int'})
        self.assertEqual(res.status_code, 422)


if __name__ == '__main__':
    unittest.main()
