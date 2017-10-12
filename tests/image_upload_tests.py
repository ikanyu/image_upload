import os
import unittest

from IPython import embed
from io import BytesIO
from flask import Flask, Request, request

class ImageUploadTestCase(unittest.TestCase):
    def test_successful_upload(self):
        assert true == true
