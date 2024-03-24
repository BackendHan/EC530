import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_inference_endpoint(self):

        response = self.client.post('/inference', json={'data': 'some_data'})
        self.assertEqual(response.status_code, 202)

    def test_training_endpoint(self):
        # 测试数据和逻辑
        response = self.client.post('/training', json={'data': 'some_data'})
        self.assertEqual(response.status_code, 202)

