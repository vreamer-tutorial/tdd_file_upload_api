import unittest

from app import app

import io
import json
import os
from pathlib import Path

class TestFileUpload(unittest.TestCase):
    def test_upload_file(self):
        # Setup / Arrange
        file_name = 'file_to_upload.txt'
        file_path = os.path.join(Path(os.path.dirname(__file__)), file_name)
        with open(file_path, 'rb') as input_file:            
            input_file_stream = io.BytesIO(input_file.read())  

        data = {            
            'file': (input_file_stream, file_name),            
            'file_name': file_name
        }
        client = app.test_client()
        
        # Execute / Act
        response = client.post('/file/upload',
                                 content_type='multipart/form-data',
                                 data=data)
        
        # Assert
        self.assertEqual(201, response.status_code)
        self.assertEqual(file_name, response.json['file_name'])
        self.assertEqual('content to upload', response.json['file_content'])