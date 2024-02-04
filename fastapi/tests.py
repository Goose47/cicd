import unittest
from main import app
from fastapi.testclient import TestClient
import json


class FastapiTests(unittest.TestCase):

    def __init__(self):
        self.app = TestClient(app)

    def test_get_hello_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Hello World!')

    def test_post_hello_endpoint(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)

    def test_get_api_endpoint(self):
        r = self.app.get('/api')
        self.assertEqual(r.json, {'status': 'test'})

    def test_correct_post_api_endpoint(self):
        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps({'name': 'Den', 'age': 100}))
        self.assertEqual(r.json, {'status': 'OK'})
        self.assertEqual(r.status_code, 200)

        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps({'name': 'Den'}))
        self.assertEqual(r.json, {'status': 'OK'})
        self.assertEqual(r.status_code, 200)

    def test_not_dict_post_api_endpoint(self):
        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps([{'name': 'Den'}]))
        self.assertEqual(r.json, {'status': 'bad input'})
        self.assertEqual(r.status_code, 400)

    def test_no_name_post_api_endpoint(self):
        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps({'age': 100}))
        self.assertEqual(r.json, {'status': 'bad input'})
        self.assertEqual(r.status_code, 400)

    def test_bad_age_post_api_endpoint(self):
        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps({'name': 'Den', 'age': '100'}))
        self.assertEqual(r.json, {'status': 'bad input'})
        self.assertEqual(r.status_code, 400)


if __name__ == '__main__':
    unittest.main()
