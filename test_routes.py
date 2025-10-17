import unittest
from app import app as flask_app


class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = flask_app.test_client()

    def test_home(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_panduan(self):
        resp = self.client.get('/panduan')
        self.assertEqual(resp.status_code, 200)

    def test_persiapan(self):
        resp = self.client.get('/persiapan')
        self.assertEqual(resp.status_code, 200)

    def test_kontak(self):
        resp = self.client.get('/kontak')
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
