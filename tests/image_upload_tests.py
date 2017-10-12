import os
import unittest

from flask import Flask, Request, request
from werkzeug.datastructures import FileStorage

class ImageUploadTestCase(client):
    def test_successful_upload(self):
        with open(os.path.dirname(os.path.abspath(__file__)) +
                '/image/testimage.png', 'r') as file:
            file = FileStorage(file)
            response = self.app.post(
                '/upload',
                data = {
                    'file': file
                },
                content_type='multipart/form-data'
            )
            json_data = json.loads(response.data.decode('utf-8'))

            self.assertIn('True', json_data['message'])

if __name__ == '__main__':
    unittest.main()
