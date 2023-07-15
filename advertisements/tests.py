from unittest import TestCase
from rest_framework.test import APIClient


class SampleTestCase(TestCase):
    def test_successful_request(self):
        url = '/api/test/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
