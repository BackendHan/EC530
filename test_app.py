# test_app.py

import unittest
import app


class TestDataUpload(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_upload_file(self):
        response = self.app.post('/upload', data={})
        self.assertEqual(response.status_code, 200)
        self.assertIn('File uploaded successfully', response.get_data(as_text=True))


# 其他测试...
class TestModelTraining(unittest.TestCase):
    # 使用 setUp 函数初始化测试客户端
    def setUp(self):
        self.app = app.app.test_client()

    def test_train_model(self):
        response = self.app.post('/train', data={})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Model training initiated', response.get_data(as_text=True))


# 其他测试...


if __name__ == '__main__':
    unittest.main()
